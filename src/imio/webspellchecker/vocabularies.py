class WebspellcheckerProtocolsVocabulary(object):
    """Vocabulary factory for http protocols
    """
    def __call__(self, context):
        return SimpleVocabulary([SimpleTerm("http", "HTTP"), SimpleTerm("https", "HTTPS")])


WebspellcheckerProtocolsVocabularyFactory = WebspellcheckerProtocolsVocabulary()
