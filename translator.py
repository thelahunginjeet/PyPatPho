import pickle

_phon_dicts = pickle.load(open('./resources/phon-dicts.pydb','rb'))


def translate(form,source_alpha='jm',target_alpha='elp'):
    """
    Accepts a phonological transcription/form and converts it from one phonetic
    encoding to another.

    form: string, required

    source_alpha: string, optional
        name of the source alphabet/encoding

    target_alpha: string, optional
        name of the target encoding

    Currently supported encodings: 'jm','elp'
    """
    return ''.join([_phon_dicts[(source_alpha,target_alpha)][x] for x in form])
