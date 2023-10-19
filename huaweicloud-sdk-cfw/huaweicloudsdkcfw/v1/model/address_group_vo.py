# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressGroupVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'set_id': 'set_id',
        'name': 'name'
    }

    def __init__(self, set_id=None, name=None):
        """AddressGroupVO

        The model defined in huaweicloud sdk

        :param set_id: 地址组id
        :type set_id: str
        :param name: 地址组名称
        :type name: str
        """
        
        

        self._set_id = None
        self._name = None
        self.discriminator = None

        if set_id is not None:
            self.set_id = set_id
        if name is not None:
            self.name = name

    @property
    def set_id(self):
        """Gets the set_id of this AddressGroupVO.

        地址组id

        :return: The set_id of this AddressGroupVO.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this AddressGroupVO.

        地址组id

        :param set_id: The set_id of this AddressGroupVO.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def name(self):
        """Gets the name of this AddressGroupVO.

        地址组名称

        :return: The name of this AddressGroupVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddressGroupVO.

        地址组名称

        :param name: The name of this AddressGroupVO.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, AddressGroupVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
