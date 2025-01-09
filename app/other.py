from kivy.app import App
from kivy.uix.webview import WebView
import subprocess

class WebApp(App):
    def build(self):
        # Start the Flask server in the background
        subprocess.Popen(["python3", "app.py"])

        # Create a WebView and set its source to the Flask server URL
        webview = WebView()
        webview.source = "http://127.0.0.1:5000"  # Flask server URL
        return webview

if __name__ == '_main_':
    WebApp().run()