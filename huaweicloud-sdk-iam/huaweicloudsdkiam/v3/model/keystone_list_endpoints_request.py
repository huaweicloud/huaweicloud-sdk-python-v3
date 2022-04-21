# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneListEndpointsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'interface': 'str',
        'service_id': 'str'
    }

    attribute_map = {
        'interface': 'interface',
        'service_id': 'service_id'
    }

    def __init__(self, interface=None, service_id=None):
        """KeystoneListEndpointsRequest

        The model defined in huaweicloud sdk

        :param interface: 终端节点平面。可能取值为：public、internal或admin。public： 用户可在公共网络接口上看到。internal：用户可在内部网络接口上看到。admin：管理员可以在安全的网络接口上看到。
        :type interface: str
        :param service_id: 服务ID。
        :type service_id: str
        """
        
        

        self._interface = None
        self._service_id = None
        self.discriminator = None

        if interface is not None:
            self.interface = interface
        if service_id is not None:
            self.service_id = service_id

    @property
    def interface(self):
        """Gets the interface of this KeystoneListEndpointsRequest.

        终端节点平面。可能取值为：public、internal或admin。public： 用户可在公共网络接口上看到。internal：用户可在内部网络接口上看到。admin：管理员可以在安全的网络接口上看到。

        :return: The interface of this KeystoneListEndpointsRequest.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this KeystoneListEndpointsRequest.

        终端节点平面。可能取值为：public、internal或admin。public： 用户可在公共网络接口上看到。internal：用户可在内部网络接口上看到。admin：管理员可以在安全的网络接口上看到。

        :param interface: The interface of this KeystoneListEndpointsRequest.
        :type interface: str
        """
        self._interface = interface

    @property
    def service_id(self):
        """Gets the service_id of this KeystoneListEndpointsRequest.

        服务ID。

        :return: The service_id of this KeystoneListEndpointsRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this KeystoneListEndpointsRequest.

        服务ID。

        :param service_id: The service_id of this KeystoneListEndpointsRequest.
        :type service_id: str
        """
        self._service_id = service_id

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
        if not isinstance(other, KeystoneListEndpointsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
