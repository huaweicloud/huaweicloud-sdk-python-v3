# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmLevelStatisticsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'level_name': 'str'
    }

    attribute_map = {
        'count': 'count',
        'level_name': 'level_name'
    }

    def __init__(self, count=None, level_name=None):
        r"""AlarmLevelStatisticsResult

        The model defined in huaweicloud sdk

        :param count: **参数解释**: 告警数量。 **取值范围**: 不涉及。
        :type count: int
        :param level_name: **参数解释**: 告警级别名称。 **取值范围**: - critical - major - minor - notice
        :type level_name: str
        """
        
        

        self._count = None
        self._level_name = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if level_name is not None:
            self.level_name = level_name

    @property
    def count(self):
        r"""Gets the count of this AlarmLevelStatisticsResult.

        **参数解释**: 告警数量。 **取值范围**: 不涉及。

        :return: The count of this AlarmLevelStatisticsResult.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this AlarmLevelStatisticsResult.

        **参数解释**: 告警数量。 **取值范围**: 不涉及。

        :param count: The count of this AlarmLevelStatisticsResult.
        :type count: int
        """
        self._count = count

    @property
    def level_name(self):
        r"""Gets the level_name of this AlarmLevelStatisticsResult.

        **参数解释**: 告警级别名称。 **取值范围**: - critical - major - minor - notice

        :return: The level_name of this AlarmLevelStatisticsResult.
        :rtype: str
        """
        return self._level_name

    @level_name.setter
    def level_name(self, level_name):
        r"""Sets the level_name of this AlarmLevelStatisticsResult.

        **参数解释**: 告警级别名称。 **取值范围**: - critical - major - minor - notice

        :param level_name: The level_name of this AlarmLevelStatisticsResult.
        :type level_name: str
        """
        self._level_name = level_name

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
        if not isinstance(other, AlarmLevelStatisticsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
