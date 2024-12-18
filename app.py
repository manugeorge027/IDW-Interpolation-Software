# import os
# from flask import Flask, request, render_template_string, send_file
# import pandas as pd
# import subprocess

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the folder if it doesn't exist

# # Embedded Templates
# upload_template = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Upload Data</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             text-align: center;
#             margin: 0;
#             padding: 20px;
#         }
#         header {
#             background-color: #4CAF50;
#             color: white;
#             padding: 15px;
#         }
#         footer {
#             margin-top: 20px;
#             padding: 10px;
#             background-color: #f1f1f1;
#             color: #555;
#         }
#         #content {
#             margin: 20px auto;
#             padding: 20px;
#             border: 1px solid #ccc;
#             background-color: #f9f9f9;
#             max-width: 800px;
#             text-align: left;
#         }
#     </style>
# </head>
# <body>
#     <header>
#         <h1>Upload Data</h1>
#     </header>
#     <h2>Upload Your File</h2>
#     <form method="POST" action="/upload" enctype="multipart/form-data">
#         <input type="file" name="file" accept=".txt,.json,.csv"><br><br>
#         <button type="submit">Submit</button>
#     </form>
#     <div id="content">
#         <p>Upload your data file for processing.</p>
#         <img src="/static/image/model.jpg" alt="Model Visualization" style="max-width: 100%; height: auto;">
#     </div>
#     <footer>
#         <p>&copy; 2024 Data Processor. All rights reserved.</p>
#     </footer>
# </body>
# </html>
# '''

# display_template = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>File Uploaded</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             text-align: center;
#             margin: 0;
#             padding: 20px;
#         }
#         header {
#             background-color: #4CAF50;
#             color: white;
#             padding: 15px;
#         }
#         footer {
#             margin-top: 20px;
#             padding: 10px;
#             background-color: #f1f1f1;
#             color: #555;
#         }
#         #content {
#             margin: 20px auto;
#             padding: 20px;
#             border: 1px solid #ccc;
#             background-color: #f9f9f9;
#             max-width: 800px;
#             text-align: left;
#         }
#     </style>
# </head>
# <body>
#     <header>
#         <h1>File Processed</h1>
#     </header>
#     <h2>File Uploaded Successfully</h2>
#     <div id="content">
#         <p>Your file has been processed and stored.</p>
#     </div>
#     <footer>
#         <p>&copy; 2024 Data Processor. All rights reserved.</p>
#     </footer>
# </body>
# </html>
# '''

# # Home route for file upload
# @app.route('/')
# def upload_file():
#     return render_template_string(upload_template)

# # File upload handling route
# @app.route('/upload', methods=['POST'])
# def handle_file():
#     if 'file' not in request.files:
#         return "No file uploaded", 400
#     uploaded_file = request.files['file']
#     if uploaded_file.filename == '':
#         return "No file selected", 400

#     # Save the file as an Excel file in the upload folder
#     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
#     uploaded_file.save(file_path)

#     # Convert to Excel format if it's a CSV file
#     if uploaded_file.filename.endswith('.csv'):
#         excel_path = file_path.rsplit('.', 1)[0] + '.xlsx'
#         df = pd.read_csv(file_path)
#         df.to_excel(excel_path, index=False)
#         file_path = excel_path

#     # Run the Python file (assumes it is in the same directory)
#     script_path = os.path.join(os.getcwd(), 'process_file.py')
#     if os.path.exists(script_path):
#         subprocess.run(['python', script_path])

#     return render_template_string(display_template)

# if __name__ == '__main__':
#     app.run(debug=True)




# import os
# import time
# from flask import Flask, request, render_template_string, send_file
# import pandas as pd
# import subprocess

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# RESULTS_FOLDER = 'results'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create the uploads folder if it doesn't exist
# os.makedirs(RESULTS_FOLDER, exist_ok=True)  # Create the results folder if it doesn't exist

# # Embedded Templates
# upload_template = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Upload Data</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             text-align: center;
#             margin: 0;
#             padding: 20px;
#         }
#         header {
#             background-color: #4CAF50;
#             color: white;
#             padding: 15px;
#         }
#         footer {
#             margin-top: 20px;
#             padding: 10px;
#             background-color: #f1f1f1;
#             color: #555;
#         }
#         #content {
#             margin: 20px auto;
#             padding: 20px;
#             border: 1px solid #ccc;
#             background-color: #f9f9f9;
#             max-width: 800px;
#             text-align: left;
#         }
#     </style>
# </head>
# <body>
#     <header>
#         <h1>Upload Data</h1>
#     </header>
#     <h2>Upload Your File</h2>
#     <form method="POST" action="/upload" enctype="multipart/form-data">
#         <input type="file" name="file" accept=".txt,.json,.csv"><br><br>
#         <button type="submit">Submit</button>
#     </form>
#     <div id="content">
#         <p>Upload your data file for processing.</p>
#         <img src="/static/image/model.jpg" alt="Model Visualization" style="max-width: 100%; height: auto;">
#     </div>
#     <footer>
#         <p>&copy; 2024 Data Processor. All rights reserved.</p>
#     </footer>
# </body>
# </html>
# '''

# processing_template = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Processing</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             text-align: center;
#             margin: 0;
#             padding: 20px;
#         }
#         header {
#             background-color: #4CAF50;
#             color: white;
#             padding: 15px;
#         }
#         footer {
#             margin-top: 20px;
#             padding: 10px;
#             background-color: #f1f1f1;
#             color: #555;
#         }
#         .progress-bar {
#             width: 80%;
#             background-color: #ccc;
#             margin: 20px auto;
#             padding: 3px;
#             border: 1px solid #333;
#         }
#         .progress-bar-fill {
#             display: block;
#             height: 20px;
#             background-color: #4CAF50;
#             width: 0%;
#         }
#     </style>
#     <script>
#         function updateProgress() {
#             let elem = document.getElementById("progress-bar-fill");
#             let width = 0;
#             let interval = setInterval(() => {
#                 if (width >= 100) {
#                     clearInterval(interval);
#                     window.location.href = "/result";
#                 } else {
#                     width++;
#                     elem.style.width = width + "%";
#                 }
#             }, 50);
#         }
#         window.onload = updateProgress;
#     </script>
# </head>
# <body>
#     <header>
#         <h1>Processing File</h1>
#     </header>
#     <div class="progress-bar">
#         <div id="progress-bar-fill" class="progress-bar-fill"></div>
#     </div>
#     <footer>
#         <p>&copy; 2024 Data Processor. All rights reserved.</p>
#     </footer>
# </body>
# </html>
# '''

# result_template = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Results</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             text-align: center;
#             margin: 0;
#             padding: 20px;
#         }
#         header {
#             background-color: #4CAF50;
#             color: white;
#             padding: 15px;
#         }
#         footer {
#             margin-top: 20px;
#             padding: 10px;
#             background-color: #f1f1f1;
#             color: #555;
#         }
#         #content {
#             margin: 20px auto;
#             padding: 20px;
#             border: 1px solid #ccc;
#             background-color: #f9f9f9;
#             max-width: 800px;
#             text-align: left;
#         }
#     </style>
# </head>
# <body>
#     <header>
#         <h1>Processing Complete</h1>
#     </header>
#     <h2>Download Your Results</h2>
#     <div id="content">
#         <a href="/download/result1.xlsx" download><button>Download Result 1</button></a><br><br>
#         <a href="/download/result2.xlsx" download><button>Download Result 2</button></a><br><br>
#         <a href="/download/result3.xlsx" download><button>Download Result 3</button></a>
#     </div>
#     <footer>
#         <p>&copy; 2024 Data Processor. All rights reserved.</p>
#     </footer>
# </body>
# </html>
# '''

# # Home route for file upload
# @app.route('/')
# def upload_file():
#     return render_template_string(upload_template)

# # File upload handling route
# @app.route('/upload', methods=['POST'])
# def handle_file():
#     if 'file' not in request.files:
#         return "No file uploaded", 400
#     uploaded_file = request.files['file']
#     if uploaded_file.filename == '':
#         return "No file selected", 400

#     # Save the file in the upload folder
#     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
#     uploaded_file.save(file_path)

#     # Convert CSV to Excel if needed
#     if uploaded_file.filename.endswith('.csv'):
#         excel_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename.rsplit('.', 1)[0] + '.xlsx')
#         df = pd.read_csv(file_path)
#         df.to_excel(excel_path, index=False)
#         file_path = excel_path

#     # Simulate running a script (replace this with actual processing logic)
#     time.sleep(2)
#     return render_template_string(processing_template)

# # Route to serve results
# @app.route('/result')
# def show_results():
#     # Simulate saving results
#     for i in range(1, 4):
#         result_path = os.path.join(RESULTS_FOLDER, f'result{i}.xlsx')
#         pd.DataFrame({'Column': [1, 2, 3]}).to_excel(result_path, index=False)
#     return render_template_string(result_template)

# # Route to download results
# @app.route('/download/<filename>')
# def download_result(filename):
#     file_path = os.path.join(RESULTS_FOLDER, filename)
#     return send_file(file_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)

# import os
# import time
# from flask import Flask, request, render_template_string, send_file
# import pandas as pd

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# RESULTS_FOLDER = 'results'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure upload folder exists
# os.makedirs(RESULTS_FOLDER, exist_ok=True)  # Ensure results folder exists

# upload_template = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Upload Data</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             text-align: center;
#             margin: 0;
#             padding: 20px;
#         }
#         header {
#             background-color: #4CAF50;
#             color: white;
#             padding: 15px;
#         }
#         footer {
#             margin-top: 20px;
#             padding: 10px;
#             background-color: #f1f1f1;
#             color: #555;
#         }
#         #content {
#             margin: 20px auto;
#             padding: 20px;
#             border: 1px solid #ccc;
#             background-color: #f9f9f9;
#             max-width: 800px;
#             text-align: left;
#         }
#     </style>
# </head>
# <body>
#     <header>
#         <h1>Upload Data</h1>
#     </header>
#     <h2>Upload Your File</h2>
#     <form method="POST" action="/upload" enctype="multipart/form-data">
#         <input type="file" name="file" accept=".txt,.json,.csv"><br><br>
#         <button type="submit">Submit</button>
#     </form>
#     <div id="content">
#         <p>Upload your data file for processing.</p>
#         <img src="/static/image/model.jpg" alt="Model Visualization" style="max-width: 100%; height: auto;">
#     </div>
#     <footer>
#         <p>&copy; 2024 Data Processor. All rights reserved.</p>
#     </footer>
# </body>
# </html>
# '''

# processing_template = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Processing</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             text-align: center;
#             margin: 0;
#             padding: 20px;
#         }
#         header {
#             background-color: #4CAF50;
#             color: white;
#             padding: 15px;
#         }
#         footer {
#             margin-top: 20px;
#             padding: 10px;
#             background-color: #f1f1f1;
#             color: #555;
#         }
#         .progress-container {
#             margin: 50px auto;
#             width: 80%;
#             background-color: #ddd;
#             border-radius: 25px;
#             overflow: hidden;
#         }
#         .progress-bar {
#             height: 30px;
#             width: 0;
#             background-color: #4CAF50;
#             text-align: center;
#             line-height: 30px;
#             color: white;
#             animation: fillProgress 5s ease-in-out forwards;
#         }
#         @keyframes fillProgress {
#             0% { width: 0; }
#             100% { width: 100%; }
#         }
#     </style>
#     <script>
#         setTimeout(() => {
#             window.location.href = "/result";
#         }, 5000);  // Redirect to results after 5 seconds
#     </script>
# </head>
# <body>
#     <header>
#         <h1>Processing File</h1>
#     </header>
#     <div class="progress-container">
#         <div class="progress-bar">Processing...</div>
#     </div>
#     <footer>
#         <p>&copy; 2024 Data Processor. All rights reserved.</p>
#     </footer>
# </body>
# </html>
# '''

# result_template = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Results</title>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             text-align: center;
#             margin: 0;
#             padding: 20px;
#         }
#         header {
#             background-color: #4CAF50;
#             color: white;
#             padding: 15px;
#         }
#         footer {
#             margin-top: 20px;
#             padding: 10px;
#             background-color: #f1f1f1;
#             color: #555;
#         }
#         #content {
#             margin: 20px auto;
#             padding: 20px;
#             border: 1px solid #ccc;
#             background-color: #f9f9f9;
#             max-width: 800px;
#             text-align: left;
#         }
#     </style>
# </head>
# <body>
#     <header>
#         <h1>Processing Complete</h1>
#     </header>
#     <h2>Download Your Results</h2>
#     <div id="content">
#         <a href="/download/result1.xlsx" download><button>Download Result 1</button></a><br><br>
#         <a href="/download/result2.xlsx" download><button>Download Result 2</button></a><br><br>
#         <a href="/download/result3.xlsx" download><button>Download Result 3</button></a>
#     </div>
#     <footer>
#         <p>&copy; 2024 Data Processor. All rights reserved.</p>
#     </footer>
# </body>
# </html>
# '''

# @app.route('/')
# def upload_file():
#     return render_template_string(upload_template)

# @app.route('/upload', methods=['POST'])
# def handle_file():
#     if 'file' not in request.files:
#         return "No file uploaded", 400
#     uploaded_file = request.files['file']
#     if uploaded_file.filename == '':
#         return "No file selected", 400

#     file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
#     uploaded_file.save(file_path)

#     # Simulate data processing
#     time.sleep(1)
#     return render_template_string(processing_template)

# @app.route('/result')
# def show_results():
#     # Simulate saving results
#     for i in range(1, 4):
#         result_path = os.path.join(RESULTS_FOLDER, f'result{i}.xlsx')
#         pd.DataFrame({'Column': [1, 2, 3]}).to_excel(result_path, index=False)
#     return render_template_string(result_template)

# @app.route('/download/<filename>')
# def download_result(filename):
#     file_path = os.path.join(RESULTS_FOLDER, filename)
#     return send_file(file_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(debug=True)
    
    
    





import os
import time
import subprocess
from flask import Flask, request, render_template_string, send_file
import pandas as pd

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

# Python script to be executed
SCRIPT_TO_RUN = "home.py"  # Replace with your Python script

upload_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Data</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 20px;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 15px;
        }
        footer {
            margin-top: 20px;
            padding: 10px;
            background-color: #f1f1f1;
            color: #555;
        }
    </style>
</head>
<body>
    <header>
        <h1>Upload Data</h1>
    </header>
    <h2>Upload Your File</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file" accept=".txt,.json,.csv"><br><br>
        <button type="submit">Submit</button>
    </form>
    <footer>
        <p>&copy; 2024 Data Processor. All rights reserved.</p>
    </footer>
</body>
</html>
'''

processing_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Processing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 20px;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 15px;
        }
        .progress-container {
            margin: 50px auto;
            width: 80%;
            background-color: #ddd;
            border-radius: 25px;
            overflow: hidden;
        }
        .progress-bar {
            height: 30px;
            width: 0;
            background-color: #4CAF50;
            text-align: center;
            line-height: 30px;
            color: white;
            animation: fillProgress 5s linear forwards;
        }
        @keyframes fillProgress {
            0% { width: 0; }
            100% { width: 100%; }
        }
    </style>
    <script>
        setTimeout(() => {
            window.location.href = "/result";
        }, 5000);  // Redirect to results after 5 seconds
    </script>
</head>
<body>
    <header>
        <h1>Processing File</h1>
    </header>
    <div class="progress-container">
        <div class="progress-bar">Processing...</div>
    </div>
</body>
</html>
'''

result_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Results</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 20px;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 15px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Processing Complete</h1>
    </header>
    <h2>Download Your Results</h2>
    <a href="/download/result.xlsx" download><button>Download Result</button></a>
</body>
</html>
'''

@app.route('/')
def upload_file():
    return render_template_string(upload_template)

@app.route('/upload', methods=['POST'])
def handle_file():
    if 'file' not in request.files:
        return "No file uploaded", 400
    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return "No file selected", 400

    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
    uploaded_file.save(file_path)

    # Run the Python script
    script_process = subprocess.Popen(
        ["python", SCRIPT_TO_RUN, file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Let the script run during the progress bar
    time.sleep(5)
    return render_template_string(processing_template)

@app.route('/result')
def show_results():
    # Simulate saving results
    result_path = os.path.join(RESULTS_FOLDER, 'result.xlsx')
    pd.DataFrame({'Processed Data': [10, 20, 30]}).to_excel(result_path, index=False)
    return render_template_string(result_template)

@app.route('/download/<filename>')
def download_result(filename):
    file_path = os.path.join(RESULTS_FOLDER, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

