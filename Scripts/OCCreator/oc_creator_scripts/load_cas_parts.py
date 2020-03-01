from typing import Dict, List, Iterable, Tuple, Any, Callable

import os
import PIL
from PIL import Image

from oc_creator_scripts.settings import OCCSettings


class OCCAgeGenderIdentifiers:
    TODDLER_HUMAN_MALE = 'pm'
    TODDLER_HUMAN_FEMALE = 'pf'
    TODDLER_HUMAN_UNISEX = 'pu'
    CHILD_HUMAN_MALE = 'cm'
    CHILD_HUMAN_FEMALE = 'cf'
    CHILD_HUMAN_UNISEX = 'cu'
    TEEN_HUMAN_MALE = 'tm'
    TEEN_HUMAN_FEMALE = 'tf'
    TEEN_HUMAN_UNISEX = 'tu'
    YOUNG_ADULT_HUMAN_MALE = 'ym'
    YOUNG_ADULT_HUMAN_FEMALE = 'yf'
    YOUNG_ADULT_HUMAN_UNISEX = 'yu'
    ADULT_HUMAN_MALE = 'am'
    ADULT_HUMAN_FEMALE = 'af'
    ADULT_HUMAN_UNISEX = 'au'
    ELDER_HUMAN_MALE = 'em'
    ELDER_HUMAN_FEMALE = 'ef'
    ELDER_HUMAN_UNISEX = 'eu'
    CHILD_DOG = 'cd'
    ADULT_LARGE_DOG = 'ad'
    ADULT_SMALL_DOG = 'al'
    CHILD_CAT = 'cc'
    ADULT_CAT = 'ac'


OCCFile_Path_Convert = {
    OCCAgeGenderIdentifiers.TODDLER_HUMAN_MALE: 'toddler_human',
    OCCAgeGenderIdentifiers.TODDLER_HUMAN_FEMALE: 'toddler_human',
    OCCAgeGenderIdentifiers.TODDLER_HUMAN_UNISEX: 'toddler_human',
    OCCAgeGenderIdentifiers.CHILD_HUMAN_MALE: 'child_human',
    OCCAgeGenderIdentifiers.CHILD_HUMAN_FEMALE: 'child_human',
    OCCAgeGenderIdentifiers.CHILD_HUMAN_UNISEX: 'child_human',
    OCCAgeGenderIdentifiers.TEEN_HUMAN_MALE: 'adult_human',
    OCCAgeGenderIdentifiers.TEEN_HUMAN_FEMALE: 'adult_human',
    OCCAgeGenderIdentifiers.TEEN_HUMAN_UNISEX: 'adult_human',
    OCCAgeGenderIdentifiers.YOUNG_ADULT_HUMAN_MALE: 'adult_human',
    OCCAgeGenderIdentifiers.YOUNG_ADULT_HUMAN_FEMALE: 'adult_human',
    OCCAgeGenderIdentifiers.YOUNG_ADULT_HUMAN_UNISEX: 'adult_human',
    OCCAgeGenderIdentifiers.ADULT_HUMAN_MALE: 'adult_human',
    OCCAgeGenderIdentifiers.ADULT_HUMAN_FEMALE: 'adult_human',
    OCCAgeGenderIdentifiers.ADULT_HUMAN_UNISEX: 'adult_human',
    OCCAgeGenderIdentifiers.ELDER_HUMAN_MALE: 'adult_human',
    OCCAgeGenderIdentifiers.ELDER_HUMAN_FEMALE: 'adult_human',
    OCCAgeGenderIdentifiers.ELDER_HUMAN_UNISEX: 'adult_human',
    OCCAgeGenderIdentifiers.CHILD_DOG: 'child_pet',
    OCCAgeGenderIdentifiers.ADULT_LARGE_DOG: 'adult_pet',
    OCCAgeGenderIdentifiers.ADULT_SMALL_DOG: 'adult_pet',
    OCCAgeGenderIdentifiers.CHILD_CAT: 'child_pet',
    OCCAgeGenderIdentifiers.ADULT_CAT: 'adult_pet'
}


class Gender:
    MALE = 'MALE'
    FEMALE = 'FEMALE'


class Age:
    TODDLER = 'TODDLER'
    CHILD = 'CHILD'
    TEEN = 'TEEN'
    YOUNG_ADULT = 'YOUNGADULT'
    ADULT = 'ADULT'
    ELDER = 'ELDER'


class Species:
    HUMAN = 'HUMAN'
    LARGE_DOG = 'LARGE_DOG'
    SMALL_DOG = 'SMALL_DOG'
    CAT = 'CAT'


OCCCasPartDataMappings: Dict[str, Dict[str, List[str]]] = {
    OCCAgeGenderIdentifiers.TODDLER_HUMAN_MALE: {
        'available_for_genders': [Gender.MALE, ],
        'available_for_ages': [Age.TODDLER, ],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.TODDLER_HUMAN_FEMALE: {
        'available_for_genders': [Gender.FEMALE, ],
        'available_for_ages': [Age.TODDLER, ],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.TODDLER_HUMAN_UNISEX: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.TODDLER, ],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.CHILD_HUMAN_MALE: {
        'available_for_genders': [Gender.MALE, ],
        'available_for_ages': [Age.CHILD, ],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.CHILD_HUMAN_FEMALE: {
        'available_for_genders': [Gender.FEMALE, ],
        'available_for_ages': [Age.CHILD, ],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.CHILD_HUMAN_UNISEX: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.CHILD, ],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.TEEN_HUMAN_MALE: {
        'available_for_genders': [Gender.MALE, ],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.TEEN_HUMAN_FEMALE: {
        'available_for_genders': [Gender.FEMALE, ],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.TEEN_HUMAN_UNISEX: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.YOUNG_ADULT_HUMAN_MALE: {
        'available_for_genders': [Gender.MALE, ],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.YOUNG_ADULT_HUMAN_FEMALE: {
        'available_for_genders': [Gender.FEMALE, ],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.YOUNG_ADULT_HUMAN_UNISEX: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.ADULT_HUMAN_MALE: {
        'available_for_genders': [Gender.MALE, ],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.ADULT_HUMAN_FEMALE: {
        'available_for_genders': [Gender.FEMALE, ],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.ADULT_HUMAN_UNISEX: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.ELDER_HUMAN_MALE: {
        'available_for_genders': [Gender.MALE, ],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.ELDER_HUMAN_FEMALE: {
        'available_for_genders': [Gender.FEMALE, ],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.ELDER_HUMAN_UNISEX: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.TEEN, Age.YOUNG_ADULT, Age.ADULT, Age.ELDER],
        'available_for_species': [Species.HUMAN, ]
    },
    OCCAgeGenderIdentifiers.CHILD_DOG: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.CHILD, ],
        'available_for_species': [Species.SMALL_DOG, Species.LARGE_DOG]
    },
    OCCAgeGenderIdentifiers.ADULT_SMALL_DOG: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.ADULT, Age.ELDER],
        'available_for_species': [Species.SMALL_DOG]
    },
    OCCAgeGenderIdentifiers.ADULT_LARGE_DOG: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.ADULT, Age.ELDER],
        'available_for_species': [Species.LARGE_DOG]
    },
    OCCAgeGenderIdentifiers.CHILD_CAT: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.CHILD, ],
        'available_for_species': [Species.CAT]
    },
    OCCAgeGenderIdentifiers.ADULT_CAT: {
        'available_for_genders': [Gender.MALE, Gender.FEMALE],
        'available_for_ages': [Age.ADULT, Age.ELDER],
        'available_for_species': [Species.CAT]
    }
}


class OCCCASPartData:
    def __init__(
        self,
        cas_part_display_name: str,
        cas_part_id: int,
        cas_part_icon_id: int,
        cas_part_author: str,
        available_for_genders: Iterable[str],
        available_for_ages: Iterable[str],
        available_for_species: Iterable[str],
        part_tags: Iterable[str]
    ):
        self.cas_part_display_name = cas_part_display_name
        self.cas_part_id = cas_part_id
        self.cas_part_icon_id = cas_part_icon_id
        self.cas_part_resource_key = hex(self.cas_part_id)
        self.cas_part_icon_resource_key = hex(self.cas_part_icon_id)
        self.cas_part_author = cas_part_author
        self.available_for_genders = tuple(available_for_genders)
        self.available_for_ages = tuple(available_for_ages)
        self.available_for_species = tuple(available_for_species)
        self.part_tags = tuple(part_tags)

    @property
    def available_for_genders_string(self) -> str:
        return self._as_enum_elements(self.available_for_genders)

    @property
    def available_for_ages_string(self) -> str:
        return self._as_enum_elements(self.available_for_ages)

    @property
    def available_for_species_string(self) -> str:
        return self._as_enum_elements(self.available_for_species)

    @property
    def part_tags_string(self) -> str:
        return self._as_enum_elements(self.part_tags)

    def _as_enum_elements(self, strings: Iterable[str]) -> str:
        result = ''
        for string in strings:
            if result != '':
                result += '\n'
            result += '    <E>' + string + '</E>'
        return result

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return '\
    <U>\n\
      <T n="part_raw_display_name">{}</T>\n\
      <T n="part_author">{}</T>\n\
      <T n="part_icon_id">{}</T>\n\
      <T n="part_id">{}</T>\n\
      <L n="available_for_genders">{}</L>\n\
      <L n="available_for_ages">{}</L>\n\
      <L n="available_for_species">{}</L>\n\
      <L n="part_tags">{}</L>\n\
    </U>'.format(
            self.cas_part_display_name,
            self.cas_part_author,
            self.cas_part_icon_id,
            self.cas_part_id,
            self.available_for_genders_string,
            self.available_for_ages_string,
            self.available_for_species_string,
            self.part_tags_string
        )


EXCLUDE_PARTS = ['nude', 'bathing']


class OCCCASPartSnippetCollection:
    def __init__(
        self,
        file_key: str,
        file_path: str,
        file_identifier: str,
        collection_name: str
    ):
        self.file_path = file_path
        self.file_key = file_key
        self.file_identifier = file_identifier
        self.collection_name = collection_name
        self.cas_parts = list()

    def add_cas_part(self, part_data: OCCCASPartData):
        self.cas_parts.append(part_data)

    @property
    def file_name(self) -> str:
        return '{}!00000000!{}.{}.SnippetTuning.xml'.format(TuningFileTypes.SNIPPET, self.file_key, self.collection_name)

    @property
    def snippet_file_name(self) -> str:
        return 'CN_OC_Vanilla_{}'.format(self.collection_name.replace(' ', '_'))

    @property
    def snippet_file_decimal_identifier(self) -> str:
        return self.file_identifier

    @property
    def cas_part_strings(self) -> str:
        result: str = ''
        for cas_part in self.cas_parts:
            result += '\n' + str(cas_part) + '\n'
        return result

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return '<?xml version="1.0" encoding="UTF-8"?>\n\
<I c="OCOutfitPartsCollection" i="snippet" m="cnoutfitcustomization.outfit_parts.outfit_parts_collection" n="{}" s="{}">\n\
  <L n="outfit_parts_list">\n\
    {}\
  </L>\n\
</I>'.format(
            self.snippet_file_name,
            self.snippet_file_decimal_identifier,
            self.cas_part_strings
        )


class TuningFileTypes:
    SNIPPET = '7DF2169C'
    CAS_PART = '034AEECB'
    CAS_PART_THUMBNAIL = '3C1AF1F2'
    DST = '00B2D882'


class OCCCasPartLoader:
    @staticmethod
    def load_cas_parts(
        input_folder_path: str=os.path.join('.', 'Input'),
        output_folder_path: str=os.path.join('.', 'Output'),
        message_out: Callable[[str], Any]=print
    ) -> Tuple[OCCCASPartSnippetCollection]:
        global OCCCasPartDataMappings, EXCLUDE_PARTS
        message_out('Working in directory {}'.format(os.getcwd()))
        message_out('Creating OC Support for files within folder \'{}\' and putting it in folder \'{}\''.format(input_folder_path, output_folder_path))
        collections: Dict[str, OCCCASPartSnippetCollection] = dict()

        image_data = dict()
        cas_part_file_names: List[str] = []

        file_names = [potential_file_name for potential_file_name in os.listdir(input_folder_path) if os.path.isfile(os.path.join(input_folder_path, potential_file_name))]
        if len(file_names) == 0:
            message_out('No files found at path \'{}\'.'.format(input_folder_path))

        for file_name in file_names:
            if file_name.endswith('.CASPartThumbnail.png'):
                (resource_type, resource_group, resource_identifier) = OCCCasPartLoader._get_resource_key(file_name)
                image_data[resource_identifier] = file_name
                continue
            if file_name.endswith('.CASPart'):
                cas_part_file_names.append(file_name)
                continue

        for cas_part_file_name in cas_part_file_names:
            (resource_type, resource_group, resource_identifier, cas_part_age_genders_identifier, cas_part_name, tags) = OCCCasPartLoader._get_cas_part_identifiers(cas_part_file_name)
            if not cas_part_name or cas_part_name.lower() in EXCLUDE_PARTS:
                message_out('No cas part name or name is excluded \'{}\''.format(cas_part_file_name))
                continue
            message_out('Parsing cas part {}'.format(cas_part_file_name))
            data_mapping = OCCCasPartDataMappings[cas_part_age_genders_identifier]
            cas_part_thumbnail_resource_key = FNVConvert.fnv64('CN_OC_Vanilla_Image_' + cas_part_name)
            dst_image_hex_key = hex(cas_part_thumbnail_resource_key)
            cas_part_data = OCCCASPartData(
                cas_part_name,
                int(resource_identifier, 16),
                cas_part_thumbnail_resource_key,
                'Maxis',
                data_mapping['available_for_genders'],
                data_mapping['available_for_ages'],
                data_mapping['available_for_species'],
                tags
            )
            output_folder = OCCFile_Path_Convert[cas_part_age_genders_identifier]
            full_file_path = os.path.join(output_folder_path, output_folder)
            if output_folder not in collections:
                identifier = FNVConvert.fnv64(output_folder)
                try:
                    os.mkdir(full_file_path)
                except:
                    pass
                collections[output_folder] = OCCCASPartSnippetCollection(
                    str(hex(identifier)),
                    full_file_path,
                    str(identifier),
                    output_folder
                )
            occ_cas_part_collection = collections[output_folder]
            if resource_identifier in image_data:
                message_out('Rescaling image for CAS Part.'.format(resource_identifier))
                thumbnail_name = image_data[resource_identifier]
                new_img_name = '{}!00000000!{}.png'.format(TuningFileTypes.DST, dst_image_hex_key[2:].upper())
                OCCCasPartLoader._resize_image(os.path.join(input_folder_path, thumbnail_name), os.path.join(occ_cas_part_collection.file_path, new_img_name))
            message_out('Adding CAS Part \'{}\''.format(cas_part_file_name))
            occ_cas_part_collection.add_cas_part(cas_part_data)

        message_out('Done creating OC Support for CAS Parts.')
        return tuple(collections.values())

    @staticmethod
    def _get_resource_key(cas_part_image_file_name: str) -> Tuple[str, str, str]:
        split_file_name: str = cas_part_image_file_name.split('.')
        resource_key = split_file_name[0]
        (resource_type, resource_group, resource_identifier) = resource_key.split('!')
        return resource_type, resource_group, resource_identifier

    @staticmethod
    def _get_cas_part_identifiers(cas_part_file_name: str) -> Tuple[str, str, str, str, str, Tuple[str]]:
        split_file_name: str = cas_part_file_name.split('.')
        resource_key = split_file_name[0]
        cas_part_name = split_file_name[1][2:]
        split_part_name = cas_part_name.split('_')
        tag: str = split_part_name[0].upper()
        cas_part_age_genders_identifier = split_file_name[1][0] + split_file_name[1][1]
        (resource_type, resource_group, resource_identifier) = resource_key.split('!')
        return resource_type, resource_group, resource_identifier, cas_part_age_genders_identifier, cas_part_name[len(tag + '_'):], (tag,)

    @staticmethod
    def _resize_image(input_file_name: str, output_file_name: str, new_width: int=56, new_height: int=56):
        img = Image.open(input_file_name)
        img = img.resize((new_width, new_height), PIL.Image.ANTIALIAS)
        img.save(output_file_name)
        img.close()


class FNVConvert:
    @staticmethod
    def fnv32(text: str, seed=2166136261, high_bit=True):
        fnv_hash = FNVConvert._fnv(text, seed, 16777619, 4294967296)
        if high_bit:
            fnv_hash |= 2147483648
        return fnv_hash

    @staticmethod
    def fnv64(text: str, seed=14695981039346656037, high_bit=True):
        fnv_hash = FNVConvert._fnv(text, seed, 1099511628211, 18446744073709551616)
        if high_bit:
            fnv_hash |= 9223372036854775808
        return fnv_hash

    @staticmethod
    def _fnv(text: str, seed, prime, size):
        string_bytes = text.lower().encode(encoding='utf-8')
        hash_value = seed
        for byte in string_bytes:
            hash_value = hash_value * prime % size
            hash_value = hash_value ^ byte
        return hash_value


in_folder = OCCSettings.input_folder_path
out_folder = OCCSettings.output_folder_path

if OCCSettings.input_is_relative_path:
    in_folder = os.path.join('.', in_folder)

if OCCSettings.output_is_relative_path:
    out_folder = os.path.join('.', out_folder)

loaded_collections = OCCCasPartLoader.load_cas_parts(input_folder_path=in_folder, output_folder_path=out_folder)
if len(loaded_collections) == 0:
    print("No snippets to write.")
else:
    print('Writing snippets.')
    for loaded_collection in loaded_collections:
        path = os.path.join(loaded_collection.file_path, loaded_collection.file_name)
        print('Creating snippet file for \'{}\' Part Count: {}'.format(path, len(loaded_collection.cas_parts)))
        f = open(path, "w+")
        f.write(str(loaded_collection))
        f.close()
    print('Done writing snippets.')
