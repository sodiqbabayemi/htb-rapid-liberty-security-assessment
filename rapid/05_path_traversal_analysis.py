"""
Rapid Security Assessment
Module 05: Path Traversal Analysis

Purpose:
    Analyze a suspected path traversal finding identified during an
    authorized security assessment.

This module is sanitized for public portfolio use.
No client identifiers, credentials, target addresses, flags,
private keys, or exploitation commands are included.

Author: Sodiq Babayemi
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Finding:
    """Represents a security finding identified during assessment."""

    title: str
    severity: str
    affected_service: str
    description: str
    impact: List[str]
    remediation: List[str]


def create_path_traversal_finding() -> Finding:
    """
    Create a sanitized representation of the path traversal finding.

    The assessment identified a potential path traversal condition
    associated with an exposed file-transfer service.
    """

    return Finding(
        title="Path Traversal Exposure",
        severity="High",
        affected_service="FTP Service",
        description=(
            "The assessment identified a potential path traversal "
            "condition within an exposed file-transfer workflow. "
            "Improper validation of file and directory references "
            "could allow an authenticated or otherwise authorized "
            "user to access files outside the intended directory."
        ),
        impact=[
            "Unauthorized access to sensitive files",
            "Potential exposure of configuration information",
            "Possible disclosure of credentials or application secrets",
            "Expansion of the attack surface through unintended file access",
            "Potential support for further compromise if sensitive data is exposed",
        ],
        remediation=[
            "Enforce strict server-side path validation.",
            "Restrict file operations to approved directories.",
            "Normalize and validate requested file paths before processing.",
            "Reject traversal sequences and unexpected path components.",
            "Apply least-privilege permissions to service accounts.",
            "Disable unnecessary file-transfer functionality.",
            "Keep the FTP service and underlying operating system patched.",
            "Monitor and review file-transfer audit logs.",
        ],
    )


def assess_risk(finding: Finding) -> str:
    """
    Provide a high-level risk assessment based on the finding severity.
    """

    risk_levels = {
        "Critical": "Immediate remediation required.",
        "High": "Prioritize remediation and validate the affected service.",
        "Medium": "Remediate within the organization's defined risk window.",
        "Low": "Address through normal security improvement activities.",
    }

    return risk_levels.get(
        finding.severity,
        "Review and classify according to the organization's risk methodology.",
    )


def generate_report(finding: Finding) -> None:
    """Display a concise security assessment report."""

    print("=" * 70)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 05: PATH TRAVERSAL ANALYSIS")
    print("=" * 70)

    print(f"\nFinding: {finding.title}")
    print(f"Severity: {finding.severity}")
    print(f"Affected Service: {finding.affected_service}")

    print("\nDescription")
    print("-" * 70)
    print(finding.description)

    print("\nPotential Impact")
    print("-" * 70)

    for index, impact in enumerate(finding.impact, start=1):
        print(f"{index}. {impact}")

    print("\nRisk Assessment")
    print("-" * 70)
    print(assess_risk(finding))

    print("\nRecommended Remediation")
    print("-" * 70)

    for index, recommendation in enumerate(
        finding.remediation, start=1
    ):
        print(f"{index}. {recommendation}")

    print("\nAssessment Status")
    print("-" * 70)
    print("Finding documented for remediation and validation.")

    print("\n" + "=" * 70)


def main() -> None:
    """Main execution function."""

    finding = create_path_traversal_finding()
    generate_report(finding)


if __name__ == "__main__":
    main()
