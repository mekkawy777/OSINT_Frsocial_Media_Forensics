from osint_forensics.workflow import InvestigationWorkflow

if __name__ == "__main__":
    workflow = InvestigationWorkflow(use_selenium=False)
    result = workflow.run_demo("demo_case")
    print("Demo completed.")
    print(result["report"]["html"])
