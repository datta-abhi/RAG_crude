from context import context

# system message to specify particularly not to hallucinate
system_message = "You are an expert in answering accurate questions only about Insurellm, the Insurance tech company.\
                Give brief, accurate answers. If you don't know the answer say so.\
                Do not make anything up if you have not been provided the relevant context."
                
def get_relevant_context(message):
    """
    fetches the details if message contains any of the keys of our Knowledge base dict.
    If multiple keys are matching fetches multiple context values as lists
    Eg: question about Avery Lancaster and Carllm will be [context-doc for Avery, context-doc for Carllm]
    """
    relevant_context = []
    
    for context_title,context_details in context.items():
        if context_title.lower() in message.lower():
            relevant_context.append(context_details)
    return relevant_context     

def add_context(message):
    """
    adds the relevant context in message to the original user message
    """                   
    
    relevant_context = get_relevant_context(message) # note relevant context is a list of docs
    if relevant_context:
        message += "\n\nThe following additional context might be relevant in answering this question:\n\n"
        for i in relevant_context:
            message+= i+ "\n\n"
    return message        

  