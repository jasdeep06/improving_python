import sys
import importSaga
import os


print(os.path.splitext(os.path.dirname(os.path.abspath(__file__))))

sys.path.append("/Users/jasdeepsinghchhabra/improving_python/importSaga/code")
from sizeFunction import approximate_size
print(sys.path)


print(approximate_size("/Users/jasdeepsinghchhabra/improving_python/importSaga/dataAndCaller/data/video.mp4"))