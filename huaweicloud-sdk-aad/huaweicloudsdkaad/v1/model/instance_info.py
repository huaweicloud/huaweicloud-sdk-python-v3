# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceInfo:

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
        'ips': 'list[InstanceIpInfo]',
        'expire_time': 'int',
        'service_bandwidth': 'int',
        'instance_status': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'ips': 'ips',
        'expire_time': 'expire_time',
        'service_bandwidth': 'service_bandwidth',
        'instance_status': 'instance_status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, instance_id=None, instance_name=None, ips=None, expire_time=None, service_bandwidth=None, instance_status=None, enterprise_project_id=None):
        """InstanceInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param instance_name: 实例名
        :type instance_name: str
        :param ips: 实例IP
        :type ips: list[:class:`huaweicloudsdkaad.v1.InstanceIpInfo`]
        :param expire_time: 实例过期时间
        :type expire_time: int
        :param service_bandwidth: 业务带宽
        :type service_bandwidth: int
        :param instance_status: 实例状态
        :type instance_status: int
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._ips = None
        self._expire_time = None
        self._service_bandwidth = None
        self._instance_status = None
        self._enterprise_project_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if ips is not None:
            self.ips = ips
        if expire_time is not None:
            self.expire_time = expire_time
        if service_bandwidth is not None:
            self.service_bandwidth = service_bandwidth
        if instance_status is not None:
            self.instance_status = instance_status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceInfo.

        实例ID

        :return: The instance_id of this InstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceInfo.

        实例ID

        :param instance_id: The instance_id of this InstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceInfo.

        实例名

        :return: The instance_name of this InstanceInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceInfo.

        实例名

        :param instance_name: The instance_name of this InstanceInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def ips(self):
        """Gets the ips of this InstanceInfo.

        实例IP

        :return: The ips of this InstanceInfo.
        :rtype: list[:class:`huaweicloudsdkaad.v1.InstanceIpInfo`]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this InstanceInfo.

        实例IP

        :param ips: The ips of this InstanceInfo.
        :type ips: list[:class:`huaweicloudsdkaad.v1.InstanceIpInfo`]
        """
        self._ips = ips

    @property
    def expire_time(self):
        """Gets the expire_time of this InstanceInfo.

        实例过期时间

        :return: The expire_time of this InstanceInfo.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this InstanceInfo.

        实例过期时间

        :param expire_time: The expire_time of this InstanceInfo.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def service_bandwidth(self):
        """Gets the service_bandwidth of this InstanceInfo.

        业务带宽

        :return: The service_bandwidth of this InstanceInfo.
        :rtype: int
        """
        return self._service_bandwidth

    @service_bandwidth.setter
    def service_bandwidth(self, service_bandwidth):
        """Sets the service_bandwidth of this InstanceInfo.

        业务带宽

        :param service_bandwidth: The service_bandwidth of this InstanceInfo.
        :type service_bandwidth: int
        """
        self._service_bandwidth = service_bandwidth

    @property
    def instance_status(self):
        """Gets the instance_status of this InstanceInfo.

        实例状态

        :return: The instance_status of this InstanceInfo.
        :rtype: int
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this InstanceInfo.

        实例状态

        :param instance_status: The instance_status of this InstanceInfo.
        :type instance_status: int
        """
        self._instance_status = instance_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this InstanceInfo.

        企业项目ID

        :return: The enterprise_project_id of this InstanceInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this InstanceInfo.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this InstanceInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, InstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
