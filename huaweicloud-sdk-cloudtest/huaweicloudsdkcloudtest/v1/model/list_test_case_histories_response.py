# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTestCaseHistoriesResponse(SdkResponse):

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
        'values': 'list[ExternalTestCaseHistoryVo]'
    }

    attribute_map = {
        'total': 'total',
        'values': 'values'
    }

    def __init__(self, total=None, values=None):
        r"""ListTestCaseHistoriesResponse

        The model defined in huaweicloud sdk

        :param total: 起始记录数 大于 实际总条数时， 值为0， 分页请求才有此值
        :type total: int
        :param values: 实际的数据类型：单个对象，集合 或 NULL
        :type values: list[:class:`huaweicloudsdkcloudtest.v1.ExternalTestCaseHistoryVo`]
        """
        
        super(ListTestCaseHistoriesResponse, self).__init__()

        self._total = None
        self._values = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if values is not None:
            self.values = values

    @property
    def total(self):
        r"""Gets the total of this ListTestCaseHistoriesResponse.

        起始记录数 大于 实际总条数时， 值为0， 分页请求才有此值

        :return: The total of this ListTestCaseHistoriesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTestCaseHistoriesResponse.

        起始记录数 大于 实际总条数时， 值为0， 分页请求才有此值

        :param total: The total of this ListTestCaseHistoriesResponse.
        :type total: int
        """
        self._total = total

    @property
    def values(self):
        r"""Gets the values of this ListTestCaseHistoriesResponse.

        实际的数据类型：单个对象，集合 或 NULL

        :return: The values of this ListTestCaseHistoriesResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ExternalTestCaseHistoryVo`]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ListTestCaseHistoriesResponse.

        实际的数据类型：单个对象，集合 或 NULL

        :param values: The values of this ListTestCaseHistoriesResponse.
        :type values: list[:class:`huaweicloudsdkcloudtest.v1.ExternalTestCaseHistoryVo`]
        """
        self._values = values

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
        if not isinstance(other, ListTestCaseHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
