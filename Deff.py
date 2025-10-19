import ifcopenshell
from ifcopenshell.util.element import get_psets

def get_infos_from_Pset(file_path: str, ifc_type: str):
    """Liefert eine Liste mit einem Eintrag pro Objekt:
       GUID, Familie, Typ, tin_Leistung, Gleichzeitigkeitsfaktor, Kommentare
    """
    ifc = ifcopenshell.open(file_path)
    rows = []

    for obj in ifc.by_type(ifc_type):
        psets = get_psets(obj)
        p = psets.get("Pset_Elektro", {})  # falls das Pset fehlt

        rows.append({
            "GUID": obj.GlobalId,
            "ifc_type": ifc_type,
            "Familie": p.get("Familie"),
            "Typ": p.get("Typ"),
            "tin_Leistung": p.get("tin_Leistung"),
            "Gleichzeitigkeitsfaktor": p.get("Gleichzeitigkeitsfaktor"),
            "Kommentare": p.get("Kommentare")
        })

    return rows







