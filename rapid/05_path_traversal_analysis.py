"""
Rapid Security Assessment
Module 05: Path Traversal Analysis

This module documents the path traversal issue recorded during
the Rapid assessment.

The public version has been sanitized. Target addresses,
credentials, flags, private keys, and exploitation commands
have been removed.
"""

from dataclasses import dataclass


@dataclass
class Finding:
    """Store the main details of a security finding."""

    title: str
    severity: str
    affected_service: str
    description: str
    impact: list[str]
    remediation: list[str]


def create_path_traversal_finding() -> Finding:
    """Create the sanitized path traversal finding."""

    return Finding(
        title="Path Traversal Exposure",
        severity="High",
        affected_service="FTP Service",
        description=(
            "The assessment identified a potential path traversal "
            "condition in the file-transfer service. Poor handling "
            "of file and directory references could allow access "
            "outside the intended FTP directory."
        ),
        impact=[
            "Unauthorized access to sensitive files",
            "Potential exposure of configuration information",
            "Possible disclosure of credentials or application secrets",
            "Access to files outside the intended service boundary",
            "Possible support for further compromise if sensitive data is exposed",
        ],
        remediation=[
            "Enforce server-side path validation.",
            "Limit file operations to approved directories.",
            "Normalize and validate file paths before processing.",
            "Reject traversal sequences and unexpected path components.",
            "Apply least-privilege permissions to the FTP service account.",
            "Disable unnecessary FTP functionality.",
            "Keep the FTP service and operating system patched.",
            "Monitor and review FTP activity in the audit logs.",
        ],
    )


def assess_risk(finding: Finding) -> str:
    """Return a simple risk-priority message."""

    risk_levels = {
        "Critical": "Immediate remediation required.",
        "High": "Prioritize remediation and validate the affected service.",
        "Medium": "Remediate within the organization's defined risk window.",
        "Low": "Address through normal security improvement activities.",
    }

    return risk_levels.get(
        finding.severity,
        "Review the finding using the organization's risk methodology.",
    )


def display_report(finding: Finding) -> None:
    """Print the finding in a readable format."""

    print("\n" + "=" * 70)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 05 — PATH TRAVERSAL ANALYSIS")
    print("=" * 70)

    print(f"\nFinding          : {finding.title}")
    print(f"Severity         : {finding.severity}")
    print(f"Affected service : {finding.affected_service}")

    print("\nDescription")
    print("-" * 70)
    print(finding.description)

    print("\nPotential impact")
    print("-" * 70)

    for number, impact in enumerate(finding.impact, start=1):
        print(f"{number}. {impact}")

    print("\nRisk assessment")
    print("-" * 70)
    print(assess_risk(finding))

    print("\nRecommended remediation")
    print("-" * 70)

    for number, recommendation in enumerate(
        finding.remediation,
        start=1,
    ):
        print(f"{number}. {recommendation}")

    print("\nAssessment status")
    print("-" * 70)
    print("Finding documented for remediation and validation.")

    print("\n" + "=" * 70)


def main() -> None:
    finding = create_path_traversal_finding()
    display_report(finding)


if __name__ == "__main__":
    main()
