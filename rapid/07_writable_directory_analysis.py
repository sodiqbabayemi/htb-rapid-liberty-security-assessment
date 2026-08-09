"""
Rapid Security Assessment
Module 07: Writable Directory Analysis

This module documents the writable-resource condition identified
during the Rapid assessment.

The public version has been sanitized. Target addresses,
credentials, private keys, flags, sensitive paths, and
exploitation commands have been removed.
"""


def get_writable_location():
    """Return the writable-resource condition recorded during assessment."""

    return {
        "service": "FTP",
        "port": 2121,
        "resource_type": "Directory",
        "write_capability": True,
        "access_control": "Insufficiently restricted",
        "risk_level": "High",
    }


def assess_write_risk(location):
    """Describe the risks associated with the writable location."""

    risks = []

    if location["write_capability"]:
        risks.extend(
            [
                "Unauthorized users may be able to place files in the location.",
                "Writable resources can increase the impact of a service compromise.",
                "Unexpected files may be introduced into trusted directories.",
                "File-write capability may be chained with other weaknesses.",
                "Improper permissions can weaken filesystem integrity.",
            ]
        )

    return risks


def review_security_boundaries():
    """List the controls that should protect a writable resource."""

    return {
        "Authentication": "Should be required where appropriate",
        "Directory confinement": "Required",
        "Least privilege": "Required",
        "Write permissions": "Limited to necessary locations",
        "File integrity monitoring": "Recommended",
    }


def get_remediation_recommendations():
    """Return recommended controls for the writable resource."""

    return [
        "Remove unnecessary write permissions.",
        "Apply least-privilege filesystem permissions.",
        "Restrict writable directories to locations that actually require them.",
        "Prevent service users from modifying sensitive system resources.",
        "Separate upload locations from executable or trusted directories.",
        "Review ownership and permissions of service-accessible directories.",
        "Monitor unexpected file creation and modification.",
        "Disable unnecessary anonymous write functionality.",
        "Review permissions again after remediation.",
    ]


def display_report(location, risks, boundaries, recommendations):
    """Print the writable-directory assessment in a readable format."""

    print("\n" + "=" * 70)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 07 — WRITABLE DIRECTORY ANALYSIS")
    print("=" * 70)

    print("\nResource")
    print("-" * 70)
    print(f"Service          : {location['service']}")
    print(f"Port             : {location['port']}")
    print(f"Resource type    : {location['resource_type']}")
    print(f"Write capability  : {location['write_capability']}")
    print(f"Access control   : {location['access_control']}")
    print(f"Risk level       : {location['risk_level']}")

    print("\nSecurity risks")
    print("-" * 70)

    for risk in risks:
        print(f"- {risk}")

    print("\nSecurity boundaries")
    print("-" * 70)

    for boundary, requirement in boundaries.items():
        print(f"{boundary:<24}: {requirement}")

    print("\nRecommended remediation")
    print("-" * 70)

    for recommendation in recommendations:
        print(f"- {recommendation}")

    print("\n" + "=" * 70)


def main():
    location = get_writable_location()
    risks = assess_write_risk(location)
    boundaries = review_security_boundaries()
    recommendations = get_remediation_recommendations()

    display_report(
        location,
        risks,
        boundaries,
        recommendations,
    )


if __name__ == "__main__":
    main()
