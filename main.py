import socketio
from website import createApp
app = createApp()

if __name__ == "__main__":
    app.run(app)