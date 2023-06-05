import pkg_resources
from symspellpy import SymSpell, Verbosity


"""Loading all the corrector components for faster response"""
sym_spell = SymSpell(max_dictionary_edit_distance = 2, prefix_length=7)

dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
bigram_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_bigramdictionary_en_243_342.txt"
)

sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=1)


class SpellHandler:
    def __init__(self) -> None:
       pass

    def text_corrector(self, input_text):
        suggestions = sym_spell.lookup_compound(input_text, max_edit_distance=2)

        sent = []
        for suggest in suggestions:
            sent.append(suggest)

        predicted_sentence = str(sent[0])
        splitter = predicted_sentence[:-6]
        return splitter

