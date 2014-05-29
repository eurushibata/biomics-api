from flask import url_for
from manage import db
from mongoengine import *

connect('tcga')

class Tcga(db.Document):
	AliquotID = db.StringField(required=True)
	Level1Data = db.StringField(required=True)
	Disease = db.StringField(required=True)
	BCRBatch = db.IntField(required=True)
	Platform = db.StringField(required=True)
	Level2Data = db.StringField(required=True)
	ReceivingCenter = db.StringField(required=True)
	Level3Data = db.StringField(required=True)

	# [{'Aliquot ID': 'TCGA-AV-A03D-20A-02D-A29J-05', 'Level 1 Data': 'Submitted', 'Disease': 'ACC', 'BCR Batch': '0', 'Platform': 'HumanMethylation450', 'Level 2 Data': 'Submitted', 'Receiving Center': 'jhu-usc.edu (CGCC)', 'Level 3 Data': 'Submitted'}, {'Aliquot ID': 'TCGA-OR-A5J1-01A-11D-A29H-01', 'Level 1 Data': 'Submitted', 'Disease': 'ACC', 'BCR Batch': '304', 'Platform': 'Genome_Wide_SNP_6', 'Level 2 Data': 'Submitted', 'Receiving Center': 'broad.mit.edu (CGCC)', 'Level 3 Data': 'Submitted'}, {'Aliquot ID': 'TCGA-OR-A5J1-01A-11D-A29I-10', 'Level 1 Data': 'Not Submitted', 'Disease': 'ACC', 'BCR Batch': '304', 'Platform': 'Curated Mutation Calling', 'Level 2 Data': 'Submitted', 'Receiving Center': 'broad.mit.edu (GSC)', 'Level 3 Data': 'Not Submitted'}]

	# ReferenceField

class Url(db.Document):
	AliquotID =
	Level = 
	fileName =
	fileId = 
	archiveName = 
	archiveId = 
	fileUrl = 

class Review(db.Document):


	# https://tcga-data.nci.nih.gov/datareports/aliquotArchive.json?aliquotId=TCGA-AV-A03D-20A-02D-A29J-05&level=2