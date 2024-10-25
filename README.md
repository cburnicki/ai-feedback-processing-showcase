# User feedback message processing ai agent

This is a simple showcase project that uses different ai frameworks to process sample user feedback messages for an elearning platform and decide what actions to take.

Currently, you can run the showcase using the following frameworks:

- **[CrewAI](https://www.crewai.com/)**
- **[Ell](https://docs.ell.so/index.html)**

## Before you start

Although the ai agents can be configured to run with any LLM, by default, OpenAI's GPT is used.
Therefore, **make sure `OPENAI_API_KEY` is set**.

## Run

To start the crewai example, run:
`pdm run crewai_example`

To start the ell example, run:
`pdm run ell_example`
