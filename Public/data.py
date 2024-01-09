colors = {
    'black':'#3133F',
    'main':'#164D76',
    'secondary':'0077B6',
    'accent':'#00B4DB',
    'white':'#FFFFFF'
}

text = {
    'Landing Page' : {
        'org_info' : 'Project Blue (PB) is a youth-led nonprofit organization that focuses on raising awareness and providing sustainable solutions on ocean pollution and marine conservation.',
        'org_background' : 'Project Blue started as a cleanup idea that turned into an organization after the realization that cleanups aren’t enough and that we have to be more sustainable. We do a mix of physical and online projects that advocate for the oceans. It was founded in the province of Ilocos last December 2020.',
        'slogan' : 'More than cleanups',
        'slogan_info' : 'Raising awareness and providing sustainable solutions on ocean pollution and marine conservation in the Philippines.',

        'benefits_text' : 'Become a Project Blue member today and unlock a world of opportunities to make a lasting impact on the environment while advancing your personal and professional growth!',
        'benefits' : {
            "✨ Impactful Contribution": {
                "Engage in Meaningful Projects": "Actively contribute to hands-on projects focused on environmental conservation, floating fish cages, life vests, and more.",
                "See Your Impact": "Witness the tangible results of your efforts as Project Blue works towards creating a positive and lasting impact on the environment."
            },
            "🗣️ Skill Development and Networking": {
                "Professional Growth": "Access skill development opportunities through workshops, training sessions, and leadership roles within your chosen committee.",
                "Build a Network": "Connect with like-minded individuals, professionals, and key stakeholders, fostering valuable relationships for personal and career development."
            },
            "🫂 Inclusive Community": {
                "Diverse and Inclusive": "Join a diverse team that welcomes individuals from various backgrounds, including students and professionals, creating an inclusive and supportive community.",
                "Shared Values": "Be part of a dedicated team united by a common goal of environmental conservation, fostering collaboration and camaraderie."
            },
            "🎖️ Recognition and Appreciation": {
                "Certification of Commitment": "Receive official acknowledgment and certification for your commitment to Project Blue's mission as a certified changemaker.",
                "Public Recognition": "Enjoy public recognition for your contributions through social media shout-outs, newsletters, and acknowledgment at Project Blue events."
            },
            "🤝 Exclusive Opportunities": {
                "Leadership Roles": "Take on leadership positions in committees, developing and showcasing your leadership skills in areas such as engineering, creative projects, and more.",
                "Exclusive Events": "Attend exclusive events, webinars, and gatherings, gaining access to unique learning experiences and networking opportunities within the environmental conservation sector."
            }
        },

        'apply' : 'Lorem ipsum dolor sit amet',
        'donate_description' : 'Lorem ipsum dolor sit amet',
        'donate_done' : 'Lorem ipsum dolor sit amet',


    }
}

landing_page_impact = [
    ('Farmers given livelihood', 4),
    ('SustainaBoats donated', 15),
    ('Bottles upcycled', 5000),
    ('Communities reached', 12),
    ('Mothers with PWD children empowered', 5),
    ('Filipinos reached in speaking engagements', 13500)
]

donation_methods = {
    'BDO' : ('012620009274', 'Adem Marione C. Inovejas', '.png'),
    'UnionBank' : ('1094 8544 9981', 'Adem Marione C. Inovejas', '.png'),
    'PayMaya' : ('09275584432', 'Adem I.', '.webp'),
    'GCash' : ('09275584432', 'Adem I.', '.png')
}

def get_image(filename):
    s = filename.replace(' ', '%20')
    return f'https://github.com/malenariz/IEdeathon24_Images/blob/main/{s}?raw=true'