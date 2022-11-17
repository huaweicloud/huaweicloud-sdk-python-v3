# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcHistoryUsageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'usage': 'list[RtcHistoryUsage]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'usage': 'usage',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, usage=None, x_request_id=None):
        """ListRtcHistoryUsageResponse

        The model defined in huaweicloud sdk

        :param usage: 时间戳及相应时间的指标数值列表
        :type usage: list[:class:`huaweicloudsdkcloudrtc.v1.RtcHistoryUsage`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListRtcHistoryUsageResponse, self).__init__()

        self._usage = None
        self._x_request_id = None
        self.discriminator = None

        if usage is not None:
            self.usage = usage
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def usage(self):
        """Gets the usage of this ListRtcHistoryUsageResponse.

        时间戳及相应时间的指标数值列表

        :return: The usage of this ListRtcHistoryUsageResponse.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v1.RtcHistoryUsage`]
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ListRtcHistoryUsageResponse.

        时间戳及相应时间的指标数值列表

        :param usage: The usage of this ListRtcHistoryUsageResponse.
        :type usage: list[:class:`huaweicloudsdkcloudrtc.v1.RtcHistoryUsage`]
        """
        self._usage = usage

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListRtcHistoryUsageResponse.

        :return: The x_request_id of this ListRtcHistoryUsageResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListRtcHistoryUsageResponse.

        :param x_request_id: The x_request_id of this ListRtcHistoryUsageResponse.
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
        if not isinstance(other, ListRtcHistoryUsageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
