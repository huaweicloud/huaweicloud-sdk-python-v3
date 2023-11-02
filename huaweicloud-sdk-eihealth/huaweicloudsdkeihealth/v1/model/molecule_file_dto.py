# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MoleculeFileDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'MoleculeFile',
        'count': 'int'
    }

    attribute_map = {
        'file': 'file',
        'count': 'count'
    }

    def __init__(self, file=None, count=None):
        """MoleculeFileDto

        The model defined in huaweicloud sdk

        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.MoleculeFile`
        :param count: 分子个数
        :type count: int
        """
        
        

        self._file = None
        self._count = None
        self.discriminator = None

        self.file = file
        self.count = count

    @property
    def file(self):
        """Gets the file of this MoleculeFileDto.

        :return: The file of this MoleculeFileDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.MoleculeFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this MoleculeFileDto.

        :param file: The file of this MoleculeFileDto.
        :type file: :class:`huaweicloudsdkeihealth.v1.MoleculeFile`
        """
        self._file = file

    @property
    def count(self):
        """Gets the count of this MoleculeFileDto.

        分子个数

        :return: The count of this MoleculeFileDto.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MoleculeFileDto.

        分子个数

        :param count: The count of this MoleculeFileDto.
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
        if not isinstance(other, MoleculeFileDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
