# coding: utf-8

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
        'create_time': 'int',
        'shared_quota': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str'
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
        'create_time': 'create_time',
        'shared_quota': 'shared_quota',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name'
    }

    def __init__(self, resource_id=None, version=None, quota_status=None, used_status=None, host_id=None, host_name=None, charging_mode=None, tags=None, expire_time=None, create_time=None, shared_quota=None, enterprise_project_id=None, enterprise_project_name=None):
        r"""QuotaResourcesResponseInfo

        The model defined in huaweicloud sdk

        :param resource_id: **参数解释** : HSS配额的资源ID **取值范围** : 字符长度1-128位 
        :type resource_id: str
        :param version: **参数解释**： 资源规格编码 **取值范围**： 包含如下6种。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。
        :type version: str
        :param quota_status: **参数解释**： 配额状态 **取值范围**： 包含如下3种。 - normal : 正常 - expired : 已过期 - freeze : 已冻结
        :type quota_status: str
        :param used_status: **参数解释**： 使用状态 **取值范围**： 包含如下2种。 - idle : 空闲 - used : 使用中
        :type used_status: str
        :param host_id: **参数解释**: 服务器ID **取值范围**: 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-128位 
        :type host_name: str
        :param charging_mode: **参数解释**： 计费模式 **取值范围**: - packet_cycle ：包周期。 - on_demand ：按需。
        :type charging_mode: str
        :param tags: **参数解释**： 标签 **取值范围**: 不涉及
        :type tags: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        :param expire_time: **参数解释**： 过期时间 **取值范围**: -1到9223372036854775807，-1表示没有到期时间
        :type expire_time: int
        :param create_time: **参数解释**： 创建时间 **取值范围**: 0到9223372036854775807
        :type create_time: int
        :param shared_quota: **参数解释**： 是否共享配额 **取值范围**: - shared：共享的 - unshared：非共享的
        :type shared_quota: str
        :param enterprise_project_id: **参数解释**: 主机所属的企业项目ID。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。 **取值范围**: 字符长度1-256位 
        :type enterprise_project_id: str
        :param enterprise_project_name: **参数解释**: 所属企业项目名称 **取值范围**: 字符长度1-256位 
        :type enterprise_project_name: str
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
        self._create_time = None
        self._shared_quota = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
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
        if create_time is not None:
            self.create_time = create_time
        if shared_quota is not None:
            self.shared_quota = shared_quota
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this QuotaResourcesResponseInfo.

        **参数解释** : HSS配额的资源ID **取值范围** : 字符长度1-128位 

        :return: The resource_id of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this QuotaResourcesResponseInfo.

        **参数解释** : HSS配额的资源ID **取值范围** : 字符长度1-128位 

        :param resource_id: The resource_id of this QuotaResourcesResponseInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def version(self):
        r"""Gets the version of this QuotaResourcesResponseInfo.

        **参数解释**： 资源规格编码 **取值范围**： 包含如下6种。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。

        :return: The version of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this QuotaResourcesResponseInfo.

        **参数解释**： 资源规格编码 **取值范围**： 包含如下6种。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。

        :param version: The version of this QuotaResourcesResponseInfo.
        :type version: str
        """
        self._version = version

    @property
    def quota_status(self):
        r"""Gets the quota_status of this QuotaResourcesResponseInfo.

        **参数解释**： 配额状态 **取值范围**： 包含如下3种。 - normal : 正常 - expired : 已过期 - freeze : 已冻结

        :return: The quota_status of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._quota_status

    @quota_status.setter
    def quota_status(self, quota_status):
        r"""Sets the quota_status of this QuotaResourcesResponseInfo.

        **参数解释**： 配额状态 **取值范围**： 包含如下3种。 - normal : 正常 - expired : 已过期 - freeze : 已冻结

        :param quota_status: The quota_status of this QuotaResourcesResponseInfo.
        :type quota_status: str
        """
        self._quota_status = quota_status

    @property
    def used_status(self):
        r"""Gets the used_status of this QuotaResourcesResponseInfo.

        **参数解释**： 使用状态 **取值范围**： 包含如下2种。 - idle : 空闲 - used : 使用中

        :return: The used_status of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._used_status

    @used_status.setter
    def used_status(self, used_status):
        r"""Sets the used_status of this QuotaResourcesResponseInfo.

        **参数解释**： 使用状态 **取值范围**： 包含如下2种。 - idle : 空闲 - used : 使用中

        :param used_status: The used_status of this QuotaResourcesResponseInfo.
        :type used_status: str
        """
        self._used_status = used_status

    @property
    def host_id(self):
        r"""Gets the host_id of this QuotaResourcesResponseInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度1-64位 

        :return: The host_id of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this QuotaResourcesResponseInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度1-64位 

        :param host_id: The host_id of this QuotaResourcesResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this QuotaResourcesResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-128位 

        :return: The host_name of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this QuotaResourcesResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-128位 

        :param host_name: The host_name of this QuotaResourcesResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this QuotaResourcesResponseInfo.

        **参数解释**： 计费模式 **取值范围**: - packet_cycle ：包周期。 - on_demand ：按需。

        :return: The charging_mode of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this QuotaResourcesResponseInfo.

        **参数解释**： 计费模式 **取值范围**: - packet_cycle ：包周期。 - on_demand ：按需。

        :param charging_mode: The charging_mode of this QuotaResourcesResponseInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def tags(self):
        r"""Gets the tags of this QuotaResourcesResponseInfo.

        **参数解释**： 标签 **取值范围**: 不涉及

        :return: The tags of this QuotaResourcesResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this QuotaResourcesResponseInfo.

        **参数解释**： 标签 **取值范围**: 不涉及

        :param tags: The tags of this QuotaResourcesResponseInfo.
        :type tags: list[:class:`huaweicloudsdkhss.v5.TagInfo`]
        """
        self._tags = tags

    @property
    def expire_time(self):
        r"""Gets the expire_time of this QuotaResourcesResponseInfo.

        **参数解释**： 过期时间 **取值范围**: -1到9223372036854775807，-1表示没有到期时间

        :return: The expire_time of this QuotaResourcesResponseInfo.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this QuotaResourcesResponseInfo.

        **参数解释**： 过期时间 **取值范围**: -1到9223372036854775807，-1表示没有到期时间

        :param expire_time: The expire_time of this QuotaResourcesResponseInfo.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def create_time(self):
        r"""Gets the create_time of this QuotaResourcesResponseInfo.

        **参数解释**： 创建时间 **取值范围**: 0到9223372036854775807

        :return: The create_time of this QuotaResourcesResponseInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this QuotaResourcesResponseInfo.

        **参数解释**： 创建时间 **取值范围**: 0到9223372036854775807

        :param create_time: The create_time of this QuotaResourcesResponseInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def shared_quota(self):
        r"""Gets the shared_quota of this QuotaResourcesResponseInfo.

        **参数解释**： 是否共享配额 **取值范围**: - shared：共享的 - unshared：非共享的

        :return: The shared_quota of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._shared_quota

    @shared_quota.setter
    def shared_quota(self, shared_quota):
        r"""Sets the shared_quota of this QuotaResourcesResponseInfo.

        **参数解释**： 是否共享配额 **取值范围**: - shared：共享的 - unshared：非共享的

        :param shared_quota: The shared_quota of this QuotaResourcesResponseInfo.
        :type shared_quota: str
        """
        self._shared_quota = shared_quota

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this QuotaResourcesResponseInfo.

        **参数解释**: 主机所属的企业项目ID。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。 **取值范围**: 字符长度1-256位 

        :return: The enterprise_project_id of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this QuotaResourcesResponseInfo.

        **参数解释**: 主机所属的企业项目ID。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。 **取值范围**: 字符长度1-256位 

        :param enterprise_project_id: The enterprise_project_id of this QuotaResourcesResponseInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this QuotaResourcesResponseInfo.

        **参数解释**: 所属企业项目名称 **取值范围**: 字符长度1-256位 

        :return: The enterprise_project_name of this QuotaResourcesResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this QuotaResourcesResponseInfo.

        **参数解释**: 所属企业项目名称 **取值范围**: 字符长度1-256位 

        :param enterprise_project_name: The enterprise_project_name of this QuotaResourcesResponseInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

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
