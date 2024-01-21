colors = {
    'black':'#3133F',
    'main':'#164D76',
    'secondary':'0077B6',
    'accent':'#00B4DB',
    'white':'#FFFFFF'
}

text = {

    'Membership Status' : {

        "Message" : "Welcome aboard to the Project Blue PH Membership Tiers page, where the tides of commitment meet the shores of distinction in our shared journey towards environmental stewardship. As you navigate this section, you'll discover the tiers that reflect the dedication and impact of our valued members.\n\nEach tier represents a unique level of engagement, recognizing individuals for their contributions to our mission. Whether you are a Sea Sprout just beginning your journey or a Deep Sea Steward with years of dedicated service, these tiers symbolize the diverse efforts shaping Project Blue PH.\n\nJoin us in celebrating your milestones this year and inspiring further excellence in our collective pursuit of a sustainable and thriving marine environment. 🌊💙"
        
    },

    'Exit Process Page' : {
        'Intro' : """As much as we cherish every moment spent together, we understand that life is a journey filled with transitions and new chapters. If you find yourself considering the decision to step away from Project Blue, we want you to know that your choice is respected, and your experiences with us have left an indelible mark on our organization.
            \n\nOur Member Exit Process is designed with transparency and continuous improvement in mind. Your valuable insights, concerns, and feedback are paramount in shaping the future of Project Blue. This page serves as a guide, ensuring that your exit process is smooth, informative, and supportive. In line with this, kindly comply with all the steps to make your exit official. Note that failure to comply with any of them will invalidate your exit request.
            """,

        'Steps' : {
            'Exit Form Submission' : {
            'Instruction' : """To proceed, kindly fill out our Exit Form. Your feedback is crucial to our ongoing efforts to improve and enhance the Project Blue experience. Feel free to share your thoughts, concerns, and suggestions.""",
            'URL' : 'facebook.com'
            },

            'Confirmation and Acknowledgment' : {
                'Instruction' : """Once you've submitted the Exit Form, you'll receive an automated confirmation email thanking you for your contributions.""",
                'URL' : None
            },

            'Virtual Consultation' : {
                'Instruction' : """Please schedule a virtual consultation by clicking here. We value your insights and would appreciate the opportunity to address any concerns you may have.""",
                'URL' : 'facebook.com'
            },

            'Data Analysis and Evaluation' : {
                'Instruction' : """Your input matters. Periodically, we analyze exit data to identify trends and areas for improvement. Kindly fill out this feedback form as your thoughts will greatly contribute to our ongoing commitment to enhance the Project Blue experience.""",
                'URL' : 'facebook.com'
            },
        },

        'Outro' : """Thank you for being a part of Project Blue. We understand that this decision is a personal one, and we genuinely appreciate the time and energy you've invested in our mission. We wish you the very best in all your future endeavors.
            \n\nSea you around,
            \n\nProject Blue
            """
    },

    'Project Evaluation Report Page' : {

        'Message' : """Welcome to the Project Blue Project Evaluations Page, an exclusive hub designed for our dedicated members. Here, we invite you to embark on a comprehensive journey through our ongoing and completed projects, providing valuable insights, collaboration opportunities, and a platform for continuous improvement.""",

    }

}

def get_image(filename):
    s = filename.replace(' ', '%20')
    return f'https://github.com/malenariz/IEdeathon24_Images/blob/main/{s}?raw=true'