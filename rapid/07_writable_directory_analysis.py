"""
Rapid Security Assessment
Module 07: Writable Directory Analysis

Purpose:
    Analyze the security implications of writable locations exposed
    through an improperly restricted service.

Source:
    Sanitized from the Rapid Hack The Box assessment.

Security Notice:
    Target addresses, credentials, private keys, flags, sensitive
    paths, and exploitation commands have intentionally been excluded.
"""


def define_writable_location():
    """
    Define the writable-resource condition identified during assessment.
    """

    return {
        "service": "FTP",
        "port": 2121,
        "resource_type": "Directory",
        "write_capability": True,
        "access_control": "Insufficiently restricted",
        "risk_level": "High",
    }


def analyze_write_risk(location):
    """
    Analyze the security implications of excessive write access.
    """

    risks = []

    if location["write_capability"]:
        risks.extend([
            "Unauthorized users may be able to place files in the location.",
            "Writable resources can increase the impact of a service compromise.",
            "Unexpected files may be introduced into trusted directories.",
            "File-write capability may enable chaining with other weaknesses.",
            "Improper permissions can undermine filesystem integrity.",
        ])

    return risks


def assess_security_boundaries(location):
    """
    Evaluate the security boundaries surrounding the writable resource.
    """

    boundaries = {
        "authentication": "Should be required where appropriate",
        "directory_confinement": "Required",
        "least_privilege": "Required",
        "write_permissions": "Should be limited to necessary locations",
        "file_integrity_monitoring": "Recommended",
    }

    return boundaries


def recommend_remediation():
    """
    Provide defensive recommendations for writable resources.
    """

    return [
        "Remove unnecessary write permissions.",
        "Apply least-privilege filesystem permissions.",
        "Restrict writable directories to explicitly required locations.",
        "Ensure service users cannot modify sensitive system resources.",
        "Separate upload locations from executable or trusted directories.",
        "Review ownership and permissions of service-accessible directories.",
        "Monitor unexpected file creation and modification.",
        "Disable unnecessary anonymous write functionality.",
        "Perform a permissions review after remediation.",
    ]


def generate_report(location, risks, boundaries, recommendations):
    """
    Generate a sanitized writable-directory assessment report.
    """

    print("=" * 70)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 07: WRITABLE DIRECTORY ANALYSIS")
    print("=" * 70)

    print("\nResource")
    print("-" * 70)
    print(f"Service: {location['service']}")
    print(f"Port: {location['port']}")
    print(f"Resource type: {location['resource_type']}")
    print(f"Write capability: {location['write_capability']}")
    print(f"Access control: {location['access_control']}")
    print(f"Risk level: {location['risk_level']}")

    print("\nSecurity Risks")
    print("-" * 70)

    for risk in risks:
        print(f"- {risk}")

    print("\nSecurity Boundaries")
    print("-" * 70)

    for boundary, requirement in boundaries.items():
        print(f"{boundary}: {requirement}")

    print("\nRecommended Remediation")
    print("-" * 70)

    for recommendation in recommendations:
        print(f"- {recommendation}")


def main():
    location = define_writable_location()
    risks = analyze_write_risk(location)
    boundaries = assess_security_boundaries(location)
    recommendations = recommend_remediation()

    generate_report(
        location,
        risks,
        boundaries,
        recommendations
    )


if __name__ == "__main__":
    main()
