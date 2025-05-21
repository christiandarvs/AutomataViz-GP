from graphviz import Digraph
import streamlit as st
import time


regex_options = [
    "--- Select ---",
    "(a+b)* (aa+bb) (aa+bb)* (ab+ba+aba) (bab+aba+bbb) (a+b+bb+aa)* (bb+aa+aba) (aaa+bab+bba) (aaa+bab+bba)*",
    "(1+0)* (11+00+101+010) (11+00)* (11+00+0+1) (1+0+11) (11+00)* (101+000+111) (1+0)* (101+000+111+001+100) (11+00+1+0)*",
]

"""
(1+0)* (11+00+101+010) (11+00)* (11+00+0+1) (1+0+11) (11+00)* (101+000+111) (1+0)* (101+000+111+001+100) (11+00+1+0)*


(a+b)* (aa+bb) (aa+bb)* (ab+ba+aba) (bab+aba+bbb) (a+b+bb+aa)* (bb+aa+aba) (aaa+bab+bba) (aaa+bab+bba)*
"""

# DFA for (a+b)* (aa+bb) (aa+bb)* (ab+ba+aba) (bab+aba+bbb) (a+b+bb+aa)* (bb+aa+aba) (aaa+bab+bba) (aaa+bab+bba)*
dfa_1 = {
    "states": [
        "0",
        "1",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "2",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "3",
        "30",
        "31",
        "32",
        "33",
        "34",
        "35",
        "36",
        "37",
        "38",
        "39",
        "4",
        "40",
        "41",
        "42",
        "43",
        "44",
        "45",
        "5",
        "6",
        "7",
        "8",
        "9",
    ],
    "alphabet": ["a", "b"],
    "start_state": "0",
    "end_states": ["1", "13", "2", "5", "9"],
    "transitions": {
        ("0", "a"): "44",
        ("0", "b"): "45",
        ("1", "a"): "15",
        ("1", "b"): "8",
        ("10", "a"): "4",
        ("10", "b"): "17",
        ("11", "a"): "3",
        ("11", "b"): "21",
        ("12", "a"): "3",
        ("12", "b"): "1",
        ("13", "a"): "7",
        ("13", "b"): "10",
        ("14", "a"): "7",
        ("14", "b"): "9",
        ("15", "a"): "7",
        ("15", "b"): "10",
        ("16", "a"): "11",
        ("16", "b"): "8",
        ("17", "a"): "13",
        ("17", "b"): "8",
        ("18", "a"): "15",
        ("18", "b"): "10",
        ("19", "a"): "20",
        ("19", "b"): "16",
        ("2", "a"): "2",
        ("2", "b"): "10",
        ("20", "a"): "18",
        ("20", "b"): "21",
        ("21", "a"): "18",
        ("21", "b"): "16",
        ("22", "a"): "20",
        ("22", "b"): "19",
        ("23", "a"): "22",
        ("23", "b"): "43",
        ("24", "a"): "39",
        ("24", "b"): "22",
        ("25", "a"): "38",
        ("25", "b"): "23",
        ("26", "a"): "24",
        ("26", "b"): "40",
        ("27", "a"): "24",
        ("27", "b"): "22",
        ("28", "a"): "22",
        ("28", "b"): "40",
        ("29", "a"): "25",
        ("29", "b"): "32",
        ("3", "a"): "13",
        ("3", "b"): "10",
        ("30", "a"): "25",
        ("30", "b"): "28",
        ("31", "a"): "25",
        ("31", "b"): "22",
        ("32", "a"): "31",
        ("32", "b"): "27",
        ("33", "a"): "30",
        ("33", "b"): "41",
        ("34", "a"): "25",
        ("34", "b"): "26",
        ("35", "a"): "29",
        ("35", "b"): "35",
        ("36", "a"): "29",
        ("36", "b"): "22",
        ("37", "a"): "39",
        ("37", "b"): "33",
        ("38", "a"): "38",
        ("38", "b"): "33",
        ("39", "a"): "38",
        ("39", "b"): "42",
        ("4", "a"): "15",
        ("4", "b"): "9",
        ("40", "a"): "37",
        ("40", "b"): "22",
        ("41", "a"): "24",
        ("41", "b"): "36",
        ("42", "a"): "34",
        ("42", "b"): "43",
        ("43", "a"): "37",
        ("43", "b"): "35",
        ("44", "a"): "39",
        ("44", "b"): "45",
        ("45", "a"): "44",
        ("45", "b"): "43",
        ("5", "a"): "7",
        ("5", "b"): "9",
        ("6", "a"): "5",
        ("6", "b"): "6",
        ("7", "a"): "2",
        ("7", "b"): "10",
        ("8", "a"): "12",
        ("8", "b"): "6",
        ("9", "a"): "14",
        ("9", "b"): "6",
    },
}

# DFA for (1+0)* (11+00+101+010) (11+00)* (11+00+0+1) (1+0+11) (11+00)* (101+000+111) (1+0)* (101+000+111+001+100) (11+00+1+0)*
dfa_2 = {
    "states": [
        "0",
        "1",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "2",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "3",
        "30",
        "31",
        "32",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ],
    "alphabet": ["0", "1"],
    "start_state": "0",
    "end_states": ["1"],
    "transitions": {
        ("0", "0"): "29",
        ("0", "1"): "31",
        ("1", "0"): "1",
        ("1", "1"): "1",
        ("10", "0"): "12",
        ("10", "1"): "6",
        ("11", "0"): "8",
        ("11", "1"): "17",
        ("12", "0"): "8",
        ("12", "1"): "6",
        ("13", "0"): "12",
        ("13", "1"): "10",
        ("14", "0"): "11",
        ("14", "1"): "9",
        ("15", "0"): "8",
        ("15", "1"): "9",
        ("16", "0"): "18",
        ("16", "1"): "13",
        ("17", "0"): "15",
        ("17", "1"): "13",
        ("18", "0"): "8",
        ("18", "1"): "13",
        ("19", "0"): "14",
        ("19", "1"): "16",
        ("2", "0"): "3",
        ("2", "1"): "1",
        ("20", "0"): "22",
        ("20", "1"): "13",
        ("21", "0"): "16",
        ("21", "1"): "16",
        ("22", "0"): "8",
        ("22", "1"): "16",
        ("23", "0"): "16",
        ("23", "1"): "20",
        ("24", "0"): "16",
        ("24", "1"): "17",
        ("25", "0"): "24",
        ("25", "1"): "19",
        ("26", "0"): "23",
        ("26", "1"): "21",
        ("27", "0"): "24",
        ("27", "1"): "21",
        ("28", "0"): "21",
        ("28", "1"): "21",
        ("29", "0"): "25",
        ("29", "1"): "30",
        ("3", "0"): "1",
        ("3", "1"): "1",
        ("30", "0"): "27",
        ("30", "1"): "26",
        ("31", "0"): "32",
        ("31", "1"): "26",
        ("32", "0"): "25",
        ("32", "1"): "28",
        ("4", "0"): "3",
        ("4", "1"): "5",
        ("5", "0"): "3",
        ("5", "1"): "2",
        ("6", "0"): "4",
        ("6", "1"): "5",
        ("7", "0"): "18",
        ("7", "1"): "6",
        ("8", "0"): "6",
        ("8", "1"): "13",
        ("9", "0"): "7",
        ("9", "1"): "7",
    },
}

# CFG for (a+b)* (aa+bb) (aa+bb)* (ab+ba+aba) (bab+aba+bbb) (a+b+bb+aa)* (bb+aa+aba) (aaa+bab+bba) (aaa+bab+bba)*
cfg_1 = """
    S -> aS | bS | aaA | bbA \n
    A -> AAa | bbA | abB | baB | abaB \n
    B -> babC | abaC | bbbC \n
    C -> aC | bC | bbC | aaC | D \n
    D -> bbE | aaE | abaE \n
    F -> aaaF | babF | bbaF | ^
"""

# CFG for (1+0)* (11+00+101+010) (11+00)* (11+00+0+1) (1+0+11) (11+00)* (101+000+111) (1+0)* (101+000+111+001+100) (11+00+1+0)*
cfg_2 = """
    S -> 1S | 0S | 11A | 00A | 101A | 010A \n
    A -> 11A | 00A | B \n
    B -> 11C | 00C | 0C | 1C \n
    C -> 1D | 0D | 11D \n
    D -> 11D | 00D | 100E | 000E | 111E \n
    E -> 1E | 0E | 101F | 000F | 111F | 001F | 100F \n
    F -> 11F | 00F | 1F | 0F | ^
"""


# Generate DFA visualization using Graphviz
def generate_dfa_visualization(dfa):
    graph_attr = {
        "rankdir": "LR",
        "nodesep": "0.5",
        "ranksep": "0.75",
        # "concentrate": "true",
    }

    dot = Digraph(
        engine="dot",
        graph_attr=graph_attr,
        node_attr={
            "fontsize": "18",
            "width": "0.5",
            "height": "0.5",
            "fixedsize": "true",
        },
        edge_attr={"fontsize": "18"},
    )

    dot.node("", shape="none")  # Invisible start arrow
    dot.edge("", dfa["start_state"])

    for state in dfa["states"]:
        shape = "doublecircle" if state in dfa["end_states"] else "circle"
        dot.node(state, shape=shape)

    # Group transitions with same source & target
    grouped_transitions = {}
    for (src, sym), dst in dfa["transitions"].items():
        key = (src, dst)
        grouped_transitions.setdefault(key, []).append(sym)

    for (src, dst), symbols in grouped_transitions.items():
        dot.edge(src, dst, label=",".join(symbols))

    return dot


# Generate PDA visualization using Graphviz
def generate_pda_visualization(pda):
    dot = Digraph(engine="dot", renderer="gd")

    # Add graph nodes for the states
    for state in pda["states"]:
        if state in pda["start_state"] or state in pda["accept_states"]:
            dot.node(state, shape="ellipse")
        elif state in pda["push_states"]:
            dot.node(state, shape="rectangle")
        else:
            dot.node(state, shape="diamond")

    # Add edges/transitions
    for transition, target_state in pda["transitions"].items():
        source_state, symbol = transition
        dot.edge(source_state, target_state, label=symbol)

    # Return the Graphviz graph for the DFA visualization
    return dot


# Validate given string for DFA
def validate_dfa(dfa, string):
    state_checks = []
    current_state = dfa["start_state"]

    # Iterate through each character in string
    for char in string:
        # Check if transition has "0,1", if so replace char with "0,1"
        if (current_state, "0,1") in dfa["transitions"].keys():
            char = "0,1"

        # Check if transition has "a,b", if so replace char with "a,b"
        if (current_state, "a,b") in dfa["transitions"].keys():
            char = "a,b"

        transition = (current_state, char)
        transition_exists = transition in dfa["transitions"].keys()
        state_checks.append((current_state, transition_exists))

        # Check if current char is in transitions
        if transition_exists:
            current_state = dfa["transitions"][transition]
        # Return False if current character in the string is not in the dfa transitions
        else:
            return (False, state_checks)

    # Add state check for last transition
    if current_state in dfa["end_states"]:
        state_checks.append((current_state, True))
    else:
        state_checks.append((current_state, False))

    result = (
        current_state in dfa["end_states"]
    )  # Checks if last current_state is in dfa end_states

    # Return the validation result and state_checks array
    return (result, state_checks)


# Generate validation animation
def animate_dfa_validation(dfa, state_checks):
    dot = generate_dfa_visualization(dfa)  # Generate the DFA visualization
    graph = st.graphviz_chart(
        dot.source,
        use_container_width=True,
    )  # Create a Streamlit Graphviz component

    # Iterate through each state in state_checks
    for state_check in state_checks:
        state, is_valid = state_check

        time.sleep(1)  # Add a delay for visualization purposes

        if is_valid and state in dfa["end_states"]:
            dot.node(state, style="filled", fillcolor="green")  # Set end state to green
            graph.graphviz_chart(
                dot.source, use_container_width=True
            )  # Render the updated visualization

        elif not is_valid:
            dot.node(state, style="filled", fillcolor="red")  # Set invalid state to red
            graph.graphviz_chart(
                dot.source, use_container_width=True
            )  # Render the updated visualization

        else:
            dot.node(state, style="filled", fillcolor="orange")
            graph.graphviz_chart(dot.source, use_container_width=True)

            time.sleep(0.5)
            dot.node(
                state, style="filled", fillcolor="white"
            )  # Set previous state back to white
            graph.graphviz_chart(
                dot.source, use_container_width=True
            )  # Render the updated visualization
