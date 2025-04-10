# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteStackEnhancedRequest:

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
        'stack_name': 'str',
        'body': 'DeleteStackEnhancedRequestBody'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'stack_name': 'stack_name',
        'body': 'body'
    }

    def __init__(self, client_request_id=None, stack_name=None, body=None):
        r"""DeleteStackEnhancedRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param stack_name: 资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_name: str
        :param body: Body of the DeleteStackEnhancedRequest
        :type body: :class:`huaweicloudsdkaos.v1.DeleteStackEnhancedRequestBody`
        """
        
        

        self._client_request_id = None
        self._stack_name = None
        self._body = None
        self.discriminator = None

        self.client_request_id = client_request_id
        self.stack_name = stack_name
        if body is not None:
            self.body = body

    @property
    def client_request_id(self):
        r"""Gets the client_request_id of this DeleteStackEnhancedRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this DeleteStackEnhancedRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        r"""Sets the client_request_id of this DeleteStackEnhancedRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this DeleteStackEnhancedRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def stack_name(self):
        r"""Gets the stack_name of this DeleteStackEnhancedRequest.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_name of this DeleteStackEnhancedRequest.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        r"""Sets the stack_name of this DeleteStackEnhancedRequest.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_name: The stack_name of this DeleteStackEnhancedRequest.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def body(self):
        r"""Gets the body of this DeleteStackEnhancedRequest.

        :return: The body of this DeleteStackEnhancedRequest.
        :rtype: :class:`huaweicloudsdkaos.v1.DeleteStackEnhancedRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DeleteStackEnhancedRequest.

        :param body: The body of this DeleteStackEnhancedRequest.
        :type body: :class:`huaweicloudsdkaos.v1.DeleteStackEnhancedRequestBody`
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
        if not isinstance(other, DeleteStackEnhancedRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
