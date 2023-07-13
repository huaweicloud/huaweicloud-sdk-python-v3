# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadBalancerStatusHealthMonitor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'provisioning_status': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'provisioning_status': 'provisioning_status'
    }

    def __init__(self, type=None, id=None, name=None, provisioning_status=None):
        """LoadBalancerStatusHealthMonitor

        The model defined in huaweicloud sdk

        :param type: 协议类型。取值：TCP、UDP_CONNECT或HTTP。
        :type type: str
        :param id: 健康检查器ID。
        :type id: str
        :param name: 健康检查器名称。
        :type name: str
        :param provisioning_status: 健康检查器的配置状态。取值：ACTIVE表示使用中。
        :type provisioning_status: str
        """
        
        

        self._type = None
        self._id = None
        self._name = None
        self._provisioning_status = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status

    @property
    def type(self):
        """Gets the type of this LoadBalancerStatusHealthMonitor.

        协议类型。取值：TCP、UDP_CONNECT或HTTP。

        :return: The type of this LoadBalancerStatusHealthMonitor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LoadBalancerStatusHealthMonitor.

        协议类型。取值：TCP、UDP_CONNECT或HTTP。

        :param type: The type of this LoadBalancerStatusHealthMonitor.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this LoadBalancerStatusHealthMonitor.

        健康检查器ID。

        :return: The id of this LoadBalancerStatusHealthMonitor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancerStatusHealthMonitor.

        健康检查器ID。

        :param id: The id of this LoadBalancerStatusHealthMonitor.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this LoadBalancerStatusHealthMonitor.

        健康检查器名称。

        :return: The name of this LoadBalancerStatusHealthMonitor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancerStatusHealthMonitor.

        健康检查器名称。

        :param name: The name of this LoadBalancerStatusHealthMonitor.
        :type name: str
        """
        self._name = name

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancerStatusHealthMonitor.

        健康检查器的配置状态。取值：ACTIVE表示使用中。

        :return: The provisioning_status of this LoadBalancerStatusHealthMonitor.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancerStatusHealthMonitor.

        健康检查器的配置状态。取值：ACTIVE表示使用中。

        :param provisioning_status: The provisioning_status of this LoadBalancerStatusHealthMonitor.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

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
        if not isinstance(other, LoadBalancerStatusHealthMonitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
