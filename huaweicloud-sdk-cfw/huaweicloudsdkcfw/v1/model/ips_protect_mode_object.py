# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpsProtectModeObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'mode': 'int'
    }

    attribute_map = {
        'id': 'id',
        'mode': 'mode'
    }

    def __init__(self, id=None, mode=None):
        """IpsProtectModeObject

        The model defined in huaweicloud sdk

        :param id: ips防护模式id
        :type id: str
        :param mode: ips防护模式，0：观察模式，1：严格模式，2：中等模式，3：宽松模式
        :type mode: int
        """
        
        

        self._id = None
        self._mode = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if mode is not None:
            self.mode = mode

    @property
    def id(self):
        """Gets the id of this IpsProtectModeObject.

        ips防护模式id

        :return: The id of this IpsProtectModeObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpsProtectModeObject.

        ips防护模式id

        :param id: The id of this IpsProtectModeObject.
        :type id: str
        """
        self._id = id

    @property
    def mode(self):
        """Gets the mode of this IpsProtectModeObject.

        ips防护模式，0：观察模式，1：严格模式，2：中等模式，3：宽松模式

        :return: The mode of this IpsProtectModeObject.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this IpsProtectModeObject.

        ips防护模式，0：观察模式，1：严格模式，2：中等模式，3：宽松模式

        :param mode: The mode of this IpsProtectModeObject.
        :type mode: int
        """
        self._mode = mode

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
        if not isinstance(other, IpsProtectModeObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
