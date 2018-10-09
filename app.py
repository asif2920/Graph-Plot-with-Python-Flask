from flask import Flask,Markup,render_template
from graph import build_graph
app = Flask(__name__)

labels = ["January","February","March","April","May","June","July","August"]
values = [10,9,8,7,6,4,7,8]
@app.route("/bar")
def chart ():
    bar_labels = labels
    bar_values = values
    return render_template('chart.html',title="Bar Graph", values=bar_values, labels=bar_labels)
@app.route("/line")
def line ():
    line_labels = labels
    line_values = values
    return render_template('lineChart.html', title="Line Graph", values=line_values, labels=line_labels)
@app.route("/pie")
def pie ():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
    return render_template('pieChart.html', title="Pie Graph", set=zip(values, labels, colors))
@app.route("/graph")
def graph ():
    x1 = [0, 1, 2, 3, 4]
    y1 = [10, 30, 40, 5, 50]
    x2 = [0, 1, 2, 3, 4]
    y2 = [50, 30, 20, 10, 50]
    x3 = [0, 1, 2, 3, 4]
    y3 = [0, 30, 10, 5, 30]	
    graph1_url = build_graph(x1,y1);
    graph2_url = build_graph(x2,y2);
    graph3_url = build_graph(x3,y3);
 
    return render_template('graph.html', graph1=graph1_url, graph2=graph2_url, graph3=graph3_url)
if __name__ == "__main__":
    app.run()