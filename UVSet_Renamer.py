import maya.cmds as cmds
import maya.OpenMaya as OM

def check_selection_type():
	geo_select = cmds.ls(sl = True)
	
	if not geo_select:
		OM.MGlobal.displayError("Make a selection")
	
	else:
		for sel in geo_select:
			if cmds.nodeType(sel) == "transform":
				if cmds.listRelatives(sel, shapes = True, typ = "mesh"):
					if cmds.polyUVSet(sel, q = True, auv = True)[0] == "map1":
						print("Skipped")
						continue
						
					else:
						cmds.polyUVSet(sel, rename=True, newUVSet='map1')
						#test = cmds.polyUVSet(sel, q = True, auv = True)
						#print(test)
				else:
					grp_select = cmds.listRelatives(c = True)
					for each in grp_select:
						if cmds.polyUVSet(each, q = True, auv = True)[0] == "map1":
							print("Skipped")
							continue
						else:
							cmds.polyUVSet(each, rename=True, newUVSet='map1')



check_selection_type()