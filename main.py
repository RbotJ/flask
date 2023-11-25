from app import app  # Import the app from your .app file
import os

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
