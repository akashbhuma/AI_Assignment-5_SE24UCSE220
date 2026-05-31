# Bayesian Network for Loan Approval Prediction

## Overview

This implements a Bayesian Network using Python and the pgmpy library to predict loan approval decisions. The model evaluates multiple applicant-related factors and uses probabilistic reasoning to determine the likelihood of loan approval.

Bayesian Networks are graphical models that represent variables and their conditional dependencies through a Directed Acyclic Graph (DAG). They are widely used in Artificial Intelligence for decision-making under uncertainty.

---

## Objective

The objective of this project is to:

- Model a loan approval system using Bayesian Networks.
- Represent relationships between financial and personal factors.
- Perform probabilistic inference using evidence.
- Predict the probability of loan approval.

---

## Technologies Used

- Python 3
- pgmpy
- Bayesian Networks
- Probability Theory
- Artificial Intelligence

---

## Problem Statement

Financial institutions consider several factors before approving a loan application. These factors include:

- Income
- Credit Score
- Employment Status
- Age
- Existing Debt

The Bayesian Network combines these factors and predicts whether a loan is likely to be approved or rejected.

---

## Network Structure

The Bayesian Network consists of six nodes.

### Input Variables

1. Income
2. Credit Score
3. Employment Status
4. Age
5. Existing Debt

### Output Variable

6. Loan Approval


## Variable Representation

### Income

| Value | Meaning |
|---------|---------|
| 0 | Low Income |
| 1 | High Income |

### Credit Score

| Value | Meaning |
|---------|---------|
| 0 | Poor Credit Score |
| 1 | Good Credit Score |

### Employment Status

| Value | Meaning |
|---------|---------|
| 0 | Unemployed |
| 1 | Employed |

### Age

| Value | Meaning |
|---------|---------|
| 0 | Young Applicant |
| 1 | Adult Applicant |

### Existing Debt

| Value | Meaning |
|---------|---------|
| 0 | Low Debt |
| 1 | High Debt |

### Loan Approval

| Value | Meaning |
|---------|---------|
| 0 | Loan Rejected |
| 1 | Loan Approved |

---

## Bayesian Network Components

### Prior Probability Tables

The following variables have predefined probability distributions:

- Income
- Credit Score
- Employment Status
- Age
- Existing Debt

### Conditional Probability Table (CPT)

Loan Approval depends on:

- Income
- Credit Score
- Employment Status
- Age
- Existing Debt

## Evidence Used

The following evidence is provided to the inference engine:

```text
Income = High
Credit Score = Good
Employment Status = Employed
Age = Adult
Existing Debt = Low
```

The Bayesian Network computes:

```text
P(LoanApproval | Income, CreditScore,
EmploymentStatus, Age, ExistingDebt)
```

---

## Working Procedure

### Step 1

Create the Bayesian Network structure.

### Step 2

Define the probability distributions for all input variables.

### Step 3

Create the Conditional Probability Table for Loan Approval.

### Step 4

Add all probability tables to the model.

### Step 5

Validate the Bayesian Network.

### Step 6

Provide evidence values.

### Step 7

Perform inference using the Variable Elimination algorithm.

### Step 8

## Sample Output

```text
BAYESIAN NETWORK FOR LOAN APPROVAL SYSTEM

Network Structure Created

Conditional Probability Tables Added

Model Validation Successful

Evidence Provided:
Income            : High
Credit Score      : Good
Employment Status : Employed
Age               : Adult
Existing Debt     : Low

Inference Result:

+-----------------+---------------------+
| LoanApproval    | phi(LoanApproval)   |
+=================+=====================+
| LoanApproval(0) | 0.9000              |
+-----------------+---------------------+
| LoanApproval(1) | 0.1000              |
+-----------------+---------------------+

Variable Meaning:
Income            : 0 = Low, 1 = High
Credit Score      : 0 = Poor, 1 = Good
Employment Status : 0 = Unemployed, 1 = Employed
Age               : 0 = Young, 1 = Adult
Existing Debt     : 0 = Low Debt, 1 = High Debt
Loan Approval     : 0 = Rejected, 1 = Approved
```

---
## Installation

Install the required library:

```bash
pip install pgmpy
```

---

## How to Run

Execute the program using:

```bash
python bayesianNetworks.py
```

The system will create the Bayesian Network, validate the model, perform inference, and display the loan approval probabilities.

---
