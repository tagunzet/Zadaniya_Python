
import re
import requests
import codecs
import cgi
import io, cgitb, sys

cgitb.enable()

if hasattr(sys.stdout, "buffer"):
  def bwrite(s):
    sys.stdout.flush()
    sys.stdout.buffer.write(s)
  write = sys.stdout.write
else:
  wrapper = io.TextIOWrapper(sys.stdout)
  def bwrite(s):
    wrapper.flush()
    sys.stdout.write(s)
  write = wrapper.write

write("Content-type: text/html;charset=utf-8\r\n\r\n")


form = cgi.FieldStorage()

email = form.getfirst("email", "")


s = requests.Session()
data = {"scemail":"tdv@nso.ru", "scpassword":"sosochek322"}
url = "https://help.bars.group/index.php?/Base/User/Login"
r = s.post(url, data=data)
s.cookies
print(s.cookies)