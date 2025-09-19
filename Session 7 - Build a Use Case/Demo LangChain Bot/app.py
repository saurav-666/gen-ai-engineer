from flask import Flask, Response, request, render_template, jsonify, session
import asyncio
from langchain_bot import chatbot

app = Flask(__name__)
app.secret_key = "secret"

# Function to convert async generator into a synchronous generator
def async_to_sync(generator):
    try:
        # Try to get the existing event loop
        loop = asyncio.get_event_loop()
    except RuntimeError:
        # If no event loop is found, create a new one for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    async_gen = generator.__aiter__()

    while True:
        try:
            # Fetch the next item from the async generator
            item = loop.run_until_complete(async_gen.__anext__())
            yield item
        except StopAsyncIteration:
            break

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    query = data.get("input", "")

    if not query:
        return Response("No input provided", status=400)

    # Store query or prepare some session state if needed
    # Can be saved in memory or database as per your requirement
    session['query'] = query
    return jsonify({"message": "Input received!"}), 200

# Flask route that streams chat messages as they are generated
@app.route('/stream', methods=['GET'])
def stream():
    query = session.get('query')  # Retrieve the query from session

    if not query:
        return Response("No input provided", status=400)

    # Streaming the chat using SSE, wrapping async generator with sync converter
    def generate():
        for chunk in async_to_sync(chatbot(query)):
            yield f"data: {chunk}\n\n"  # SSE format
        # Signal the end of the stream
        yield "data: [END]\n\n"

    # Streaming the chat using SSE
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
