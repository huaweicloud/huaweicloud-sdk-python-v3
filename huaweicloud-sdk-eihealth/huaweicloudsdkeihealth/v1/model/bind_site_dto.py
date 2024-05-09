# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindSiteDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'receptor': 'ReceptorDrugFile',
        'bounding_box': 'BoundingBoxDto',
        'remove_ion': 'bool',
        'remove_water': 'bool',
        'remove_ligand': 'bool',
        'add_hydrogen': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'receptor': 'receptor',
        'bounding_box': 'bounding_box',
        'remove_ion': 'remove_ion',
        'remove_water': 'remove_water',
        'remove_ligand': 'remove_ligand',
        'add_hydrogen': 'add_hydrogen'
    }

    def __init__(self, name=None, receptor=None, bounding_box=None, remove_ion=None, remove_water=None, remove_ligand=None, add_hydrogen=None):
        """BindSiteDto

        The model defined in huaweicloud sdk

        :param name: 靶点名称
        :type name: str
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
        
        

        self._name = None
        self._receptor = None
        self._bounding_box = None
        self._remove_ion = None
        self._remove_water = None
        self._remove_ligand = None
        self._add_hydrogen = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.receptor = receptor
        if bounding_box is not None:
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
    def name(self):
        """Gets the name of this BindSiteDto.

        靶点名称

        :return: The name of this BindSiteDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BindSiteDto.

        靶点名称

        :param name: The name of this BindSiteDto.
        :type name: str
        """
        self._name = name

    @property
    def receptor(self):
        """Gets the receptor of this BindSiteDto.

        :return: The receptor of this BindSiteDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        return self._receptor

    @receptor.setter
    def receptor(self, receptor):
        """Sets the receptor of this BindSiteDto.

        :param receptor: The receptor of this BindSiteDto.
        :type receptor: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFile`
        """
        self._receptor = receptor

    @property
    def bounding_box(self):
        """Gets the bounding_box of this BindSiteDto.

        :return: The bounding_box of this BindSiteDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.BoundingBoxDto`
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        """Sets the bounding_box of this BindSiteDto.

        :param bounding_box: The bounding_box of this BindSiteDto.
        :type bounding_box: :class:`huaweicloudsdkeihealth.v1.BoundingBoxDto`
        """
        self._bounding_box = bounding_box

    @property
    def remove_ion(self):
        """Gets the remove_ion of this BindSiteDto.

        去除受体中的离子

        :return: The remove_ion of this BindSiteDto.
        :rtype: bool
        """
        return self._remove_ion

    @remove_ion.setter
    def remove_ion(self, remove_ion):
        """Sets the remove_ion of this BindSiteDto.

        去除受体中的离子

        :param remove_ion: The remove_ion of this BindSiteDto.
        :type remove_ion: bool
        """
        self._remove_ion = remove_ion

    @property
    def remove_water(self):
        """Gets the remove_water of this BindSiteDto.

        去除受体中的水分子

        :return: The remove_water of this BindSiteDto.
        :rtype: bool
        """
        return self._remove_water

    @remove_water.setter
    def remove_water(self, remove_water):
        """Sets the remove_water of this BindSiteDto.

        去除受体中的水分子

        :param remove_water: The remove_water of this BindSiteDto.
        :type remove_water: bool
        """
        self._remove_water = remove_water

    @property
    def remove_ligand(self):
        """Gets the remove_ligand of this BindSiteDto.

        去除受体中的配体分子

        :return: The remove_ligand of this BindSiteDto.
        :rtype: bool
        """
        return self._remove_ligand

    @remove_ligand.setter
    def remove_ligand(self, remove_ligand):
        """Sets the remove_ligand of this BindSiteDto.

        去除受体中的配体分子

        :param remove_ligand: The remove_ligand of this BindSiteDto.
        :type remove_ligand: bool
        """
        self._remove_ligand = remove_ligand

    @property
    def add_hydrogen(self):
        """Gets the add_hydrogen of this BindSiteDto.

        增加氢原子

        :return: The add_hydrogen of this BindSiteDto.
        :rtype: bool
        """
        return self._add_hydrogen

    @add_hydrogen.setter
    def add_hydrogen(self, add_hydrogen):
        """Sets the add_hydrogen of this BindSiteDto.

        增加氢原子

        :param add_hydrogen: The add_hydrogen of this BindSiteDto.
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
        if not isinstance(other, BindSiteDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
