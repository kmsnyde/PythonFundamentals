# Importing the update_mailing_list_extended function from your previous exercise
# If you desire, you can do this all in a single file
from your_previous_exercise_file.functions_extended import update_mailing_list_extended as ml_updater

# The dictionary with the original mailing list
mailing_list = dict({'307919e9-d6f0-4ecf-9bef-c1320db8941a': ['afarrimond0', 'thartus0@reuters.com', 'opt-out'],
                     '68a32cae-847a-47c5-a77c-0d14ccf11e70': ['tdelicate1', 'skinmond1@ca.gov', 'opt-out'],
                     '8743d75d-c62a-4bae-8990-3390fefbe5c7': ['edelahuntyk', 'fglossup2@gmail.com', 'OPT-OUT'],
                     'a50bd76f-bc4d-4141-9b5d-3bfb9cb4c65d': ['tdelicate10', 'hpatel3@springer.com', 'active'],
                     '26edd0b3-0040-4ba9-8c19-9b69d565df36': ['ogelder2', 'bissett4@mozilla.org', 'unsubscribed'],
                     '5c96189f-95fe-4638-9753-081a6e1a82e8': ['bnornable3', 'aerrett5@over-blog.com', 'opt-out'],
                     '480fb04a-d7cd-47c5-8079-b580cb14b4d9': ['csheraton4', 'pgatherell6-1.com', 'active'],
                     'd08649ee-62ae-4d1a-b578-fdde309bb721': ['tstodart5', 'schasmoor7@gmail.com', 'active'],
                     '5772c293-c2a9-41ff-a8d3-6c666fc19d9a': ['mbaudino6', 'hpatel3@springer.com', 'unsubscribed'],
                     '9e8fb253-d80d-47b5-8e1d-9a89b5bcc41b': ['paspling7', 'dandersen9@mozilla.org', 'active'],
                     '055dff79-7d09-4194-95f2-48dd586b8bd7': ['mknapton8', 'vlewndenh@spiegel.de', 'active'],
                     '5216dc65-05bb-4aba-a516-3c1317091471': ['ajelf9', 'kmacpaikei@purevolume.com', 'unsubscribed'],
                     '41c30786-aa84-4d60-9879-0c53f8fad970': ['cgoodleyh', 'ccowlinj@hp.com', 'active'],
                     '3fd55224-dbff-4c89-baec-629a3442d8f7': ['smcgonnelli', 'dcarragherk@gmail.com', 'opt-out'],
                     '2ac17a63-a64b-42fc-8780-02c5549f23a7': ['mmayoralj', 'bparsissonl@domainmarket.com',
                                                              'unsubscribed']})

def send_message_interval(mailing_list):
     """
       Your docstring documentation starts here.

       For more information on how to proper document your function, please refer to the official PEP8:
        https://www.python.org/dev/peps/pep-0008/#documentation-strings.

    """

    # Array to hold users ids
    ids = []

    # Loop through the mailing list
    for item in # Your dictionary:
        # Append the resulting ids to the list

        # 30 seconds delay after 'send' the next email
        # Tip: you can use a python native package for this task

    # return the list of ids
    return ids