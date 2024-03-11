from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

def add_note(note):
    notes.append(note)

def delete_note(note_id):
    if 0 <= note_id < len(notes):
        del notes[note_id]

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            add_note(note)

        note_id = request.form.get("note_id")
        if note_id:
            delete_note(int(note_id))

        action = request.form.get("action")
        if action == "edit":
            note_id = int(request.form.get("note_id"))
            edit_note = request.form.get("new_note")
            notes[note_id] = edit_note
            return redirect(url_for('index'))

    current_date = datetime.now().strftime('%Y-%m-%d')
    edit_note = request.args.get('edit_note', '')
    return render_template("home.html", notes=notes, current_date=current_date, edit_note=edit_note)

if __name__ == '__main__':
    app.run(debug=True)
