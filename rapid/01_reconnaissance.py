"""
Rapid Security Assessment
Module 01: Reconnaissance

Purpose:
    Structure and summarize reconnaissance findings from an
    authorized security assessment.

Source:
    Sanitized from the Rapid assessment documentation.

Note:
    Target-specific IP addresses, credentials, flags, private keys,
    and other sensitive engagement information have been removed.
"""


def summarize_reconnaissance():
    """
    Summarize the services identified during initial reconnaissance.
    """

    findings = {
        "22/tcp": {
            "service": "SSH",
            "state": "open",
            "observation": "SSH service detected during reconnaissance.",
        },
        "2121/tcp": {
            "service": "FTP",
            "state": "open",
            "observation": (
                "FTP service detected; anonymous authentication "
                "was reported as permitted."
            ),
        },
    }

    return findings


def display_findings(findings):
    """Display reconnaissance findings in a readable format."""

    print("=" * 60)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 01: RECONNAISSANCE")
    print("=" * 60)

    for port, details in findings.items():
        print(f"\nPort: {port}")
        print(f"Service: {details['service']}")
        print(f"State: {details['state']}")
        print(f"Observation: {details['observation']}")


def main():
    findings = summarize_reconnaissance()
    display_findings(findings)


if __name__ == "__main__":
    main()
