def generate_study_plan(style, subjects, attention, time_pref, focus_subject):

    plan = []

    for sub in subjects:

        # Focus subject priority
        if sub.lower() == focus_subject.lower():
            plan.append(f"🔥 PRIORITY: Focus deeply on {sub}")

        if style == "Video Learner":
            plan.append(f"🎥 Watch video lectures for {sub}")

        elif style == "Practice Learner":
            plan.append(f"🧠 Solve problems and MCQs for {sub}")

        elif style == "Text Learner":
            plan.append(f"📖 Read notes/book for {sub}")

        elif style == "Group Learner":
            plan.append(f"👥 Discuss {sub} with peers")

        else:
            plan.append(f"🔁 Use mixed methods for {sub}")

    # Attention span logic
    plan.append(f"⏱ Study in {attention}-minute focused sessions")

    # Time preference logic
    plan.append(f"⏰ Best study time: {time_pref}")

    return plan