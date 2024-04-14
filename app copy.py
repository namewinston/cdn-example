from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Define the directory to serve static files from
public_dir = os.path.join(os.getcwd(), 'static')

@app.route('/<path:filename>')
def serve_file(filename):
    # Add caching headers to the response: cache for 1 day
    response = send_from_directory(public_dir, filename)
    response.headers['Cache-Control'] = 'public, max-age=86400'
    return response

if __name__ == '__main__':
    # Run the server
    app.run(port=3000, debug=True)
