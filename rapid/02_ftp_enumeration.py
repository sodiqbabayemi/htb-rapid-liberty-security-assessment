"""
Rapid Security Assessment
Module 02: FTP Enumeration

Purpose:
    Structure and summarize FTP enumeration findings from an
    authorized security assessment.

Source:
    Sanitized from the Rapid assessment documentation.

Security Notice:
    Target addresses, credentials, flags, private keys, and other
    sensitive
    engagement information have intentionally been removed.
"""


def ftp_service_profile():
    """
    Define the FTP service identified during reconnaissance.
    """

    return {
        "port": 2121,
        "protocol": "FTP",
        "state": "open",
        "anonymous_access": True,
        "assessment_focus": [
            "Service identification",
            "Authentication configuration",
            "Anonymous access review",
            "Exposed resource analysis",
        ],
    }


def assess_ftp_configuration(profile):
    """
    Identify security observations from the FTP configuration.
    """

    observations = []

    if profile["state"] == "open":
        observations.append(
            "FTP service is externally reachable within the assessment scope."
        )

    if profile["anonymous_access"]:
        observations.append(
            "Anonymous FTP authentication was reported as enabled."
        )

    return observations


def display_report(profile, observations):
    """Display a sanitized FTP enumeration summary."""

    print("=" * 60)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 02: FTP ENUMERATION")
    print("=" * 60)

    print(f"\nService: {profile['protocol']}")
    print(f"Port: {profile['port']}")
    print(f"State: {profile['state']}")
    print(f"Anonymous access: {profile['anonymous_access']}")

    print("\nAssessment focus:")

    for item in profile["assessment_focus"]:
        print(f"  - {item}")

    print("\nSecurity observations:")

    for observation in observations:
        print(f"  - {observation}")


def main():
    profile = ftp_service_profile()
    observations = assess_ftp_configuration(profile)

    display_report(profile, observations)


if __name__ == "__main__":
    main()
