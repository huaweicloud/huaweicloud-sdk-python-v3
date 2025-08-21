# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ItemVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'name': 'str',
        'value': 'int'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, key=None, name=None, value=None):
        r"""ItemVO

        The model defined in huaweicloud sdk

        :param key: **参数解释**： 聚合项 **取值范围**： 不涉及
        :type key: str
        :param name: **参数解释**： 聚合项名称 **取值范围**： 不涉及
        :type name: str
        :param value: **参数解释**： 统计值 **取值范围**： 不涉及
        :type value: int
        """
        
        

        self._key = None
        self._name = None
        self._value = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def key(self):
        r"""Gets the key of this ItemVO.

        **参数解释**： 聚合项 **取值范围**： 不涉及

        :return: The key of this ItemVO.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ItemVO.

        **参数解释**： 聚合项 **取值范围**： 不涉及

        :param key: The key of this ItemVO.
        :type key: str
        """
        self._key = key

    @property
    def name(self):
        r"""Gets the name of this ItemVO.

        **参数解释**： 聚合项名称 **取值范围**： 不涉及

        :return: The name of this ItemVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ItemVO.

        **参数解释**： 聚合项名称 **取值范围**： 不涉及

        :param name: The name of this ItemVO.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this ItemVO.

        **参数解释**： 统计值 **取值范围**： 不涉及

        :return: The value of this ItemVO.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ItemVO.

        **参数解释**： 统计值 **取值范围**： 不涉及

        :param value: The value of this ItemVO.
        :type value: int
        """
        self._value = value

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
        if not isinstance(other, ItemVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
