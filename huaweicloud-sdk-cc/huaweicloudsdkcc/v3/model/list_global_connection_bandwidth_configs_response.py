# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalConnectionBandwidthConfigsResponse(SdkResponse):

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
        'configs': 'ListGlobalConnectionBandwidthConfigs'
    }

    attribute_map = {
        'request_id': 'request_id',
        'configs': 'configs'
    }

    def __init__(self, request_id=None, configs=None):
        """ListGlobalConnectionBandwidthConfigsResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param configs: 
        :type configs: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthConfigs`
        """
        
        super(ListGlobalConnectionBandwidthConfigsResponse, self).__init__()

        self._request_id = None
        self._configs = None
        self.discriminator = None

        self.request_id = request_id
        if configs is not None:
            self.configs = configs

    @property
    def request_id(self):
        """Gets the request_id of this ListGlobalConnectionBandwidthConfigsResponse.

        资源ID标识符。

        :return: The request_id of this ListGlobalConnectionBandwidthConfigsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListGlobalConnectionBandwidthConfigsResponse.

        资源ID标识符。

        :param request_id: The request_id of this ListGlobalConnectionBandwidthConfigsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def configs(self):
        """Gets the configs of this ListGlobalConnectionBandwidthConfigsResponse.

        :return: The configs of this ListGlobalConnectionBandwidthConfigsResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthConfigs`
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this ListGlobalConnectionBandwidthConfigsResponse.

        :param configs: The configs of this ListGlobalConnectionBandwidthConfigsResponse.
        :type configs: :class:`huaweicloudsdkcc.v3.ListGlobalConnectionBandwidthConfigs`
        """
        self._configs = configs

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
        if not isinstance(other, ListGlobalConnectionBandwidthConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
