"""
Rapid Security Assessment
Module 06: File Access Analysis

Purpose:
    Analyze the security implications of unauthorized filesystem
    access through an improperly restricted FTP service.

Source:
    Sanitized from the Rapid Hack The Box assessment.

Security Notice:
    Target addresses, credentials, private keys, flags, sensitive
    file paths, and exploitation commands have intentionally been
    excluded.
"""


def define_file_access_condition():
    """
    Define the filesystem access condition observed during assessment.
    """

    return {
        "service": "FTP",
        "port": 2121,
        "access_control": "Improperly restricted",
        "directory_isolation": False,
        "filesystem_interaction": True,
        "risk_level": "Critical",
    }


def analyze_file_access_risk(condition):
    """
    Analyze the potential consequences of excessive filesystem access.
    """

    risks = []

    if not condition["directory_isolation"]:
        risks.extend([
            "The FTP service boundary may not adequately isolate users.",
            "Resources outside the intended FTP directory may become accessible.",
            "Sensitive files may be exposed to unauthorized users.",
            "File modification may become possible where write permissions exist.",
            "Filesystem access can increase the impact of other vulnerabilities.",
        ])

    return risks


def classify_access_types(condition):
    """
    Classify the types of filesystem interaction relevant to the finding.
    """

    access_types = {
        "read_access": "Potentially exposed",
        "write_access": "Dependent on filesystem permissions",
        "execute_access": "Not assumed without additional evidence",
        "directory_enumeration": "Potentially exposed",
    }

    return access_types


def recommend_file_access_controls():
    """
    Recommend controls to restrict filesystem access.
    """

    return [
        "Confine the FTP service to its designated directory.",
        "Prevent traversal outside the authorized directory.",
        "Apply least-privilege filesystem permissions.",
        "Run the service with a dedicated low-privilege account.",
        "Restrict write permissions to only required locations.",
        "Separate sensitive system files from service-accessible storage.",
        "Monitor abnormal file-access activity.",
        "Review service-account permissions regularly.",
        "Disable unnecessary FTP functionality.",
        "Validate the controls after remediation.",
    ]


def generate_report(condition, risks, access_types, controls):
    """
    Generate a sanitized file-access security report.
    """

    print("=" * 70)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 06: FILE ACCESS ANALYSIS")
    print("=" * 70)

    print("\nAssessment Condition")
    print("-" * 70)
    print(f"Service: {condition['service']}")
    print(f"Port: {condition['port']}")
    print(f"Access control: {condition['access_control']}")
    print(f"Directory isolation: {condition['directory_isolation']}")
    print(f"Filesystem interaction: {condition['filesystem_interaction']}")
    print(f"Risk level: {condition['risk_level']}")

    print("\nPotential Security Risks")
    print("-" * 70)

    for risk in risks:
        print(f"- {risk}")

    print("\nAccess Classification")
    print("-" * 70)

    for access_type, status in access_types.items():
        print(f"{access_type}: {status}")

    print("\nRecommended Controls")
    print("-" * 70)

    for control in controls:
        print(f"- {control}")


def main():
    condition = define_file_access_condition()
    risks = analyze_file_access_risk(condition)
    access_types = classify_access_types(condition)
    controls = recommend_file_access_controls()

    generate_report(
        condition,
        risks,
        access_types,
        controls
    )


if __name__ == "__main__":
    main()
