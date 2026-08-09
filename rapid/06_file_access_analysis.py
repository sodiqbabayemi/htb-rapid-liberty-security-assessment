"""
Rapid Security Assessment
Module 06: File Access Analysis

This module documents the filesystem-access condition associated
with the FTP service during the Rapid assessment.

The public version has been sanitized. Target addresses,
credentials, private keys, flags, sensitive file paths, and
exploitation commands have been removed.
"""


def get_file_access_condition():
    """Return the filesystem-access condition recorded during assessment."""

    return {
        "service": "FTP",
        "port": 2121,
        "access_control": "Improperly restricted",
        "directory_isolation": False,
        "filesystem_interaction": True,
        "risk_level": "Critical",
    }


def assess_file_access_risk(condition):
    """List the security risks associated with the access condition."""

    risks = []

    if not condition["directory_isolation"]:
        risks.extend(
            [
                "The FTP service boundary may not adequately isolate users.",
                "Resources outside the intended FTP directory may become accessible.",
                "Sensitive files may be exposed to unauthorized users.",
                "File modification may be possible where write permissions exist.",
                "Filesystem access can increase the impact of other vulnerabilities.",
            ]
        )

    return risks


def classify_access_types():
    """Describe the access types relevant to the assessment."""

    return {
        "Read access": "Potentially exposed",
        "Write access": "Depends on filesystem permissions",
        "Execute access": "Not assumed without additional evidence",
        "Directory enumeration": "Potentially exposed",
    }


def get_recommended_controls():
    """Return the recommended filesystem-access controls."""

    return [
        "Confine the FTP service to its designated directory.",
        "Prevent access outside the authorized directory.",
        "Apply least-privilege filesystem permissions.",
        "Run the service with a dedicated low-privilege account.",
        "Restrict write permissions to locations that actually require them.",
        "Keep sensitive system files outside service-accessible storage.",
        "Monitor abnormal file-access activity.",
        "Review service-account permissions regularly.",
        "Disable unnecessary FTP functionality.",
        "Validate the controls after remediation.",
    ]


def display_report(condition, risks, access_types, controls):
    """Print the file-access assessment in a readable format."""

    print("\n" + "=" * 70)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 06 — FILE ACCESS ANALYSIS")
    print("=" * 70)

    print("\nAssessment condition")
    print("-" * 70)
    print(f"Service              : {condition['service']}")
    print(f"Port                 : {condition['port']}")
    print(f"Access control       : {condition['access_control']}")
    print(f"Directory isolation  : {condition['directory_isolation']}")
    print(f"Filesystem interaction: {condition['filesystem_interaction']}")
    print(f"Risk level           : {condition['risk_level']}")

    print("\nPotential security risks")
    print("-" * 70)

    for risk in risks:
        print(f"- {risk}")

    print("\nAccess classification")
    print("-" * 70)

    for access_type, status in access_types.items():
        print(f"{access_type:<24}: {status}")

    print("\nRecommended controls")
    print("-" * 70)

    for control in controls:
        print(f"- {control}")

    print("\n" + "=" * 70)


def main():
    condition = get_file_access_condition()
    risks = assess_file_access_risk(condition)
    access_types = classify_access_types()
    controls = get_recommended_controls()

    display_report(
        condition,
        risks,
        access_types,
        controls,
    )


if __name__ == "__main__":
    main()
