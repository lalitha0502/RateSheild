from skills.whatsapp import whatsapp_message_skill

def handle_communication(command: str):
    """
    Delegates all WhatsApp-related commands to the WhatsApp skill.
    No browser automation. No Web forcing.
    """
    whatsapp_message_skill(command)
