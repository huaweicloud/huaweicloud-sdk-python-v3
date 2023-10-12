# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteStackInstanceRequest:

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
        'stack_set_name': 'str',
        'body': 'DeleteStackInstanceRequestBody'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'stack_set_name': 'stack_set_name',
        'body': 'body'
    }

    def __init__(self, client_request_id=None, stack_set_name=None, body=None):
        """DeleteStackInstanceRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param stack_set_name: 资源栈集的名称。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_set_name: str
        :param body: Body of the DeleteStackInstanceRequest
        :type body: :class:`huaweicloudsdkaos.v1.DeleteStackInstanceRequestBody`
        """
        
        

        self._client_request_id = None
        self._stack_set_name = None
        self._body = None
        self.discriminator = None

        self.client_request_id = client_request_id
        self.stack_set_name = stack_set_name
        if body is not None:
            self.body = body

    @property
    def client_request_id(self):
        """Gets the client_request_id of this DeleteStackInstanceRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this DeleteStackInstanceRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this DeleteStackInstanceRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this DeleteStackInstanceRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def stack_set_name(self):
        """Gets the stack_set_name of this DeleteStackInstanceRequest.

        资源栈集的名称。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_set_name of this DeleteStackInstanceRequest.
        :rtype: str
        """
        return self._stack_set_name

    @stack_set_name.setter
    def stack_set_name(self, stack_set_name):
        """Sets the stack_set_name of this DeleteStackInstanceRequest.

        资源栈集的名称。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_set_name: The stack_set_name of this DeleteStackInstanceRequest.
        :type stack_set_name: str
        """
        self._stack_set_name = stack_set_name

    @property
    def body(self):
        """Gets the body of this DeleteStackInstanceRequest.

        :return: The body of this DeleteStackInstanceRequest.
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteStackInstanceRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteStackInstanceRequest.

        :param body: The body of this DeleteStackInstanceRequest.
        :type body: :class:`huaweicloudsdkaos.v1.DeleteStackInstanceRequestBody`
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
        if not isinstance(other, DeleteStackInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
