import ifcopenshell, ifcopenshell.geom, ifcopenshell.util.shape

print(ifcopenshell.__version__)

file_path = "C:\\Users\\opti\\OneDrive - Burkhalter Group\\!Studium\\3.Semester\\DT_Progr\\IFC's\\Eine Steckdose\\Steckdose.IFC"

ifc_file = ifcopenshell.open(file_path)

for outlet in ifc_file.by_type("IfcOutlet"):
    print(outlet.Name)

print("hello")

print("hey")