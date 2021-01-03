# ForwardTagRemoverBot - A Telegram Bot To Hide Forward Source
#Copyright (C) 2020 by Preet <https://github.com/akhpp>
#ForwardTagRemoverBot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#ForwardTagRemoverBot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#Function to send video
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
