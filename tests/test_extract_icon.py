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

def test_extractshelldll():
	filepath = "tests/data/SHELL32-4.72.3812.600.DLL"
	extractor = ExtractIcon(filepath)
	groups = extractor.get_group_icons()
	for entry in extractor.pe.DIRECTORY_ENTRY_RESOURCE.entries:
		res_name = pefile.RESOURCE_TYPE[entry.id] if entry.id is not None else None
		print(str(entry.name), res_name, len(entry.directory.entries))
	assert False
	for g in range(0, len(groups)):
		entries = groups[g]
		#print(g, len(entries))
		best = extractor.best_icon(entries)
		for e in range(0, len(entries)):
			#print(g, best, e)
			im = extractor.export(entries, e)
			#im = extractor.export(entries, best)
			#assert im is not None
			#break
			