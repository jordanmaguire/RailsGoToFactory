import sublime, sublime_plugin, os

class GoToFactoryCommand(sublime_plugin.WindowCommand):

  # Called by Sublime
  def run(self):
    # Full path of the file. EG:
    # /Users/mydumbuser/src/my_app/app/models/program/accommodation_option.rb
    current_file = self.window.active_view().file_name()

    folders = self.window.folders()
    for folder in folders:
      if current_file.startswith(folder):
        current_folder = folder
        current_file   = current_file.replace(folder, "")

    # EG: /Users/mydumbuser/src/my_app/
    app_root = self.window.active_view().file_name()
    app_root = app_root.replace(current_file, "")

    # EG: /app/models/program/accommodation_option.rb
    #
    # dirname:  /app/models/progam
    # filename: /accommodation_option
    # extnsion: .rb
    dirname  = os.path.dirname(current_file)
    filename = os.path.basename(current_file)
    filename, extension = os.path.splitext(filename)

    if ("app/models" in dirname) or ("spec/models" in dirname):
      filename = filename.replace("_spec", "")
      expected_factory_name = filename + "_factory.rb"
      expected_factory_path = app_root + "/lib/factories/" + expected_factory_name
      self.window.open_file(expected_factory_path)
    else:
      print("This is NOT a model!")
