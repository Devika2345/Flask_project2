from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/staticfile')
def staticfile():
    return render_template('staticfile.html')
@FAI.route('/virat')
def virat():
    return render_template('virat.html')


FAI.run(debug=True)