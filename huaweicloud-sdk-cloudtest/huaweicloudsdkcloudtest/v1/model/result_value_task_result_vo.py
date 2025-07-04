# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResultValueTaskResultVo:

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
        'value': 'TaskResultVo',
        'reason': 'str',
        'page_size': 'int',
        'page_no': 'int',
        'has_more': 'bool'
    }

    attribute_map = {
        'total': 'total',
        'value': 'value',
        'reason': 'reason',
        'page_size': 'page_size',
        'page_no': 'page_no',
        'has_more': 'has_more'
    }

    def __init__(self, total=None, value=None, reason=None, page_size=None, page_no=None, has_more=None):
        r"""ResultValueTaskResultVo

        The model defined in huaweicloud sdk

        :param total: 起始记录数 大于 实际总条数时， 值为0， 分页请求才有此值
        :type total: int
        :param value: 
        :type value: :class:`huaweicloudsdkcloudtest.v1.TaskResultVo`
        :param reason: 业务失败的提示内容
        :type reason: str
        :param page_size: 每页展示条数
        :type page_size: int
        :param page_no: 页码
        :type page_no: int
        :param has_more: 是否有更多
        :type has_more: bool
        """
        
        

        self._total = None
        self._value = None
        self._reason = None
        self._page_size = None
        self._page_no = None
        self._has_more = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if value is not None:
            self.value = value
        if reason is not None:
            self.reason = reason
        if page_size is not None:
            self.page_size = page_size
        if page_no is not None:
            self.page_no = page_no
        if has_more is not None:
            self.has_more = has_more

    @property
    def total(self):
        r"""Gets the total of this ResultValueTaskResultVo.

        起始记录数 大于 实际总条数时， 值为0， 分页请求才有此值

        :return: The total of this ResultValueTaskResultVo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ResultValueTaskResultVo.

        起始记录数 大于 实际总条数时， 值为0， 分页请求才有此值

        :param total: The total of this ResultValueTaskResultVo.
        :type total: int
        """
        self._total = total

    @property
    def value(self):
        r"""Gets the value of this ResultValueTaskResultVo.

        :return: The value of this ResultValueTaskResultVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TaskResultVo`
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ResultValueTaskResultVo.

        :param value: The value of this ResultValueTaskResultVo.
        :type value: :class:`huaweicloudsdkcloudtest.v1.TaskResultVo`
        """
        self._value = value

    @property
    def reason(self):
        r"""Gets the reason of this ResultValueTaskResultVo.

        业务失败的提示内容

        :return: The reason of this ResultValueTaskResultVo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ResultValueTaskResultVo.

        业务失败的提示内容

        :param reason: The reason of this ResultValueTaskResultVo.
        :type reason: str
        """
        self._reason = reason

    @property
    def page_size(self):
        r"""Gets the page_size of this ResultValueTaskResultVo.

        每页展示条数

        :return: The page_size of this ResultValueTaskResultVo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ResultValueTaskResultVo.

        每页展示条数

        :param page_size: The page_size of this ResultValueTaskResultVo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_no(self):
        r"""Gets the page_no of this ResultValueTaskResultVo.

        页码

        :return: The page_no of this ResultValueTaskResultVo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ResultValueTaskResultVo.

        页码

        :param page_no: The page_no of this ResultValueTaskResultVo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def has_more(self):
        r"""Gets the has_more of this ResultValueTaskResultVo.

        是否有更多

        :return: The has_more of this ResultValueTaskResultVo.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        r"""Sets the has_more of this ResultValueTaskResultVo.

        是否有更多

        :param has_more: The has_more of this ResultValueTaskResultVo.
        :type has_more: bool
        """
        self._has_more = has_more

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
        if not isinstance(other, ResultValueTaskResultVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
