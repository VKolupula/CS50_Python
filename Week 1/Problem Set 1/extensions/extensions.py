ex = input("Type here: ")
ex = ex.lower().strip()

if ex.endswith(".jpg"):
     print("image/jpeg")
elif ex.endswith(".jpeg"):
     print("image/jpeg")
elif ex.endswith(".png"):
     print("image/png")
elif ex.endswith(".gif"):
     print("image/gif")
elif ex.endswith(".txt"):
     print("text/plain")
elif ex.endswith(".pdf"):
     print("application/pdf")
elif ex.endswith(".zip"):
     print("application/zip")
else:
     print("application/octet-stream")
