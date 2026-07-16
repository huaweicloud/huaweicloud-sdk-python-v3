# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuntimeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_invoke': 'ServiceInvoke',
        'service_limit': 'ServiceLimit',
        'service_secret': 'ServiceSecret',
        'server_task_limit': 'ServerTaskLimit'
    }

    attribute_map = {
        'service_invoke': 'service_invoke',
        'service_limit': 'service_limit',
        'service_secret': 'service_secret',
        'server_task_limit': 'server_task_limit'
    }

    def __init__(self, service_invoke=None, service_limit=None, service_secret=None, server_task_limit=None):
        r"""RuntimeConfig

        The model defined in huaweicloud sdk

        :param service_invoke: 
        :type service_invoke: :class:`huaweicloudsdkmodelarts.v1.ServiceInvoke`
        :param service_limit: 
        :type service_limit: :class:`huaweicloudsdkmodelarts.v1.ServiceLimit`
        :param service_secret: 
        :type service_secret: :class:`huaweicloudsdkmodelarts.v1.ServiceSecret`
        :param server_task_limit: 
        :type server_task_limit: :class:`huaweicloudsdkmodelarts.v1.ServerTaskLimit`
        """
        
        

        self._service_invoke = None
        self._service_limit = None
        self._service_secret = None
        self._server_task_limit = None
        self.discriminator = None

        self.service_invoke = service_invoke
        self.service_limit = service_limit
        if service_secret is not None:
            self.service_secret = service_secret
        if server_task_limit is not None:
            self.server_task_limit = server_task_limit

    @property
    def service_invoke(self):
        r"""Gets the service_invoke of this RuntimeConfig.

        :return: The service_invoke of this RuntimeConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServiceInvoke`
        """
        return self._service_invoke

    @service_invoke.setter
    def service_invoke(self, service_invoke):
        r"""Sets the service_invoke of this RuntimeConfig.

        :param service_invoke: The service_invoke of this RuntimeConfig.
        :type service_invoke: :class:`huaweicloudsdkmodelarts.v1.ServiceInvoke`
        """
        self._service_invoke = service_invoke

    @property
    def service_limit(self):
        r"""Gets the service_limit of this RuntimeConfig.

        :return: The service_limit of this RuntimeConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServiceLimit`
        """
        return self._service_limit

    @service_limit.setter
    def service_limit(self, service_limit):
        r"""Sets the service_limit of this RuntimeConfig.

        :param service_limit: The service_limit of this RuntimeConfig.
        :type service_limit: :class:`huaweicloudsdkmodelarts.v1.ServiceLimit`
        """
        self._service_limit = service_limit

    @property
    def service_secret(self):
        r"""Gets the service_secret of this RuntimeConfig.

        :return: The service_secret of this RuntimeConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServiceSecret`
        """
        return self._service_secret

    @service_secret.setter
    def service_secret(self, service_secret):
        r"""Sets the service_secret of this RuntimeConfig.

        :param service_secret: The service_secret of this RuntimeConfig.
        :type service_secret: :class:`huaweicloudsdkmodelarts.v1.ServiceSecret`
        """
        self._service_secret = service_secret

    @property
    def server_task_limit(self):
        r"""Gets the server_task_limit of this RuntimeConfig.

        :return: The server_task_limit of this RuntimeConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServerTaskLimit`
        """
        return self._server_task_limit

    @server_task_limit.setter
    def server_task_limit(self, server_task_limit):
        r"""Sets the server_task_limit of this RuntimeConfig.

        :param server_task_limit: The server_task_limit of this RuntimeConfig.
        :type server_task_limit: :class:`huaweicloudsdkmodelarts.v1.ServerTaskLimit`
        """
        self._server_task_limit = server_task_limit

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
        if not isinstance(other, RuntimeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
