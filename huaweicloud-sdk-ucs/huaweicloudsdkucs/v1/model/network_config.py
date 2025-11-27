# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pod_cidr': 'str',
        'service_cidr': 'str'
    }

    attribute_map = {
        'pod_cidr': 'podCIDR',
        'service_cidr': 'serviceCIDR'
    }

    def __init__(self, pod_cidr=None, service_cidr=None):
        r"""NetworkConfig

        The model defined in huaweicloud sdk

        :param pod_cidr: 容器网段
        :type pod_cidr: str
        :param service_cidr: 服务网段
        :type service_cidr: str
        """
        
        

        self._pod_cidr = None
        self._service_cidr = None
        self.discriminator = None

        if pod_cidr is not None:
            self.pod_cidr = pod_cidr
        if service_cidr is not None:
            self.service_cidr = service_cidr

    @property
    def pod_cidr(self):
        r"""Gets the pod_cidr of this NetworkConfig.

        容器网段

        :return: The pod_cidr of this NetworkConfig.
        :rtype: str
        """
        return self._pod_cidr

    @pod_cidr.setter
    def pod_cidr(self, pod_cidr):
        r"""Sets the pod_cidr of this NetworkConfig.

        容器网段

        :param pod_cidr: The pod_cidr of this NetworkConfig.
        :type pod_cidr: str
        """
        self._pod_cidr = pod_cidr

    @property
    def service_cidr(self):
        r"""Gets the service_cidr of this NetworkConfig.

        服务网段

        :return: The service_cidr of this NetworkConfig.
        :rtype: str
        """
        return self._service_cidr

    @service_cidr.setter
    def service_cidr(self, service_cidr):
        r"""Sets the service_cidr of this NetworkConfig.

        服务网段

        :param service_cidr: The service_cidr of this NetworkConfig.
        :type service_cidr: str
        """
        self._service_cidr = service_cidr

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
        if not isinstance(other, NetworkConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
