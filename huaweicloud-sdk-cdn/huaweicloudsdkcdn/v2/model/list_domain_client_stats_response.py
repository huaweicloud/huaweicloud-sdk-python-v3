# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainClientStatsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_area': 'str',
        'result': 'list[dict(str, object)]'
    }

    attribute_map = {
        'service_area': 'service_area',
        'result': 'result'
    }

    def __init__(self, service_area=None, result=None):
        r"""ListDomainClientStatsResponse

        The model defined in huaweicloud sdk

        :param service_area: 区域
        :type service_area: str
        :param result: 按域名维每天客户端访问详情统计
        :type result: list[dict(str, object)]
        """
        
        super(ListDomainClientStatsResponse, self).__init__()

        self._service_area = None
        self._result = None
        self.discriminator = None

        if service_area is not None:
            self.service_area = service_area
        if result is not None:
            self.result = result

    @property
    def service_area(self):
        r"""Gets the service_area of this ListDomainClientStatsResponse.

        区域

        :return: The service_area of this ListDomainClientStatsResponse.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        r"""Sets the service_area of this ListDomainClientStatsResponse.

        区域

        :param service_area: The service_area of this ListDomainClientStatsResponse.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def result(self):
        r"""Gets the result of this ListDomainClientStatsResponse.

        按域名维每天客户端访问详情统计

        :return: The result of this ListDomainClientStatsResponse.
        :rtype: list[dict(str, object)]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListDomainClientStatsResponse.

        按域名维每天客户端访问详情统计

        :param result: The result of this ListDomainClientStatsResponse.
        :type result: list[dict(str, object)]
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
        if not isinstance(other, ListDomainClientStatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
