"""Helper functions for creating different OpenAI assistants."""

from openai import OpenAI

MODEL = "gpt-3.5-turbo-16k"


def create_chatbot_assistant(client: OpenAI, model: str = MODEL):
    """Assistant handling customer questions 24/7 across channels."""

    instructions = (
        "You are a customer support chatbot available 24/7 on the website, Messenger and WhatsApp. "
        "Answer questions using the company's FAQ, pricing, regulations, return policy and email templates. "
        "Collect leads (name, email, phone), provide notes and cite sources for your answers."
    )

    return client.beta.assistants.create(
        name="Chatbot 24/7",
        instructions=instructions,
        model=model,
    )


def create_offer_generator_assistant(client: OpenAI, model: str = MODEL):
    """Assistant that composes branded PDF/DOCX offers."""

    instructions = (
        "Generate a coherent offer document in PDF or DOCX. "
        "Use the provided client name, scope, price variants and deadlines. "
        "Include branding, chapters, footer and signature placeholders."
    )

    return client.beta.assistants.create(
        name="Offer Generator",
        instructions=instructions,
        model=model,
    )


def create_weekly_report_assistant(client: OpenAI, model: str = MODEL):
    """Assistant that summarizes weekly results and recommendations."""

    instructions = (
        "Each week provide a summary of sales, leads, website traffic, campaigns and reviews. "
        "Return a PDF report, a link to the dashboard and five priorities for next week. "
        "Detect anomalies and drops in key metrics."
    )

    return client.beta.assistants.create(
        name="Weekly Report",
        instructions=instructions,
        model=model,
    )


def create_review_analysis_assistant(client: OpenAI, model: str = MODEL):
    """Assistant monitoring opinions and proposing responses."""

    instructions = (
        "Monitor reviews from Google, Facebook and stores. "
        "Analyse sentiment, track keywords and trends. "
        "Provide response suggestions compliant with company policy and escalate negatives with context."
    )

    return client.beta.assistants.create(
        name="Review Monitor",
        instructions=instructions,
        model=model,
    )


def create_order_assistant(client: OpenAI, model: str = MODEL):
    """Assistant answering questions about orders and returns."""

    instructions = (
        "Allow customers to check order status, return conditions and product availability. "
        "Given an order number, return the current stage and carrier. "
        "Provide return forms, labels and conditions. "
        "Integrate with ERP/WMS to check stock levels and alert about shortages."
    )

    return client.beta.assistants.create(
        name="Order Assistant",
        instructions=instructions,
        model=model,
    )


def create_sales_assistant(client: OpenAI, model: str = MODEL):
    """Assistant collecting and qualifying sales leads."""

    instructions = (
        "Collect leads through a conversational form and ask about needs. "
        "Score potential using industry, budget and timeline to set priorities. "
        "Route to the correct account owner and schedule meetings with the salesperson."
    )

    return client.beta.assistants.create(
        name="Sales Assistant",
        instructions=instructions,
        model=model,
    )

