def validate_output(answer, context):
    return{
        "length_ok":len(answer)<500,
        "contains_context":any(phrase in answer for phrase in context.split()[:10])
    }