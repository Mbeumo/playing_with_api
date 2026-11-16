from flask import Flask,request,jsonify
import csv
import urllib.request as rq


app=Flask(__name__)
CSV_URL = "https://storage.googleapis.com/qwasar-public/track-ds/imdb-movie-data.csv"

def get_movies():
    response = rq.urlopen(CSV_URL)

    lines = [line.decode("utf-8") for line in response.readlines()]

    return csv.DictReader(lines)

@app.route("/",methods=["GET"])
def filterinhome():
    #data = read_csv()
    genre =request.args["genre"]
    #with open("imdb-movie-data.csv",newline="\n",encoding="utf-8") as csvfile:
        #reader = csv.DictReader(csvfile)
    print(get_movies())
    results = []
    for row in get_movies():
        for key in row:
            if row[key] == "":
                row[key] = None
        if genre is None or genre.lower() in row["Genre"].lower():
                    results.append(row)
   # return jsonify(results)
    return str(results)
    #return jsonify({"/": "route reached","Genre": genre})

"""@genres_bp.route("/<genreval>",methods=["Get"])
def filterbyparam(genreval):
    with open("imdb-movie-data.csv",newline="\n",encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if genreval is None or row["genre"].lower()==genreval.lower():
                result.append(row)
    return jsonify(results)
"""
@app.route("/action",methods=["GET"])
def filteraction():
    print("action called")
    #data = read_csv()
    #with open("imdb-movie-data.csv",newline="\n",encoding="utf-8") as csvfile:
        #reader = csv.DictReader(csvfile)
    results=[]
    for row in get_movies():
        if "action" in row["Genre"].lower():
            results.append(row)
    #return jsonify(results)
    return str(results)


@app.route("/adventure",methods=["GET"])
def filteradventure():
    #data = read_csv()
    #with open("imdb-movie-data.csv",newline="\n",encoding="utf-8") as csvfile:
        #reader = csv.DictReader(csvfile)
    results=[]
    for row in get_movies():
        for key in row:
            if row[key] == "":
                row[key] = None
        if "adventure" in row["Genre"].lower():
            results.append(row)
    
    return str(results)
    #return jsonify(results)

@app.route("/comedy",methods=["GET"])
def filtercomedy():
    #data = read_csv()
    #with open("imdb-movie-data.csv",newline="\n",encoding="utf-8") as csvfile:
        #reader = csv.DictReader(csvfile)
    results=[]
    for row in get_movies():
        for key in row:
            if row[key] == "":
                row[key] = None
        if "comedy" in row["Genre"].lower():
            results.append(row)
    #return jsonify(results)
    return str(results)


@app.route("/drama",methods=["GET"])
def filterdrama():
    #data = read_csv()
    #with open("imdb-movie-data.csv",newline="\n",encoding="utf-8") as csvfile:
        #reader = csv.DictReader(csvfile)
    results=[]
    for row in get_movies():
        for key in row:
            if row[key] == "":
                row[key] = None
        if "drama" in row["Genre"].lower():
            results.append(row)
    return str(results)

    #return jsonify(results)

@app.route('/debug',methods=['GET'])
def debug():
    return jsonify({"debug": "route reached"})

@app.route('/romance',methods=['GET'])
def filterromance():
    #data = read_csv()
    #with open("imdb-movie-data.csv",newline="\n",encoding="utf-8") as csvfile:
        #reader = csv.DictReader(csvfile)
    results=[]
    print(get_movies())
    for row in get_movies():
        for key in row:
            if row[key] == "":
                row[key] = None
        if "romance" in row["Genre"].lower():
            results.append(row)
    return str(results)

    #return jsonify(results)

print("STARTING SERVER", flush=True)

if __name__=="__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    )