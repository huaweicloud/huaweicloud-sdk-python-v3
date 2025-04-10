# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCentralNetworkRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'central_network_id': 'str',
        'body': 'UpdateCentralNetworkRequestBody'
    }

    attribute_map = {
        'central_network_id': 'central_network_id',
        'body': 'body'
    }

    def __init__(self, central_network_id=None, body=None):
        r"""UpdateCentralNetworkRequest

        The model defined in huaweicloud sdk

        :param central_network_id: 中心网络的ID。
        :type central_network_id: str
        :param body: Body of the UpdateCentralNetworkRequest
        :type body: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkRequestBody`
        """
        
        

        self._central_network_id = None
        self._body = None
        self.discriminator = None

        self.central_network_id = central_network_id
        if body is not None:
            self.body = body

    @property
    def central_network_id(self):
        r"""Gets the central_network_id of this UpdateCentralNetworkRequest.

        中心网络的ID。

        :return: The central_network_id of this UpdateCentralNetworkRequest.
        :rtype: str
        """
        return self._central_network_id

    @central_network_id.setter
    def central_network_id(self, central_network_id):
        r"""Sets the central_network_id of this UpdateCentralNetworkRequest.

        中心网络的ID。

        :param central_network_id: The central_network_id of this UpdateCentralNetworkRequest.
        :type central_network_id: str
        """
        self._central_network_id = central_network_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCentralNetworkRequest.

        :return: The body of this UpdateCentralNetworkRequest.
        :rtype: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCentralNetworkRequest.

        :param body: The body of this UpdateCentralNetworkRequest.
        :type body: :class:`huaweicloudsdkcc.v3.UpdateCentralNetworkRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateCentralNetworkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
