# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DimensionListResult:

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
        'active_num': 'str',
        'total_num': 'str'
    }

    attribute_map = {
        'name': 'name',
        'active_num': 'active_num',
        'total_num': 'total_num'
    }

    def __init__(self, name=None, active_num=None, total_num=None):
        r"""DimensionListResult

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 统计数据名称。 **取值范围**: 不涉及。
        :type name: str
        :param active_num: **参数解释**: 活跃会话数。 **取值范围**: 不涉及。
        :type active_num: str
        :param total_num: **参数解释**: 总会话数。 **取值范围**: 不涉及。
        :type total_num: str
        """
        
        

        self._name = None
        self._active_num = None
        self._total_num = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if active_num is not None:
            self.active_num = active_num
        if total_num is not None:
            self.total_num = total_num

    @property
    def name(self):
        r"""Gets the name of this DimensionListResult.

        **参数解释**: 统计数据名称。 **取值范围**: 不涉及。

        :return: The name of this DimensionListResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DimensionListResult.

        **参数解释**: 统计数据名称。 **取值范围**: 不涉及。

        :param name: The name of this DimensionListResult.
        :type name: str
        """
        self._name = name

    @property
    def active_num(self):
        r"""Gets the active_num of this DimensionListResult.

        **参数解释**: 活跃会话数。 **取值范围**: 不涉及。

        :return: The active_num of this DimensionListResult.
        :rtype: str
        """
        return self._active_num

    @active_num.setter
    def active_num(self, active_num):
        r"""Sets the active_num of this DimensionListResult.

        **参数解释**: 活跃会话数。 **取值范围**: 不涉及。

        :param active_num: The active_num of this DimensionListResult.
        :type active_num: str
        """
        self._active_num = active_num

    @property
    def total_num(self):
        r"""Gets the total_num of this DimensionListResult.

        **参数解释**: 总会话数。 **取值范围**: 不涉及。

        :return: The total_num of this DimensionListResult.
        :rtype: str
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this DimensionListResult.

        **参数解释**: 总会话数。 **取值范围**: 不涉及。

        :param total_num: The total_num of this DimensionListResult.
        :type total_num: str
        """
        self._total_num = total_num

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
        if not isinstance(other, DimensionListResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
