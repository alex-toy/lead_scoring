import os
NAME_FILE = 'data.csv'
FULL_PATH_DATA = os.path.os.getcwd()

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
DATA_DIR = os.path.join(REPO_DIR, 'data')
FILE_DATA = os.path.join(DATA_DIR, NAME_FILE)

OUTPUTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../output'))
SAVED_FILENAME = 'processed_data.csv'

#new column names :
ID_CLIENT = 'ID_CLIENT'
ORIGINE_LEAD = 'ORIGINE_LEAD'
SOURCE_LEAD = 'SOURCE_LEAD'
NIVEAU_LEAD = 'NIVEAU_LEAD'
QUALITE_LEAD = 'QUALITE_LEAD'
CONTACT_PAR_MAIL = 'CONTACT_PAR_MAIL'
CONTACT_PAR_TELEPHONE = 'CONTACT_PAR_TELEPHONE'
STATUT_ACTUEL = 'STATUT_ACTUEL'
TARGET = 'TARGET'
NB_VISITES = 'NB_VISITES'
DUREE_SUR_SITEWEB = 'DUREE_SUR_SITEWEB'
NB_PAGES_VUES_PAR_VISITE = 'NB_PAGES_VUES_PAR_VISITE'
DERNIERE_ACTIVITE = 'DERNIERE_ACTIVITE'
DERNIERE_ACTIVITE_NOTABLE = 'DERNIERE_ACTIVITE_NOTABLE'
PAYS = 'PAYS'
VILLE = 'VILLE'
SPECIALISATION = 'SPECIALISATION'
TAGS = 'TAGS'
INDEX_ACTIVITE = 'INDEX_ACTIVITE'
INDEX_PROFIL = 'INDEX_PROFIL'
SCORE_ACTIVITE = 'SCORE_ACTIVITE'
SCORE_PROFIL = 'SCORE_PROFIL'
ANNONCE_VUE = 'ANNONCE_VUE'
MAGAZINE = 'MAGAZINE'
ARTICLE_JOURNAL = 'ARTICLE_JOURNAL'
FORUM = 'FORUM'
JOURNAUX = 'JOURNAUX'
PUB_DIGITALE = 'PUB_DIGITALE'
RECOMMANDATION = 'RECOMMANDATION'
C_ENT_PARLER_NS = 'C_ENT_PARLER_NS'
SOUH_TU_REC_INFOS = 'SOUH_TU_REC_INFOS'
SOUH_REC_MAJ_PROG = 'SOUH_REC_MAJ_PROG'
SOUH_REC_MAJ_MP = 'SOUH_REC_MAJ_MP'
SOUH_PAYER_CHEQUE = 'SOUH_PAYER_CHEQUE'
SOUH_REC_COPIE_LB = 'SOUH_REC_COPIE_LB'
 

NEW_COL_NAMES = [
    ID_CLIENT,
    ORIGINE_LEAD,
    SOURCE_LEAD,
    NIVEAU_LEAD,
    QUALITE_LEAD,
    CONTACT_PAR_MAIL,
    CONTACT_PAR_TELEPHONE,
    STATUT_ACTUEL,
    TARGET,
    NB_VISITES,
    DUREE_SUR_SITEWEB,
    NB_PAGES_VUES_PAR_VISITE,
    DERNIERE_ACTIVITE,
    DERNIERE_ACTIVITE_NOTABLE,
    PAYS,
    VILLE,
    SPECIALISATION,
    TAGS,
    INDEX_ACTIVITE,
    INDEX_PROFIL,
    SCORE_ACTIVITE,
    SCORE_PROFIL,
    ANNONCE_VUE,
    MAGAZINE,
    ARTICLE_JOURNAL,
    FORUM,
    JOURNAUX,
    PUB_DIGITALE,
    RECOMMANDATION,
    C_ENT_PARLER_NS,
    SOUH_TU_REC_INFOS,
    SOUH_REC_MAJ_PROG,
    SOUH_REC_MAJ_MP,
    SOUH_PAYER_CHEQUE,
    SOUH_REC_COPIE_LB
]

CAT_FEAT = [
    ORIGINE_LEAD, SOURCE_LEAD, NIVEAU_LEAD, TAGS, VILLE, SPECIALISATION, INDEX_ACTIVITE,
    QUALITE_LEAD, CONTACT_PAR_MAIL, STATUT_ACTUEL, DERNIERE_ACTIVITE, DERNIERE_ACTIVITE_NOTABLE
]



CAT_FEAT_TO_PROCESS = [
    ORIGINE_LEAD, SOURCE_LEAD, NIVEAU_LEAD, TAGS, VILLE, SPECIALISATION, INDEX_ACTIVITE, QUALITE_LEAD, DERNIERE_ACTIVITE_NOTABLE
]


NUM_FEAT = [ NB_VISITES, SCORE_ACTIVITE, NB_PAGES_VUES_PAR_VISITE, SCORE_PROFIL, DUREE_SUR_SITEWEB ]


COLS_TO_KEEP = CAT_FEAT + NUM_FEAT + [TARGET]


use_origin_lead = ['formulaire lead add', 'soumission landing page', 'api']

use_source_lead = ['olark chat', 'organic search', 'google', 'reference',
                    'direct traffic', 'facebook', 'referral sites', 'welingak website']

use_niveau_lead = ['select', 'autre leads', 'lead potentiel', "etudiant d'une certaine ecole"]

use_qualite_lead = ['pas du tout pertinent', 'pourrait etre pertinent', 'pas sur',
                    'tres pertinent', 'peu pertinent']

use_der_act_not = ['email ouvert', 'modifie', 'sms envoye', 'page visitee sur le site', 'conversation chat',
                    'a clique sur le lien dans le mail', 'email rejete', 'desinscrit', 'email marque comme spam']

use_tags = ['appele', 'diplome en cours', 'deja un etudiant', 'desactive', 'ferme', "interesse par d'autres cours",
            'interesse par un mba full-time', 'occupe', "perdu au profit d'un concurrent",
        'ne pas suivre de formation continue', 'reviendra apres avoir lu le courriel']

use_ville = ['select', 'autres villes de maharashtra', 'mumbai', 'autres villes', 
                'thane et sa peripherie', 'autres villes metropolitaines']

use_spec = ['marketing management', 'banking, investment and insurance',
       'hospitality management', 'finance management', 'select',
       'it projects management', 'human resource management',
       'travel and tourism', 'supply chain management',
       'operations management', 'international business',
       'business administration', 'healthcare management',
       'media and advertising', 'retail management']

use_index_act = ['moyen', 'eleve', 'faible']

#############################


use_origin_lead = ['Formulaire Lead Add', 'Soumission landing page', 'API']

use_source_lead = ['Olark Chat', 'Organic Search', 'Google', 'Reference', 'Direct Traffic', 
                   'Facebook', 'Referral Sites', 'Welingak Website']

use_niveau_lead = ['Select', 'Autre leads', 'Lead potentiel', "Etudiant d'une certaine école"]

use_qualite_lead = ['Pas du tout pertinent', 'Pourrait être pertinent', 'Pas sur', 
                    'Très pertinent', 'Peu pertinent']

use_der_act_not = ['Email ouvert', 'Modifié', 'SMS envoyé', 'Page visitée sur le site', 
                   'Conversation Chat', 'A cliqué sur le lien dans le mail', 'Email rejeté',
                   'Désinscrit', 'Email marqué comme Spam']

use_tags = ['Appelé', 'Diplôme en cours', 'Déjà un étudiant', 'Désactivé', 'Fermé', "Intéressé par d'autres cours", 
 'Intéressé par un MBA full-time',  'Occupé', "Perdu au profit d'un concurrent", 
 'Ne pas suivre de formation continue', 'Reviendra après avoir lu le courriel']

use_ville = ['Select', 'Autres villes de Maharashtra', 'Mumbai', 'Autres villes', 'Thane et sa périphérie',
               'Autres villes métropolitaines']

use_spec = ['Marketing Management', 'Banking, Investment And Insurance',
       'Hospitality Management', 'Finance Management', 'Select',
       'IT Projects Management',
       'Human Resource Management', 'Travel and Tourism',
       'Supply Chain Management', 'Operations Management',
       'International Business', 'Business Administration',
       'Healthcare Management', 'Media and Advertising',
       'Retail Management']

use_index_act = ['Moyen', 'Elevé', 'Faible']

use_lists = [
    use_origin_lead,
    use_source_lead,
    use_niveau_lead,
    use_tags,
    use_ville,
    use_spec,
    use_index_act,
    use_qualite_lead,
    use_der_act_not,
]





