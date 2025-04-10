# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DockingReceptorDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'receptor': 'ReceptorDrugFile',
        'bounding_box': 'BoundingBoxDto',
        'remove_ion': 'bool',
        'remove_water': 'bool',
        'remove_ligand': 'bool',
        'add_hydrogen': 'bool'
    }

    attribute_map = {
        'receptor': 'receptor',
        'bounding_box': 'bounding_box',
        'remove_ion': 'remove_ion',
        'remove_water': 'remove_water',
        'remove_ligand': 'remove_ligand',
        'add_hydrogen': 'add_hydrogen'
    }

    def __init__(self, receptor=None, bounding_box=None, remove_ion=None, remove_water=None, remove_ligand=None, add_hydrogen=None):
        r"""DockingReceptorDto

        The model defined in huaweicloud sdk

        :param receptor: 
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        :param bounding_box: 
        :type bounding_box: :class:`huaweicloudsdkeihealth.v1.BoundingBoxDto`
        :param remove_ion: 去除受体中的离子
        :type remove_ion: bool
        :param remove_water: 去除受体中的水分子
        :type remove_water: bool
        :param remove_ligand: 去除受体中的配体分子
        :type remove_ligand: bool
        :param add_hydrogen: 增加氢原子
        :type add_hydrogen: bool
        """
        
        

        self._receptor = None
        self._bounding_box = None
        self._remove_ion = None
        self._remove_water = None
        self._remove_ligand = None
        self._add_hydrogen = None
        self.discriminator = None

        self.receptor = receptor
        self.bounding_box = bounding_box
        if remove_ion is not None:
            self.remove_ion = remove_ion
        if remove_water is not None:
            self.remove_water = remove_water
        if remove_ligand is not None:
            self.remove_ligand = remove_ligand
        if add_hydrogen is not None:
            self.add_hydrogen = add_hydrogen

    @property
    def receptor(self):
        r"""Gets the receptor of this DockingReceptorDto.

        :return: The receptor of this DockingReceptorDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        r"""Sets the receptor of this DockingReceptorDto.

        :param receptor: The receptor of this DockingReceptorDto.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        self._receptor = receptor

    @property
    def bounding_box(self):
        r"""Gets the bounding_box of this DockingReceptorDto.

        :return: The bounding_box of this DockingReceptorDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BoundingBoxDto`
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        r"""Sets the bounding_box of this DockingReceptorDto.

        :param bounding_box: The bounding_box of this DockingReceptorDto.
        :type bounding_box: :class:`huaweicloudsdkeihealth.v1.BoundingBoxDto`
        """
        self._bounding_box = bounding_box

    @property
    def remove_ion(self):
        r"""Gets the remove_ion of this DockingReceptorDto.

        去除受体中的离子

        :return: The remove_ion of this DockingReceptorDto.
        :rtype: bool
        """
        return self._remove_ion

    @remove_ion.setter
    def remove_ion(self, remove_ion):
        r"""Sets the remove_ion of this DockingReceptorDto.

        去除受体中的离子

        :param remove_ion: The remove_ion of this DockingReceptorDto.
        :type remove_ion: bool
        """
        self._remove_ion = remove_ion

    @property
    def remove_water(self):
        r"""Gets the remove_water of this DockingReceptorDto.

        去除受体中的水分子

        :return: The remove_water of this DockingReceptorDto.
        :rtype: bool
        """
        return self._remove_water

    @remove_water.setter
    def remove_water(self, remove_water):
        r"""Sets the remove_water of this DockingReceptorDto.

        去除受体中的水分子

        :param remove_water: The remove_water of this DockingReceptorDto.
        :type remove_water: bool
        """
        self._remove_water = remove_water

    @property
    def remove_ligand(self):
        r"""Gets the remove_ligand of this DockingReceptorDto.

        去除受体中的配体分子

        :return: The remove_ligand of this DockingReceptorDto.
        :rtype: bool
        """
        return self._remove_ligand

    @remove_ligand.setter
    def remove_ligand(self, remove_ligand):
        r"""Sets the remove_ligand of this DockingReceptorDto.

        去除受体中的配体分子

        :param remove_ligand: The remove_ligand of this DockingReceptorDto.
        :type remove_ligand: bool
        """
        self._remove_ligand = remove_ligand

    @property
    def add_hydrogen(self):
        r"""Gets the add_hydrogen of this DockingReceptorDto.

        增加氢原子

        :return: The add_hydrogen of this DockingReceptorDto.
        :rtype: bool
        """
        return self._add_hydrogen

    @add_hydrogen.setter
    def add_hydrogen(self, add_hydrogen):
        r"""Sets the add_hydrogen of this DockingReceptorDto.

        增加氢原子

        :param add_hydrogen: The add_hydrogen of this DockingReceptorDto.
        :type add_hydrogen: bool
        """
        self._add_hydrogen = add_hydrogen

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DockingReceptorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
