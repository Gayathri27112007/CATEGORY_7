# Map Coloring using Constraint Satisfaction Problem

## AI Course – II AIML/REC

### Category 7 – Constraint Satisfaction Problems

### Task 1 – Map Coloring

---

## Aim

To implement the **Map Coloring problem** using a **Constraint Satisfaction Problem (CSP)**.

---

## What is CSP?

A Constraint Satisfaction Problem consists of:

1. Variables
2. Domains
3. Constraints

For this problem:

* **Variables** → States
* **Domain** → Available colors
* **Constraint** → Neighboring states must have different colors

---

## Problem

The program has four states:

```text
A, B, C, D
```

Available colors:

```text
Red, Green, Blue
```

Two neighboring states cannot have the same color.

---

## Example Map

```text
       A
      / \
     B---C
      \ /
       D
```

---

## Algorithm

1. Select a state.
2. Try a color.
3. Check whether the color violates any constraint.
4. If the color is valid, assign it.
5. Move to the next state.
6. If no color is possible, backtrack.
7. Continue until all states are colored.

---

## Technique Used

**Backtracking**

Backtracking removes an incorrect assignment and tries another possible assignment.

---

## Example Output

```text
Map Coloring using CSP
----------------------
A -> Red
B -> Green
C -> Blue
D -> Red
```

---

## Conclusion

The Map Coloring problem was successfully implemented using a Constraint Satisfaction Problem and backtracking technique.
