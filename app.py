from flask import Flask, render_template, request
import random

app = Flask(__name__)

thoughts_list = []

quotes_data = {
    "study": {
        "quotes": [
            "Your opinion shapes your future.",
            "Think wisely before judging.",
            "Different opinions create new ideas.",
"Studying while everyone sleeps hits differently.",
    "That one chapter you avoid may decide your future.",
    "Silent study sessions create loud success stories.",
    "A tired student today becomes a successful person tomorrow.",
    "The pressure you feel now is shaping your future.",
    "One focused semester can change your entire life.",
    "Students who stay consistent always stand out later.",
    "Every mark carries a story nobody sees.",
    "Studying feels temporary, regret feels permanent.",
    "You are closer to success than your stress makes you believe.",
    "The student life nobody respects now becomes the success everyone admires later.",
    "Some students fight battles nobody notices.",
    "Every small effort matters during exam season.",
    "The future belongs to students who don’t give up midway.",
    "Focus now so you can relax later.",
    "Books become powerful when combined with discipline.",
    "The dream job starts with boring study sessions.",
    "The strongest students are built during stressful nights.",
    "Your study table knows your real struggle.",
    "Success in studies is mostly consistency and patience.",
    "A focused student can defeat distractions and pressure.",
    "Study until opportunities start recognizing your name.",
    "Every sacrifice today becomes comfort tomorrow.",
    "Late-night studying creates early-life success.",
    "You are building your future one page at a time.",
    "The student who survives pressure becomes mentally strong.",
    "The effort nobody sees creates results nobody can ignore.",
    "Study now so life becomes easier later.",
    "Your dedication today becomes your confidence tomorrow.",
    "One exam doesn’t define you, but your effort does.",
    "A disciplined student eventually wins.",
    "Every chapter completed is progress.",
    "Hard study seasons create strong people.",
    "Students who stay patient always improve.",
    "A successful future is hidden inside daily study habits.",
    "The grind behind good grades is never visible.",
    "Keep studying even when motivation disappears.",
    "Every topper once struggled too.",
    "Success starts from one decision to stay serious.",
    "The student who refuses to quit always grows."

        ],
        "image": "opinion.jpg"
    },

    "Situation": {
        "quotes": [
            "Every situation teaches something.",
            "Difficult roads lead to beautiful places.",
            "Stay calm in every situation."
        ],
        "image": "situation.jpg"
    },

    "Situational": {
        "quotes": [
            "Adapt according to situations.",
            "Strong people survive every condition.",
            "Every challenge builds strength."
        ],
        "image": "situational.jpg"
    },

    "fitness": {
        "quotes": [
             "Fitness is a battle against your excuses.",
    "The body improves when the mind stays disciplined.",
    "Every workout builds confidence slowly.",
    "Results come from consistency, not motivation.",
    "The gym changes both body and mindset.",
    "Nobody regrets finishing a workout.",
    "Strong bodies are built during difficult days.",
    "Fitness teaches patience and discipline together.",
    "Every drop of sweat is progress.",
    "Transformation takes time, consistency, and sacrifice.",
    "Excuses never burn calories.",
    "The mirror reflects your habits.",
    "Fitness is self-respect in action.",
    "A healthy routine creates a healthier mindset.",
    "The hardest workout is the one you skip.",
    "Your body hears everything your mind says.",
    "Progress feels slow until people start noticing.",
    "Workout now so your future self feels proud.",
    "Discipline in fitness improves every area of life.",
    "Strong habits create strong physiques.",
    "Fitness is earned daily.",
    "The gym reveals who stays consistent under pressure.",
    "Every rep builds mental strength too.",
    "Your future body depends on today’s choices.",
    "Real confidence starts with self-care.",
    "Fitness is painful sometimes, but regret hurts longer.",
    "The strongest people once struggled with basics too.",
    "Every workout is an investment in yourself.",
    "Results happen quietly before becoming visible.",
    "Train because your health matters.",
    "A healthy body improves your energy and focus.",
    "Consistency changes bodies more than intensity.",
    "Fitness is not temporary motivation, it is lifestyle discipline.",
    "The pain of training creates the pride of transformation.",
    "Workout even when motivation disappears.",
    "Strong minds create strong bodies.",
    "People notice results, not the effort behind them.",
    "The goal is progress, not perfection.",
    "Your health becomes valuable when it starts disappearing.",
    "Fitness is one of the best forms of self-investment."
        ],
        "image": "motivational.jpg"
    },

    "success": {
        "quotes": [
             "Success usually starts where comfort ends.",
    "People admire success but ignore the sacrifices behind it.",
    "Your current situation is not your final destination.",
    "One year of discipline can completely transform your life.",
    "Success is built during lonely seasons.",
    "Nobody notices the struggle before the results appear.",
    "The comeback always starts with pain.",
    "Winners continue even when they feel tired.",
    "Your habits silently decide your future.",
    "Successful people are ordinary people with extraordinary consistency.",
    "The road to success becomes easier after self-discipline.",
    "Every successful person once doubted themselves too.",
    "Success grows slowly before it becomes visible.",
    "The strongest people are created during difficult times.",
    "Your sacrifices today become your success tomorrow.",
    "Success is earned quietly and celebrated loudly.",
    "Pressure creates stronger versions of people.",
    "The hardest phase usually comes before success.",
    "People respect results more than excuses.",
    "Every successful journey begins with one serious decision.",
    "The life you dream about requires daily effort.",
    "You become dangerous once you stop doubting yourself.",
    "Success belongs to people who stay consistent.",
    "A focused mind creates powerful results.",
    "The grind feels painful until the results arrive.",
    "Every small step matters during the success journey.",
    "Success is patience mixed with discipline.",
    "Your mindset decides your direction.",
    "The person who survives failures becomes fearless.",
    "Dreams only work when actions support them.",
    "Consistency beats motivation every time.",
    "Great things happen when excuses disappear.",
    "Success starts from controlling your distractions.",
    "Your future changes when your priorities change.",
    "The struggle phase is temporary.",
    "Every successful story once looked impossible.",
    "Confidence grows after repeated effort.",
    "Successful people master discipline first.",
    "The strongest comeback stories begin from rock bottom.",
    "Success rewards people who refuse to stop."
        ],
        "image": "motive.jpg"
    },

    "Motivation": {
        "quotes": [
            "Dream big and achieve bigger.",
            "Consistency beats talent.",
            "Work hard silently."
        ],
        "image": "motivation.jpg"
    }
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/quotes")
def quotes():

    category = random.choice(
        list(quotes_data.keys())
    )

    quote = random.choice(
        quotes_data[category]["quotes"]
    )

    return render_template(
        "quotes.html",
        category=category,
        quote=quote
    )
@app.route("/gallery")
def gallery():

    images = [
        "opinion.jpg",
        "situation.jpg",
        "situational.jpg",
        "motivational.jpg",
        "motive.jpg",
        "motivation.jpg"
    ]

    return render_template(
        "gallery.html",
        images=images
    )

@app.route("/thoughts", methods=["GET", "POST"])
def thoughts():

    if request.method == "POST":

        thought = request.form.get("thought")

        if thought:
            thoughts_list.append(thought)

    return render_template(
        "thoughts.html",
        thoughts=thoughts_list
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)