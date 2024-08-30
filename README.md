# Mailx-Git-Patch-Sender

## Setup

### Dependencies

- BSD Mailx - package `bsd-mailx` on Ubuntu/Debian.
- Python3, >= 3.10.
    - On Ubuntu 22.04, package `python3` is sufficient.
    - On earlier versions, use the `deadsnakes` PPA, and install `python3.10`.
        - Add the PPA with `sudo add-apt-repository ppa:deadsnakes/ppa`.

### Setting up Mailx

// TODO

## Usage

```shell
python3.10 main.py -s <sender> -r <recipient> [-p <subject prefix>] <patch1> [<patch2> ...]
```

Options:
- `-s` - Sender address. Should just be the first part of the email before the @ - the rest is set in by the `myorigin` in /etc/postfix/main.cf.
- `-r` - Recipient email address. Should be a complete address.
- `-p` [optional] - Prefix to add to the subject line of every email.

Example:
```shell
$ python3.10 main.py -s Oliver.Gaskell -r Oliver.Gaskell@analog.com ~/lnxdsp-u-boot/*.patch
Sending patch 1 of 21: "[PATCH 00/20] arm: Initial support for Analog Devices SC5xx boards"
Sending patch 2 of 21: "[PATCH 01/20] arm: dts: Support SC573-EZKIT"
Sending patch 3 of 21: "[PATCH 02/20] arm: dts: Support SC584-EZKIT"
Sending patch 4 of 21: "[PATCH 03/20] arm: dts: Support SC589-MINI"
Sending patch 5 of 21: "[PATCH 04/20] arm: dts: Support SC589-EZKIT"
Sending patch 6 of 21: "[PATCH 05/20] arm: dts: Support SC594-SOM-EZKIT"
Sending patch 7 of 21: "[PATCH 06/20] arm: dts: Support SC594-SOM-EZLITE"
Sending patch 8 of 21: "[PATCH 07/20] arm: dts: Support SC598-SOM-EZKIT"
Sending patch 9 of 21: "[PATCH 08/20] arm: dts: Support SC598-SOM-EZLITE"
Sending patch 10 of 21: "[PATCH 09/20] dt-bindings: arm: Add SC5xx Series binding"
Sending patch 11 of 21: "[PATCH 10/20] dt-bindings: clock: Add SC5xx clock tree bindings"
Sending patch 12 of 21: "[PATCH 11/20] dt-bindings: timer: Add SC5xx Timer bindings"
Sending patch 13 of 21: "[PATCH 12/20] arm: mach-sc5xx: clean up Kconfig"
Sending patch 14 of 21: "[PATCH 13/20] arm: SC598-SOM-EZKIT initial support"
Sending patch 15 of 21: "[PATCH 14/20] arm: SC598-SOM-EZLITE initial support"
Sending patch 16 of 21: "[PATCH 15/20] arm: SC594-SOM-EZKIT initial support"
Sending patch 17 of 21: "[PATCH 16/20] arm: SC594-SOM-EZLITE initial support"
Sending patch 18 of 21: "[PATCH 17/20] arm: SC584-EZKIT initial support"
Sending patch 19 of 21: "[PATCH 18/20] arm: SC589-EZKIT initial support"
Sending patch 20 of 21: "[PATCH 19/20] arm: SC589-MINI initial support"
Sending patch 21 of 21: "[PATCH 20/20] arm: SC573-EZKIT initial support"
```

### Creating Patch files

The recommended way to create the patch files with git is as follows:

```shell
git format-patch <ref> -n --always --start-number=0
```

Where `<ref>` is the earliest of the commits you want to send.
For example, if you have a series of commits branched from master you want to send, `master` can be used as `<ref>`.

Use of `--start-number=0` assumes the first commit in your series contains just the cover letter - this can be omitted if you don't have a cover letter commit.

This will output a series of files named `nnnn-commit-name.patch`. These can all be sent by passing `*.patch` to the program.