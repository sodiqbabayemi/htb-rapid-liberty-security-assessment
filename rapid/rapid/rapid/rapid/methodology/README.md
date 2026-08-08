# Rapid Security Assessment Methodology

## Overview

The Rapid assessment followed a structured security-assessment methodology designed to move from initial attack-surface discovery toward vulnerability analysis, access assessment, post-exploitation review, and privilege-boundary analysis.

The methodology was organized into sequential assessment phases, with observations from earlier phases informing subsequent testing and analysis.

---

## Phase 1 — Reconnaissance

### Objective

Establish an understanding of the available attack surface.

### Activities

- Identify exposed services.
- Review available service information.
- Determine potential entry points.
- Establish areas requiring deeper investigation.

### Output

A preliminary attack-surface overview used to guide subsequent enumeration.

---

## Phase 2 — Service Enumeration

### Objective

Obtain additional information about identified services and determine their security relevance.

### Activities

- Analyze exposed services.
- Review service configurations.
- Identify authentication mechanisms.
- Determine accessible functionality.
- Identify potential security weaknesses.

### Output

Service-specific assessment information.

---

## Phase 3 — Access Analysis

### Objective

Determine whether exposed services and resources enforce appropriate authentication and authorization controls.

### Activities

- Review authentication requirements.
- Review access restrictions.
- Analyze file and directory permissions.
- Evaluate user and service access.
- Identify excessive permissions.

### Output

Access-control observations and potential security risks.

---

## Phase 4 — Vulnerability Analysis

### Objective

Identify security weaknesses that could affect confidentiality, integrity, or availability.

### Activities

- Correlate service information with identified weaknesses.
- Evaluate configuration issues.
- Assess potential attack paths.
- Determine potential impact.
- Develop remediation recommendations.

### Output

Structured vulnerability observations.

---

## Phase 5 — File and Path Security

### Objective

Assess whether applications and system resources adequately protect filesystem boundaries.

### Activities

- Review file-access controls.
- Assess directory permissions.
- Evaluate path-handling controls.
- Review writable locations.
- Assess sensitive-resource exposure.

### Output

Filesystem and path-security findings.

---

## Phase 6 — SSH Security

### Objective

Evaluate the security of remote administrative access.

### Activities

- Review authentication controls.
- Assess privileged access.
- Review SSH configuration.
- Consider cryptographic controls.
- Evaluate logging and monitoring.
- Review access restrictions.

### Output

SSH security observations and hardening recommendations.

---

## Phase 7 — Post-Exploitation Analysis

### Objective

Determine the potential security impact following an initial foothold.

### Activities

- Establish current user context.
- Review system information.
- Review processes and services.
- Analyze network context.
- Review accessible resources.
- Identify privilege boundaries.
- Identify potential additional attack paths.

### Output

Post-compromise security-impact assessment.

---

## Phase 8 — Privilege Escalation Analysis

### Objective

Determine whether privilege boundaries could potentially be weakened or bypassed.

### Activities

- Review administrative permissions.
- Analyze writable resources.
- Review privileged services.
- Examine scheduled tasks.
- Assess service-account permissions.
- Review credential exposure.
- Identify potential escalation conditions.

### Output

Privilege-escalation observations and remediation recommendations.

---

# Risk Analysis

Security observations should be evaluated according to factors including:

- Likelihood
- Impact
- Exploitability
- Exposure
- Required privileges
- Existing controls
- Potential business consequences

A technical weakness should therefore be considered in the context of the surrounding security controls rather than in isolation.

---

# Evidence Management

Assessment evidence should be collected and stored securely.

Evidence may include:

- Service information
- Configuration observations
- Security logs
- Screenshots
- Assessment notes
- Tool output
- Finding references

For public portfolio presentation, sensitive evidence must be sanitized before publication.

---

# Remediation Lifecycle

The assessment follows a continuous improvement model:

```text
Identify
   ↓
Assess
   ↓
Document
   ↓
Prioritize
   ↓
Remediate
   ↓
Validate
   ↓
Monitor
   ↓
Reassess
