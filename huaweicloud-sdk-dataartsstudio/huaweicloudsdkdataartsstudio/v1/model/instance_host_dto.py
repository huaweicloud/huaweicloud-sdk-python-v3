# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceHostDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'intranet_host': 'str',
        'external_host': 'str',
        'domains': 'list[str]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'intranet_host': 'intranet_host',
        'external_host': 'external_host',
        'domains': 'domains'
    }

    def __init__(self, instance_id=None, instance_name=None, intranet_host=None, external_host=None, domains=None):
        """InstanceHostDTO

        The model defined in huaweicloud sdk

        :param instance_id: 集群id
        :type instance_id: str
        :param instance_name: 集群名
        :type instance_name: str
        :param intranet_host: 内网地址
        :type intranet_host: str
        :param external_host: 外网地址
        :type external_host: str
        :param domains: 网关域名
        :type domains: list[str]
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._intranet_host = None
        self._external_host = None
        self._domains = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if intranet_host is not None:
            self.intranet_host = intranet_host
        if external_host is not None:
            self.external_host = external_host
        if domains is not None:
            self.domains = domains

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceHostDTO.

        集群id

        :return: The instance_id of this InstanceHostDTO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceHostDTO.

        集群id

        :param instance_id: The instance_id of this InstanceHostDTO.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceHostDTO.

        集群名

        :return: The instance_name of this InstanceHostDTO.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceHostDTO.

        集群名

        :param instance_name: The instance_name of this InstanceHostDTO.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def intranet_host(self):
        """Gets the intranet_host of this InstanceHostDTO.

        内网地址

        :return: The intranet_host of this InstanceHostDTO.
        :rtype: str
        """
        return self._intranet_host

    @intranet_host.setter
    def intranet_host(self, intranet_host):
        """Sets the intranet_host of this InstanceHostDTO.

        内网地址

        :param intranet_host: The intranet_host of this InstanceHostDTO.
        :type intranet_host: str
        """
        self._intranet_host = intranet_host

    @property
    def external_host(self):
        """Gets the external_host of this InstanceHostDTO.

        外网地址

        :return: The external_host of this InstanceHostDTO.
        :rtype: str
        """
        return self._external_host

    @external_host.setter
    def external_host(self, external_host):
        """Sets the external_host of this InstanceHostDTO.

        外网地址

        :param external_host: The external_host of this InstanceHostDTO.
        :type external_host: str
        """
        self._external_host = external_host

    @property
    def domains(self):
        """Gets the domains of this InstanceHostDTO.

        网关域名

        :return: The domains of this InstanceHostDTO.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this InstanceHostDTO.

        网关域名

        :param domains: The domains of this InstanceHostDTO.
        :type domains: list[str]
        """
        self._domains = domains

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
        if not isinstance(other, InstanceHostDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
