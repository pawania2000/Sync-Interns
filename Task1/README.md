#Desktop Notifier
This is a simple script that sends desktop notifications to the user. The script uses the 'plyer' library to display notifications, which provides a unified API to send notifications on various platforms such as Windows, macOS, and Linux.

#Usage
To use the script, simply run the script in your Python environment. The script will read the contents of the text file specified in the 'filename' variable and send a notification for each line in the file. The notification will include the title specified in the 'title' variable and the message specified in the 'message' variable.

The 'notification.notify()' function can also take other optional parameters, such as the 'app_icon' parameter to specify the icon for the notification, and the 'timeout' parameter to specify the duration for which the notification will be displayed.

#Requirements
•Python 3.x
•plyer library (install using pip install plyer)
