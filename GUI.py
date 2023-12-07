from flask import Flask
import folium
import webbrowser
import threading
import tkinter as tk

app = Flask(__name__)

@app.route("/")
# This is the base map
def base():
    return generate_map([45.52336, -122.6750])

@app.route("/open-street-map")
# This map uses Stamen Toner
def open_street_map():
    m = folium.Map(
        location=[45.52336, -122.6750],
        tiles='Stamen Toner',
        zoom_start=13
    )
    folium.Marker(
        location=[45.52336, -122.6750],
        popup="<b>Marker here</b>",
        tooltip="Click Here!"
    ).add_to(m)
    return m._repr_html_()

@app.route("/map-marker")
def map_marker():
    m = folium.Map(
        location=[45.52336, -122.6750],
        tiles='Stamen Terrain',
        zoom_start=12
    )
    folium.Marker(
        location=[45.52336, -122.6750],
        popup="<b>Marker here</b>",
        tooltip="Click Here!"
    ).add_to(m)

    folium.Marker(
        location=[45.53236, -122.8750],
        popup="<b>Marker 2 here</b>",
        tooltip="Click Here!",
        icon=folium.Icon(color='green')
    ).add_to(m)

    folium.Marker(
        location=[45.54236, -122.8750],
        popup="<b>Marker 3 here</b>",
        tooltip="Click Here!",
        icon=folium.Icon(color='red')
    ).add_to(m)
    return m._repr_html_()

def generate_map(location):
    m = folium.Map(location=location)
    html = m.get_root().render()
    with open("map.html", "w") as f:
        f.write(html)
    return f"Map generated at {location}"

def start_flask():
    app.run(debug=False, use_reloader=False)

def open_browser():
    webbrowser.open('http://127.0.0.1:5000/')

def create_tkinter_window():
    root = tk.Tk()
    root.title("Flask and Tkinter Integration")

    button1 = tk.Button(root, text="Base Map", command=lambda: webbrowser.open('http://127.0.0.1:5000/'))
    button1.pack()

    button2 = tk.Button(root, text="Open Street Map", command=lambda: webbrowser.open('http://127.0.0.1:5000/open-street-map'))
    button2.pack()

    button3 = tk.Button(root, text="Map Marker", command=lambda: webbrowser.open('http://127.0.0.1:5000/map-marker'))
    button3.pack()

    root.mainloop()

if __name__ == "__main__":
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.start()

    # Generate Tkinter window
    create_tkinter_window()

