from sound.effects.echo import echofilter
# from ..effects.echo import echofilter


def voc():
    # voc __name__: sound.filters.vocoder
    print('voc __name__:', __name__)
    echofilter(1, 2, 3, 4)
    pass
