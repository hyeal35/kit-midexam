from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/ride')
def ride():
    return render_template('ride.html')

@app.route('/ride/<int:num>')
def ride_num(num):
    if num ==1:
        return '''
        <script>alert('돈이 많이 깨졌다 놀 돈이 사라졌다!')
            history.back(-1)
            </script>
            '''

    if num ==2:
        return '''
        <script>alert('차가 많이 정체가 되었다 결국 지각이다')
            history.back(-1)
            </script>
            '''

    if num ==3:
        return '''
        <script>alert('역시 정각 대중교통 지하철이다.')
            history.back(-2)
            </script>
            '''

@app.route('/eat')
def eat():
    return render_template('eat.html')

@app.route('/eat/<int:num>')
def eat_num(num):
    if num ==1:
        return '''
        <script>alert('국밥은 싫다고 그랬지.')
            history.back(-1)
            </script>
            '''

    if num ==2:
        return '''
        <script>alert('웨이팅이 너무 많다 ㅜㅜ')
            history.back(-1)
            </script>
            '''

    if num ==3:
        return '''
        <script>alert('맛있다!')
            history.back(-2)
            </script>
            '''