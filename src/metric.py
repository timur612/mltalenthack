from Levenshtein import distance
import json


def levenshtein_between_json(true_json: str, predicted_json: str) -> int:
    total_l_dis = 0

    true_text = json.load(open(true_json))
    gpt_text = json.load(open(predicted_json))

    for key in true_text["resume"].keys():
        if key == "contactItems":
            contact_true = ""
            contact_pred = ""
            for contact in true_text["resume"][key]:
                for contact_key in true_text["resume"][key][0]:
                    contact_true += contact[contact_key]
            for contact in gpt_text["resume"][key]:
                for contact_key in gpt_text["resume"][key][0]:
                    contact_pred += contact[contact_key]

            total_l_dis += distance(contact_true, contact_pred)

        elif key == "educationItems":
            ed_true = ""
            ed_pred = ""
            for education in true_text["resume"][key]:
                for education_key in true_text["resume"][key][0]:
                    ed_true += education[education_key]
            for education in gpt_text["resume"][key]:
                for education_key in gpt_text["resume"][key][0]:
                    ed_pred += education[education_key]

            total_l_dis += distance(ed_true, ed_pred)

        elif key == "experienceItems":
            exp_true = ""
            exp_pred = ""
            for experience in true_text["resume"][key]:
                for experience_key in true_text["resume"][key][0]:
                    exp_true += experience[experience_key]
            for experience in gpt_text["resume"][key]:
                for experience_key in gpt_text["resume"][key][0]:
                    exp_pred += experience[experience_key]

            total_l_dis += distance(exp_true, exp_pred)

        elif key == "languageItems":
            lang_true = ""
            lang_pred = ""
            for language in true_text["resume"][key]:
                for language_key in true_text["resume"][key][0]:
                    lang_true += language[language_key]
            for language in gpt_text["resume"][key]:
                for language_key in gpt_text["resume"][key][0]:
                    lang_pred += language[language_key]

            total_l_dis += distance(lang_true, lang_pred)

        else:
            total_l_dis += distance(true_text["resume"][key], gpt_text["resume"][key])

    return total_l_dis
