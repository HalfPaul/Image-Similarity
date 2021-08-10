from Ahash import Ahash
from Phash import Phash
from Dhash import Dhash
from Whash import Whash

algos = [Ahash, Phash, Dhash, Whash]

for algo in algos:
    img1 = algo("images/image1.jpg")
    img2 = algo("images/image2.jpg")
    img3 = algo("images/image3.jpg")
    assert img1.check_similarity(img2)
    assert not img1.check_similarity(img3)
    print(type(img1).__name__, "- Success")
    
