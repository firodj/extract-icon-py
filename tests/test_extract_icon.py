from extract_icon import *
from PIL import Image, ImageChops

def test_extracticon():
	filepath = 'tests/data/hello.exe'
	extractor = ExtractIcon(filepath)
	groups = extractor.get_group_icons()

	assert 1 == len(groups)
	assert 9 == len(groups[0])

	assert 6 == extractor.best_icon(groups[0])

	im1 = extractor.export(groups[0], 6)
	im2 = Image.open('tests/data/psxfin.png')	

	b = ImageChops.difference(im1, im2).getbbox()
	assert b is None