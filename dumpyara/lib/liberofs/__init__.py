"""fsck.erofs wrapper."""

from subprocess import STDOUT, check_output

def erofs(command: str):
	return check_output(f"fsck.erofs {command}", shell=True, stderr=STDOUT)
