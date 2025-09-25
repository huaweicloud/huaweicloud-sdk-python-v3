# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KernelTimeDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parse_time': 'int',
        'rewrite_time': 'int',
        'plan_time': 'int',
        'execution_time': 'int',
        'other_time': 'int'
    }

    attribute_map = {
        'parse_time': 'parse_time',
        'rewrite_time': 'rewrite_time',
        'plan_time': 'plan_time',
        'execution_time': 'execution_time',
        'other_time': 'other_time'
    }

    def __init__(self, parse_time=None, rewrite_time=None, plan_time=None, execution_time=None, other_time=None):
        r"""KernelTimeDetails

        The model defined in huaweicloud sdk

        :param parse_time: **参数解释**: SQL解析时间（单位：微秒）。 **取值范围**: 不涉及。
        :type parse_time: int
        :param rewrite_time: **参数解释**: SQL重写时间（单位：微秒）。 **取值范围**: 不涉及。
        :type rewrite_time: int
        :param plan_time: **参数解释**: SQL生成计划时间（单位：微秒）。 **取值范围**: 不涉及。
        :type plan_time: int
        :param execution_time: **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。
        :type execution_time: int
        :param other_time: **参数解释**: 其余耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type other_time: int
        """
        
        

        self._parse_time = None
        self._rewrite_time = None
        self._plan_time = None
        self._execution_time = None
        self._other_time = None
        self.discriminator = None

        self.parse_time = parse_time
        self.rewrite_time = rewrite_time
        self.plan_time = plan_time
        self.execution_time = execution_time
        self.other_time = other_time

    @property
    def parse_time(self):
        r"""Gets the parse_time of this KernelTimeDetails.

        **参数解释**: SQL解析时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The parse_time of this KernelTimeDetails.
        :rtype: int
        """
        return self._parse_time

    @parse_time.setter
    def parse_time(self, parse_time):
        r"""Sets the parse_time of this KernelTimeDetails.

        **参数解释**: SQL解析时间（单位：微秒）。 **取值范围**: 不涉及。

        :param parse_time: The parse_time of this KernelTimeDetails.
        :type parse_time: int
        """
        self._parse_time = parse_time

    @property
    def rewrite_time(self):
        r"""Gets the rewrite_time of this KernelTimeDetails.

        **参数解释**: SQL重写时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The rewrite_time of this KernelTimeDetails.
        :rtype: int
        """
        return self._rewrite_time

    @rewrite_time.setter
    def rewrite_time(self, rewrite_time):
        r"""Sets the rewrite_time of this KernelTimeDetails.

        **参数解释**: SQL重写时间（单位：微秒）。 **取值范围**: 不涉及。

        :param rewrite_time: The rewrite_time of this KernelTimeDetails.
        :type rewrite_time: int
        """
        self._rewrite_time = rewrite_time

    @property
    def plan_time(self):
        r"""Gets the plan_time of this KernelTimeDetails.

        **参数解释**: SQL生成计划时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The plan_time of this KernelTimeDetails.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        r"""Sets the plan_time of this KernelTimeDetails.

        **参数解释**: SQL生成计划时间（单位：微秒）。 **取值范围**: 不涉及。

        :param plan_time: The plan_time of this KernelTimeDetails.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def execution_time(self):
        r"""Gets the execution_time of this KernelTimeDetails.

        **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The execution_time of this KernelTimeDetails.
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        r"""Sets the execution_time of this KernelTimeDetails.

        **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :param execution_time: The execution_time of this KernelTimeDetails.
        :type execution_time: int
        """
        self._execution_time = execution_time

    @property
    def other_time(self):
        r"""Gets the other_time of this KernelTimeDetails.

        **参数解释**: 其余耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The other_time of this KernelTimeDetails.
        :rtype: int
        """
        return self._other_time

    @other_time.setter
    def other_time(self, other_time):
        r"""Sets the other_time of this KernelTimeDetails.

        **参数解释**: 其余耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param other_time: The other_time of this KernelTimeDetails.
        :type other_time: int
        """
        self._other_time = other_time

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
        if not isinstance(other, KernelTimeDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
