# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHostedDirectConnectResponse(SdkResponse):

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
        'hosted_connect': 'HostedDirectConnect'
    }

    attribute_map = {
        'request_id': 'request_id',
        'hosted_connect': 'hosted_connect'
    }

    def __init__(self, request_id=None, hosted_connect=None):
        """ShowHostedDirectConnectResponse

        The model defined in huaweicloud sdk

        :param request_id: 操作请求ID
        :type request_id: str
        :param hosted_connect: 
        :type hosted_connect: :class:`huaweicloudsdkdc.v3.HostedDirectConnect`
        """
        
        super(ShowHostedDirectConnectResponse, self).__init__()

        self._request_id = None
        self._hosted_connect = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if hosted_connect is not None:
            self.hosted_connect = hosted_connect

    @property
    def request_id(self):
        """Gets the request_id of this ShowHostedDirectConnectResponse.

        操作请求ID

        :return: The request_id of this ShowHostedDirectConnectResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowHostedDirectConnectResponse.

        操作请求ID

        :param request_id: The request_id of this ShowHostedDirectConnectResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def hosted_connect(self):
        """Gets the hosted_connect of this ShowHostedDirectConnectResponse.

        :return: The hosted_connect of this ShowHostedDirectConnectResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.HostedDirectConnect`
        """
        return self._hosted_connect

    @hosted_connect.setter
    def hosted_connect(self, hosted_connect):
        """Sets the hosted_connect of this ShowHostedDirectConnectResponse.

        :param hosted_connect: The hosted_connect of this ShowHostedDirectConnectResponse.
        :type hosted_connect: :class:`huaweicloudsdkdc.v3.HostedDirectConnect`
        """
        self._hosted_connect = hosted_connect

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
        if not isinstance(other, ShowHostedDirectConnectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
