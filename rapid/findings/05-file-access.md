# Finding 05 — File Access & Permission Security Assessment

## Assessment Area

**File Access Control & Filesystem Permissions**

## Objective

The file-access assessment evaluated whether files and directories within the assessed environment were appropriately protected against unauthorized reading, modification, or execution.

The objective was to identify excessive permissions and determine whether filesystem access was consistent with the principle of least privilege.

---

## Assessment Approach

The assessment considered:

1. File and directory permissions.
2. Ownership relationships.
3. User access.
4. Group access.
5. Writable locations.
6. Executable permissions.
7. Sensitive file exposure.
8. Service-account permissions.
9. Privilege boundaries.

The results were correlated with the subsequent writable-directory and privilege-escalation analysis.

---

## Security Considerations

Filesystem permissions are an important security boundary.

Incorrect permissions can allow a user or compromised service to:

- Read sensitive information
- Modify protected files
- Replace legitimate application content
- Write executable content
- Modify configuration files
- Influence privileged processes
- Establish a pathway toward privilege escalation

The presence of a writable file or directory does not automatically constitute a vulnerability. Its security impact depends on ownership, execution context, privileges, and how the resource is used.

---

## Least Privilege

Files and directories should follow the principle of least privilege.

Access should be granted only when required by:

- The user
- The application
- The service
- The operating system component

Unnecessary write permissions should be removed because write access can create a greater security impact than read-only access.

---

## Sensitive Resources

Particular attention should be given to resources containing:

- Authentication information
- Application configuration
- Security configuration
- Credentials
- Private keys
- Logs
- Backups
- Service configuration
- Executable components

Sensitive resources should not be accessible to unauthorized users or low-privileged services.

---

## Writable Locations

Writable directories require additional review.

Security teams should determine:

- Who owns the directory.
- Which users can write to it.
- Whether privileged processes use its contents.
- Whether executable content can be placed there.
- Whether files can be replaced or modified.
- Whether inherited permissions create unintended access.

A writable location becomes more significant when a privileged process subsequently trusts or executes content from that location.

---

## Security Impact

Excessive filesystem permissions may lead to:

- Unauthorized information disclosure
- Unauthorized file modification
- Application tampering
- Configuration manipulation
- Malicious content placement
- Persistence opportunities
- Privilege escalation

The final severity should be determined based on the affected resource and privilege context.

---

## Recommended Remediation

Organizations should:

- Apply least-privilege permissions.
- Review filesystem ownership.
- Remove unnecessary write permissions.
- Restrict sensitive directories.
- Separate application and administrative privileges.
- Review service-account permissions.
- Protect executable files.
- Secure configuration files.
- Monitor sensitive filesystem changes.
- Conduct periodic permission audits.

---

## Validation

After remediation, security teams should verify that:

- Unauthorized users cannot read protected files.
- Unauthorized users cannot modify protected files.
- Sensitive directories have appropriate permissions.
- Service accounts have only required access.
- Writable directories are appropriately restricted.
- Privileged processes do not rely on untrusted writable locations.
- Filesystem changes are appropriately monitored.

---

## Risk Considerations

Risk should be evaluated using:

- Permission level
- Resource sensitivity
- Ownership
- Process privileges
- Execution context
- Network exposure
- Potential impact
- Availability of compensating controls

---

## Related Assessment Modules

- [`06_file_access_analysis.py`](../06_file_access_analysis.py)
- [`07_writable_directory_analysis.py`](../07_writable_directory_analysis.py)
- [`12_privilege_escalation_analysis.py`](../12_privilege_escalation_analysis.py)

---

## Evidence Handling

This public portfolio version has been sanitized.

The repository does not contain:

- Client identifiers
- Target IP addresses
- Internal hostnames
- Credentials
- Private keys
- Authentication tokens
- Sensitive file contents
- Confidential screenshots

Technical evidence has been generalized where necessary.

---

## Status

**Assessment Stage:** Completed

**Portfolio Classification:** Sanitized security assessment documentation
