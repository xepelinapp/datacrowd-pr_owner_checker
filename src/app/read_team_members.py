import json
import subprocess

from typing import Union

from lib.logger import Logger

logger = Logger()


def get_target_team_members(target_team: str, target_org: str) -> Union[list, bool]:
    # setup
    header_accept = "Accept: application/vnd.github+json"
    header_api_ver = "X-GitHub-Api-Version: 2022-11-28"
    cmds = [
        "gh",
        "api",
        "-X", "GET",
        "-H", header_accept,
        "-H", header_api_ver,
        f"orgs/{target_org}/teams/{target_team}/members",
        "--jq", ".[] | {userId: .login}",
    ]
    logger.debug(cmds)
    # exec
    logger.info(f"Getting team members from '{target_team}' on GitHub teams for org '{target_org}'...")
    run_output = subprocess.run(args=cmds, capture_output=True)
    logger.debug(run_output.returncode)
    # if returncode != 0, exit
    if run_output.returncode != 0:
        logger.debug(run_output.stderr)
        logger.critical("Error retreiving target team members. Exiting now")
        return False
    output_list = run_output.stdout.decode(encoding="utf-8").split()
    logger.debug(output_list)
    logger.debug(type(output_list))
    return_list = parse_team_members(members_list=output_list)
    return return_list


def parse_team_members(members_list: list) -> list:
    # exec
    return_members_list = []
    for member in members_list:
        team_member = json.loads(s=member)
        logger.debug(f"Team member user ID: @{team_member.get('userId')}")
        return_members_list.append(f"@{team_member.get('userId')}")
    logger.debug(f"Target team has {len(members_list)} team members")
    return return_members_list
