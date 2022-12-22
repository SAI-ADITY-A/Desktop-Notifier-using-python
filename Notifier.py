import time
from plyer import notification

notification.notify(
    title = "Please Drink some Water!",
    message = "Getting enough water every day is important for your health. Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones.",
    app_icon = "icon.ico",
    timeout = 12
)