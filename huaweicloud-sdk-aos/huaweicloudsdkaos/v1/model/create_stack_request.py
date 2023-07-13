# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStackRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_request_id': 'str',
        'body': 'CreateStackRequestBody'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'body': 'body'
    }

    def __init__(self, client_request_id=None, body=None):
        """CreateStackRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param body: Body of the CreateStackRequest
        :type body: :class:`huaweicloudsdkaos.v1.CreateStackRequestBody`
        """
        
        

        self._client_request_id = None
        self._body = None
        self.discriminator = None

        self.client_request_id = client_request_id
        if body is not None:
            self.body = body

    @property
    def client_request_id(self):
        """Gets the client_request_id of this CreateStackRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this CreateStackRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this CreateStackRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this CreateStackRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def body(self):
        """Gets the body of this CreateStackRequest.

        :return: The body of this CreateStackRequest.
        :rtype: :class:`huaweicloudsdkaos.v1.CreateStackRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateStackRequest.

        :param body: The body of this CreateStackRequest.
        :type body: :class:`huaweicloudsdkaos.v1.CreateStackRequestBody`
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
        if not isinstance(other, CreateStackRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
