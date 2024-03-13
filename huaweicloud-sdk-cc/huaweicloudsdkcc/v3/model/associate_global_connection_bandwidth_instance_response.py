# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateGlobalConnectionBandwidthInstanceResponse(SdkResponse):

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
        'gcbandwidths': 'list[AssociateGlobalConnectionBandwidthInstanceResponseInfo]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'gcbandwidths': 'gcbandwidths'
    }

    def __init__(self, request_id=None, gcbandwidths=None):
        """AssociateGlobalConnectionBandwidthInstanceResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param gcbandwidths: 全域互联带宽绑定实例响应详情。
        :type gcbandwidths: list[:class:`huaweicloudsdkcc.v3.AssociateGlobalConnectionBandwidthInstanceResponseInfo`]
        """
        
        super(AssociateGlobalConnectionBandwidthInstanceResponse, self).__init__()

        self._request_id = None
        self._gcbandwidths = None
        self.discriminator = None

        self.request_id = request_id
        self.gcbandwidths = gcbandwidths

    @property
    def request_id(self):
        """Gets the request_id of this AssociateGlobalConnectionBandwidthInstanceResponse.

        资源ID标识符。

        :return: The request_id of this AssociateGlobalConnectionBandwidthInstanceResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AssociateGlobalConnectionBandwidthInstanceResponse.

        资源ID标识符。

        :param request_id: The request_id of this AssociateGlobalConnectionBandwidthInstanceResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def gcbandwidths(self):
        """Gets the gcbandwidths of this AssociateGlobalConnectionBandwidthInstanceResponse.

        全域互联带宽绑定实例响应详情。

        :return: The gcbandwidths of this AssociateGlobalConnectionBandwidthInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.AssociateGlobalConnectionBandwidthInstanceResponseInfo`]
        """
        return self._gcbandwidths

    @gcbandwidths.setter
    def gcbandwidths(self, gcbandwidths):
        """Sets the gcbandwidths of this AssociateGlobalConnectionBandwidthInstanceResponse.

        全域互联带宽绑定实例响应详情。

        :param gcbandwidths: The gcbandwidths of this AssociateGlobalConnectionBandwidthInstanceResponse.
        :type gcbandwidths: list[:class:`huaweicloudsdkcc.v3.AssociateGlobalConnectionBandwidthInstanceResponseInfo`]
        """
        self._gcbandwidths = gcbandwidths

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
        if not isinstance(other, AssociateGlobalConnectionBandwidthInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
