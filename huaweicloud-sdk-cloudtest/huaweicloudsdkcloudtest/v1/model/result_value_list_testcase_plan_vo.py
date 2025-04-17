# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResultValueListTestcasePlanVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'value': 'list[TestcasePlanVo]',
        'reason': 'str'
    }

    attribute_map = {
        'total': 'total',
        'value': 'value',
        'reason': 'reason'
    }

    def __init__(self, total=None, value=None, reason=None):
        r"""ResultValueListTestcasePlanVo

        The model defined in huaweicloud sdk

        :param total: 起始记录数 大于 实际总条数时， 值为0， 分页请求才有此值
        :type total: int
        :param value: 实际的数据类型：单个对象，集合 或 NULL
        :type value: list[:class:`huaweicloudsdkcloudtest.v1.TestcasePlanVo`]
        :param reason: 业务失败的提示内容，对内接口才有此值
        :type reason: str
        """
        
        

        self._total = None
        self._value = None
        self._reason = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if value is not None:
            self.value = value
        if reason is not None:
            self.reason = reason

    @property
    def total(self):
        r"""Gets the total of this ResultValueListTestcasePlanVo.

        起始记录数 大于 实际总条数时， 值为0， 分页请求才有此值

        :return: The total of this ResultValueListTestcasePlanVo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ResultValueListTestcasePlanVo.

        起始记录数 大于 实际总条数时， 值为0， 分页请求才有此值

        :param total: The total of this ResultValueListTestcasePlanVo.
        :type total: int
        """
        self._total = total

    @property
    def value(self):
        r"""Gets the value of this ResultValueListTestcasePlanVo.

        实际的数据类型：单个对象，集合 或 NULL

        :return: The value of this ResultValueListTestcasePlanVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestcasePlanVo`]
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ResultValueListTestcasePlanVo.

        实际的数据类型：单个对象，集合 或 NULL

        :param value: The value of this ResultValueListTestcasePlanVo.
        :type value: list[:class:`huaweicloudsdkcloudtest.v1.TestcasePlanVo`]
        """
        self._value = value

    @property
    def reason(self):
        r"""Gets the reason of this ResultValueListTestcasePlanVo.

        业务失败的提示内容，对内接口才有此值

        :return: The reason of this ResultValueListTestcasePlanVo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ResultValueListTestcasePlanVo.

        业务失败的提示内容，对内接口才有此值

        :param reason: The reason of this ResultValueListTestcasePlanVo.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, ResultValueListTestcasePlanVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
