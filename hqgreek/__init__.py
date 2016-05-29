import logging

from .classes import Verb, Noun, Adjective

__all__ = ['Verb', 'Noun', 'Adjective']

logging.getLogger(__name__).addHandler(logging.NullHandler())
