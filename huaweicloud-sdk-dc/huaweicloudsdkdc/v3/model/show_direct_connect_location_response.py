# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDirectConnectLocationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'direct_connect_location': 'DirectConnectLocationEntry',
        'request_id': 'str'
    }

    attribute_map = {
        'direct_connect_location': 'direct_connect_location',
        'request_id': 'request_id'
    }

    def __init__(self, direct_connect_location=None, request_id=None):
        r"""ShowDirectConnectLocationResponse

        The model defined in huaweicloud sdk

        :param direct_connect_location: 
        :type direct_connect_location: :class:`huaweicloudsdkdc.v3.DirectConnectLocationEntry`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ShowDirectConnectLocationResponse, self).__init__()

        self._direct_connect_location = None
        self._request_id = None
        self.discriminator = None

        if direct_connect_location is not None:
            self.direct_connect_location = direct_connect_location
        if request_id is not None:
            self.request_id = request_id

    @property
    def direct_connect_location(self):
        r"""Gets the direct_connect_location of this ShowDirectConnectLocationResponse.

        :return: The direct_connect_location of this ShowDirectConnectLocationResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.DirectConnectLocationEntry`
        """
        return self._direct_connect_location

    @direct_connect_location.setter
    def direct_connect_location(self, direct_connect_location):
        r"""Sets the direct_connect_location of this ShowDirectConnectLocationResponse.

        :param direct_connect_location: The direct_connect_location of this ShowDirectConnectLocationResponse.
        :type direct_connect_location: :class:`huaweicloudsdkdc.v3.DirectConnectLocationEntry`
        """
        self._direct_connect_location = direct_connect_location

    @property
    def request_id(self):
        r"""Gets the request_id of this ShowDirectConnectLocationResponse.

        请求ID。

        :return: The request_id of this ShowDirectConnectLocationResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ShowDirectConnectLocationResponse.

        请求ID。

        :param request_id: The request_id of this ShowDirectConnectLocationResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ShowDirectConnectLocationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
