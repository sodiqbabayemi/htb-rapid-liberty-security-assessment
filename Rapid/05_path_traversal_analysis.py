"""
Rapid Security Assessment
Module 05: Path Traversal Analysis

Purpose:
    Analyze the security implications of a path-traversal weakness
    identified in an authorized laboratory FTP assessment.

Source:
    Sanitized from the Rapid Hack The Box assessment.

Security Notice:
    Target addresses, credentials, flags, private keys, and
    exploitation commands have intentionally been excluded.
"""


def define_path_traversal_finding():
    """
    Define the path-traversal condition identified during assessment.
    """

    return {
        "vulnerability": "FTP Path Traversal",
        "severity": "Critical",
        "affected_service": "FTP",
        "port": 2121,
        "security_boundary": "FTP directory",
        "observed_condition": (
            "Filesystem paths outside the intended FTP directory "
            "could be referenced through path traversal."
        ),
    }


def analyze_security_impact(finding):
    """
    Analyze the potential impact of breaking the intended
    filesystem boundary.
    """

    impacts = []

    if finding["vulnerability"] == "FTP Path Traversal":
        impacts = [
            "FTP directory isolation may be bypassed.",
            "Files outside the intended service directory may become accessible.",
            "Sensitive filesystem information may be exposed.",
            "Filesystem interaction may extend beyond the intended service scope.",
            "The weakness may be chained with other vulnerabilities.",
        ]

    return impacts


def identify_attack_chain_risk():
    """
    Describe the relationship between path traversal and
    other security weaknesses without exposing exploit details.
    """

    return [
        "Exposed FTP service",
        "Anonymous authentication",
        "Path-traversal weakness",
        "Filesystem interaction",
        "Potential file access or write capability",
        "Possible authenticated host access",
    ]


def recommend_controls():
    """
    Recommend defensive controls for preventing path traversal.
    """

    return [
        "Upgrade or replace vulnerable FTP software.",
        "Enforce strict directory confinement.",
        "Canonicalize and validate requested filesystem paths.",
        "Reject parent-directory traversal attempts.",
        "Apply least-privilege filesystem permissions.",
        "Prevent network-facing services from unnecessary filesystem access.",
        "Restrict FTP exposure to trusted networks.",
        "Monitor FTP activity for abnormal path requests.",
        "Perform post-remediation security validation.",
    ]


def generate_report(finding, impacts, attack_chain, controls):
    """
    Display a sanitized path-traversal security report.
    """

    print("=" * 70)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 05: PATH TRAVERSAL ANALYSIS")
    print("=" * 70)

    print("\nFinding")
    print("-" * 70)
    print(f"Vulnerability: {finding['vulnerability']}")
    print(f"Severity: {finding['severity']}")
    print(f"Service: {finding['affected_service']}")
    print(f"Port: {finding['port']}")
    print(f"Security boundary: {finding['security_boundary']}")
    print(f"Observed condition: {finding['observed_condition']}")

    print("\nPotential Security Impact")
    print("-" * 70)

    for impact in impacts:
        print(f"- {impact}")

    print("\nAttack-Chain Context")
    print("-" * 70)

    for step_number, step in enumerate(attack_chain, start=1):
        print(f"{step_number}. {step}")

    print("\nRecommended Security Controls")
    print("-" * 70)

    for control in controls:
        print(f"- {control}")


def main():
    finding = define_path_traversal_finding()
    impacts = analyze_security_impact(finding)
    attack_chain = identify_attack_chain_risk()
    controls = recommend_controls()

    generate_report(
        finding,
        impacts,
        attack_chain,
        controls
    )


if __name__ == "__main__":
    main()
