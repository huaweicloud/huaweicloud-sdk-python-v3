# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddResourceToIteratorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iterator_uri': 'str',
        'is_async': 'bool',
        'body': 'AddResourceInfo'
    }

    attribute_map = {
        'iterator_uri': 'iterator_uri',
        'is_async': 'is_async',
        'body': 'body'
    }

    def __init__(self, iterator_uri=None, is_async=None, body=None):
        r"""AddResourceToIteratorRequest

        The model defined in huaweicloud sdk

        :param iterator_uri: 迭代uri
        :type iterator_uri: str
        :param is_async: 是否异步返回, 默认false， 超过500时，前端传true
        :type is_async: bool
        :param body: Body of the AddResourceToIteratorRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.AddResourceInfo`
        """
        
        

        self._iterator_uri = None
        self._is_async = None
        self._body = None
        self.discriminator = None

        self.iterator_uri = iterator_uri
        if is_async is not None:
            self.is_async = is_async
        if body is not None:
            self.body = body

    @property
    def iterator_uri(self):
        r"""Gets the iterator_uri of this AddResourceToIteratorRequest.

        迭代uri

        :return: The iterator_uri of this AddResourceToIteratorRequest.
        :rtype: str
        """
        return self._iterator_uri

    @iterator_uri.setter
    def iterator_uri(self, iterator_uri):
        r"""Sets the iterator_uri of this AddResourceToIteratorRequest.

        迭代uri

        :param iterator_uri: The iterator_uri of this AddResourceToIteratorRequest.
        :type iterator_uri: str
        """
        self._iterator_uri = iterator_uri

    @property
    def is_async(self):
        r"""Gets the is_async of this AddResourceToIteratorRequest.

        是否异步返回, 默认false， 超过500时，前端传true

        :return: The is_async of this AddResourceToIteratorRequest.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        r"""Sets the is_async of this AddResourceToIteratorRequest.

        是否异步返回, 默认false， 超过500时，前端传true

        :param is_async: The is_async of this AddResourceToIteratorRequest.
        :type is_async: bool
        """
        self._is_async = is_async

    @property
    def body(self):
        r"""Gets the body of this AddResourceToIteratorRequest.

        :return: The body of this AddResourceToIteratorRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AddResourceInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AddResourceToIteratorRequest.

        :param body: The body of this AddResourceToIteratorRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.AddResourceInfo`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddResourceToIteratorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
