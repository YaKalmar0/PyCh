WORD = "luvpy"

class Editor:
    def view_document(self):
        print("Your document: #prints here")

    def edit_document(self):
        print("Editing is forbidden in FREE-version.")

class ProEditor(Editor):
    def edit_document(self):
        print("Edit your document: #edit here")

def main():
    print("Please, enter your License Key:")
    key = input()
    if (key == WORD):  #keyword - "luvpy"
        obj = ProEditor()
        obj.view_document()
        obj.edit_document()
    else:
        obj = Editor()
        obj.view_document()
        obj.edit_document()

if __name__ == "__main__":
    main()