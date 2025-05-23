# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LigandDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ligand': 'DrugFile',
        'count': 'int'
    }

    attribute_map = {
        'ligand': 'ligand',
        'count': 'count'
    }

    def __init__(self, ligand=None, count=None):
        r"""LigandDto

        The model defined in huaweicloud sdk

        :param ligand: 
        :type ligand: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        :param count: 计算个数
        :type count: int
        """
        
        

        self._ligand = None
        self._count = None
        self.discriminator = None

        self.ligand = ligand
        self.count = count

    @property
    def ligand(self):
        r"""Gets the ligand of this LigandDto.

        :return: The ligand of this LigandDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        return self._ligand

    @ligand.setter
    def ligand(self, ligand):
        r"""Sets the ligand of this LigandDto.

        :param ligand: The ligand of this LigandDto.
        :type ligand: :class:`huaweicloudsdkeihealth.v1.DrugFile`
        """
        self._ligand = ligand

    @property
    def count(self):
        r"""Gets the count of this LigandDto.

        计算个数

        :return: The count of this LigandDto.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this LigandDto.

        计算个数

        :param count: The count of this LigandDto.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, LigandDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
