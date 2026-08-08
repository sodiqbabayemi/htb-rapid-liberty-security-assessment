"""
Rapid Security Assessment
Module 08: SSH Access Analysis

Purpose:
    Analyze the SSH access stage of an authorized security assessment
    and document the security implications of credentials obtained
    through the earlier attack chain.

Source:
    Sanitized from the Rapid assessment documentation.

Security Notice:
    Target addresses, usernames, passwords, private keys, flags,
    and exploitation commands have intentionally been excluded.
"""


def define_ssh_access():
    """
    Define the SSH service and access condition identified during
    the assessment.
    """

    return {
        "service": "SSH",
        "port": 22,
        "state": "open",
        "authentication_method": "Credential-based",
        "access_status": "Authenticated access obtained during assessment",
    }


def analyze_ssh_security(access):
    """
    Analyze the security implications of the SSH access condition.
    """

    findings = []

    if access["state"] == "open":
        findings.append({
            "finding": "SSH service exposed",
            "severity": "Medium",
            "impact": (
                "An exposed SSH service increases the importance of "
                "strong authentication, access restrictions, and monitoring."
            ),
            "recommendation": (
                "Restrict SSH exposure to trusted networks where possible "
                "and enforce strong authentication controls."
            ),
        })

    if access["access_status"] == "Authenticated access obtained during assessment":
        findings.append({
            "finding": "Authenticated SSH access",
            "severity": "High",
            "impact": (
                "Compromised credentials can provide legitimate remote "
                "access to the host."
            ),
            "recommendation": (
                "Rotate compromised credentials, enforce least privilege, "
                "and review authentication and access logs."
            ),
        })

    return findings


def identify_security_controls():
    """
    Define recommended controls for protecting SSH infrastructure.
    """

    return [
        "Use strong, unique credentials.",
        "Prefer SSH key-based authentication where appropriate.",
        "Disable unnecessary password authentication.",
        "Restrict SSH access through network-level controls.",
        "Apply least privilege to SSH-enabled accounts.",
        "Disable unnecessary SSH accounts.",
        "Keep the SSH service and operating system patched.",
        "Monitor authentication attempts and successful logins.",
        "Implement appropriate brute-force protection.",
        "Rotate credentials following a confirmed compromise.",
    ]


def generate_report(access, findings, controls):
    """
    Generate a sanitized SSH security assessment report.
    """

    print("=" * 70)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 08: SSH ACCESS ANALYSIS")
    print("=" * 70)

    print("\nSSH Service")
    print("-" * 70)
    print(f"Service: {access['service']}")
    print(f"Port: {access['port']}")
    print(f"State: {access['state']}")
    print(f"Authentication: {access['authentication_method']}")
    print(f"Access status: {access['access_status']}")

    print("\nSecurity Findings")
    print("-" * 70)

    for number, finding in enumerate(findings, start=1):
        print(f"\nFinding {number}: {finding['finding']}")
        print(f"Severity: {finding['severity']}")
        print(f"Impact: {finding['impact']}")
        print(f"Recommendation: {finding['recommendation']}")

    print("\nRecommended SSH Security Controls")
    print("-" * 70)

    for control in controls:
        print(f"- {control}")


def main():
    access = define_ssh_access()
    findings = analyze_ssh_security(access)
    controls = identify_security_controls()

    generate_report(
        access,
        findings,
        controls
    )


if __name__ == "__main__":
    main()
