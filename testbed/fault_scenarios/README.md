# Fault Scenario Library

Each scenario is a YAML file with the schema:

```yaml
id: bgp_md5_mismatch_r1_r2
protocol: bgp
topology: T2
severity: high       # low | medium | high | critical
description: >
  BGP session between R1 and R2 fails to establish because the MD5
  authentication key on R1 was changed but R2 still uses the old key.

trigger:
  device: R1
  commands:
    - configure terminal
    - router bgp 65001
    - neighbor 10.0.0.2 password NEW_KEY_MISMATCH
    - end

ground_truth:
  root_cause: bgp.authentication.md5_mismatch
  affected_devices: [R1, R2]
  remediation:
    device: R1
    commands:
      - configure terminal
      - router bgp 65001
      - neighbor 10.0.0.2 password ORIGINAL_KEY
      - end
  verification:
    device: R1
    expect:
      - cmd: show ip bgp summary
        contains: "10.0.0.2  4  65002      Established"
```

## Counts by protocol (target = 50 total)

| Protocol | Count |
|----------|-------|
| BGP      | 15    |
| OSPF     | 15    |
| VLAN     | 10    |
| STP      | 10    |
