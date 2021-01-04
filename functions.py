def sendMedia(update,context):
 try:
  update.message.reply_video(update.message.video.file_id)
 except Exception as e:
 	update.message.reply_text(e)
 
#Function to send file
def sendFile(update,context): 
 try:
  	update.message.reply_document(update.message.document.file_id)
 except Exception as e:
  	update.message.reply_text(e)
  	
#Function to send image
def sendPhoto(update,context):
 try:
   update.message.reply_photo(update.message.photo[-1].file_id)
 except Exception as e:
  	update.message.reply_text
