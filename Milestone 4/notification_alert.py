# -*- coding: utf-8 -*-
"""Notification Alert

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TllnO4GCpDjaVCSOJPRqN-1xawzhaZMT
"""

import pandas as pd

def analyze_single_warehouse_data(row, capacity_threshold=0.8, low_utilization_threshold=0.4, risk_threshold="High", sentiment_threshold="Negative"):
    """
    Analyze a single row of warehouse data to provide a single alert for stock management based on utilization, risk analysis, and sentiment.

    Args:
        row (pd.Series): A single row of the warehouse data.
        capacity_threshold (float): Threshold for high utilization (default: 80%).
        low_utilization_threshold (float): Threshold for low utilization (default: 40%).
        risk_threshold (str): Risk level considered critical (default: "High").
        sentiment_threshold (str): Sentiment level considered critical (default: "Negative").

    Returns:
        Tuple: Alert for the specific month with recommended action and reason.
    """
    # Calculate warehouse utilization
    utilization = row['Monthly Incoming'] / row['Warehouse Capacity']

    # Analyze risk factors and sentiment
    if utilization > capacity_threshold or row['Risk Analysis'] == risk_threshold:
        if row['Sentiment'] == sentiment_threshold:
            return (row['Month'], "SELL", f"High utilization ({utilization:.2f}), {row['Risk Analysis']} risk, {row['Sentiment']} sentiment")
        else:
            return (row['Month'], "MONITOR", f"High utilization ({utilization:.2f}) with {row['Risk Analysis']} risk")
    elif utilization < low_utilization_threshold:  # If utilization is very low
        return (row['Month'], "BUY", f"Low utilization ({utilization:.2f}), consider buying material")
    else:
        return (row['Month'], "NO ACTION", "Utilization and risk factors are within acceptable limits")

# Load the warehouse data
data = pd.read_csv("/content/drive/MyDrive/clothing_warehouse_data (1).csv")

# Input: Get user-specified filter
user_input_month = input("Enter the month to analyze (e.g., January): ")

# Filter the dataset for the specified month
filtered_data = data[data['Month'] == user_input_month]

if not filtered_data.empty:
    # Analyze the first row for the given month
    alert = analyze_single_warehouse_data(filtered_data.iloc[0])
    print("\n--- Single Notification ---\n")
    print(f"Month: {alert[0]} | Action: {alert[1]} | Reason: {alert[2]}")
else:
    print(f"No data found for the month: {user_input_month}")

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def analyze_single_warehouse_data(row, capacity_threshold=0.8, low_utilization_threshold=0.4, risk_threshold="High", sentiment_threshold="Negative"):
    """
    Analyze a single row of warehouse data to provide a single alert for stock management based on utilization, risk analysis, and sentiment.
    """
    utilization = row['Monthly Incoming'] / row['Warehouse Capacity']

    if utilization > capacity_threshold or row['Risk Analysis'] == risk_threshold:
        if row['Sentiment'] == sentiment_threshold:
            return (row['Month'], "SELL", f"High utilization ({utilization:.2f}), {row['Risk Analysis']} risk, {row['Sentiment']} sentiment")
        else:
            return (row['Month'], "MONITOR", f"High utilization ({utilization:.2f}) with {row['Risk Analysis']} risk")
    elif utilization < low_utilization_threshold:
        return (row['Month'], "BUY", f"Low utilization ({utilization:.2f}), consider buying material")
    else:
        return (row['Month'], "NO ACTION", "Utilization and risk factors are within acceptable limits")

def send_email_notification(sender_email, sender_password, recipient_email, subject, message):
    """
    Send an email notification via Gmail.

    Args:
        sender_email (str): Sender's Gmail address.
        sender_password (str): Sender's app password or Gmail password.
        recipient_email (str): Recipient's email address.
        subject (str): Subject of the email.
        message (str): Body content of the email.
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        # Connect to the Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Main Script
if __name__ == "__main__":
    # Load the warehouse data
    data = pd.read_csv("/content/drive/MyDrive/clothing_warehouse_data (1).csv")

    # Input: Get user-specified filter
    user_input_month = input("Enter the month to analyze (e.g., January): ")

    # Filter the dataset for the specified month
    filtered_data = data[data['Month'] == user_input_month]

    if not filtered_data.empty:
        # Analyze the first row for the given month
        alert = analyze_single_warehouse_data(filtered_data.iloc[0])
        notification_message = f"Month: {alert[0]} | Action: {alert[1]} | Reason: {alert[2]}"

        print("\n--- Single Notification ---\n")
        print(notification_message)

        # Gmail Notification
        sender_email = "gkarthik3603@gmail.com"  # Replace with your Gmail address
        sender_password = "azea syda glwm ****"  # Replace with your Gmail app password
        recipient_email = "aidl4mars@gmail.com"  # Replace with recipient's email address
        subject = "Warehouse Alert Notification"
        send_email_notification(sender_email, sender_password, recipient_email, subject, notification_message)
    else:
        print(f"No data found for the month: {user_input_month}")
