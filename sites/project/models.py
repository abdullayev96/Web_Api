from django.db import models


"""
    [
  {
    "logo": "https://lh3.googleusercontent.com/pw/AMWts8Bm9NH2R8-7IJ1oejEj-8DcPntY3rM8DRtp6CSEkpJYSNauwKWXe8jy8xxCFOWRw1dgauJcdAW4qN6_xdBaAtaTpUH3dwYFWDlJi10XW2UAkIHHCW-9seH9oiF1W2HEBq6Kydd2mDxI9j6ld7ySD3E=s512-no?authuser=0",
    "title": "Alto's Oddsey",
    "subTitle": "Altoning qiziqarli sarguzashtlarining davomi!",
    "desc": "<p>Ufqning narigi tomonida bepoyon va o‘rganilmagan ulug‘vor cho‘l tomon yo'l oling. Alto va uning do'stlariga qo'shiling va uning sirlarini kashf qilish uchun cho'l bo'ylab cheksiz sayohatga chiqing. Shamol esadigan tepaliklarga chiqing, ajoyib kanyonlarni kesib o'ting va uydan uzoqda joylashgan uzoq vaqt yashirin ibodatxonalarni o'rganing. Va taraqqiyotingiz sari yana ajoyib kashfiyotlar qilishni davom eting.</p>\n<br/>\n<b>MOD: CHEKSIZ PULLAR</b>\n\n",
    "type": "game",
    "version": "1.0.16",
    "size": "80.45MB",
    "os": "5.0.0",
    "updated": "27-Iyun-2022",
    "advantage": "premium",
    "category": "arcade",
    "download": {
      "dw1": "https://drive.google.com/file/d/1VAP8ZlLjm9szmtzCoAiT7Kmg8zdTxbMB/view?usp=share_link",
      "dw2": "https://www.mediafire.com/file/qv9vh9a3p4d704h/altosodyssey-1658845695-www.androeed.ru.apk/file"
    },
    "screenShots": {
      "screen1": "https://lh3.googleusercontent.com/pw/AMWts8DUEq8MGGAWvjeVVhYx62fp3l6kGklJiyVVv92eq21maanx8Lq69YOKaRixCDihs1usKo4JH4jRp_c7lRx9yXobLfTwdXl4i06KJfTJiKUKhGL_X1lhdHd8Ikru17QBbkxHlCGV5oq9HYIjVE1xLmU=w1280-h720-no?authuser=0",
      "screen2": "https://lh3.googleusercontent.com/pw/AMWts8DtKqCnvpSPwhBgKrllyObA5kKVuumxtq43ANSWMlaa2mgrqFm9rSWvyOc4lS1YxFpUUrsoY0WJEOuj054mRb-gW5jreggM3NSYR_SNJtI0AumFLEcInlCeaLRkeyRbmnq7ZSGPsu6SstKorASuh7I=w1280-h720-no?authuser=0",
      "screen3": "https://lh3.googleusercontent.com/pw/AMWts8Ao_D5Xdk3BIEq_Iw6bkldGYsMlyjaGyE4C2tkuT_bZn7h-wDn5UMX2i6zGaweb5vNsAqUlr1S-Kh-_urC3QmEiGqWwPotun7S9LD83Uei1pdKP_PFjTZVHA3Qhjbg1-HXjWl57nfHVv4PoYWtkoiM=w474-h296-no?authuser=0"
    },
    "likes": 0,
    "comments": [],
    "id": 1
  }
]
"""
class  Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Users(models.Model):
    logo  = models.ImageField(upload_to='book')
    title = models.CharField(max_length=400)
    subtitle = models.CharField(max_length=200)
    desc = models.TextField()
    type = models.CharField(max_length=100)
    version = models.FloatField(default=1)
    size = models.CharField(max_length=300)
    os = models.FloatField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    advantage = models.CharField(max_length=400)
    category  = models.ForeignKey("Category", on_delete=models.CASCADE)
    downland = models.CharField(max_length=4000)
    url_name = models.CharField(max_length=2000)
    screen = models.ImageField(upload_to='images/')
    screen1 = models.ImageField(upload_to='good/')
    screen2 = models.ImageField(upload_to='cool/')
    likes = models.BigIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



