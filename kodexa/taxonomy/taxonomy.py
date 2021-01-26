import random
from typing import List, Optional
import uuid

class Taxon:

    def __init__(self, label: str, name: str, id: Optional[str] = None, color: Optional[str] = None,
                 value_path: Optional[str] = None, data_path: Optional[str] = None, options=None,
                 metadata_path: Optional[str] = None, node_types=None, enabled=True):
        if options is None:
            options = []
        if node_types is None:
            node_types = []
        self.id = id if id and len(id) > 0 else str(uuid.uuid4())
        self.name: str = name
        self.label: str = label
        self.color = "#" + ("%06x" % random.randint(0, 0xFFFFFF)) if color is None else color
        self.children: List[Taxon] = []
        self.value_path = value_path
        self.data_path = data_path
        self.metadata_path = metadata_path
        self.node_types = node_types
        self.options = options
        self.enabled = enabled

    @staticmethod
    def from_dict(dict_taxon):
        new_taxon = Taxon(label=dict_taxon['label'], name=dict_taxon['name'], id=dict_taxon['id'],
                          color=dict_taxon['color'], node_types=dict_taxon['nodeTypes'],
                          options=dict_taxon['options'], enabled=self.enabled,
                          value_path=dict_taxon['valuePath'] if 'valuePath' in dict_taxon else None,
                          data_path=dict_taxon['dataPath'] if 'dataPath' in dict_taxon else None,
                          metadata_path=dict_taxon['metadataPath'] if 'metadataPath' in dict_taxon else None)

        if 'children' in dict_taxon:
            for child_taxon_dict in dict_taxon['children']:
                new_taxon.children.append(Taxon.from_dict(child_taxon_dict))

        return new_taxon

    def to_dict(self):
        dict = {'id': self.id, 'name': self.name, 'color': self.color, 'valuePath': self.value_path,
                'label': self.label, 'nodeTypes': self.node_types, 'options': self.options, 'enabled': self.enabled,
                'dataPath': self.data_path, 'metadataPath': self.metadata_path, 'children': []}

        for child in self.children:
            dict['children'].append(child.to_dict())

        return dict


class Taxonomy:

    def __init__(self, taxonomy_type='CONTENT', enabled=True, ref=""):
        self.taxons: List[Taxon] = []
        self.taxonomy_type = taxonomy_type
        self.enabled = enabled
        self.ref = ref

    def add_taxon(self, label: str, name: str):
        new_taxon = Taxon(label, name)
        self.taxons.append(new_taxon)
        return new_taxon

    @staticmethod
    def from_dict(dict_taxonomy):
        new_taxonomy = Taxonomy(ref=dict_taxonomy['ref'], enabled=dict_taxonomy['enabled'],
                                taxonomy_type=dict_taxonomy['taxonomyType'])

        if 'taxons' in dict_taxonomy:
            for taxon_dict in dict_taxonomy['taxons']:
                new_taxonomy.taxons.append(Taxon.from_dict(taxon_dict))

        return new_taxonomy

    def to_dict(self):
        dict = {'taxonomyType': self.taxonomy_type, 'enabled': self.enabled, 'ref': self.ref, 'taxons': []}

        for child in self.taxons:
            dict['taxons'].append(child.to_dict())

        return dict


class RemoteTaxonomy:

    @staticmethod
    def get(ref: str):
        from kodexa import KodexaPlatform
        url = f"{KodexaPlatform.get_url()}/api/taxonomies/{ref.replace(':', '/')}"

        import requests
        response = requests.get(url,
                                headers={"x-access-token": KodexaPlatform.get_access_token(),
                                         "content-type": "application/json"})

        return Taxonomy.from_dict()
