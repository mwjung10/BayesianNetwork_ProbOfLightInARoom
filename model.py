from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD


def build_bayesian_network():
    model = DiscreteBayesianNetwork([("Room", "Light"), ("Room", "MSTeams")])

    model.add_cpds(
        TabularCPD(
            variable="Room",
            variable_card=2,
            values=[[0.6], [0.4]],
        )
    )

