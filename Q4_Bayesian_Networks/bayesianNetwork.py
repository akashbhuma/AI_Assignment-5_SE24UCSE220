import warnings
warnings.filterwarnings("ignore")

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


print(" BAYESIAN NETWORK FOR LOAN APPROVAL ")


model = DiscreteBayesianNetwork([
    ("Income", "LoanApproval"),
    ("CreditScore", "LoanApproval"),
    ("EmploymentStatus", "LoanApproval")
])

print("Network Structure Created")

cpd_income = TabularCPD(
    variable="Income",
    variable_card=2,
    values=[[0.4], [0.6]]
)

cpd_credit = TabularCPD(
    variable="CreditScore",
    variable_card=2,
    values=[[0.3], [0.7]]
)

cpd_employment = TabularCPD(
    variable="EmploymentStatus",
    variable_card=2,
    values=[[0.2], [0.8]]
)

cpd_loan = TabularCPD(
    variable="LoanApproval",
    variable_card=2,
    values=[
        [0.98, 0.85, 0.80, 0.65, 0.75, 0.60, 0.50, 0.10],
        [0.02, 0.15, 0.20, 0.35, 0.25, 0.40, 0.50, 0.90]
    ],
    evidence=["Income", "CreditScore", "EmploymentStatus"],
    evidence_card=[2, 2, 2]
)

model.add_cpds(
    cpd_income,
    cpd_credit,
    cpd_employment,
    cpd_loan
)

print("Conditional Probability Tables Added")

if model.check_model():
    print("Model Validation Successful\n")

infer = VariableElimination(model)

print("Evidence Provided:")
print("Income = High")
print("Credit Score = Good")
print("Employment Status = Employed\n")

result = infer.query(
    variables=["LoanApproval"],
    evidence={
        "Income": 1,
        "CreditScore": 1,
        "EmploymentStatus": 1
    }
)

print("Inference Result:")

print(result)

print("\nConclusion:")
print("The Bayesian Network predicts the probability")
print("of Loan Approval based on the given evidence.")
