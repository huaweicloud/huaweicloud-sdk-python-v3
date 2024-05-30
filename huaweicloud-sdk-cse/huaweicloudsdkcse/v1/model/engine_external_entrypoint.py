# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineExternalEntrypoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'external_address': 'str',
        'public_address': 'str',
        'service_endpoint': 'dict(str, EntrypointItem)',
        'public_service_endpoint': 'dict(str, EntrypointItem)'
    }

    attribute_map = {
        'external_address': 'externalAddress',
        'public_address': 'publicAddress',
        'service_endpoint': 'serviceEndpoint',
        'public_service_endpoint': 'publicServiceEndpoint'
    }

    def __init__(self, external_address=None, public_address=None, service_endpoint=None, public_service_endpoint=None):
        """EngineExternalEntrypoint

        The model defined in huaweicloud sdk

        :param external_address: 微服务引擎暴露的IP地址。
        :type external_address: str
        :param public_address: 微服务引擎的公网地址。
        :type public_address: str
        :param service_endpoint: 微服务引擎组件的访问地址。
        :type service_endpoint: dict(str, EntrypointItem)
        :param public_service_endpoint: 微服务引擎组件的公网地址。
        :type public_service_endpoint: dict(str, EntrypointItem)
        """
        
        

        self._external_address = None
        self._public_address = None
        self._service_endpoint = None
        self._public_service_endpoint = None
        self.discriminator = None

        if external_address is not None:
            self.external_address = external_address
        if public_address is not None:
            self.public_address = public_address
        if service_endpoint is not None:
            self.service_endpoint = service_endpoint
        if public_service_endpoint is not None:
            self.public_service_endpoint = public_service_endpoint

    @property
    def external_address(self):
        """Gets the external_address of this EngineExternalEntrypoint.

        微服务引擎暴露的IP地址。

        :return: The external_address of this EngineExternalEntrypoint.
        :rtype: str
        """
        return self._external_address

    @external_address.setter
    def external_address(self, external_address):
        """Sets the external_address of this EngineExternalEntrypoint.

        微服务引擎暴露的IP地址。

        :param external_address: The external_address of this EngineExternalEntrypoint.
        :type external_address: str
        """
        self._external_address = external_address

    @property
    def public_address(self):
        """Gets the public_address of this EngineExternalEntrypoint.

        微服务引擎的公网地址。

        :return: The public_address of this EngineExternalEntrypoint.
        :rtype: str
        """
        return self._public_address

    @public_address.setter
    def public_address(self, public_address):
        """Sets the public_address of this EngineExternalEntrypoint.

        微服务引擎的公网地址。

        :param public_address: The public_address of this EngineExternalEntrypoint.
        :type public_address: str
        """
        self._public_address = public_address

    @property
    def service_endpoint(self):
        """Gets the service_endpoint of this EngineExternalEntrypoint.

        微服务引擎组件的访问地址。

        :return: The service_endpoint of this EngineExternalEntrypoint.
        :rtype: dict(str, EntrypointItem)
        """
        return self._service_endpoint

    @service_endpoint.setter
    def service_endpoint(self, service_endpoint):
        """Sets the service_endpoint of this EngineExternalEntrypoint.

        微服务引擎组件的访问地址。

        :param service_endpoint: The service_endpoint of this EngineExternalEntrypoint.
        :type service_endpoint: dict(str, EntrypointItem)
        """
        self._service_endpoint = service_endpoint

    @property
    def public_service_endpoint(self):
        """Gets the public_service_endpoint of this EngineExternalEntrypoint.

        微服务引擎组件的公网地址。

        :return: The public_service_endpoint of this EngineExternalEntrypoint.
        :rtype: dict(str, EntrypointItem)
        """
        return self._public_service_endpoint

    @public_service_endpoint.setter
    def public_service_endpoint(self, public_service_endpoint):
        """Sets the public_service_endpoint of this EngineExternalEntrypoint.

        微服务引擎组件的公网地址。

        :param public_service_endpoint: The public_service_endpoint of this EngineExternalEntrypoint.
        :type public_service_endpoint: dict(str, EntrypointItem)
        """
        self._public_service_endpoint = public_service_endpoint

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
        if not isinstance(other, EngineExternalEntrypoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
