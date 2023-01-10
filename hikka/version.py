"""Represents current userbot version"""
__version__ = (6, 3, 1)

import git
import os

try:
    branch = git.Repo(
        path=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ).active_branch.name
except Exception:
    branch = "master"
