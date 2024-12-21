from english.handlers.activity_handlers import handle_audio_exercises,handle_movies_sentences,handle_phrasal_verbs,handle_podcast_exercises
from english.handlers.grammar_handlers import handle_past_tense, handle_present_tense, handle_future_tense, handle_modal_verbs, handle_conditional,handle_ielts_linked_words
from english.handlers.vocabulary_handlers import (handle_questions_IELTS,handle_ielts_vocabulary,handle_films_vocabulary,handle_books_vocabulary,handle_day_vocabulary)
from english.handlers.start_handlers import welcome,grammar,vocabulary,IETLS

state_handlers = {
    "phrasal_verbs": handle_phrasal_verbs,
    "movies_sentences": handle_movies_sentences,
    "audio_exercises": handle_audio_exercises,
    "past_tense": handle_past_tense,
    "present_tense": handle_present_tense,
    "future_tense": handle_future_tense,
    "modal_verbs": handle_modal_verbs,
    "conditional_setence": handle_conditional,
    "ielts_vocabulary": handle_ielts_vocabulary,
    "ielts_linked_words": handle_ielts_linked_words,
    "new_vocabulary": handle_day_vocabulary,
    "films_vocabulary": handle_films_vocabulary,
    "books_vocabulary": handle_books_vocabulary,
    "questions_IELTS": handle_questions_IELTS,
}
english_to_handler = {
    "💭 Phrasal Verbs": handle_phrasal_verbs,
    "🎬 Movie Exercises": handle_movies_sentences,
    "🎧 Listening Exercises": handle_audio_exercises,
    "🎙️ Podcast Exercises": handle_podcast_exercises,
    "🕰️ Past": handle_past_tense,
    "🎁 Present": handle_present_tense,
    "🔮 Future": handle_future_tense,
    "🗯️ Modal Verbs": handle_modal_verbs,
    "🔍 Conditional": handle_conditional,
    "🔗 Linking Words": handle_ielts_linked_words,
    "🗣️ Speaking Questions":handle_questions_IELTS,
    "🆕 Daily Word":handle_day_vocabulary,
    "📜 IELTS Vocabulary":handle_ielts_vocabulary,
    "🎬 Films Vocabulary":handle_films_vocabulary,
    "📚 Books Vocabulary":handle_books_vocabulary
}

text_responses_english = {
    "🇬🇧 English": {"response": "🌟 It was a pleasure to help you with your English today! 😊📚","state": "none","keyboard": welcome,},
    "▶️ Start": {"response": "👋 Hi, I'm your English Trainer Bot! 😊 I'm here to help you improve your English skills. Let's get started! 🚀📚","keyboard": welcome,},
    "start": { "response": "👋 Hi, I'm your English Trainer Bot! 😊 I'm here to help you improve your English skills. Let's get started! 🚀📚","keyboard": welcome,},
    "🆕 Vocabulary": {"response": "Choose a topic:","state": "grammar","keyboard": vocabulary,},
    "📚 Grammar": {"response": "Choose a topic:","state": "grammar","keyboard": grammar,},
    "📜 IELTS": {"response": "Choose a topic:","state": "grammar","keyboard": IETLS,},
}
