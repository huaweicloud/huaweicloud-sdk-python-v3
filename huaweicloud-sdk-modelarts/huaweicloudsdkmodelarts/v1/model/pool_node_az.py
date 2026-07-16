# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolNodeAz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'az': 'str',
        'count': 'int'
    }

    attribute_map = {
        'az': 'az',
        'count': 'count'
    }

    def __init__(self, az=None, count=None):
        r"""PoolNodeAz

        The model defined in huaweicloud sdk

        :param az: **参数解释**：可用区名称。 **取值范围**：不涉及。
        :type az: str
        :param count: **参数解释**：可用区资源实例的数量。 **取值范围**：不涉及。
        :type count: int
        """
        
        

        self._az = None
        self._count = None
        self.discriminator = None

        self.az = az
        self.count = count

    @property
    def az(self):
        r"""Gets the az of this PoolNodeAz.

        **参数解释**：可用区名称。 **取值范围**：不涉及。

        :return: The az of this PoolNodeAz.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this PoolNodeAz.

        **参数解释**：可用区名称。 **取值范围**：不涉及。

        :param az: The az of this PoolNodeAz.
        :type az: str
        """
        self._az = az

    @property
    def count(self):
        r"""Gets the count of this PoolNodeAz.

        **参数解释**：可用区资源实例的数量。 **取值范围**：不涉及。

        :return: The count of this PoolNodeAz.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this PoolNodeAz.

        **参数解释**：可用区资源实例的数量。 **取值范围**：不涉及。

        :param count: The count of this PoolNodeAz.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PoolNodeAz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
