# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEndpointOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_type': 'EndpointType',
        'weight': 'int',
        'ip_address': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'weight': 'weight',
        'ip_address': 'ip_address'
    }

    def __init__(self, resource_id=None, resource_type=None, weight=None, ip_address=None):
        """CreateEndpointOption

        The model defined in huaweicloud sdk

        :param resource_id: 对应后端资源的ID，比如EIP的ID。
        :type resource_id: str
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkga.v1.EndpointType`
        :param weight: 终端节点权重。
        :type weight: int
        :param ip_address: IP地址。
        :type ip_address: str
        """
        
        

        self._resource_id = None
        self._resource_type = None
        self._weight = None
        self._ip_address = None
        self.discriminator = None

        self.resource_id = resource_id
        self.resource_type = resource_type
        if weight is not None:
            self.weight = weight
        self.ip_address = ip_address

    @property
    def resource_id(self):
        """Gets the resource_id of this CreateEndpointOption.

        对应后端资源的ID，比如EIP的ID。

        :return: The resource_id of this CreateEndpointOption.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this CreateEndpointOption.

        对应后端资源的ID，比如EIP的ID。

        :param resource_id: The resource_id of this CreateEndpointOption.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this CreateEndpointOption.

        :return: The resource_type of this CreateEndpointOption.
        :rtype: :class:`huaweicloudsdkga.v1.EndpointType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this CreateEndpointOption.

        :param resource_type: The resource_type of this CreateEndpointOption.
        :type resource_type: :class:`huaweicloudsdkga.v1.EndpointType`
        """
        self._resource_type = resource_type

    @property
    def weight(self):
        """Gets the weight of this CreateEndpointOption.

        终端节点权重。

        :return: The weight of this CreateEndpointOption.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateEndpointOption.

        终端节点权重。

        :param weight: The weight of this CreateEndpointOption.
        :type weight: int
        """
        self._weight = weight

    @property
    def ip_address(self):
        """Gets the ip_address of this CreateEndpointOption.

        IP地址。

        :return: The ip_address of this CreateEndpointOption.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this CreateEndpointOption.

        IP地址。

        :param ip_address: The ip_address of this CreateEndpointOption.
        :type ip_address: str
        """
        self._ip_address = ip_address

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
        if not isinstance(other, CreateEndpointOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
