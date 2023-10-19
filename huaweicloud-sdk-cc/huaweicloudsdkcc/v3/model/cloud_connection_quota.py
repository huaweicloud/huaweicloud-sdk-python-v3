# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudConnectionQuota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'cloud_connection_id': 'str',
        'region_id': 'str',
        'quota_type': 'str',
        'quota_number': 'int',
        'quota_used': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'cloud_connection_id': 'cloud_connection_id',
        'region_id': 'region_id',
        'quota_type': 'quota_type',
        'quota_number': 'quota_number',
        'quota_used': 'quota_used'
    }

    def __init__(self, domain_id=None, cloud_connection_id=None, region_id=None, quota_type=None, quota_number=None, quota_used=None):
        """CloudConnectionQuota

        The model defined in huaweicloud sdk

        :param domain_id: 实例所属帐号ID。
        :type domain_id: str
        :param cloud_connection_id: 资源ID标识符。
        :type cloud_connection_id: str
        :param region_id: RegionID。
        :type region_id: str
        :param quota_type: 配额类型： - cloud_connection: 可加载的云连接实例数 - cloud_connection_region: 某云连接实例下可加载的Region数 - cloud_connection_route: 某云连接实例下可加载的路由数 - region_network_instance: 某云连接实例下某个Region下可加载的网络实例数
        :type quota_type: str
        :param quota_number: 配额数量。
        :type quota_number: int
        :param quota_used: 配额使用数量。
        :type quota_used: int
        """
        
        

        self._domain_id = None
        self._cloud_connection_id = None
        self._region_id = None
        self._quota_type = None
        self._quota_number = None
        self._quota_used = None
        self.discriminator = None

        self.domain_id = domain_id
        self.cloud_connection_id = cloud_connection_id
        self.region_id = region_id
        if quota_type is not None:
            self.quota_type = quota_type
        if quota_number is not None:
            self.quota_number = quota_number
        if quota_used is not None:
            self.quota_used = quota_used

    @property
    def domain_id(self):
        """Gets the domain_id of this CloudConnectionQuota.

        实例所属帐号ID。

        :return: The domain_id of this CloudConnectionQuota.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CloudConnectionQuota.

        实例所属帐号ID。

        :param domain_id: The domain_id of this CloudConnectionQuota.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def cloud_connection_id(self):
        """Gets the cloud_connection_id of this CloudConnectionQuota.

        资源ID标识符。

        :return: The cloud_connection_id of this CloudConnectionQuota.
        :rtype: str
        """
        return self._cloud_connection_id

    @cloud_connection_id.setter
    def cloud_connection_id(self, cloud_connection_id):
        """Sets the cloud_connection_id of this CloudConnectionQuota.

        资源ID标识符。

        :param cloud_connection_id: The cloud_connection_id of this CloudConnectionQuota.
        :type cloud_connection_id: str
        """
        self._cloud_connection_id = cloud_connection_id

    @property
    def region_id(self):
        """Gets the region_id of this CloudConnectionQuota.

        RegionID。

        :return: The region_id of this CloudConnectionQuota.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this CloudConnectionQuota.

        RegionID。

        :param region_id: The region_id of this CloudConnectionQuota.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def quota_type(self):
        """Gets the quota_type of this CloudConnectionQuota.

        配额类型： - cloud_connection: 可加载的云连接实例数 - cloud_connection_region: 某云连接实例下可加载的Region数 - cloud_connection_route: 某云连接实例下可加载的路由数 - region_network_instance: 某云连接实例下某个Region下可加载的网络实例数

        :return: The quota_type of this CloudConnectionQuota.
        :rtype: str
        """
        return self._quota_type

    @quota_type.setter
    def quota_type(self, quota_type):
        """Sets the quota_type of this CloudConnectionQuota.

        配额类型： - cloud_connection: 可加载的云连接实例数 - cloud_connection_region: 某云连接实例下可加载的Region数 - cloud_connection_route: 某云连接实例下可加载的路由数 - region_network_instance: 某云连接实例下某个Region下可加载的网络实例数

        :param quota_type: The quota_type of this CloudConnectionQuota.
        :type quota_type: str
        """
        self._quota_type = quota_type

    @property
    def quota_number(self):
        """Gets the quota_number of this CloudConnectionQuota.

        配额数量。

        :return: The quota_number of this CloudConnectionQuota.
        :rtype: int
        """
        return self._quota_number

    @quota_number.setter
    def quota_number(self, quota_number):
        """Sets the quota_number of this CloudConnectionQuota.

        配额数量。

        :param quota_number: The quota_number of this CloudConnectionQuota.
        :type quota_number: int
        """
        self._quota_number = quota_number

    @property
    def quota_used(self):
        """Gets the quota_used of this CloudConnectionQuota.

        配额使用数量。

        :return: The quota_used of this CloudConnectionQuota.
        :rtype: int
        """
        return self._quota_used

    @quota_used.setter
    def quota_used(self, quota_used):
        """Sets the quota_used of this CloudConnectionQuota.

        配额使用数量。

        :param quota_used: The quota_used of this CloudConnectionQuota.
        :type quota_used: int
        """
        self._quota_used = quota_used

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
        if not isinstance(other, CloudConnectionQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
