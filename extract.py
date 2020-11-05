def extract_dimension(ifc_file, ifc_type : str):

    if ifc_type=="IfcCovering":
        df = pd.DataFrame(columns = ["Name","IFC_Type", "Perimeter", "Area", "Volume"])
        name_list = []
        perimeter_list = []
        area_list = []
        vol_list = []
        products = ifc_file.by_type(ifc_type)
        for product in products:
            for i, definition in enumerate(product.IsDefinedBy):
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                if i == 0:
                    for property in property_set.HasProperties:
                        if property.Name == "Reference":
                            name_list.append(property.NominalValue.wrappedValue)
                
            if property_set.Name == "PSet_Revit_Dimensions":
                tmp = []
                for property in property_set.HasProperties:
                    tmp.append(property.Name)
                    #print(property.Name)
                    if property.Name == "Perimeter":
                        perimeter_list.append(property.NominalValue.wrappedValue)
                    if property.Name == "Area":
                        area_list.append(property.NominalValue.wrappedValue)
                    if property.Name == "Volume":
                        vol_list.append(property.NominalValue.wrappedValue)
                #print(len(tmp))
                if not "Perimeter" in tmp:
                    perimeter_list.append(np.nan)
                elif not "Area" in tmp:
                    area_list.append(np.nan)
                elif not "Volume" in tmp:
                    vol_list.append(np.nan)

        df["Perimeter"] = perimeter_list
        df["Area"] = area_list
        df["Volume"] = vol_list
        df["IFC_Type"] = ifc_type
        df["Name"] = name_list

        return df

    elif ifc_type=="IfcWall":
        df = pd.DataFrame(columns = ["Name","IFC_Type", "Length", "Area", "Volume"])
        name_list = []
        len_list = []
        area_list = []
        vol_list = []
        products = ifc_file.by_type(ifc_type)
        for product in products:
            for i, definition in enumerate(product.IsDefinedBy):
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                if i == 0:
                    for property in property_set.HasProperties:
                        if property.Name == "Reference":
                            name_list.append(property.NominalValue.wrappedValue)
                
            if property_set.Name == "PSet_Revit_Dimensions":
                tmp = []
                for property in property_set.HasProperties:
                    tmp.append(property.Name)
                    #print(property.Name)
                    if property.Name == "Length":
                        len_list.append(property.NominalValue.wrappedValue)
                    if property.Name == "Area":
                        area_list.append(property.NominalValue.wrappedValue)
                    if property.Name == "Volume":
                        vol_list.append(property.NominalValue.wrappedValue)
                #print(len(tmp))
                if not "Length" in tmp:
                    len_list.append(np.nan)
                elif not "Area" in tmp:
                    area_list.append(np.nan)
                elif not "Volume" in tmp:
                    vol_list.append(np.nan)

        df["Length"] = length_list
        df["Area"] = area_list
        df["Volume"] = vol_list
        df["IFC_Type"] = ifc_type
        df["Name"] = name_list

        return df

    elif ifc_type=="IfcSlab":
        df = pd.DataFrame(columns = ["Name","IFC_Type", "Perimeter", "Area", "Volume", "Thickness"])
        name_list = []
        perimeter_list = []
        area_list = []
        vol_list = []
        thick_list = []
        products = ifc_file.by_type(ifc_type)
        for product in products:
            for i, definition in enumerate(product.IsDefinedBy):
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                if i == 0:
                    for property in property_set.HasProperties:
                        if property.Name == "Reference":
                            name_list.append(property.NominalValue.wrappedValue)
                
            if property_set.Name == "PSet_Revit_Dimensions":
                tmp = []
                for property in property_set.HasProperties:
                    tmp.append(property.Name)
                    #print(property.Name)
                    if property.Name == "Perimeter":
                        perimeter_list.append(property.NominalValue.wrappedValue)
                    if property.Name == "Area":
                        area_list.append(property.NominalValue.wrappedValue)
                    if property.Name == "Volume":
                        vol_list.append(property.NominalValue.wrappedValue)
                    if property.Name == "Thickness":
                        thick_list.append(property.NominalValue.wrappedValue)
                #print(len(tmp))
                if not "Perimeter" in tmp:
                    perimeter_list.append(np.nan)
                elif not "Area" in tmp:
                    area_list.append(np.nan)
                elif not "Volume" in tmp:
                    vol_list.append(np.nan)
                elif not "Thickness" in tmp:
                    thick_list.append(np.nan)

        df["Perimeter"] = perimeter_list
        df["Area"] = area_list
        df["Volume"] = vol_list
        df["IFC_Type"] = ifc_type
        df["Name"] = name_list
        df["Thickness"] = thick_list

        return df

    elif ifc_type=="IfcDoor":
        df = pd.DataFrame(columns = ["Name","IFC_Type", "Thickness", "Height", "Width"])
        name_list = []
        thick_list = []
        height_list = []
        width_list = []
        products = ifc_file.by_type(ifc_type)
        for product in products:
            for i, definition in enumerate(product.IsDefinedBy):
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                if i == 0:
                    for property in property_set.HasProperties:
                        if property.Name == "Reference":
                            name_list.append(property.NominalValue.wrappedValue)
                
            if property_set.Name == "PSet_Revit_Type_Dimensions":
                tmp = []
                for property in property_set.HasProperties:
                    tmp.append(property.Name)
                    #print(property.Name)
                    if property.Name == "Thickness":
                        thick_list.append(property.NominalValue.wrappedValue)
                    if property.Name == "Height":
                        height_list.append(property.NominalValue.wrappedValue)
                    if property.Name == "Width":
                        width_list.append(property.NominalValue.wrappedValue)
                #print(len(tmp))
                if not "Thickness" in tmp:
                    thick_list.append(np.nan)
                elif not "Height" in tmp:
                    height_list.append(np.nan)
                elif not "Width" in tmp:
                    width_list.append(np.nan)

        df["Thickness"] = thick_list
        df["Height"] = height_list
        df["Width"] = width_list
        df["IFC_Type"] = ifc_type
        df["Name"] = name_list

        return df