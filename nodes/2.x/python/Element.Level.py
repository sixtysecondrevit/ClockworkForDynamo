import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetLevel(item):
	val = None
	if hasattr(item, "LevelId"): 
		val = item.Document.GetElement(item.LevelId)
		if val: return val
	if hasattr(item, "Level"):
		val = item.Level
		if val: return val
	if hasattr(item, "GenLevel"):
		val = item.GenLevel
		if val: return val
	if not val:
		try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.INSTANCE_REFERENCE_LEVEL_PARAM).AsElementId())
		except: 
			try: return item.Document.GetElement(item.get_Parameter(BuiltInParameter.INSTANCE_SCHEDULE_ONLY_LEVEL_PARAM).AsElementId())
			except: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetLevel(x) for x in items]
else: OUT = GetLevel(items)