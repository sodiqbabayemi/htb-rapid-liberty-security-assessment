"""
Rapid Security Assessment
Module 03: FTP Access Analysis

Purpose:
    Analyze FTP access controls and document security observations
    identified during an authorized laboratory assessment.

Source:
    Sanitized from the Rapid Hack The Box assessment.

Note:
    Target IP addresses, credentials, private keys, flags, and
    exploitation commands have intentionally been excluded.
"""


def analyze_ftp_access():
    """
    Define the FTP access conditions observed during the assessment.
    """

    return {
        "service": "FTP",
        "port": 2121,
        "anonymous_login": True,
        "authentication_required": False,
        "exposed_resources": True,
    }


def evaluate_access_control(profile):
    """
    Evaluate the security implications of the FTP configuration.
    """

    findings = []

    if profile["anonymous_login"]:
        findings.append({
            "finding": "Anonymous FTP access",
            "severity": "High",
            "impact": (
                "Unauthenticated users can interact with the FTP service."
            ),
            "recommendation": (
                "Disable anonymous access unless explicitly required."
            ),
        })

    if profile["exposed_resources"]:
        findings.append({
            "finding": "FTP resource exposure",
            "severity": "High",
            "impact": (
                "Files available through the FTP service may expose "
                "information useful for further security analysis."
            ),
            "recommendation": (
                "Restrict accessible files and review FTP directory permissions."
            ),
        })

    return findings


def generate_report(profile, findings):
    """
    Generate a sanitized security assessment report.
    """

    print("=" * 65)
    print("RAPID SECURITY ASSESSMENT")
    print("MODULE 03: FTP ACCESS ANALYSIS")
    print("=" * 65)

    print("\nService Information")
    print("-" * 65)
    print(f"Protocol: {profile['service']}")
    print(f"Port: {profile['port']}")
    print(f"Anonymous login: {profile['anonymous_login']}")
    print(f"Authentication required: {profile['authentication_required']}")

    print("\nSecurity Findings")
    print("-" * 65)

    for index, finding in enumerate(findings, start=1):
        print(f"\nFinding {index}: {finding['finding']}")
        print(f"Severity: {finding['severity']}")
        print(f"Impact: {finding['impact']}")
        print(f"Recommendation: {finding['recommendation']}")


def main():
    profile = analyze_ftp_access()
    findings = evaluate_access_control(profile)

    generate_report(profile, findings)


if __name__ == "__main__":
    main()
