# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTestCasesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'values': 'list[ExternalTestCaseVo]',
        'total': 'int'
    }

    attribute_map = {
        'values': 'values',
        'total': 'total'
    }

    def __init__(self, values=None, total=None):
        """ListTestCasesResponse

        The model defined in huaweicloud sdk

        :param values: 用例详情列表
        :type values: list[:class:`huaweicloudsdkcloudtest.v1.ExternalTestCaseVo`]
        :param total: 用例总数
        :type total: int
        """
        
        super(ListTestCasesResponse, self).__init__()

        self._values = None
        self._total = None
        self.discriminator = None

        if values is not None:
            self.values = values
        if total is not None:
            self.total = total

    @property
    def values(self):
        """Gets the values of this ListTestCasesResponse.

        用例详情列表

        :return: The values of this ListTestCasesResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ExternalTestCaseVo`]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ListTestCasesResponse.

        用例详情列表

        :param values: The values of this ListTestCasesResponse.
        :type values: list[:class:`huaweicloudsdkcloudtest.v1.ExternalTestCaseVo`]
        """
        self._values = values

    @property
    def total(self):
        """Gets the total of this ListTestCasesResponse.

        用例总数

        :return: The total of this ListTestCasesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListTestCasesResponse.

        用例总数

        :param total: The total of this ListTestCasesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListTestCasesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
