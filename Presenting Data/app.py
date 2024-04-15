from flask import Flask, render_template, request, jsonify
import sqlite3
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/Me')
def test():
    return render_template('Me.html')

@app.route('/jobAnalysisT', methods=['POST', 'GET'])
def search():
    if request.method == "GET":
        return render_template('search.html')
    
    if request.method == "POST":
        title = request.form["jobTitle"]
        state = request.form["jobState"]
        conn = sqlite3.connect(r"C:\Users\user\Desktop\My Projects\CS50-s_FinalProject\Collecting Data\GOV.UK\Jobs.db")
        
        cursor = conn.cursor()
        cursor.execute(f'SELECT AVG(avgSalary) FROM Jobs;')
        Avg = cursor.fetchall()[0][0]
        cursor.close()
        
        cursor = conn.cursor()
        cursor.execute(f'SELECT AVG(avgSalary) FROM Jobs WHERE title LIKE "{title}%" AND state like "{state}%";')
        avg = cursor.fetchall()[0][0]
        cursor.close()

        cursor = conn.cursor()
        cursor.execute(f'SELECT max(maxSalary) FROM Jobs WHERE title LIKE "{title}%" AND state like "{state}%";')
        max = cursor.fetchall()[0][0]
        cursor.close()
        
        cursor = conn.cursor()
        cursor.execute(f'SELECT min(minSalary) FROM Jobs WHERE title LIKE "{title}%" AND state like "{state}%";')
        min = cursor.fetchall()[0][0]
        cursor.close()
        
        cursor = conn.cursor()
        cursor.execute(f'SELECT state, COALESCE(AVG(avgSalary), 0) AS average_salary FROM Jobs WHERE title LIKE "{title}%" AND state like "{state}%" GROUP BY state HAVING average_salary <> 0 ORDER BY average_salary DESC;')
        Data = cursor.fetchall()
        data = [{'state': row[0], 'avg_salary': row[1]} for row in Data]
        cursor.close()
        
        cursor = conn.cursor()
        cursor.execute(f'SELECT city, COALESCE(AVG(avgSalary), 0) AS average_salary FROM Jobs WHERE title LIKE "{title}%" AND state like "{state}%" GROUP BY city HAVING average_salary <> 0 ORDER BY average_salary DESC;')
        Data1 = cursor.fetchall()
        data1 = [{'city': row[0], 'avg_salary': row[1]} for row in Data1]
        cursor.close()

        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM Jobs WHERE title LIKE "{title}%" and state LIKE "{state}%" LIMIT 100;')
        all_jobs_data = cursor.fetchall()
        cursor.close()

        cursor = conn.cursor()
        cursor.execute(f'SELECT company, COALESCE(AVG(avgSalary), 0) AS average_salary FROM Jobs WHERE title LIKE "{title}%" AND state like "{state}%" GROUP BY company HAVING average_salary <> 0 ORDER BY average_salary DESC;')
        Data2 = cursor.fetchall()
        data2 = [{'company': row[0], 'avg_salary': row[1]} for row in Data2]
        cursor.close()

        cursor = conn.cursor()
        cursor.execute(f'SELECT category, COALESCE(AVG(avgSalary), 0) AS average_salary FROM Jobs WHERE title LIKE "{title}%" AND state like "{state}%" GROUP BY category HAVING average_salary <> 0 ORDER BY average_salary DESC;')
        Data3 = cursor.fetchall()
        data3 = [{'category': row[0], 'avg_salary': row[1]} for row in Data3]
        cursor.close()

        conn.close()

        return render_template('search.html', sqlJsonData=data, sqlJsonData1=data1, sqlJsonData2=data2, sqlJsonData3=data3, all_jobs_data=all_jobs_data, min=min, max=max, avg=avg, Avg=Avg, round=round, len=len)
    
@app.route('/jobSearch', methods=["POST", "GET"])
def jobSearch():
    if request.method == "GET":
        return render_template('jobSearch.html')
    elif request.method == "POST":
        conn = sqlite3.connect(r"C:\Users\user\Desktop\My Projects\CS50-s_FinalProject\Collecting Data\GOV.UK\Jobs.db")
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM Jobs WHERE title LIKE "{request.form["jobTitle"]}%" and state = "{request.form["jobState"]}%" LIMIT 100;')
        jobSearch = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('jobSearch.html', jobSearch=jobSearch)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
