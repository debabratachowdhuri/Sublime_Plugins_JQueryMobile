import sublime, sublime_plugin

class MobileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "<!DOCTYPE html>\
        		\n<html lang=\"en\">\
        		\n\t<head>\
        		\n\t\t<meta charset=\"UTF-8\">\
        		\n\t\t<title>Persistent Footer</title>\
        		\n\t\t<link rel=\"stylesheet\" href=\"http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css\" /></script>\
        		\n\t\t<script src=\"http://code.jquery.com/jquery-1.11.1.min.js\">\
        		\n\t\t<script src=\"http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js\"></script>\
        		\n\t\t<meta name=\"viewport\" content=\"width=divece-width,initial-scale=1\">\
        		\n</head>\
        		\n<body>\
        		\n\
        		\n</body>\
        		\n</html>")