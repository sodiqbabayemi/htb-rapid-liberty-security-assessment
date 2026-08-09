"""
Rapid Security Assessment
Module 08: SSH Access Analysis

This module documents the SSH access stage of the Rapid
assessment and the security implications of credentials
obtained during the earlier assessment stage.

The public version has been sanitized. Usernames, passwords,
private keys, target addresses, flags, and exploitation commands
have been removed.
"""


def get_ssh_access():
    """Return the SSH access condition recorded during assessment."""

    return {
        "service": "SSH",
        "port": 22,
        "state": "open",
        "authentication_method": "Credential-based",
        "access_status": "Authenticated access obtained during assessment",
    }


def assess_ssh_security(access):
    """Review the SSH exposure and access condition."""

    findings = []

    if access["state"] == "open":
        findings.append(
            {
                "finding": "SSH service exposed",
                "severity": "Medium",
                "impact": (
                    "An exposed SSH service makes strong authentication, "
                    "access restrictions, and monitoring important."
                ),
                "recommendation": (
                    "Restrict SSH exposure to trusted networks where "
                    "possible and enforce strong authentication controls."
                ),
            }
        )

    if access["access_status"] == (
        "Authenticated access obtained during assessment"
    ):
        findings.append(
            {
                "finding": "Authenticated SSH access",
                "severity": "High",
                "impact": (
                    "Compromised credentials can provide legitimate "
                    "remote access to the host."
                ),
                "recommendation": (
                    "Rotate compromised credentials, enforce least "
                    "privilege, and review authentication logs."
                ),
            }
        )

    return findings


def get_ssh_security_controls():
    """Return recommended controls for securing SSH."""

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
        "Rotate credentials after a confirmed compromise.",
    ]


def display_report(access, findings, controls):
    """Print the SSH assessment results."""

    print("\n" + "=" * 70)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 08 — SSH ACCESS ANALYSIS")
    print("=" * 70)

    print("\nSSH service")
    print("-" * 70)
    print(f"Service             : {access['service']}")
    print(f"Port                : {access['port']}")
    print(f"State               : {access['state']}")
    print(f"Authentication      : {access['authentication_method']}")
    print(f"Access status       : {access['access_status']}")

    print("\nSecurity findings")
    print("-" * 70)

    for number, finding in enumerate(findings, start=1):
        print(f"\nFinding {number}: {finding['finding']}")
        print(f"Severity       : {finding['severity']}")
        print(f"Impact         : {finding['impact']}")
        print(f"Recommendation : {finding['recommendation']}")

    print("\nRecommended SSH security controls")
    print("-" * 70)

    for control in controls:
        print(f"- {control}")

    print("\n" + "=" * 70)


def main():
    access = get_ssh_access()
    findings = assess_ssh_security(access)
    controls = get_ssh_security_controls()

    display_report(
        access,
        findings,
        controls,
    )


if __name__ == "__main__":
    main()
