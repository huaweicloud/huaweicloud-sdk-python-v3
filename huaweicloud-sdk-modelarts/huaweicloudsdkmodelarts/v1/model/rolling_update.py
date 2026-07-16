# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RollingUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_surge': 'str',
        'max_unavailable': 'str'
    }

    attribute_map = {
        'max_surge': 'max_surge',
        'max_unavailable': 'max_unavailable'
    }

    def __init__(self, max_surge=None, max_unavailable=None):
        r"""RollingUpdate

        The model defined in huaweicloud sdk

        :param max_surge: **参数解释：** 滚动更新时最多可以启动多少个Pod。 **约束限制：** 百分数类型字符串。 **取值范围：** 1%-100%。 **默认取值：** 1%。
        :type max_surge: str
        :param max_unavailable: **参数解释：** 滚动更新时最多可以删除多少个Pod。 **约束限制：** 百分数类型字符串。 **取值范围：** 1%-100%。 **默认取值：** 1%。
        :type max_unavailable: str
        """
        
        

        self._max_surge = None
        self._max_unavailable = None
        self.discriminator = None

        if max_surge is not None:
            self.max_surge = max_surge
        if max_unavailable is not None:
            self.max_unavailable = max_unavailable

    @property
    def max_surge(self):
        r"""Gets the max_surge of this RollingUpdate.

        **参数解释：** 滚动更新时最多可以启动多少个Pod。 **约束限制：** 百分数类型字符串。 **取值范围：** 1%-100%。 **默认取值：** 1%。

        :return: The max_surge of this RollingUpdate.
        :rtype: str
        """
        return self._max_surge

    @max_surge.setter
    def max_surge(self, max_surge):
        r"""Sets the max_surge of this RollingUpdate.

        **参数解释：** 滚动更新时最多可以启动多少个Pod。 **约束限制：** 百分数类型字符串。 **取值范围：** 1%-100%。 **默认取值：** 1%。

        :param max_surge: The max_surge of this RollingUpdate.
        :type max_surge: str
        """
        self._max_surge = max_surge

    @property
    def max_unavailable(self):
        r"""Gets the max_unavailable of this RollingUpdate.

        **参数解释：** 滚动更新时最多可以删除多少个Pod。 **约束限制：** 百分数类型字符串。 **取值范围：** 1%-100%。 **默认取值：** 1%。

        :return: The max_unavailable of this RollingUpdate.
        :rtype: str
        """
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, max_unavailable):
        r"""Sets the max_unavailable of this RollingUpdate.

        **参数解释：** 滚动更新时最多可以删除多少个Pod。 **约束限制：** 百分数类型字符串。 **取值范围：** 1%-100%。 **默认取值：** 1%。

        :param max_unavailable: The max_unavailable of this RollingUpdate.
        :type max_unavailable: str
        """
        self._max_unavailable = max_unavailable

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
        if not isinstance(other, RollingUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
