#!/usr/bin/python

import csv
"""The purpose of this module is to parse each FCC
ULS database type into corresponding python types"""

def tryConvertString( input ):
	"""
	Try some different string encodings.
	Hopefully someday we can find the standard the FCC uses.
	"""
	for conversion in [ 'iso_8859_1', 'cp1252', 'utf-8' ]:
		try:
			return unicode(input, conversion, 'strict' )
		except UnicodeDecodeError:
			pass
	return unicode( input, 'iso_8859_1', 'ignore' )

def parse( fileLikeObject, keys ):
	"""Map a key list onto a CSV file and do some conversions"""
	intKeys=[
		"antennaNumber",
		"locationNumber",
		"fccRegistrationNumber",
		"frequencyNumber",
		"prototypeSequenceId",
		"sequenceNumber",
		"uniqueSystemIdentifier",
		"voyageNumber",
		]

	iso8859Keys=[
		"firstName",
		"middleInitial",
		"lastName",
		"suffix",
		"address",
		"city",
		]

	for row in csv.reader(fileLikeObject, delimiter='|'):
		retn = dict(zip(keys, row))
		for key in intKeys:
			if (key in retn) and retn[key]:
				retn[key] = int(retn[key])
		for key in iso8859Keys:
			if (key in retn) and retn[key]:
				retn[key] = tryConvertString( retn[key] )
		yield retn


def parseAM(fileLikeObject):
	"""Parse AM.dat table"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"operatorClass",
		"groupCode",
		"regionCode",
		"trusteeCallSign",
		"trusteeIndicator",
		"physicianCertification",
		"veSignature",
		"systematicCallSignChange",
		"vanityCallSignChange",
		"vanityRelationship",
		"previousCallSign",
		"previousOperatorClass",
		"trusteeName",
		]

	return parse( fileLikeObject, keys )

def parseCO(fileLikeObject):
	"""Parse CO.dat table"""
	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"callSign",
		"commentDate",
		"description",
		"statusCode",
		"statusDate"
		]

	return parse( fileLikeObject, keys )

def parseEN(fileLikeObject):
	"""Parse EN.dat table"""

	keys = [
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"entityType",
		"licenseeId",
		"entityName",
		"firstName",
		"middleInitial",
		"lastName",
		"suffix",
		"phone",
		"fax",
		"email",
		"address",
		"city",
		"state",
		"zip",
		"poBox",
		"attentionLine",
		"sgin",
		"fccRegistrationNumber",
		"applicationTypeCode",
		"applicationTypeCodeOther",
		"statusCode",
		"statusDate",
		]

	return parse( fileLikeObject, keys )

def parseHD(fileLikeObject):
	"""Parse HD.dat table"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"licenseStatus",
		"radioServiceCode",
		"grantDate",
		"expiredDate",
		"cancellationDate",
		"eligibilityRuleNum",
		"reservedPosition1",
		"alien",
		"alienGovernment",
		"alienCorporation",
		"alienOfficer",
		"alienControl",
		"revoked",
		"convicted",
		"adjudged",
		"reservedPosition2",
		"commonCarrier",
		"nonCommonCarrier",
		"privateComm",
		"fixed",
		"mobile",
		"radiolocation",
		"satellite",
		"developmentalOrStaOrDemonstration",
		"interconnectedService",
		"certifierFirstName",
		"certifierMI",
		"certifierLastName",
		"certifierSuffix",
		"certifierTitle",
		"female",
		"blackOrAfricanAmerican",
		"nativeAmerican",
		"hawaiian",
		"asian",
		"white",
		"hispanic",
		"effectiveDate",
		"lastActionDate",
		"auctionId",
		"broadcastServicesRegulatoryStatus",
		"bandManager",
		"broadcastServicesTypeOfRadioService",
		"alienRuling",
		"licenseeNameChange",
		]

	return parse( fileLikeObject, keys )

def parseHS(fileLikeObject):
	"""Parse HS.dat table"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"callSign",
		"logDate",
		"code",
		]

	return parse( fileLikeObject, keys )

def parseLA(fileLikeObject):
	"""Parse LA.dat table"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"callSign",
		"attachmentCode",
		"attachmentDescription",
		"attachmentDate",
		"attachmentFileName",
		"actionPerformed",
		]

	return parse( fileLikeObject, keys )

def parseSC(fileLikeObject):
	"""Parse SC.dat table"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"specialConditionType",
		"specialConditionCode",
		"statusCode",
		"statusDate",
		]

	return parse( fileLikeObject, keys )

def parseSF(fileLikeObject):
	"""Parse SF.dat table"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"licenseFreeFormType",
		"uniqueLicenseFreeFormIdentifier",
		"sequenceNumber",
		"licenseFreeFormCondition",
		"statusCode",
		"statusDate",
		]

	return parse( fileLikeObject, keys )


def parseSV(fileLikeObject):
	"""Parse SV.dat table"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"voyageNumber"
		"voyageDescription",
		]

	return parse( fileLikeObject, keys )

def parseTP(fileLikeObject):
	"""Parse TP.dat table - Transmission Method or Protocol"""

	keys=[
		"recordType",
		"uniqueSystemIdentifier",
		"ulsFileNumber",
		"ebfNumber",
		"callSign",
		"locationNumber",
		"antennaNumber",
		"prototypeSequenceId",
		"protocol",
		"protocolDescription",
		"actionPerformed",
		"statusCode",
		"statusDate",
		]

	return parse( fileLikeObject, keys )
