"""
Rapid Security Assessment
Module 01: Reconnaissance

This module records the services identified during the initial
reconnaissance stage of the Rapid assessment.

The original assessment contained target-specific information.
This public version has been sanitized before publication.
"""


def get_reconnaissance_findings():
    """Return the services identified during reconnaissance."""

    findings = {
        "22/tcp": {
            "service": "SSH",
            "state": "open",
            "observation": "SSH service was identified during reconnaissance.",
        },
        "2121/tcp": {
            "service": "FTP",
            "state": "open",
            "observation": (
                "FTP was identified and anonymous authentication "
                "was reported as permitted."
            ),
        },
    }

    return findings


def display_findings(findings):
    """Print the reconnaissance results in a readable format."""

    print("\n" + "=" * 60)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 01 — RECONNAISSANCE")
    print("=" * 60)

    for port, details in findings.items():
        print(f"\n[{port}]")
        print(f"Service     : {details['service']}")
        print(f"State       : {details['state']}")
        print(f"Observation : {details['observation']}")

    print("\n" + "=" * 60)


def main():
    findings = get_reconnaissance_findings()
    display_findings(findings)


if __name__ == "__main__":
    main()
