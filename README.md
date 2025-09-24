[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Y0K_x94e)
# Event Waitlist Manager (SLL)

## Story (why this matters)
Your club’s free workshop filled up fast. You’re running the **waitlist**: people
join at the end, may cancel, and sometimes a staffer **bumps** someone to the
**front** (VIP, accessibility). You need a tiny waitlist that stays correct.

## Technical description (what to build)
Implement a **singly linked list**–backed `Waitlist` in `src/waitlist.py` with:

- `__len__(self)` → number of people
- `to_list(self)` → names from head to tail
- `join(self, name)` → append at tail (**O(1)**)
- `find(self, name)` → `True/False`
- `cancel(self, name)` → remove first match; return `True` if removed
- `bump(self, name)` → move first match to **head**; return `True` if moved

Target performance: `join` is **O(1)** (track `tail`), `cancel`/`bump` are **O(N)**
to search and **O(1)** to relink.

## Hints
1. Handle **empty** and **single-element** lists explicitly.
2. On `cancel`, if you remove the **tail**, remember to move the `tail` pointer.
3. On `bump`, **unlink** the node first, then insert it at **head**.

## Run tests locally
```bash
python -m pytest -q

OR

python -m pytest -q tests/test_waitlist.py
```
## Common problems
- Running tests from the wrong folder (run from the repo root).

- Not updating tail when deleting the last element.

- Forgetting to update the size after insert/delete.

- Returning None instead of True/False in cancel/bump.