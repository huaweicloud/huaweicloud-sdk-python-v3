# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MappingJoinFieldVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field1_id': 'int',
        'field2_id': 'int',
        'field1_name': 'str',
        'field2_name': 'str'
    }

    attribute_map = {
        'field1_id': 'field1_id',
        'field2_id': 'field2_id',
        'field1_name': 'field1_name',
        'field2_name': 'field2_name'
    }

    def __init__(self, field1_id=None, field2_id=None, field1_name=None, field2_name=None):
        """MappingJoinFieldVO

        The model defined in huaweicloud sdk

        :param field1_id: 属性id
        :type field1_id: int
        :param field2_id: 属性id
        :type field2_id: int
        :param field1_name: 名称
        :type field1_name: str
        :param field2_name: 名称
        :type field2_name: str
        """
        
        

        self._field1_id = None
        self._field2_id = None
        self._field1_name = None
        self._field2_name = None
        self.discriminator = None

        self.field1_id = field1_id
        self.field2_id = field2_id
        self.field1_name = field1_name
        self.field2_name = field2_name

    @property
    def field1_id(self):
        """Gets the field1_id of this MappingJoinFieldVO.

        属性id

        :return: The field1_id of this MappingJoinFieldVO.
        :rtype: int
        """
        return self._field1_id

    @field1_id.setter
    def field1_id(self, field1_id):
        """Sets the field1_id of this MappingJoinFieldVO.

        属性id

        :param field1_id: The field1_id of this MappingJoinFieldVO.
        :type field1_id: int
        """
        self._field1_id = field1_id

    @property
    def field2_id(self):
        """Gets the field2_id of this MappingJoinFieldVO.

        属性id

        :return: The field2_id of this MappingJoinFieldVO.
        :rtype: int
        """
        return self._field2_id

    @field2_id.setter
    def field2_id(self, field2_id):
        """Sets the field2_id of this MappingJoinFieldVO.

        属性id

        :param field2_id: The field2_id of this MappingJoinFieldVO.
        :type field2_id: int
        """
        self._field2_id = field2_id

    @property
    def field1_name(self):
        """Gets the field1_name of this MappingJoinFieldVO.

        名称

        :return: The field1_name of this MappingJoinFieldVO.
        :rtype: str
        """
        return self._field1_name

    @field1_name.setter
    def field1_name(self, field1_name):
        """Sets the field1_name of this MappingJoinFieldVO.

        名称

        :param field1_name: The field1_name of this MappingJoinFieldVO.
        :type field1_name: str
        """
        self._field1_name = field1_name

    @property
    def field2_name(self):
        """Gets the field2_name of this MappingJoinFieldVO.

        名称

        :return: The field2_name of this MappingJoinFieldVO.
        :rtype: str
        """
        return self._field2_name

    @field2_name.setter
    def field2_name(self, field2_name):
        """Sets the field2_name of this MappingJoinFieldVO.

        名称

        :param field2_name: The field2_name of this MappingJoinFieldVO.
        :type field2_name: str
        """
        self._field2_name = field2_name

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
        if not isinstance(other, MappingJoinFieldVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
