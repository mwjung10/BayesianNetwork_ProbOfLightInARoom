from model import build_bayesian_network, model_inference

if __name__ == "__main__":
    model = build_bayesian_network()

    variables = ["Light"]
    result_no_evidence = model_inference(model, variables)
    print("Inference without evidence:")
    print(result_no_evidence)

    evidence = {"MSTeams": "on"}
    result_with_evidence = model_inference(model, variables, evidence)
    print("\nInference with evidence (MSteams is on):")
    print(result_with_evidence)
