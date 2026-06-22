from graph import app

inputs = {
    "question": "what is langgraph?"
}

for event in app.stream(inputs):

    print("\nEVENT:")
    print(event)

result = app.invoke(
    {
        "question": "what is langgraph?"
    }
)

print("\nFINAL STATE")
print(result)