import anthropic, requests, json, os, random
from datetime import datetime

ANTHROPIC_KEY = os.environ["ANTHROPIC_API_KEY"]
META_TOKEN    = os.environ["META_ACCESS_TOKEN"]
IG_ACCOUNT_ID = os.environ["IG_ACCOUNT_ID"]
LOG_FILE      = "post_log.json"

TOPICS = [
  "diabetic retinopathy warning signs Tirupati",
  "retinal detachment emergency signs Tirupati",
  "macular degeneration age related risk",
  "children eye exam school age Tirupati",
  "dry eyes remedies summer Andhra Pradesh",
  "floaters in vision when to worry",
  "cataract surgery recovery tips Tirupati",
  "screen time eye strain tips Telugu families",
  "pilgrim eye care Tirupati Tirumala",
  "glaucoma silent vision thief awareness",
]

def pick_topic():
    try:
        log = json.load(open(LOG_FILE))
    except:
        log = {"used": []}
    remaining = [t for t in TOPICS if t not in log["used"]]
    if not remaining:
        log["used"] = []
        remaining = TOPICS
    topic = random.choice(remaining)
    log["used"].append(topic)
    json.dump(log, open(LOG_FILE, "w"))
    return topic

def get_season():
    m = datetime.now().month
    if m in [3,4,5]: return "Peak summer in Tirupati - UV exposure and dry eyes very common"
    elif m in [6,7,8]: return "Monsoon - conjunctivitis and eye infections spike in Tirupati"
    elif m in [10,11]: return "Diwali season - firecracker eye injury awareness important"
    elif m == 1: return "Sankranti - pilgrim season in Tirupati at its peak"
    else: return "Remind patients about routine eye check-ups in Tirupati"

def generate_post(topic):
    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system="""You are the social media voice of Dr. Madhavi Retina Eye Care,
located in Tirupati, Andhra Pradesh. Dr. Madhavi is a senior retina
specialist serving Tirupati and surrounding Rayalaseema region.
GOALS: Drive patients to book appointments. Establish Dr. Madhavi as
the number 1 retina expert in Tirupati.
EVERY POST MUST:
- Open with a hook
- Explain clearly in simple language
- Include 1 sentence in Telugu script
- Mention Dr. Madhavi and Tirupati by name
- End with CTA: phone number 94402 28492 and Tirupati
- Include 25 hashtags mixing local and medical tags
- Stay under 2200 characters
TONE: Warm, friendly, trusted family doctor.""",
        messages=[{"role": "user", "content": f"""
Write an Instagram post about: {topic}
Seasonal context: {get_season()}
Today: {datetime.now().strftime("%B %Y")}
Return ONLY the post text, nothing else.
"""}]
    )
    return msg.content[0].text

def post_to_instagram(caption):
    image_url = "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=1080"
    r = requests.post(
        f"https://graph.facebook.com/v20.0/{IG_ACCOUNT_ID}/media",
        data={"image_url": image_url, "caption": caption, "access_token": META_TOKEN}
    )
    print("Media response:", r.json())
    creation_id = r.json()["id"]
    r2 = requests.post(
        f"https://graph.facebook.com/v20.0/{IG_ACCOUNT_ID}/media_publish",
        data={"creation_id": creation_id, "access_token": META_TOKEN}
    )
    print("Publish response:", r2.json())
    print(f"Posted at {datetime.now()}: {caption[:60]}...")

topic   = pick_topic()
caption = generate_post(topic)
post_to_instagram(caption)
