# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TypeProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'killchain': 'str',
        'ttps': 'str',
        'effects': 'str'
    }

    attribute_map = {
        'killchain': 'killchain',
        'ttps': 'ttps',
        'effects': 'effects'
    }

    def __init__(self, killchain=None, ttps=None, effects=None):
        """TypeProperties

        The model defined in huaweicloud sdk

        :param killchain: Kill chain事件分类，仅当business为attack有效
        :type killchain: str
        :param ttps: Mitre Array 事件分类，仅当business为attack有效
        :type ttps: str
        :param effects: 影响，适用全部类型
        :type effects: str
        """
        
        

        self._killchain = None
        self._ttps = None
        self._effects = None
        self.discriminator = None

        if killchain is not None:
            self.killchain = killchain
        if ttps is not None:
            self.ttps = ttps
        if effects is not None:
            self.effects = effects

    @property
    def killchain(self):
        """Gets the killchain of this TypeProperties.

        Kill chain事件分类，仅当business为attack有效

        :return: The killchain of this TypeProperties.
        :rtype: str
        """
        return self._killchain

    @killchain.setter
    def killchain(self, killchain):
        """Sets the killchain of this TypeProperties.

        Kill chain事件分类，仅当business为attack有效

        :param killchain: The killchain of this TypeProperties.
        :type killchain: str
        """
        self._killchain = killchain

    @property
    def ttps(self):
        """Gets the ttps of this TypeProperties.

        Mitre Array 事件分类，仅当business为attack有效

        :return: The ttps of this TypeProperties.
        :rtype: str
        """
        return self._ttps

    @ttps.setter
    def ttps(self, ttps):
        """Sets the ttps of this TypeProperties.

        Mitre Array 事件分类，仅当business为attack有效

        :param ttps: The ttps of this TypeProperties.
        :type ttps: str
        """
        self._ttps = ttps

    @property
    def effects(self):
        """Gets the effects of this TypeProperties.

        影响，适用全部类型

        :return: The effects of this TypeProperties.
        :rtype: str
        """
        return self._effects

    @effects.setter
    def effects(self, effects):
        """Sets the effects of this TypeProperties.

        影响，适用全部类型

        :param effects: The effects of this TypeProperties.
        :type effects: str
        """
        self._effects = effects

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
        if not isinstance(other, TypeProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
