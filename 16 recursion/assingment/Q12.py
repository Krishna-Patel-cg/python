def reverse(text):
  if len(text) <= 1:
    return text
  return reverse(text[1:]) + text[0]
print(reverse("cat"))

def reverse(text):
  if text=="":
    return ""
  return text[-1]+reverse(text[:-1])
print(reverse("cat"))