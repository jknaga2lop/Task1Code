def transform_dict(keys_list, original_dict):
    if len(keys_list) != len(original_dict):
        raise ValueError("The length of the list and dictionary must be the same.")
    
    new_dict = {}
    for key, value in zip(keys_list, original_dict.items()):
        new_dict[key] = {"category": value[0], "filter": value[1]}
    
    # Print each entry on a new line
    for key, value in new_dict.items():
        print(f"{key}: {value}")

# Example usage:
keys_list = ["var_c_cateogry1_filter",
             "var_category_comp_filter",
             "var_category2_comp_filter",
             "var_size_comp_filter",
             "var_custom_category1_filter",
             "var_c_brand_filter",
             "var_SKUSize_filter",
             "var_d_province_filter",
             "var_c_category1_filter2",
             "var_category_comp_filter2",
             "var_category2_comp_filter2",
             "var_size_comp_filter2",
             "var_c_brand_filter2",
             "var_SKUSize_filter2"]
original_dict = {
            "upper(tpm.category1)":"c.category1",
            "tpm.category_comp":"category_comp",
            "tpm.category2_comp":"category2_comp",
            "tpm.size_comp": "size_comp",
            "tcs.custom_category1":"custom_category1",
            "tpm.brand":"c.brand",
            "CONCAT(tpm.jid, ' (', tpm.size, ')' )": "SKUSize",
            "p.province_avail":"d.province",
            "upper(m.category1)":"c.category1",
            "m.category_comp": "category_comp",
            "m.category2_comp": "category2_comp",
            "m.size_comp": "size_comp",
            "m.brand": "c.brand",
            "CONCAT(m.jid, ' (', m.size, ')' )": "SKUSize"
}

transform_dict(keys_list, original_dict)
