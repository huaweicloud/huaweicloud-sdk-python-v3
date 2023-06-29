# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessorDto:

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
        'id': 'str',
        'accessor_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'accessor_type': 'accessor_type'
    }

    def __init__(self, name=None, id=None, accessor_type=None):
        """AccessorDto

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param id: 
        :type id: str
        :param accessor_type: 
        :type accessor_type: str
        """
        
        

        self._name = None
        self._id = None
        self._accessor_type = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.accessor_type = accessor_type

    @property
    def name(self):
        """Gets the name of this AccessorDto.

        :return: The name of this AccessorDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessorDto.

        :param name: The name of this AccessorDto.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this AccessorDto.

        :return: The id of this AccessorDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessorDto.

        :param id: The id of this AccessorDto.
        :type id: str
        """
        self._id = id

    @property
    def accessor_type(self):
        """Gets the accessor_type of this AccessorDto.

        :return: The accessor_type of this AccessorDto.
        :rtype: str
        """
        return self._accessor_type

    @accessor_type.setter
    def accessor_type(self, accessor_type):
        """Sets the accessor_type of this AccessorDto.

        :param accessor_type: The accessor_type of this AccessorDto.
        :type accessor_type: str
        """
        self._accessor_type = accessor_type

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
        if not isinstance(other, AccessorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
