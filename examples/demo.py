'''Examples of how moodsmith is used'''

from moodsmith import positive_quote

print("-- Positive demo --")
print(positive_quote(language="en", name="bob", enthusiasm=3))
print(positive_quote(language="en", seed=123))
print(positive_quote(language="es", name="bob", enthusiasm=2))
print(positive_quote(language="fr", seed=123, enthusiasm=0))
# Consistent seed will ensure identical outputs between runs
