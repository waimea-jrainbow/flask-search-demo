#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class CreatureTable:

    NAME = "creatures"

    SCHEMA = """
        CREATE TABLE creatures (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            species TEXT NOT NULL,
            name    TEXT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO creatures (species, name)
        VALUES
            ("Dragon",  "Pippa"),
            ("Unicorn", "Barry"),
            ("Vampire", "Helen"),
            ("Troll", "Ian"),
            ("Fairy", "Summer"),
            ("Centaur", "Keely"),
            ("Griffin", "Rogan"),
            ("Centaur", "Shannon"),
            ("Dryad", "Vielka"),
            ("Wisp", "Christen"),
            ("Goblin", "Aidan"),
            ("Lich", "Chelsea"),
            ("Goblin", "Ila"),
            ("Unicorn", "Allistair"),
            ("Manticore", "Henry"),
            ("Troll", "Magee"),
            ("Troll", "Bradley"),
            ("Zombie", "Ishmael"),
            ("Centaur", "Josiah"),
            ("Unicorn", "Elton"),
            ("Manticore", "Hu"),
            ("Unicorn", "Dieter"),
            ("Dryad", "Myles"),
            ("Vampire", "August"),
            ("Dryad", "Joelle"),
            ("Ogre", "Colleen"),
            ("Werewolf", "Kermit"),
            ("Elf", "Joseph"),
            ("Zombie", "Stacey"),
            ("Goblin", "Galena"),
            ("Griffin", "Riley"),
            ("Griffin", "Keelie"),
            ("Lich", "Tatyana"),
            ("Fairy", "Mechelle"),
            ("Goblin", "Dacey"),
            ("Werewolf", "Aretha"),
            ("Zombie", "Lilah"),
            ("Elf", "Armand"),
            ("Griffin", "Valentine"),
            ("Manticore", "Aurora"),
            ("Wisp", "Merritt"),
            ("Elf", "Wing"),
            ("Manticore", "Lael"),
            ("Fairy", "Lunea"),
            ("Manticore", "Jamalia"),
            ("Dryad", "Celeste"),
            ("Mermaid", "Tanya"),
            ("Goblin", "Kamal"),
            ("Dryad", "Amela"),
            ("Dragon", "Ethan"),
            ("Troll", "August"),
            ("Lich", "Seth"),
            ("Lich", "Mechelle"),
            ("Vampire", "Linus"),
            ("Dragon", "Ori"),
            ("Griffin", "Nevada"),
            ("Werewolf", "Jordan"),
            ("Centaur", "Fallon"),
            ("Fairy", "Buckminster"),
            ("Centaur", "Colette"),
            ("Griffin", "Allistair"),
            ("Zombie", "Jolene"),
            ("Elf", "Nayda"),
            ("Fairy", "Francesca"),
            ("Elf", "Thane"),
            ("Dryad", "Aphrodite"),
            ("Werewolf", "Anjolie"),
            ("Dryad", "Todd"),
            ("Centaur", "Isaiah"),
            ("Dryad", "Barbara"),
            ("Unicorn", "Tatum"),
            ("Dryad", "Wallace"),
            ("Dryad", "Bruno"),
            ("Elf", "Kiayada"),
            ("Mermaid", "Jaquelyn"),
            ("Elf", "Brenna"),
            ("Unicorn", "Cynthia"),
            ("Dragon", "Sarah"),
            ("Mermaid", "Philip"),
            ("Dragon", "Donovan"),
            ("Dragon", "Kyle"),
            ("Griffin", "Aline"),
            ("Dryad", "Rylee"),
            ("Unicorn", "Lacey"),
            ("Centaur", "Anastasia"),
            ("Mermaid", "Imogene"),
            ("Dryad", "Charlotte"),
            ("Troll", "Benjamin"),
            ("Fairy", "Drake"),
            ("Dragon", "Charity"),
            ("Manticore", "Drew"),
            ("Dragon", "Debra"),
            ("Zombie", "Angela"),
            ("Troll", "Daquan"),
            ("Manticore", "Zachary"),
            ("Mermaid", "Bruce"),
            ("Ogre", "Fuller"),
            ("Goblin", "Clayton"),
            ("Dryad", "Dai"),
            ("Griffin", "Stuart")
    """
 

# Add more table classes here...



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1,
#     Table2,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
#       foreign keys AFTER the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    CreatureTable,
    # Add more tables here...
]

