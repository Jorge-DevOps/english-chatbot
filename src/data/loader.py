import json

# Función para cargar los datos desde archivos JSON
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Cargar todos los datos de ejercicios
def load_exercise_data():
    return {
        "movies_sentences": load_json("dictionaries/movies_sentences.json"),
        "phrasal_verbs": load_json("dictionaries/phrasal_verbs.json"),
        "writing_exercises": load_json("dictionaries/writing_exercises.json"),
        "audio_exercises": load_json("dictionaries/listening/audio_exercises.json"),
        "modal_verbs": load_json("dictionaries/grammar/modalVerbs/modal_verbs.json"),
        "conditional_setence": load_json("dictionaries/grammar/conditional/conditional_setence.json"),
        "ielts_linked_words": load_json("dictionaries/IELTS/ielts_linked_words.json"),
        "ielts_vocabulary": load_json("dictionaries/vocabulary/ielts_vocabulary.json"),
        "ielts_speakingQuestions": load_json("dictionaries/IELTS/ielts_speakingQuestions.json"),
        "films_vocabulary": load_json("dictionaries/vocabulary/films_vocabulary.json"),
        "books_vocabulary": load_json("dictionaries/vocabulary/books_vocabulary.json"),
        "podcast_exercises": load_json("dictionaries/listening/podcast_exercises.json"),
        # daily
        "daily_Vocabulary": load_json("dictionaries/daily/dailyVocabulary.json"),
        "english_tips": load_json("dictionaries/daily/english_tips.json"),
        "IELTS_tips": load_json("dictionaries/daily/IELTS_tips.json"),
        "daily_PhrasalVerbs": load_json("dictionaries/daily/dailyPhrasalVerbs.json"),
        "daily_Verbs": load_json("dictionaries/daily/dailyVerbs.json"),
        "vocabulary": load_json("dictionaries/daily/dailyVocabularyFull.json"),
        # Grammar
        "past_tense": load_json("dictionaries/grammar/timeTense/past_sentences.json"),
        "present_tense": load_json("dictionaries/grammar/timeTense/present_tense.json"),
        "futuro_tense": load_json("dictionaries/grammar/timeTense/future_tense.json"),
    }
