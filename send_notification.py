import random
import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Firebase Admin
cred = credentials.Certificate("Service_key.json")
firebase_admin.initialize_app(cred)

def get_random_instagram_notification():
    """
    Returns a random Instagram-like notification.
    """
    notifications = [
        "user1 liked your photo",
        "user2 sent you a friend request",
        "user3 started a live video",
        "user4 commented on your post",
        "user5 tagged you in a photo",
        "user6 shared your post",
        "user7 followed you",
        "user8 sent you a message",
    ]
    return random.choice(notifications)


def send_notification(token, title, body):
    """
    Sends a push notification to a device using FCM.
    """
    try:
        # Create the notification payload
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=token,  # Target device's FCM token
        )

        # Send the notification
        response = messaging.send(message)
        print("Successfully sent message:", response)
        return response

    except Exception as e:
        print("Error sending message:", e)
        return None


if __name__ == "__main__":
    # Replace with the target device's FCM token
    fcm_token = "dgfYQvJVc80w25AwI-pVfM:APA91bF9jjGi-FhZH9DXzspJ2lpuyKNrtuk6PRQa18q-sFul_uoC9hFhZC68iLtM9xeLySnQpXERscJGM9yW9Mx7h0sF0DlSlLzOAiwJ54Wd1aPzUc2oAhs"
    # Generate a random Instagram-like notification
    notification_body = get_random_instagram_notification()
    notification_title = "Instagram Notification"

    # Send the notification
    send_notification(fcm_token, notification_title, notification_body)
