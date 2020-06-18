from glob import iglob
import shutil
import os

path=r'C:\\Users\\PANCH MUKESH\\Downloads\\Soumya\\files'
dest=open('meg.mp3','wb')
for filename in iglob(os.path.join(path,'*.mp3')):
	shutil.copyfileobj(open(filename,'rb'),dest)

dest.close()