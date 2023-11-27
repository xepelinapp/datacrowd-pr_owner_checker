import json
import subprocess

from typing import Union

from lib.logger import Logger

logger = Logger()


def get_pr_info(pr_number: int, **kwargs) -> Union[list, bool]:
    # setup
    target_repo = kwargs.get("repo", None)
    target_org = kwargs.get("org", None)
    if target_org is None or target_repo is None:
        logger.critical("No repo provided. Exiting now")
        raise Exception
    repo = f"{target_org}/{target_repo}"
    logger.debug(msg=repo)
    cmds = [
        "gh",
        "pr",
        "view",
        f"{pr_number}",
        "--repo", repo,
        "--json", "author,createdAt,state",
        "--jq", ". | {author:.author.login, createdAt: .createdAt, state: .state}",
    ]
    logger.debug(cmds)
    # executing gh cli
    logger.info(f"Getting PR info for PR #{pr_number} on repo '{repo}'...")
    run_output = subprocess.run(args=cmds, capture_output=True)
    logger.debug(run_output.returncode)
    # if returncode != 0, exit
    if run_output.returncode != 0:
        logger.debug(run_output.returncode)
        logger.debug(run_output.stderr)
        logger.critical("Error retrieving PR data. Exiting now")
        return False
    output_list = run_output.stdout.decode(encoding="utf-8").split()
    logger.debug(output_list)
    logger.debug(type(output_list))
    return output_list


def parse_pr_info(pr_info: list, **kwargs) -> bool:
    # setup
    authorized_authors = kwargs["auth_authors"]
    # exec
    for pr in pr_info:
        pr_data = json.loads(s=pr)
        pr_author = pr_data.get("author", None)
        valid_author = validate_pr_author(pr_author=pr_author, authorized_authors=authorized_authors)
        logger.info(f"PR author: {pr_author}; is PR author valid? {valid_author}")
    return valid_author


def validate_pr_author(pr_author: str, authorized_authors: list) -> bool:
    # setup
    logger.debug(f"env var crowders: {authorized_authors}")
    logger.debug(type(authorized_authors))
    auth_list = authorized_authors
    logger.debug(auth_list)
    logger.debug(type(auth_list))
    logger.debug(f"Corrected author: @{pr_author}")
    if f"@{pr_author}" in auth_list:
        return True
    else:
        return False
