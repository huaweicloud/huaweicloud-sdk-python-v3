# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPubMetricsResponse(SdkResponse):

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
        'result': 'list[EventPubMetricsItem]'
    }

    attribute_map = {
        'total': 'total',
        'result': 'result'
    }

    def __init__(self, total=None, result=None):
        r"""ListPubMetricsResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param result: 指标列表
        :type result: list[:class:`huaweicloudsdkeg.v1.EventPubMetricsItem`]
        """
        
        super(ListPubMetricsResponse, self).__init__()

        self._total = None
        self._result = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if result is not None:
            self.result = result

    @property
    def total(self):
        r"""Gets the total of this ListPubMetricsResponse.

        总数

        :return: The total of this ListPubMetricsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListPubMetricsResponse.

        总数

        :param total: The total of this ListPubMetricsResponse.
        :type total: int
        """
        self._total = total

    @property
    def result(self):
        r"""Gets the result of this ListPubMetricsResponse.

        指标列表

        :return: The result of this ListPubMetricsResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.EventPubMetricsItem`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListPubMetricsResponse.

        指标列表

        :param result: The result of this ListPubMetricsResponse.
        :type result: list[:class:`huaweicloudsdkeg.v1.EventPubMetricsItem`]
        """
        self._result = result

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
        if not isinstance(other, ListPubMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
