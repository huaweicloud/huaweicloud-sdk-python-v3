# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompatibleInstanceVolumeResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'used': 'float',
        'size': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'size': 'size'
    }

    def __init__(self, type=None, used=None, size=None):
        r"""CompatibleInstanceVolumeResp

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 类型。 **取值范围**： 不涉及。
        :type type: str
        :param used: **参数解释**： 已使用空间。 **取值范围**： 不涉及。
        :type used: float
        :param size: **参数解释**： 总大小。 **取值范围**： 不涉及。
        :type size: int
        """
        
        

        self._type = None
        self._used = None
        self._size = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if used is not None:
            self.used = used
        if size is not None:
            self.size = size

    @property
    def type(self):
        r"""Gets the type of this CompatibleInstanceVolumeResp.

        **参数解释**： 类型。 **取值范围**： 不涉及。

        :return: The type of this CompatibleInstanceVolumeResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CompatibleInstanceVolumeResp.

        **参数解释**： 类型。 **取值范围**： 不涉及。

        :param type: The type of this CompatibleInstanceVolumeResp.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        r"""Gets the used of this CompatibleInstanceVolumeResp.

        **参数解释**： 已使用空间。 **取值范围**： 不涉及。

        :return: The used of this CompatibleInstanceVolumeResp.
        :rtype: float
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this CompatibleInstanceVolumeResp.

        **参数解释**： 已使用空间。 **取值范围**： 不涉及。

        :param used: The used of this CompatibleInstanceVolumeResp.
        :type used: float
        """
        self._used = used

    @property
    def size(self):
        r"""Gets the size of this CompatibleInstanceVolumeResp.

        **参数解释**： 总大小。 **取值范围**： 不涉及。

        :return: The size of this CompatibleInstanceVolumeResp.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this CompatibleInstanceVolumeResp.

        **参数解释**： 总大小。 **取值范围**： 不涉及。

        :param size: The size of this CompatibleInstanceVolumeResp.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, CompatibleInstanceVolumeResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
