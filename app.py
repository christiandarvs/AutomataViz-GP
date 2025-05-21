import streamlit as st
import utils


def main():
    st.set_page_config(page_title="AutomataViz", layout="wide")

    # Initialize streamlit session state values
    if len(st.session_state) == 0:
        st.session_state.disabled = True
        st.session_state.placeholder_text = ""

    # Callback function for regex_input
    def regex_input_callbk():
        # Set disable for string_input and validate_button
        if st.session_state.regex_input == "--- Select ---":
            st.session_state.disabled = True
        else:
            st.session_state.disabled = False

        # Set placeholder text for string_input
        if st.session_state.regex_input == utils.regex_options[1]:
            st.session_state.placeholder_text = "aaababaaabab"
        elif st.session_state.regex_input == utils.regex_options[2]:
            st.session_state.placeholder_text = "1111000111"
        else:
            st.session_state.placeholder_text = ""

        # Clear string_input
        st.session_state.string_input = ""

    title_con = st.container()
    st.divider()
    regex_to_dfa_con = st.container()
    cfg_and_pda_exp = st.expander("Show CFG and PDA Conversion")

    with title_con:
        st.title("AutomataViz")
        st.markdown(
            """
            **Contributors** 
            - John Rafael Batino
            - Yuri Anton Cariscal
            - Christian Elijah Darvin
            - Renz Aaron Paulan
            """
        )
        col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Available Conversions**")
        st.markdown(
            """
        1. Regular Expression to Deterministic Finite Automaton
        2. Regular Expression to Context Free Grammar
        3. Regular Expression to Push Down Automaton
        """
        )

    with col2:
        st.markdown("**Regular Expressions**")
        st.markdown(
            """
        1. `(a+b)* (aa+bb) (aa+bb)* (ab+ba+aba) (bab+aba+bbb) (a+b+bb+aa)* (bb+aa+aba) (aaa+bab+bba) (aaa+bab+bba)*`
        2. `(1+0)* (11+00+101+010) (11+00)* (11+00+0+1) (1+0+11) (11+00)* (101+000+111) (1+0)* (101+000+111+001+100) (11+00+1+0)*`
        """
        )

    # Code block for regex to dfa feature
    with regex_to_dfa_con:
        regex_input = st.selectbox(
            label="Regular Expression",
            options=utils.regex_options,
            key="regex_input",
            on_change=regex_input_callbk,
        )

        string_input = st.text_input(
            label="Enter a string: ",
            key="string_input",
            disabled=st.session_state.disabled,
            placeholder=st.session_state.placeholder_text,
        )

        # Validate button to run string validation
        validate_button = st.button(
            label="Validate", disabled=st.session_state.disabled
        )

        # Output for regex_input, display dfa, cfg, and pda of selected regex
        if regex_input == utils.regex_options[1]:
            current_dfa = utils.dfa_1
            st.write("**Deterministic Finite Automaton**")
            if not string_input:
                dfa = utils.generate_dfa_visualization(current_dfa)
                st.graphviz_chart(dfa)

            with cfg_and_pda_exp:
                st.write("**Context Free Grammar**")
                st.markdown(utils.cfg_1)

                st.write("**Pushdown Automaton**")
                st.image("./images/pda_1.png")

        elif regex_input == utils.regex_options[2]:
            current_dfa = utils.dfa_2
            st.write("**Deterministic Finite Automaton**")
            if not string_input:
                dfa = utils.generate_dfa_visualization(current_dfa)
                st.graphviz_chart(dfa)

            with cfg_and_pda_exp:
                st.write("**Context Free Grammar**")
                st.markdown(utils.cfg_2)

                st.write("**Pushdown Automaton**")
                st.image("./images/pda_2.png")

        # Output for string_input, play validation animation on displayed dfa
        if validate_button or string_input:
            string_input = string_input.replace(" ", "")  # Removes any whitespaces

            # Check if string_input is empty
            if len(string_input) == 0:
                st.error("Empty/Invalid Input", icon="❌")

            # Check if string_input has characters not in the alphabet of selected regex
            elif not all(char in current_dfa["alphabet"] for char in string_input):
                st.error(
                    f"String '{string_input}' contains invalid characters, please only use characters from the alphabet: {current_dfa['alphabet']}",
                    icon="❌",
                )

            else:
                st.write(f"Entered String: `{string_input}`")
                is_valid, state_checks = utils.validate_dfa(current_dfa, string_input)
                utils.animate_dfa_validation(current_dfa, state_checks)
                if is_valid:
                    st.success(
                        f"The string '{string_input}' is valid for the DFA.", icon="✔️"
                    )
                else:
                    st.error(
                        f"The string '{string_input}' is not valid for the DFA.",
                        icon="❌",
                    )


if __name__ == "__main__":
    main()
