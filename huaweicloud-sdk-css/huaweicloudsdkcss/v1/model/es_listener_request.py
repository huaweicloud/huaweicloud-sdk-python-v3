# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsListenerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default_tls_container_ref': 'str',
        'client_ca_tls_container_ref': 'str'
    }

    attribute_map = {
        'default_tls_container_ref': 'default_tls_container_ref',
        'client_ca_tls_container_ref': 'client_ca_tls_container_ref'
    }

    def __init__(self, default_tls_container_ref=None, client_ca_tls_container_ref=None):
        """EsListenerRequest

        The model defined in huaweicloud sdk

        :param default_tls_container_ref: 监听器使用的服务器证书ID。
        :type default_tls_container_ref: str
        :param client_ca_tls_container_ref: 监听器使用的CA证书ID。如果更新双向认证，则该参数为必选。
        :type client_ca_tls_container_ref: str
        """
        
        

        self._default_tls_container_ref = None
        self._client_ca_tls_container_ref = None
        self.discriminator = None

        self.default_tls_container_ref = default_tls_container_ref
        if client_ca_tls_container_ref is not None:
            self.client_ca_tls_container_ref = client_ca_tls_container_ref

    @property
    def default_tls_container_ref(self):
        """Gets the default_tls_container_ref of this EsListenerRequest.

        监听器使用的服务器证书ID。

        :return: The default_tls_container_ref of this EsListenerRequest.
        :rtype: str
        """
        return self._default_tls_container_ref

    @default_tls_container_ref.setter
    def default_tls_container_ref(self, default_tls_container_ref):
        """Sets the default_tls_container_ref of this EsListenerRequest.

        监听器使用的服务器证书ID。

        :param default_tls_container_ref: The default_tls_container_ref of this EsListenerRequest.
        :type default_tls_container_ref: str
        """
        self._default_tls_container_ref = default_tls_container_ref

    @property
    def client_ca_tls_container_ref(self):
        """Gets the client_ca_tls_container_ref of this EsListenerRequest.

        监听器使用的CA证书ID。如果更新双向认证，则该参数为必选。

        :return: The client_ca_tls_container_ref of this EsListenerRequest.
        :rtype: str
        """
        return self._client_ca_tls_container_ref

    @client_ca_tls_container_ref.setter
    def client_ca_tls_container_ref(self, client_ca_tls_container_ref):
        """Sets the client_ca_tls_container_ref of this EsListenerRequest.

        监听器使用的CA证书ID。如果更新双向认证，则该参数为必选。

        :param client_ca_tls_container_ref: The client_ca_tls_container_ref of this EsListenerRequest.
        :type client_ca_tls_container_ref: str
        """
        self._client_ca_tls_container_ref = client_ca_tls_container_ref

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
        if not isinstance(other, EsListenerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
