from model import build_bayesian_network, ModelInference

if __name__ == "__main__":
    model = build_bayesian_network()

    result_no_evidence = ModelInference(model)
    print("Inference without evidence:")
    print(result_no_evidence)

    evidence = {"MSTeams": "on"}
    result_with_evidence = ModelInference(model, evidence)
    print("\nInference with evidence (MSteams is on):")
    print(result_with_evidence)