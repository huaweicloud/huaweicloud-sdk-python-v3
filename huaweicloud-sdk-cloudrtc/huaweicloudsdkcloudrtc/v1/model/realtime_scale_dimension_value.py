# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RealtimeScaleDimensionValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimension': 'str',
        'online_users': 'int'
    }

    attribute_map = {
        'dimension': 'dimension',
        'online_users': 'online_users'
    }

    def __init__(self, dimension=None, online_users=None):
        """RealtimeScaleDimensionValue

        The model defined in huaweicloud sdk

        :param dimension: 维度值，如查询维度为region，则此处取值可能为GD 
        :type dimension: str
        :param online_users: 在线观众数
        :type online_users: int
        """
        
        

        self._dimension = None
        self._online_users = None
        self.discriminator = None

        if dimension is not None:
            self.dimension = dimension
        if online_users is not None:
            self.online_users = online_users

    @property
    def dimension(self):
        """Gets the dimension of this RealtimeScaleDimensionValue.

        维度值，如查询维度为region，则此处取值可能为GD 

        :return: The dimension of this RealtimeScaleDimensionValue.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """Sets the dimension of this RealtimeScaleDimensionValue.

        维度值，如查询维度为region，则此处取值可能为GD 

        :param dimension: The dimension of this RealtimeScaleDimensionValue.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def online_users(self):
        """Gets the online_users of this RealtimeScaleDimensionValue.

        在线观众数

        :return: The online_users of this RealtimeScaleDimensionValue.
        :rtype: int
        """
        return self._online_users

    @online_users.setter
    def online_users(self, online_users):
        """Sets the online_users of this RealtimeScaleDimensionValue.

        在线观众数

        :param online_users: The online_users of this RealtimeScaleDimensionValue.
        :type online_users: int
        """
        self._online_users = online_users

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
        if not isinstance(other, RealtimeScaleDimensionValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
