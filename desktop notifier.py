from plyer import notification  
  
notification_title = 'Hello!'  
notification_message = 'Thank you for reading'  
  
notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = None,  
    timeout = 10,  
    toast = False  
    )  