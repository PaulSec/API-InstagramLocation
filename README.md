Instagram Location OSINT Tool 
==========

Quick util to retrieve Instagram pictures from a specific location

### How to use it? 

```python
from InstagramLocationAPI import *

InstagramLocationAPI = InstagramLocationAPI()
res = InstagramLocationAPI.search('-122.4369134', '37.7571571')
print res
```

the variable *res* will contain some JSON including all the pictures that have been taken in the area. 
I also added a file called *json.output* will show you what kind of information you can retrieve. 

### Contribute

If you find a bug or anything, feel free to ping me on Twitter: [@PaulWebSec](https://www.twitter.com/PaulWebSec)