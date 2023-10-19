# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubnetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'cidr': 'str',
        'name': 'str',
        'id': 'str',
        'gateway_ip': 'str',
        'vpc_id': 'str',
        'status': 'str',
        'ipv6_enable': 'bool'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'cidr': 'cidr',
        'name': 'name',
        'id': 'id',
        'gateway_ip': 'gateway_ip',
        'vpc_id': 'vpc_id',
        'status': 'status',
        'ipv6_enable': 'ipv6_enable'
    }

    def __init__(self, availability_zone=None, cidr=None, name=None, id=None, gateway_ip=None, vpc_id=None, status=None, ipv6_enable=None):
        """SubnetInfo

        The model defined in huaweicloud sdk

        :param availability_zone: 子网id
        :type availability_zone: str
        :param cidr: vpc cidr
        :type cidr: str
        :param name: 子网名称
        :type name: str
        :param id: 子网id
        :type id: str
        :param gateway_ip: 子网网关ip
        :type gateway_ip: str
        :param vpc_id: vpc id
        :type vpc_id: str
        :param status: 子网的状态
        :type status: str
        :param ipv6_enable: 是否支持ipv6，boolean值为true表示是，false表示否
        :type ipv6_enable: bool
        """
        
        

        self._availability_zone = None
        self._cidr = None
        self._name = None
        self._id = None
        self._gateway_ip = None
        self._vpc_id = None
        self._status = None
        self._ipv6_enable = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if cidr is not None:
            self.cidr = cidr
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if gateway_ip is not None:
            self.gateway_ip = gateway_ip
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if status is not None:
            self.status = status
        if ipv6_enable is not None:
            self.ipv6_enable = ipv6_enable

    @property
    def availability_zone(self):
        """Gets the availability_zone of this SubnetInfo.

        子网id

        :return: The availability_zone of this SubnetInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this SubnetInfo.

        子网id

        :param availability_zone: The availability_zone of this SubnetInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def cidr(self):
        """Gets the cidr of this SubnetInfo.

        vpc cidr

        :return: The cidr of this SubnetInfo.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this SubnetInfo.

        vpc cidr

        :param cidr: The cidr of this SubnetInfo.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def name(self):
        """Gets the name of this SubnetInfo.

        子网名称

        :return: The name of this SubnetInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubnetInfo.

        子网名称

        :param name: The name of this SubnetInfo.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this SubnetInfo.

        子网id

        :return: The id of this SubnetInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubnetInfo.

        子网id

        :param id: The id of this SubnetInfo.
        :type id: str
        """
        self._id = id

    @property
    def gateway_ip(self):
        """Gets the gateway_ip of this SubnetInfo.

        子网网关ip

        :return: The gateway_ip of this SubnetInfo.
        :rtype: str
        """
        return self._gateway_ip

    @gateway_ip.setter
    def gateway_ip(self, gateway_ip):
        """Sets the gateway_ip of this SubnetInfo.

        子网网关ip

        :param gateway_ip: The gateway_ip of this SubnetInfo.
        :type gateway_ip: str
        """
        self._gateway_ip = gateway_ip

    @property
    def vpc_id(self):
        """Gets the vpc_id of this SubnetInfo.

        vpc id

        :return: The vpc_id of this SubnetInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this SubnetInfo.

        vpc id

        :param vpc_id: The vpc_id of this SubnetInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def status(self):
        """Gets the status of this SubnetInfo.

        子网的状态

        :return: The status of this SubnetInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubnetInfo.

        子网的状态

        :param status: The status of this SubnetInfo.
        :type status: str
        """
        self._status = status

    @property
    def ipv6_enable(self):
        """Gets the ipv6_enable of this SubnetInfo.

        是否支持ipv6，boolean值为true表示是，false表示否

        :return: The ipv6_enable of this SubnetInfo.
        :rtype: bool
        """
        return self._ipv6_enable

    @ipv6_enable.setter
    def ipv6_enable(self, ipv6_enable):
        """Sets the ipv6_enable of this SubnetInfo.

        是否支持ipv6，boolean值为true表示是，false表示否

        :param ipv6_enable: The ipv6_enable of this SubnetInfo.
        :type ipv6_enable: bool
        """
        self._ipv6_enable = ipv6_enable

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
        if not isinstance(other, SubnetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
