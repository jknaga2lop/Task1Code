def process_string(input_string):
    # Remove newline characters and replace with space
    cleaned_string = input_string.replace('\n', ' ')
    
    # Replace tabs or consecutive spaces with a single space
    cleaned_string = ' '.join(cleaned_string.split())
    
    # Replace '{{' and '}}' with double quotes
    cleaned_string = cleaned_string.replace('{{', '"').replace('}}', '",')
    
    # Enclose the string with parentheses
    processed_string = f"[{cleaned_string}]"
    
    print(processed_string)

# Example usage:
input_string = '''
        {{ var_date_filter }}
        {{var_c_category1_filter}}
        {{var_category_comp_filter}}
        {{var_category2_comp_filter}}
        {{var_size_comp_filter}}
        {{var_custom_category1_filter}}
        {{var_c_brand_filter}}
        {{var_SKUSize_filter}}
'''

process_string(input_string)
