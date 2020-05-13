import pickle

_phon_dicts = pickle.load(open('./resources/phon-dicts.pydb','rb'))


def translate(form,source_alpha='jm',target_alpha='elp',cmu_delim='.'):
    """
    Accepts a phonological transcription/form and converts it from one phonetic
    encoding to another.

    form: string, required

    source_alpha: string, optional
        name of the source alphabet/encoding

    target_alpha: string, optional
        name of the target encoding

    cmu_delim: string, optional
        CMU transcriptions need a delimiter because they use two-letter codes;
        cmu_delim is the input/output delimiter when 'cmu' is source/target

    Currently supported encodings: 'jm','elp','cmu'

    NOTE: These source -> target -> source may not return the same form, as some
    codes ('elp','jm') make finer distinctions than other; for example, 'cmu' has
    only one schwa and 'jm' and 'elp' have two.
    """
    if target_alpha is 'cmu':
        return cmu_delim.join([_phon_dicts[(source_alpha,target_alpha)][x] for x in form])
    if source_alpha is 'cmu':
        return ''.join([_phon_dicts[(source_alpha,target_alpha)][x] for x in form.split(cmu_delim)])
    # no delimiters necessary in input or output
    return ''.join([_phon_dicts[(source_alpha,target_alpha)][x] for x in form])
