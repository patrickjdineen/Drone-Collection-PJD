from drone_api import app, routes
#could also do from drone_api import drone.routs

if __name__ == "__main__":
    app.run(debug=False)