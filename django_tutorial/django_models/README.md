# Django Models
-   A model is the single, definitive source of information about your data

-   Field types
    - null (True for empty values. Default is False)
    - blank(True for a blank field. Default is False)
    - choices - A sequence of 2-tuples to use as choices for a field
                e.g:
                choices = [
                    ('ENG', 'English'),
                    ('MTH', 'Mathematics'),
                    ('FRN', 'French'),
                ]

    - default - The default value for the field
    - help_text - "help" text to be displayed with the form widget
    - primary_key - If True, this field is the primary key for the model
    - unique - If True, this field must be unique throughout the table


# Verbose Field Names
- Verbose name: It's an optional first positional argument given to all the fields, except for ForeignKey, ManyToManyField and OneToOneField.

- For example: name = models.CharField("Your Name:", max_length = 30)