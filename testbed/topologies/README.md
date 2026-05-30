# Reference Topologies

This directory holds the 4 reference topologies used by the NetAgent benchmark.

| ID | Name | Description |
|----|------|-------------|
| T1 | Enterprise | 2 cores + 2 access switches, single OSPF area |
| T2 | Service Provider | 4-router BGP/OSPF backbone (iBGP + eBGP) |
| T3 | Datacenter | Leaf-spine with L2/L3 boundary |
| T4 | Mixed | Combined BGP + OSPF + VLANs |

Each topology is defined as a CML YAML file plus an accompanying `testbed.yaml`
(pyATS format) describing device credentials and connectivity for the agent.

## Files (to be added in Week 2)
- `T1_enterprise.yaml` — CML topology
- `T1_testbed.yaml` — pyATS testbed
- `T2_sp.yaml`, `T2_testbed.yaml`
- `T3_dc.yaml`, `T3_testbed.yaml`
- `T4_mixed.yaml`, `T4_testbed.yaml`
