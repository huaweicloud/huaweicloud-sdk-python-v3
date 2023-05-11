# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHostedDirectConnectRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hosted_connect_id': 'str',
        'body': 'UpdateHostedDirectConnectRequestBody'
    }

    attribute_map = {
        'hosted_connect_id': 'hosted_connect_id',
        'body': 'body'
    }

    def __init__(self, hosted_connect_id=None, body=None):
        """UpdateHostedDirectConnectRequest

        The model defined in huaweicloud sdk

        :param hosted_connect_id: 托管专线连接ID。
        :type hosted_connect_id: str
        :param body: Body of the UpdateHostedDirectConnectRequest
        :type body: :class:`huaweicloudsdkdc.v3.UpdateHostedDirectConnectRequestBody`
        """
        
        

        self._hosted_connect_id = None
        self._body = None
        self.discriminator = None

        self.hosted_connect_id = hosted_connect_id
        if body is not None:
            self.body = body

    @property
    def hosted_connect_id(self):
        """Gets the hosted_connect_id of this UpdateHostedDirectConnectRequest.

        托管专线连接ID。

        :return: The hosted_connect_id of this UpdateHostedDirectConnectRequest.
        :rtype: str
        """
        return self._hosted_connect_id

    @hosted_connect_id.setter
    def hosted_connect_id(self, hosted_connect_id):
        """Sets the hosted_connect_id of this UpdateHostedDirectConnectRequest.

        托管专线连接ID。

        :param hosted_connect_id: The hosted_connect_id of this UpdateHostedDirectConnectRequest.
        :type hosted_connect_id: str
        """
        self._hosted_connect_id = hosted_connect_id

    @property
    def body(self):
        """Gets the body of this UpdateHostedDirectConnectRequest.

        :return: The body of this UpdateHostedDirectConnectRequest.
        :rtype: :class:`huaweicloudsdkdc.v3.UpdateHostedDirectConnectRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateHostedDirectConnectRequest.

        :param body: The body of this UpdateHostedDirectConnectRequest.
        :type body: :class:`huaweicloudsdkdc.v3.UpdateHostedDirectConnectRequestBody`
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
        if not isinstance(other, UpdateHostedDirectConnectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
