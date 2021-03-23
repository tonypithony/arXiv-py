# How to create an uncompressed tar archive from a list of filenames:

import tarfile
tar = tarfile.open("sample.tar.gz", "w:gz") # ("sample.tar", "w")
for name in ["Scripts", "Deep Learning For Dummies.pdf", "usedDisk.py",
			 "arxiv-tar.py", "sample.tar"]:
    tar.add(name)
tar.close()


#How to extract an entire tar archive to the current working directory:

# import tarfile
# tar = tarfile.open("sample.tar.gz") # ("sample.tar")
# tar.extractall()
# tar.close()

