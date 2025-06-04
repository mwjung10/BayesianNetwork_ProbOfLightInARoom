from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


def build_bayesian_network():
    model = DiscreteBayesianNetwork([("Room", "Light"), ("Room", "MSTeams")])

    model.add_cpds(
        TabularCPD(
            variable="Room",
            variable_card=2,
            values=[[0.6], [0.4]],
            state_names={"Room": ["absent", "present"]}
        ),
        TabularCPD(
            variable="Light",
            variable_card=2,
            values=[[0.95, 0.5],
                    [0.05, 0.5]],
            evidence=["Room"],
            evidence_card=[2],
            state_names={
                "Light": ["off", "on"],
                "Room": ["absent", "present"]
            }
        ),
        TabularCPD(
            variable="MSTeams",
            variable_card=2,
            values=[[0.95, 0.2],
                    [0.05, 0.8]],
            evidence=["Room"],
            evidence_card=[2],
            state_names={
                "MSTeams": ["off", "on"],
                "Room": ["absent", "present"]
            }
        )
    )

    if not model.check_model():
        raise ValueError("Model is not valid. Please check the CPDs and structure.")

    return model


def ModelInference(model, evidence=None):
    infer = VariableElimination(model)
    if evidence:
        return infer.query(variables=["Light"], evidence=evidence)
    else:
        return infer.query(variables=["Light"])

