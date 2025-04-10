# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNodeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider': 'str',
        'body': 'NodeRequest'
    }

    attribute_map = {
        'provider': 'provider',
        'body': 'body'
    }

    def __init__(self, provider=None, body=None):
        r"""CreateNodeRequest

        The model defined in huaweicloud sdk

        :param provider: 服务提供者：ief或hilens，选择设备纳管到不同的平台。不填默认为hilens平台
        :type provider: str
        :param body: Body of the CreateNodeRequest
        :type body: :class:`huaweicloudsdkhilens.v3.NodeRequest`
        """
        
        

        self._provider = None
        self._body = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider
        if body is not None:
            self.body = body

    @property
    def provider(self):
        r"""Gets the provider of this CreateNodeRequest.

        服务提供者：ief或hilens，选择设备纳管到不同的平台。不填默认为hilens平台

        :return: The provider of this CreateNodeRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this CreateNodeRequest.

        服务提供者：ief或hilens，选择设备纳管到不同的平台。不填默认为hilens平台

        :param provider: The provider of this CreateNodeRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def body(self):
        r"""Gets the body of this CreateNodeRequest.

        :return: The body of this CreateNodeRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.NodeRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateNodeRequest.

        :param body: The body of this CreateNodeRequest.
        :type body: :class:`huaweicloudsdkhilens.v3.NodeRequest`
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
        if not isinstance(other, CreateNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
