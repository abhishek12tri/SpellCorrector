import pkg_resources
from symspellpy import SymSpell, Verbosity


class SpellHandler:
    def __init__(self) -> None:
        self.symspell = SymSpell(max_dictionary_edit_distance = 2, prefix_length=7)
        self.dict_path = pkg_resources.resource_filename("symspellpy", "frequency_bigramdictionary_en_243_342.txt")
        self.bigram_path = pkg_resources.resource_filename("symspellpy", "frequency_dictionary_en_82_765.txt")

    def text_corrector(self, input_text):
        self.symspell.load_dictionary(self.dict_path, term_index=0, count_index=1)
        self.symspell.load_bigram_dictionary(self.bigram_path, term_index=0, count_index=1)

        suggestions = self.symspell.lookup_compound(input_text, max_edit_distance=2)

        print(suggestions)
        sent = []
        for suggest in suggestions:
            sent.append(suggest)

        print(sent)
        predicted_sentence = str(sent[0])
        print(predicted_sentence)
        splitter = predicted_sentence[:-6]
        return splitter

