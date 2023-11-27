#!/bin/python
import os
import sys

from app.read_team_members import get_target_team_members
from app.validate_pr_data import get_pr_info, parse_pr_info
from lib.logger import Logger

logger = Logger()


def main():
    # NOTE: refactored to work with YAML input
    # /* PR number */
    try:
        pr_number = os.environ["INPUT_PRNUM"]
    except KeyError:
        pr_number = None
    if pr_number == "" or pr_number is None:
        logger.critical("No PR number provided. Exiting now")
        sys.exit(1)
    # /* target owner team */
    try:
        target_team = os.environ["INPUT_TARGETTEAM"]
    except KeyError:
        target_team = None
    if target_team is None:
        logger.critical("No target owner team provided. Exiting now")
        sys.exit(1)
    # /* target github org */
    try:
        target_org = os.environ["INPUT_TARGETORG"]
    except KeyError:
        target_org = None
    if target_org is None:
        logger.critical("No target owner team provided. Exiting now")
        sys.exit(1)
    # /* target repo */
    try:
        target_repo = os.environ["INPUT_TARGETREPO"]
    except KeyError:
        target_repo = None
    if target_repo is None:
        logger.critical("No target owner team provided. Exiting now")
        sys.exit(1)
    # KEY: log out pr_number
    logger.debug(msg=f"PR number: {pr_number}")
    # for poc v2, get team members from gh api
    team_members = get_target_team_members(target_team=target_team, target_org=target_org)
    if team_members is False:
        sys.exit(1)
    logger.debug(f"Team members: {team_members}")
    # pdb.set_trace()
    # get pr info
    logger.info("Proceeding...")
    exec_pr_info = get_pr_info(pr_number=pr_number, repo=target_repo, org=target_org)
    if exec_pr_info is False:
        sys.exit(1)
    valid_author = parse_pr_info(pr_info=exec_pr_info, auth_authors=team_members)
    logger.debug(f"Valid author: {valid_author}")
    if valid_author:
        logger.info(True)
        return True
    else:
        logger.warning(False)
        sys.exit(11)


if __name__ == "__main__":
    main()
