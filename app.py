# # from flask import Flask, render_template, Response, jsonify, request, session
# # from flask_wtf import FlaskForm
# # from wtforms import FileField, SubmitField
# # from werkzeug.utils import secure_filename
# # from wtforms.validators import InputRequired
# # import os
# # import cv2
# # from YOLO_Video import video_detection

# # app = Flask(__name__)
# # app.config['SECRET_KEY'] = 'Virus'
# # app.config['UPLOAD_FOLDER'] = 'static/files'

# # class UploadFileForm(FlaskForm):
# #     file = FileField("File", validators=[InputRequired()])
# #     submit = SubmitField("Run")

# # def generate_frames(path_x=''):
# #     yolo_output = video_detection(path_x)
# #     for detection_ in yolo_output:
# #         ret, buffer = cv2.imencode('.jpg', detection_)
# #         if not ret:
# #             continue
# #         frame = buffer.tobytes()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# # def generate_frames_web(path_x):
# #     yolo_output = video_detection(path_x)
# #     for detection_ in yolo_output:
# #         ret, buffer = cv2.imencode('.jpg', detection_)
# #         if not ret:
# #             continue
# #         frame = buffer.tobytes()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# # @app.route('/', methods=['GET', 'POST'])
# # @app.route('/home', methods=['GET', 'POST'])
# # def home():
# #     session.clear()
# #     return render_template('bet.html')

# # @app.route("/webcam", methods=['GET', 'POST'])
# # def webcam():
# #     session.clear()
# #     return render_template('ui.html')

# # @app.route('/FrontPage', methods=['GET', 'POST'])
# # def front():
# #     form = UploadFileForm()
# #     if form.validate_on_submit():
# #         file = form.file.data
# #         file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
# #         file.save(file_path)
# #         session['video_path'] = file_path
# #     return render_template('bettervideo.html', form=form)

# # @app.route('/video')
# # def video():
# #     video_path = session.get('video_path', None)
# #     if not video_path:
# #         return "No video uploaded.", 400
# #     return Response(generate_frames(path_x=video_path), mimetype='multipart/x-mixed-replace; boundary=frame')

# # @app.route('/webapp')
# # def webapp():
# #     return Response(generate_frames_web(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')

# # if __name__ == "__main__":
# #     app.run(debug=True)




# from flask import Flask, render_template, Response, jsonify, request, session
# from flask_wtf import FlaskForm
# from wtforms import FileField, SubmitField
# from werkzeug.utils import secure_filename
# from wtforms.validators import InputRequired
# import os
# import cv2
# from YOLO_Video import video_detection

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'Virus'
# app.config['UPLOAD_FOLDER'] = 'static/files'

# class UploadFileForm(FlaskForm):
#     file = FileField("File", validators=[InputRequired()])
#     submit = SubmitField("Run")

# def generate_frames(path_x=''):
#     yolo_output = video_detection(path_x)
#     for detection_ in yolo_output:
#         ret, buffer = cv2.imencode('.jpg', detection_)
#         if not ret:
#             continue
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# def generate_frames_web(path_x):
#     yolo_output = video_detection(path_x)
#     for detection_ in yolo_output:
#         ret, buffer = cv2.imencode('.jpg', detection_)
#         if not ret:
#             continue
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/', methods=['GET', 'POST'])
# @app.route('/home', methods=['GET', 'POST'])
# def home():
#     session.clear()
#     return render_template('bet.html')

# @app.route("/webcam", methods=['GET', 'POST'])
# def webcam():
#     if request.method == 'POST':
#         session.clear()

#         file = request.files['file']
#         if file:
#             filename = secure_filename(file.filename)
#             file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(file_path)
#             session['video_path'] = file_path

#         return render_template('success.html')  # Replace with your success page

#     return render_template('ui.html')

# @app.route('/FrontPage', methods=['GET', 'POST'])
# def front():
#     form = UploadFileForm()
#     if form.validate_on_submit():
#         file = form.file.data
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
#         file.save(file_path)
#         session['video_path'] = file_path
#     return render_template('bettervideo.html', form=form)

# @app.route('/video')
# def video():
#     video_path = session.get('video_path', None)
#     if not video_path:
#         return "No video uploaded.", 400
#     return Response(generate_frames(path_x=video_path), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/webapp')
# def webapp():
#     return Response(generate_frames_web(path_x=0), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, Response, jsonify, request, session
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import os
import cv2
from YOLO_Video import video_detection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Virus'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Run")

def generate_frames(path_x=''):
    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        ret, buffer = cv2.imencode('.jpg', detection_)
        if not ret:
            continue
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_frames_web(path_x):
    yolo_output = video_detection(path_x)
    for detection_ in yolo_output:
        ret, buffer = cv2.imencode('.jpg', detection_)
        if not ret:
            continue
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    session.clear()
    return render_template('better.html')

@app.route("/webcam", methods=['GET', 'POST'])
def webcam():
    if request.method == 'POST':
        session.clear()

        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            session['video_path'] = file_path

        return render_template('success.html')  # Replace with your success page

    return render_template('ui.html')

@app.route('/FrontPage', methods=['GET', 'POST'])
def front():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(file_path)
        session['video_path'] = file_path
    return render_template('bettervideo.html', form=form)

@app.route('/video')
def video():
    video_path = session.get('video_path', None)
    if not video_path:
        return "No video uploaded.", 400
    return Response(generate_frames(path_x=video_path), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/webapp')
def webapp():
    return Response(generate_frames_web(path_x=1), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)

