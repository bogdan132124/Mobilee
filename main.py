import json
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


class PinYourNoteApp(App):
    def build(self):
        # Load notes from JSON file
        try:
            with open('notes.json', 'r') as file:
                notes_data = json.load(file)
        except FileNotFoundError:
            notes_data = []

        # Save notes to JSON file
        def save_notes():
            with open('notes.json', 'w') as file:
                json.dump(notes_data, file)

        # Add a note to the JSON data
        def add_note(self):
            today = date_entry.text
            notes_title = notes_title_entry.text
            notes = notes_entry.text
            if (len(today) <= 0) & (len(notes_title) <= 0) & (len(notes) <= 1):
                popup = Popup(title='Error', content=Label(text='ENTER REQUIRED DETAILS'), size_hint=(None, None),
                              size=(400, 200))
                popup.open()
            else:
                note = {'date': today, 'title': notes_title, 'notes': notes}
                notes_data.append(note)
                save_notes()
                popup = Popup(title='Success', content=Label(text='Note added'), size_hint=(None, None),
                              size=(400, 200))
                popup.open()

        # View all notes in the JSON data
        def view_notes(self):
            date = date_entry.text
            notes_title = notes_title_entry.text
            if (len(date) <= 0) & (len(notes_title) <= 0):
                notes_info = ""
                for note in notes_data:
                    notes_info += "Date: " + note['date'] + "\nTitle: " + note['title'] + "\nNotes: " + note[
                        'notes'] + "\n\n"
                if len(notes_info) > 0:
                    popup = Popup(title='Notes', content=Label(text=notes_info), size_hint=(None, None),
                                  size=(400, 200))
                    popup.open()
                else:
                    popup = Popup(title='Error', content=Label(text='No note found'), size_hint=(None, None),
                                  size=(400, 200))
                    popup.open()
            else:
                filtered_notes = [note for note in notes_data if note['date'] == date and note['title'] == notes_title]
                if len(filtered_notes) > 0:
                    notes_info = ""
                    for note in filtered_notes:
                        notes_info += "Date: " + note['date'] + "\nTitle: " + note['title'] + "\nNotes: " + note[
                            'notes'] + "\n\n"
                    popup = Popup(title='Notes', content=Label(text=notes_info), size_hint=(None, None),
                                  size=(400, 200))
                    popup.open()
                else:
                    popup = Popup(title='Error', content=Label(text='No note found'), size_hint=(None, None),
                                  size=(400, 200))
                    popup.open()

        # Delete notes from the JSON data
        def delete_notes(self):
            date = date_entry.text
            notes_title = notes_title_entry.text

            if choice == 'yes':
                notes_data.clear()
                save_notes()
                popup = Popup(title='Success', content=Label(text='Note(s) Deleted'), size_hint=(None, None),
                              size=(400, 200))
                popup.open()
            else:
                if (len(date) <= 0) & (len(notes_title) <= 0):
                    popup = Popup(title='Error', content=Label(text='ENTER REQUIRED DETAILS'), size_hint=(None, None),
                                  size=(400, 200))
                    popup.open()
                    return
                else:
                    filtered_notes = [note for note in notes_data if
                                      note['date'] == date and note['title'] == notes_title]
                    if len(filtered_notes) > 0:
                        for note in filtered_notes:
                            notes_data.remove(note)
                        save_notes()
                        popup = Popup(title='Success', content=Label(text='Note(s) Deleted'), size_hint=(None, None),
                                      size=(400, 200))
                        popup.open()
                    else:
                        popup = Popup(title='Error', content=Label(text='No note found'), size_hint=(None, None),
                                      size=(400, 200))
                        popup.open()

        # Update notes in the JSON data
        def update_notes(self):
            today = date_entry.text
            notes_title = notes_title_entry.text
            notes = notes_entry.text
            if (len(today) <= 0) & (len(notes_title) <= 0) & (len(notes) <= 1):
                popup = Popup(title='Error', content=Label(text='ENTER REQUIRED DETAILS'), size_hint=(None, None),
                              size=(400, 200))
                popup.open()
            else:
                filtered_notes = [note for note in notes_data if note['date'] == today and note['title'] == notes_title]
                if len(filtered_notes) > 0:
                    for note in filtered_notes:
                        note['notes'] = notes
                    save_notes()
                    popup = Popup(title='Success', content=Label(text='Note Updated'), size_hint=(None, None),
                                  size=(400, 200))
                    popup.open()
                else:
                    popup = Popup(title='Error', content=Label(text='No note found'), size_hint=(None, None),
                                  size=(400, 200))
                    popup.open()

        root = BoxLayout(orientation='vertical')

        date_label = Label(text='Enter Date (yyyy-mm-dd):')
        notes_title_label = Label(text='Enter Notes Title:')
        notes_label = Label(text='Enter Notes:')

        date_entry = TextInput()
        notes_title_entry = TextInput()
        notes_entry = TextInput()

        add_button = Button(text='Add Note')
        view_button = Button(text='View Notes')
        delete_button = Button(text='Delete Note')
        update_button = Button(text='Update Note')

        add_button.bind(on_press=add_note)
        view_button.bind(on_press=view_notes)
        delete_button.bind(on_press=delete_notes)
        update_button.bind(on_press=update_notes)

        layout = GridLayout(cols=2)
        layout.add_widget(date_label)
        layout.add_widget(date_entry)
        layout.add_widget(notes_title_label)
        layout.add_widget(notes_title_entry)
        layout.add_widget(notes_label)
        layout.add_widget(notes_entry)
        layout.add_widget(add_button)

        layout.add_widget(view_button)
        layout.add_widget(delete_button)
        layout.add_widget(update_button)

        scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scrollview.add_widget(layout)

        root.add_widget(scrollview)

        return root


if __name__ == '__main__':
    PinYourNoteApp().run()
