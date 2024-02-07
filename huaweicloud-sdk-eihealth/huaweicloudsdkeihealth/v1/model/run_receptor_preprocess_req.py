# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunReceptorPreprocessReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'ReceptorDrugFileReq',
        'remove_water': 'bool',
        'remove_ion': 'bool',
        'remove_ligand': 'bool',
        'add_hydrogen': 'bool'
    }

    attribute_map = {
        'file': 'file',
        'remove_water': 'remove_water',
        'remove_ion': 'remove_ion',
        'remove_ligand': 'remove_ligand',
        'add_hydrogen': 'add_hydrogen'
    }

    def __init__(self, file=None, remove_water=None, remove_ion=None, remove_ligand=None, add_hydrogen=None):
        """RunReceptorPreprocessReq

        The model defined in huaweicloud sdk

        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        :param remove_water: 去除水分子
        :type remove_water: bool
        :param remove_ion: 去除离子
        :type remove_ion: bool
        :param remove_ligand: 去除配体分子
        :type remove_ligand: bool
        :param add_hydrogen: 增加氢原子
        :type add_hydrogen: bool
        """
        
        

        self._file = None
        self._remove_water = None
        self._remove_ion = None
        self._remove_ligand = None
        self._add_hydrogen = None
        self.discriminator = None

        self.file = file
        if remove_water is not None:
            self.remove_water = remove_water
        if remove_ion is not None:
            self.remove_ion = remove_ion
        if remove_ligand is not None:
            self.remove_ligand = remove_ligand
        if add_hydrogen is not None:
            self.add_hydrogen = add_hydrogen

    @property
    def file(self):
        """Gets the file of this RunReceptorPreprocessReq.

        :return: The file of this RunReceptorPreprocessReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this RunReceptorPreprocessReq.

        :param file: The file of this RunReceptorPreprocessReq.
        :type file: :class:`huaweicloudsdkeihealth.v1.ReceptorDrugFileReq`
        """
        self._file = file

    @property
    def remove_water(self):
        """Gets the remove_water of this RunReceptorPreprocessReq.

        去除水分子

        :return: The remove_water of this RunReceptorPreprocessReq.
        :rtype: bool
        """
        return self._remove_water

    @remove_water.setter
    def remove_water(self, remove_water):
        """Sets the remove_water of this RunReceptorPreprocessReq.

        去除水分子

        :param remove_water: The remove_water of this RunReceptorPreprocessReq.
        :type remove_water: bool
        """
        self._remove_water = remove_water

    @property
    def remove_ion(self):
        """Gets the remove_ion of this RunReceptorPreprocessReq.

        去除离子

        :return: The remove_ion of this RunReceptorPreprocessReq.
        :rtype: bool
        """
        return self._remove_ion

    @remove_ion.setter
    def remove_ion(self, remove_ion):
        """Sets the remove_ion of this RunReceptorPreprocessReq.

        去除离子

        :param remove_ion: The remove_ion of this RunReceptorPreprocessReq.
        :type remove_ion: bool
        """
        self._remove_ion = remove_ion

    @property
    def remove_ligand(self):
        """Gets the remove_ligand of this RunReceptorPreprocessReq.

        去除配体分子

        :return: The remove_ligand of this RunReceptorPreprocessReq.
        :rtype: bool
        """
        return self._remove_ligand

    @remove_ligand.setter
    def remove_ligand(self, remove_ligand):
        """Sets the remove_ligand of this RunReceptorPreprocessReq.

        去除配体分子

        :param remove_ligand: The remove_ligand of this RunReceptorPreprocessReq.
        :type remove_ligand: bool
        """
        self._remove_ligand = remove_ligand

    @property
    def add_hydrogen(self):
        """Gets the add_hydrogen of this RunReceptorPreprocessReq.

        增加氢原子

        :return: The add_hydrogen of this RunReceptorPreprocessReq.
        :rtype: bool
        """
        return self._add_hydrogen

    @add_hydrogen.setter
    def add_hydrogen(self, add_hydrogen):
        """Sets the add_hydrogen of this RunReceptorPreprocessReq.

        增加氢原子

        :param add_hydrogen: The add_hydrogen of this RunReceptorPreprocessReq.
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
        if not isinstance(other, RunReceptorPreprocessReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
