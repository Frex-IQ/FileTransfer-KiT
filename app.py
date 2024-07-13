from flask import Flask, render_template, request, send_file, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    # Allow all file extensions
    return '.' in filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file and allowed_file(file.filename):
        filename = file.filename
        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'
        except Exception as e:
            return f'Error uploading file: {e}'
    else:
        return 'File upload failed'

@app.route('/list')
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('list.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return 'File not found'

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return redirect(url_for('list_files'))  # Redirect to the list page after deletion
    else:
        return 'File not found'

@app.route('/rename/<filename>', methods=['GET', 'POST'])
def rename_file(filename):
    if request.method == 'POST':
        new_name = request.form.get('new_name')
        if not new_name:
            return 'New name not provided'
        
        old_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        new_path = os.path.join(app.config['UPLOAD_FOLDER'], new_name)
        
        if os.path.exists(old_path):
            if os.path.exists(new_path):
                return f'A file with the name "{new_name}" already exists.'
            
            os.rename(old_path, new_path)
            return redirect(url_for('list_files'))  # Redirect to the list page after renaming
        else:
            return 'File not found'
    
    # Handle GET request to show rename form or redirect if needed
    return render_template('rename.html', filename=filename)

@app.route('/photos')
def show_photos():
    # Example: Filter files with image extensions
    image_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('photos.html', image_files=image_files)

@app.route('/videos')
def show_videos():
    # Example: Filter files with video extensions
    video_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if f.lower().endswith(('.mp4', '.avi', '.mov'))]
    return render_template('videos.html', video_files=video_files)

if __name__ == '__main__':
    app.run(debug=True)
