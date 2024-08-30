#! /usr/bin/env python3

import argparse
import sys
import re
from subprocess import Popen, PIPE, STDOUT

# mailx -s "Mailx test" -r "Oliver.Gaskell" "Oliver.Gaskell@analog.com"
def mailx_command(subject: str, sender: str, recipient: str) -> str:
    return ["mailx", "-s", subject, "-r", sender, recipient]

def send_email(command: list[str], body: str):
    p = Popen(command, stdout=PIPE, stdin=PIPE, stderr=PIPE, text=True)
    p.communicate(input=body)
    p.terminate()

def get_subject(patch: str) -> str:
    regex = re.compile(r"^Subject: (.*)$", re.MULTILINE)
    return regex.search(patch).group(1)

def send_patches(sender, recipient, patches: list[str], extra_subj: str | None = None):
    if extra_subj is not None:
        prefix = extra_subj + " "
    else:
        prefix = ""


    for i, p in enumerate(patches):
        with open(p, "r") as f:
            patch = f.read()

        subj = prefix + get_subject(patch)

        print(f"Sending patch {i + 1} of {len(patches)}: \"{subj}\"")
        command = mailx_command(subj, sender, recipient)
        send_email(command, patch)

if __name__ == "__main__":
    # Simply run with "./main.py -s <sender> -r <recipient> <patch1> <patch2> ..."
    # Best way to format patches is `git format-patch <ref> -n --always --start-number=0`
    # Or omit --start-number=0 if you don't have a cover letter commit

    parser = argparse.ArgumentParser(
        prog = "Mailx-Git-Patch-Sender",
        description = "Utility used to send git patch files with BSD mailx."
    )

    parser.add_argument('-s', '--sender', required=True, help="The senders email address. Should be just the part before the @ - the rest is provided by /etc/mailname.")
    parser.add_argument('-r', '--recipient', required=True, help="The recipient/s email address/es. Should be full email address/es.")
    parser.add_argument('filenames', nargs="+", help="The patches to send.")

    parser.add_argument('-p', '--prefix-subject', help="Prefix to add to the subject line of all emails.")

    args = parser.parse_args()

    send_patches(
        args.sender,
        args.recipient,
        args.filenames,
        args.prefix_subject
    )
