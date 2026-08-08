"""
Rapid Security Assessment
Module 02: FTP Enumeration

This module records the FTP service identified during the
assessment and summarizes the main configuration observations.

The public version has been sanitized. Target-specific
information has been removed.
"""


def get_ftp_service_profile():
    """Return the FTP service information identified during assessment."""

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
    """Review the FTP profile and record relevant observations."""

    observations = []

    if profile["state"] == "open":
        observations.append(
            "The FTP service was identified as open on port "
            f"{profile['port']}."
        )

    if profile["anonymous_access"]:
        observations.append(
            "Anonymous FTP authentication was reported as enabled."
        )

    return observations


def display_report(profile, observations):
    """Print the FTP enumeration results."""

    print("\n" + "=" * 60)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 02 — FTP ENUMERATION")
    print("=" * 60)

    print(f"\nService            : {profile['protocol']}")
    print(f"Port               : {profile['port']}")
    print(f"State              : {profile['state']}")
    print(
        f"Anonymous access   : "
        f"{profile['anonymous_access']}"
    )

    print("\nAssessment focus:")

    for item in profile["assessment_focus"]:
        print(f"  - {item}")

    print("\nSecurity observations:")

    for observation in observations:
        print(f"  - {observation}")

    print("\n" + "=" * 60)


def main():
    profile = get_ftp_service_profile()
    observations = assess_ftp_configuration(profile)

    display_report(profile, observations)


if __name__ == "__main__":
    main()
