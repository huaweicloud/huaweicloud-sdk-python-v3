# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGlobalConnectionBandwidthResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'globalconnection_bandwidth': 'GlobalConnectionBandwidth'
    }

    attribute_map = {
        'request_id': 'request_id',
        'globalconnection_bandwidth': 'globalconnection_bandwidth'
    }

    def __init__(self, request_id=None, globalconnection_bandwidth=None):
        """ShowGlobalConnectionBandwidthResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param globalconnection_bandwidth: 
        :type globalconnection_bandwidth: :class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidth`
        """
        
        super(ShowGlobalConnectionBandwidthResponse, self).__init__()

        self._request_id = None
        self._globalconnection_bandwidth = None
        self.discriminator = None

        self.request_id = request_id
        self.globalconnection_bandwidth = globalconnection_bandwidth

    @property
    def request_id(self):
        """Gets the request_id of this ShowGlobalConnectionBandwidthResponse.

        资源ID标识符。

        :return: The request_id of this ShowGlobalConnectionBandwidthResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowGlobalConnectionBandwidthResponse.

        资源ID标识符。

        :param request_id: The request_id of this ShowGlobalConnectionBandwidthResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def globalconnection_bandwidth(self):
        """Gets the globalconnection_bandwidth of this ShowGlobalConnectionBandwidthResponse.

        :return: The globalconnection_bandwidth of this ShowGlobalConnectionBandwidthResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidth`
        """
        return self._globalconnection_bandwidth

    @globalconnection_bandwidth.setter
    def globalconnection_bandwidth(self, globalconnection_bandwidth):
        """Sets the globalconnection_bandwidth of this ShowGlobalConnectionBandwidthResponse.

        :param globalconnection_bandwidth: The globalconnection_bandwidth of this ShowGlobalConnectionBandwidthResponse.
        :type globalconnection_bandwidth: :class:`huaweicloudsdkcc.v3.GlobalConnectionBandwidth`
        """
        self._globalconnection_bandwidth = globalconnection_bandwidth

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
        if not isinstance(other, ShowGlobalConnectionBandwidthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
