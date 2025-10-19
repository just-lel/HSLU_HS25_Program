import Deff



file_path = "C:\\Users\\opti\\OneDrive - Burkhalter Group\\!Studium\\3.Semester\\DT_Progr\\IFC's\\Eine Steckdose\\Steckdose.IFC"

ifc_type = "IfcOutlet"

dict_outlet = Deff.get_infos_from_Pset(file_path, ifc_type)

print(dict_outlet)



