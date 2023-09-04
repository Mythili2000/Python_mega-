contents = ["All carrots are to be sliced" \
            "longitudinally.",
            "The carrots were repeatedly sliced.",
            "The crrots are very good for health"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)

a = "I am a string"\
    "on my own"