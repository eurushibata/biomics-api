import json

class TCGA:
	def populate(obj):
		for index, item in enumerate(obj):
			db.tcga.insert(item)