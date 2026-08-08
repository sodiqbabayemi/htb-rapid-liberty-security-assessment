"""
Rapid Security Assessment
Module 03: FTP Access Analysis

This module reviews the FTP access conditions recorded during
the Rapid assessment and turns them into security findings.

The public version has been sanitized. Target-specific details,
credentials, private keys, flags, and exploitation commands
have been removed.
"""


def get_ftp_access_profile():
    """Return the FTP access conditions recorded during assessment."""

    return {
        "service": "FTP",
        "port": 2121,
        "anonymous_login": True,
        "authentication_required": False,
        "exposed_resources": True,
    }


def evaluate_access_control(profile):
    """Turn the recorded access conditions into security findings."""

    findings = []

    if profile["anonymous_login"]:
        findings.append(
            {
                "finding": "Anonymous FTP access",
                "severity": "High",
                "impact": (
                    "Unauthenticated users can interact with "
                    "the FTP service."
                ),
                "recommendation": (
                    "Disable anonymous access unless it is "
                    "explicitly required."
                ),
            }
        )

    if profile["exposed_resources"]:
        findings.append(
            {
                "finding": "FTP resource exposure",
                "severity": "High",
                "impact": (
                    "Files available through the FTP service "
                    "may expose information useful for further "
                    "security analysis."
                ),
                "recommendation": (
                    "Restrict accessible files and review "
                    "FTP directory permissions."
                ),
            }
        )

    return findings


def display_report(profile, findings):
    """Print the FTP access findings in a readable format."""

    print("\n" + "=" * 65)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 03 — FTP ACCESS ANALYSIS")
    print("=" * 65)

    print("\nService information")
    print("-" * 65)
    print(f"Protocol               : {profile['service']}")
    print(f"Port                   : {profile['port']}")
    print(f"Anonymous login        : {profile['anonymous_login']}")
    print(
        f"Authentication required: "
        f"{profile['authentication_required']}"
    )
    print(f"Exposed resources      : {profile['exposed_resources']}")

    print("\nSecurity findings")
    print("-" * 65)

    for number, finding in enumerate(findings, start=1):
        print(f"\nFinding {number}: {finding['finding']}")
        print(f"Severity       : {finding['severity']}")
        print(f"Impact         : {finding['impact']}")
        print(f"Recommendation : {finding['recommendation']}")

    print("\n" + "=" * 65)


def main():
    profile = get_ftp_access_profile()
    findings = evaluate_access_control(profile)

    display_report(profile, findings)


if __name__ == "__main__":
    main()
