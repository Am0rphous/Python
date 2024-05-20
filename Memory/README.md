# Memory

### Load stuff into memory
- [source code by joslinm](https://stackoverflow.com/questions/11159077/python-load-2gb-of-text-file-to-memory). - [mmap — https://docs.python.org/3/library/mmap.html](https://docs.python.org/3/library/mmap.html)
````
import mmap

with open('dump.xml', 'rb') as f:
  # Size 0 will read the ENTIRE file into memory!
  m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) #File is open read-only

  # Proceed with your code here -- note the file is already in memory
  # so "readine" here will be as fast as could be
  data = m.readline()
  while data:
    # Do stuff
    data = m.readline()
````
