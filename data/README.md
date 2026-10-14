# Sample Input Data

All times are 24-hour `HH:MM`. Quantities and capacities are in "units" of food.

| File | Purpose |
|---|---|
| `sample_input.json` | Valid dataset with 13 donations, each built to hit a specific matching scenario (below). |
| `invalid_inputs.json` | 38 cases. Each breaks exactly one validation rule and lists the error `validate_dataset` should raise. |
| `empty_input.json` | Empty donation, recipient and volunteer lists. Valid input that should produce zero assignments. |

## Scenarios in `sample_input.json`

| Donation | Area | Scenario | Expected outcome |
|---|---|---|---|
| D001 | Fullerton | Normal compatible match | Assigned to R001 with V001 |
| D002 | Anaheim | Normal compatible match | Assigned to R002 with V002 |
| D003 | Fullerton | Baked Goods, but Fullerton shelter only takes Prepared Meals | Unassigned: food type |
| D004 | Fullerton | 80 units; V003 can carry it but R001 only holds 50 | Unassigned: recipient capacity |
| D005 | Placentia | 40 units; R003 can hold it but V004 only carries 25 | Unassigned: vehicle capacity |
| D006 / D007 | Brea | Both 25 units competing for R004 (capacity 30). D006 arrives first, D007 expires sooner | FIFO picks D006; greedy picks D007 and defers D006 |
| D008 / D009 / D010 | Orange | V006 has max 2 pickups. D008 arrives first with the longest shelf life | FIFO takes D008 + D009; greedy takes D009 + D010 and D008 is starved (fairness case) |
| D011 | Fullerton | Only a 15-minute window (16:30-16:45) | Near-expiry but still assignable; top greedy priority |
| D012 | Fullerton | Ready 19:30, after the shelter closes and volunteers leave | Unassigned: no time overlap |
| D013 | Yorba Linda | No recipient or volunteer in that area | Unassigned: area mismatch |

The D006/D007 and D008-D010 outcomes depend on the FIFO and greedy schedulers tracking remaining
recipient capacity and volunteer pickups as they assign, which isn't implemented yet.
