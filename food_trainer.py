from clarifai_basic import ClarifaiCustomModel

concept = ClarifaiCustomModel()

# train bubble tea
concept.positive('https://upload.wikimedia.org/wikipedia/commons/a/a2/Bubble_Tea.png', 'bubbletea')
concept.positive('https://upload.wikimedia.org/wikipedia/commons/0/00/BubbleTeaHoneydewMapleStreet20July2008.jpg', 'bubbletea')
concept.positive('http://www.ru-screwd.com.php53-14.ord1-1.websitetestlink.com/wp-content/uploads/2011/08/mango-bubble-tea.jpg', 'bubbletea')
concept.positive('http://dontcallmeafoodblogger.files.wordpress.com/2013/03/p3030940.jpg', 'bubbletea')
concept.positive('http://25.media.tumblr.com/tumblr_ljey0zEIS91qcezjyo1_400.jpg', 'bubbletea')
concept.negative('http://d261z78q37tks5.cloudfront.net/blog/wp-content/uploads/2012/03/coffee_th.jpg', 'bubbletea')
concept.negative('http://www.dunkindonuts.com/content/dunkindonuts/en/menu/beverages/icedbeverages/tea/iced_tea/_jcr_content/block/image.img.png/1397647558307.png', 'bubbletea')
concept.negative('http://www.bonappetit.com/wp-content/uploads/2013/07/thai-style-iced-tea-646.jpg', 'bubbletea')
concept.negative('http://www.taisin-ss.co.jp/icemold/english/blog/wp-content/uploads/2014/04/Fotolia_11776028_M.jpg', 'bubbletea')
concept.negative('http://images2.westword.com/imager/five-cocktails-only-a-dickhead-would-order/u/original/6460314/cocktail_5.jpg', 'bubbletea')

concept.train('bubbletea')
