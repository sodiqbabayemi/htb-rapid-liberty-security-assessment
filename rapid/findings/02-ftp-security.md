# Finding 02 — FTP Service Security Assessment

## Assessment Area

**FTP Enumeration & Access Security**

## Objective

The FTP assessment evaluated the security exposure associated with the identified File Transfer Protocol service.

The objective was to determine whether the service presented authentication, configuration, access-control, or information-disclosure risks that could increase the attack surface.

---

## Assessment Approach

The assessment considered:

1. Identification of the FTP service.
2. Review of the exposed service configuration.
3. Assessment of authentication requirements.
4. Review of accessible resources.
5. Evaluation of potential unauthorized access conditions.
6. Identification of security controls required to reduce exposure.

The FTP assessment was subsequently correlated with the broader vulnerability and access-control analysis.

---

## Security Considerations

FTP requires careful security management because traditional FTP communication can expose authentication and file-transfer activity when appropriate encryption is not implemented.

Security considerations include:

- Authentication controls
- Anonymous access
- File and directory permissions
- Service exposure
- Encryption
- User authorization
- Upload permissions
- Download permissions
- Logging and monitoring
- Network restrictions

---

## Authentication Assessment

Authentication controls should be reviewed to determine whether:

- Anonymous access is enabled unnecessarily.
- Weak credentials are permitted.
- Shared accounts are being used.
- Administrative accounts are exposed.
- Authentication attempts are adequately monitored.
- Access is restricted to authorized users.

Where anonymous or unnecessary access exists, the exposure should be removed unless explicitly required by the business function.

---

## File Access Assessment

FTP users should only have access to files and directories required for their authorized responsibilities.

Particular attention should be given to:

- Writable directories
- Sensitive configuration files
- Application files
- Backup files
- Credentials
- System files
- Executable content

The principle of least privilege should be applied to all FTP accounts.

---

## Encryption Considerations

Traditional FTP does not inherently provide encrypted communication.

Where sensitive information is transferred, organizations should consider secure alternatives such as:

- SFTP
- FTPS
- Secure managed file-transfer platforms

The appropriate solution should be selected according to organizational requirements and threat models.

---

## Potential Security Impact

An improperly configured FTP service may increase the risk of:

- Unauthorized file access
- Credential exposure
- Sensitive information disclosure
- Unauthorized file modification
- Malicious file upload
- Lateral movement
- Further compromise of connected systems

The actual severity depends on the configuration, accessibility, permissions, and sensitivity of the resources exposed.

---

## Recommended Remediation

Organizations should:

- Disable FTP where it is not required.
- Prefer encrypted file-transfer protocols.
- Disable unnecessary anonymous access.
- Enforce strong authentication.
- Apply least-privilege permissions.
- Restrict FTP access using network controls.
- Prevent access to sensitive system directories.
- Monitor authentication and file-transfer activity.
- Maintain centralized security logs.
- Regularly review FTP accounts and permissions.
- Remove inactive accounts.
- Apply secure configuration baselines.

---

## Validation

After remediation, administrators should verify that:

- Unauthorized users cannot authenticate.
- Anonymous access is disabled where unnecessary.
- Users can access only authorized directories.
- Sensitive files cannot be accessed through the service.
- File-upload permissions are appropriately restricted.
- Secure encryption is enforced where required.
- Authentication and file-transfer events are logged.

---

## Related Assessment Modules

- [`02_ftp_enumeration.py`](../02_ftp_enumeration.py)
- [`03_ftp_access_analysis.py`](../03_ftp_access_analysis.py)
- [`04_vulnerability_analysis.py`](../04_vulnerability_analysis.py)

---

## Evidence Handling

This public portfolio version contains no:

- Credentials
- Client identifiers
- Target IP addresses
- Internal hostnames
- Private keys
- Flags
- Confidential screenshots

Sensitive assessment evidence has been removed or generalized.

---

## Status

**Assessment Stage:** Completed

**Portfolio Classification:** Sanitized security assessment documentation
