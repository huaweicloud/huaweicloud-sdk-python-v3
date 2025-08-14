# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQuotasDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'version': 'str',
        'category': 'str',
        'quota_status': 'str',
        'used_status': 'str',
        'host_name': 'str',
        'resource_id': 'str',
        'charging_mode': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'version': 'version',
        'category': 'category',
        'quota_status': 'quota_status',
        'used_status': 'used_status',
        'host_name': 'host_name',
        'resource_id': 'resource_id',
        'charging_mode': 'charging_mode',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, region=None, enterprise_project_id=None, version=None, category=None, quota_status=None, used_status=None, host_name=None, resource_id=None, charging_mode=None, limit=None, offset=None):
        r"""ListQuotasDetailRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param version: **参数解释**： 主机开通的版本 **约束限制**: 不涉及 **取值范围**： 包含如下7种输入。 - hss.version.null ：无。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。 **默认取值**: 不涉及
        :type version: str
        :param category: **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - host_resource ：主机 - container_resource ：容器 **默认取值**: 不涉及
        :type category: str
        :param quota_status: **参数解释**: 配额状态 **约束限制**: 不涉及 **取值范围**: 包含如下三种： - normal ： 正常 - expired ：过期 - freeze ：冻结 **默认取值**: 不涉及
        :type quota_status: str
        :param used_status: **参数解释**: 使用状态 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - idle ：空闲的 - used ：使用中 **默认取值**: 不涉及
        :type used_status: str
        :param host_name: **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type host_name: str
        :param resource_id: **参数解释** : HSS配额的资源ID **约束限制** : 不涉及 **取值范围** : 字符长度1-128位 **默认取值** : 不涉及 
        :type resource_id: str
        :param charging_mode: **参数解释**： 收费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle ：包年/包月。 - on_demand ：按需。 **默认取值**: 不涉及
        :type charging_mode: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._version = None
        self._category = None
        self._quota_status = None
        self._used_status = None
        self._host_name = None
        self._resource_id = None
        self._charging_mode = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if version is not None:
            self.version = version
        if category is not None:
            self.category = category
        if quota_status is not None:
            self.quota_status = quota_status
        if used_status is not None:
            self.used_status = used_status
        if host_name is not None:
            self.host_name = host_name
        if resource_id is not None:
            self.resource_id = resource_id
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def region(self):
        r"""Gets the region of this ListQuotasDetailRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListQuotasDetailRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListQuotasDetailRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListQuotasDetailRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListQuotasDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListQuotasDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListQuotasDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListQuotasDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def version(self):
        r"""Gets the version of this ListQuotasDetailRequest.

        **参数解释**： 主机开通的版本 **约束限制**: 不涉及 **取值范围**： 包含如下7种输入。 - hss.version.null ：无。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。 **默认取值**: 不涉及

        :return: The version of this ListQuotasDetailRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListQuotasDetailRequest.

        **参数解释**： 主机开通的版本 **约束限制**: 不涉及 **取值范围**： 包含如下7种输入。 - hss.version.null ：无。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。 **默认取值**: 不涉及

        :param version: The version of this ListQuotasDetailRequest.
        :type version: str
        """
        self._version = version

    @property
    def category(self):
        r"""Gets the category of this ListQuotasDetailRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - host_resource ：主机 - container_resource ：容器 **默认取值**: 不涉及

        :return: The category of this ListQuotasDetailRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListQuotasDetailRequest.

        **参数解释**: 类别 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - host_resource ：主机 - container_resource ：容器 **默认取值**: 不涉及

        :param category: The category of this ListQuotasDetailRequest.
        :type category: str
        """
        self._category = category

    @property
    def quota_status(self):
        r"""Gets the quota_status of this ListQuotasDetailRequest.

        **参数解释**: 配额状态 **约束限制**: 不涉及 **取值范围**: 包含如下三种： - normal ： 正常 - expired ：过期 - freeze ：冻结 **默认取值**: 不涉及

        :return: The quota_status of this ListQuotasDetailRequest.
        :rtype: str
        """
        return self._quota_status

    @quota_status.setter
    def quota_status(self, quota_status):
        r"""Sets the quota_status of this ListQuotasDetailRequest.

        **参数解释**: 配额状态 **约束限制**: 不涉及 **取值范围**: 包含如下三种： - normal ： 正常 - expired ：过期 - freeze ：冻结 **默认取值**: 不涉及

        :param quota_status: The quota_status of this ListQuotasDetailRequest.
        :type quota_status: str
        """
        self._quota_status = quota_status

    @property
    def used_status(self):
        r"""Gets the used_status of this ListQuotasDetailRequest.

        **参数解释**: 使用状态 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - idle ：空闲的 - used ：使用中 **默认取值**: 不涉及

        :return: The used_status of this ListQuotasDetailRequest.
        :rtype: str
        """
        return self._used_status

    @used_status.setter
    def used_status(self, used_status):
        r"""Sets the used_status of this ListQuotasDetailRequest.

        **参数解释**: 使用状态 **约束限制**: 不涉及 **取值范围**: 包含如下两种： - idle ：空闲的 - used ：使用中 **默认取值**: 不涉及

        :param used_status: The used_status of this ListQuotasDetailRequest.
        :type used_status: str
        """
        self._used_status = used_status

    @property
    def host_name(self):
        r"""Gets the host_name of this ListQuotasDetailRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The host_name of this ListQuotasDetailRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListQuotasDetailRequest.

        **参数解释**: 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListQuotasDetailRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListQuotasDetailRequest.

        **参数解释** : HSS配额的资源ID **约束限制** : 不涉及 **取值范围** : 字符长度1-128位 **默认取值** : 不涉及 

        :return: The resource_id of this ListQuotasDetailRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListQuotasDetailRequest.

        **参数解释** : HSS配额的资源ID **约束限制** : 不涉及 **取值范围** : 字符长度1-128位 **默认取值** : 不涉及 

        :param resource_id: The resource_id of this ListQuotasDetailRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ListQuotasDetailRequest.

        **参数解释**： 收费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle ：包年/包月。 - on_demand ：按需。 **默认取值**: 不涉及

        :return: The charging_mode of this ListQuotasDetailRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ListQuotasDetailRequest.

        **参数解释**： 收费模式 **约束限制**: 不涉及 **取值范围**: - packet_cycle ：包年/包月。 - on_demand ：按需。 **默认取值**: 不涉及

        :param charging_mode: The charging_mode of this ListQuotasDetailRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def limit(self):
        r"""Gets the limit of this ListQuotasDetailRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListQuotasDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListQuotasDetailRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListQuotasDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListQuotasDetailRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListQuotasDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListQuotasDetailRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListQuotasDetailRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListQuotasDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
