# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainTrafficSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traffic_list': 'list[TrafficSummaryData]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'traffic_list': 'traffic_list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, traffic_list=None, x_request_id=None):
        r"""ListDomainTrafficSummaryResponse

        The model defined in huaweicloud sdk

        :param traffic_list: 域名对应的流量汇总列表。
        :type traffic_list: list[:class:`huaweicloudsdklive.v2.TrafficSummaryData`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListDomainTrafficSummaryResponse, self).__init__()

        self._traffic_list = None
        self._x_request_id = None
        self.discriminator = None

        if traffic_list is not None:
            self.traffic_list = traffic_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def traffic_list(self):
        r"""Gets the traffic_list of this ListDomainTrafficSummaryResponse.

        域名对应的流量汇总列表。

        :return: The traffic_list of this ListDomainTrafficSummaryResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.TrafficSummaryData`]
        """
        return self._traffic_list

    @traffic_list.setter
    def traffic_list(self, traffic_list):
        r"""Sets the traffic_list of this ListDomainTrafficSummaryResponse.

        域名对应的流量汇总列表。

        :param traffic_list: The traffic_list of this ListDomainTrafficSummaryResponse.
        :type traffic_list: list[:class:`huaweicloudsdklive.v2.TrafficSummaryData`]
        """
        self._traffic_list = traffic_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListDomainTrafficSummaryResponse.

        :return: The x_request_id of this ListDomainTrafficSummaryResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListDomainTrafficSummaryResponse.

        :param x_request_id: The x_request_id of this ListDomainTrafficSummaryResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListDomainTrafficSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
