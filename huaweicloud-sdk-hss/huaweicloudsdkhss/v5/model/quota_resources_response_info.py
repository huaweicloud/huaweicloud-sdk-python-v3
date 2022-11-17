# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaResourcesResponseInfo:

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
        'version': 'str',
        'quota_status': 'str',
        'used_status': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'charging_mode': 'str',
        'tags': 'list[TagInfo]',
        'expire_time': 'int',
        'shared_quota': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'version': 'version',
        'quota_status': 'quota_status',
        'used_status': 'used_status',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'charging_mode': 'charging_mode',
        'tags': 'tags',
        'expire_time': 'expire_time',
        'shared_quota': 'shared_quota'
    }

    def __init__(self, resource_id=None, version=None, quota_status=None, used_status=None, host_id=None, host_name=None, charging_mode=None, tags=None, expire_time=None, shared_quota=None):
        """QuotaResourcesResponseInfo

        The model defined in huaweicloud sdk

        :param resource_id: 主机安全配额的资源ID
        :type resource_id: str
        :param version: 资源规格编码，包含如下:   - hss.version.basic : 基础版   - hss.version.enterprise : 企业版   - hss.version.premium : 旗舰版   - hss.version.wtp : 网页防篡改版   - hss.version.container : 容器版
        :type version: str
        :param quota_status: 配额状态   - normal : 正常   - expired : 已过期   - freeze : 已冻结
        :type quota_status: str
        :param used_status: 使用状态   - idle : 空闲   - used : 使用中
        :type used_status: str
        :param host_id: 服务器ID
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param charging_mode: 计费模式   - packet_cycle : 包周期   - on_demand : 按需
        :type charging_mode: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        :param expire_time: 过期时间，-1表示没有到期时间
        :type expire_time: int
        :param shared_quota: 是否共享配额   - shared：共享的   - unshared：非共享的
        :type shared_quota: str
        """
        
        

        self._resource_id = None
        self._version = None
        self._quota_status = None
        self._used_status = None
        self._host_id = None
        self._host_name = None
        self._charging_mode = None
        self._tags = None
        self._expire_time = None
        self._shared_quota = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if version is not None:
            self.version = version
        if quota_status is not None:
            self.quota_status = quota_status
        if used_status is not None:
            self.used_status = used_status
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if tags is not None:
            self.tags = tags
        if expire_time is not None:
            self.expire_time = expire_time
        if shared_quota is not None:
            self.shared_quota = shared_quota

    @property
    def resource_id(self):
        """Gets the resource_id of this QuotaResourcesResponseInfo.

        主机安全配额的资源ID

        :return: The resource_id of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this QuotaResourcesResponseInfo.

        主机安全配额的资源ID

        :param resource_id: The resource_id of this QuotaResourcesResponseInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def version(self):
        """Gets the version of this QuotaResourcesResponseInfo.

        资源规格编码，包含如下:   - hss.version.basic : 基础版   - hss.version.enterprise : 企业版   - hss.version.premium : 旗舰版   - hss.version.wtp : 网页防篡改版   - hss.version.container : 容器版

        :return: The version of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this QuotaResourcesResponseInfo.

        资源规格编码，包含如下:   - hss.version.basic : 基础版   - hss.version.enterprise : 企业版   - hss.version.premium : 旗舰版   - hss.version.wtp : 网页防篡改版   - hss.version.container : 容器版

        :param version: The version of this QuotaResourcesResponseInfo.
        :type version: str
        """
        self._version = version

    @property
    def quota_status(self):
        """Gets the quota_status of this QuotaResourcesResponseInfo.

        配额状态   - normal : 正常   - expired : 已过期   - freeze : 已冻结

        :return: The quota_status of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._quota_status

    @quota_status.setter
    def quota_status(self, quota_status):
        """Sets the quota_status of this QuotaResourcesResponseInfo.

        配额状态   - normal : 正常   - expired : 已过期   - freeze : 已冻结

        :param quota_status: The quota_status of this QuotaResourcesResponseInfo.
        :type quota_status: str
        """
        self._quota_status = quota_status

    @property
    def used_status(self):
        """Gets the used_status of this QuotaResourcesResponseInfo.

        使用状态   - idle : 空闲   - used : 使用中

        :return: The used_status of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._used_status

    @used_status.setter
    def used_status(self, used_status):
        """Sets the used_status of this QuotaResourcesResponseInfo.

        使用状态   - idle : 空闲   - used : 使用中

        :param used_status: The used_status of this QuotaResourcesResponseInfo.
        :type used_status: str
        """
        self._used_status = used_status

    @property
    def host_id(self):
        """Gets the host_id of this QuotaResourcesResponseInfo.

        服务器ID

        :return: The host_id of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this QuotaResourcesResponseInfo.

        服务器ID

        :param host_id: The host_id of this QuotaResourcesResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this QuotaResourcesResponseInfo.

        服务器名称

        :return: The host_name of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this QuotaResourcesResponseInfo.

        服务器名称

        :param host_name: The host_name of this QuotaResourcesResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def charging_mode(self):
        """Gets the charging_mode of this QuotaResourcesResponseInfo.

        计费模式   - packet_cycle : 包周期   - on_demand : 按需

        :return: The charging_mode of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this QuotaResourcesResponseInfo.

        计费模式   - packet_cycle : 包周期   - on_demand : 按需

        :param charging_mode: The charging_mode of this QuotaResourcesResponseInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def tags(self):
        """Gets the tags of this QuotaResourcesResponseInfo.

        标签

        :return: The tags of this QuotaResourcesResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this QuotaResourcesResponseInfo.

        标签

        :param tags: The tags of this QuotaResourcesResponseInfo.
        :type tags: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        """
        self._tags = tags

    @property
    def expire_time(self):
        """Gets the expire_time of this QuotaResourcesResponseInfo.

        过期时间，-1表示没有到期时间

        :return: The expire_time of this QuotaResourcesResponseInfo.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this QuotaResourcesResponseInfo.

        过期时间，-1表示没有到期时间

        :param expire_time: The expire_time of this QuotaResourcesResponseInfo.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def shared_quota(self):
        """Gets the shared_quota of this QuotaResourcesResponseInfo.

        是否共享配额   - shared：共享的   - unshared：非共享的

        :return: The shared_quota of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._shared_quota

    @shared_quota.setter
    def shared_quota(self, shared_quota):
        """Sets the shared_quota of this QuotaResourcesResponseInfo.

        是否共享配额   - shared：共享的   - unshared：非共享的

        :param shared_quota: The shared_quota of this QuotaResourcesResponseInfo.
        :type shared_quota: str
        """
        self._shared_quota = shared_quota

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
        if not isinstance(other, QuotaResourcesResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
