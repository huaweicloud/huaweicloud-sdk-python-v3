# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'group_id': 'str',
        'create_time': 'datetime',
        'enterprise_project_id': 'str',
        'type': 'str',
        'association_ep_ids': 'list[str]',
        'tags': 'list[ResourceGroupTagRelation]',
        'instances': 'list[Instance]',
        'comb_relation': 'CombRelation',
        'related_ep_ids': 'list[str]',
        'enterprise_project_id_and_tags': 'list[EnterpriseProjectIdAndTags]',
        'status': 'str',
        'event_status': 'str',
        'resource_statistics': 'OneResourceGroupRespResourceStatistics',
        'resource_level': 'str',
        'product_names': 'str',
        'ep_resource_statistics': 'list[EpResourceStatistics]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'create_time': 'create_time',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'association_ep_ids': 'association_ep_ids',
        'tags': 'tags',
        'instances': 'instances',
        'comb_relation': 'comb_relation',
        'related_ep_ids': 'related_ep_ids',
        'enterprise_project_id_and_tags': 'enterprise_project_id_and_tags',
        'status': 'status',
        'event_status': 'event_status',
        'resource_statistics': 'resource_statistics',
        'resource_level': 'resource_level',
        'product_names': 'product_names',
        'ep_resource_statistics': 'ep_resource_statistics'
    }

    def __init__(self, group_name=None, group_id=None, create_time=None, enterprise_project_id=None, type=None, association_ep_ids=None, tags=None, instances=None, comb_relation=None, related_ep_ids=None, enterprise_project_id_and_tags=None, status=None, event_status=None, resource_statistics=None, resource_level=None, product_names=None, ep_resource_statistics=None):
        r"""ShowResourceGroupResponse

        The model defined in huaweicloud sdk

        :param group_name: 资源分组的名称
        :type group_name: str
        :param group_id: 资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串
        :type group_id: str
        :param create_time: 资源分组的创建时间
        :type create_time: datetime
        :param enterprise_project_id: 资源分组归属企业项目ID
        :type enterprise_project_id: str
        :param type: 资源添加/匹配方式，取值只能为EPS（匹配企业项目）,TAG（匹配标签）,NAME（匹配实例名称）, COMB（组合匹配）,Manual（手动添加）
        :type type: str
        :param association_ep_ids: 该资源分组内包含的资源来源的企业项目ID，type为EPS时必传
        :type association_ep_ids: list[str]
        :param tags: 当资源匹配规则为匹配标签时,所指定的标签规则
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        :param instances: 实例名称匹配参数
        :type instances: list[:class:`huaweicloudsdkces.v2.Instance`]
        :param comb_relation: 
        :type comb_relation: :class:`huaweicloudsdkces.v2.CombRelation`
        :param related_ep_ids: 当资源匹配规则为匹配企业项目时，指定的企业项目列表
        :type related_ep_ids: list[str]
        :param enterprise_project_id_and_tags: 匹配企业项目或匹配标签参数
        :type enterprise_project_id_and_tags: list[:class:`huaweicloudsdkces.v2.EnterpriseProjectIdAndTags`]
        :param status: 指标告警状态，取值为health（告警中）、unhealthy（已触发）、no_alarm_rule（未设置告警规则）
        :type status: str
        :param event_status: 事件告警状态，取值为health（告警中）、unhealthy（已触发）、no_alarm_rule（未设置告警规则）
        :type event_status: str
        :param resource_statistics: 
        :type resource_statistics: :class:`huaweicloudsdkces.v2.OneResourceGroupRespResourceStatistics`
        :param resource_level: dimension: 子维度,product: 云产品
        :type resource_level: str
        :param product_names: 创建资源层级为云产品时的云产品的取值，一般由\&quot;服务命名空间,服务首层维度名称\&quot;组成，如\&quot;SYS.ECS,instance_id\&quot;。多个云产品则用“;”隔开，如\&quot;SERVICE.BMS,instance_id;SYS.ECS,instance_id\&quot;。
        :type product_names: str
        :param ep_resource_statistics: 每个企业项目关联的资源状态
        :type ep_resource_statistics: list[:class:`huaweicloudsdkces.v2.EpResourceStatistics`]
        """
        
        super(ShowResourceGroupResponse, self).__init__()

        self._group_name = None
        self._group_id = None
        self._create_time = None
        self._enterprise_project_id = None
        self._type = None
        self._association_ep_ids = None
        self._tags = None
        self._instances = None
        self._comb_relation = None
        self._related_ep_ids = None
        self._enterprise_project_id_and_tags = None
        self._status = None
        self._event_status = None
        self._resource_statistics = None
        self._resource_level = None
        self._product_names = None
        self._ep_resource_statistics = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if create_time is not None:
            self.create_time = create_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        if association_ep_ids is not None:
            self.association_ep_ids = association_ep_ids
        if tags is not None:
            self.tags = tags
        if instances is not None:
            self.instances = instances
        if comb_relation is not None:
            self.comb_relation = comb_relation
        if related_ep_ids is not None:
            self.related_ep_ids = related_ep_ids
        if enterprise_project_id_and_tags is not None:
            self.enterprise_project_id_and_tags = enterprise_project_id_and_tags
        if status is not None:
            self.status = status
        if event_status is not None:
            self.event_status = event_status
        if resource_statistics is not None:
            self.resource_statistics = resource_statistics
        if resource_level is not None:
            self.resource_level = resource_level
        if product_names is not None:
            self.product_names = product_names
        if ep_resource_statistics is not None:
            self.ep_resource_statistics = ep_resource_statistics

    @property
    def group_name(self):
        r"""Gets the group_name of this ShowResourceGroupResponse.

        资源分组的名称

        :return: The group_name of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ShowResourceGroupResponse.

        资源分组的名称

        :param group_name: The group_name of this ShowResourceGroupResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowResourceGroupResponse.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :return: The group_id of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowResourceGroupResponse.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :param group_id: The group_id of this ShowResourceGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowResourceGroupResponse.

        资源分组的创建时间

        :return: The create_time of this ShowResourceGroupResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowResourceGroupResponse.

        资源分组的创建时间

        :param create_time: The create_time of this ShowResourceGroupResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowResourceGroupResponse.

        资源分组归属企业项目ID

        :return: The enterprise_project_id of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowResourceGroupResponse.

        资源分组归属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowResourceGroupResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ShowResourceGroupResponse.

        资源添加/匹配方式，取值只能为EPS（匹配企业项目）,TAG（匹配标签）,NAME（匹配实例名称）, COMB（组合匹配）,Manual（手动添加）

        :return: The type of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowResourceGroupResponse.

        资源添加/匹配方式，取值只能为EPS（匹配企业项目）,TAG（匹配标签）,NAME（匹配实例名称）, COMB（组合匹配）,Manual（手动添加）

        :param type: The type of this ShowResourceGroupResponse.
        :type type: str
        """
        self._type = type

    @property
    def association_ep_ids(self):
        r"""Gets the association_ep_ids of this ShowResourceGroupResponse.

        该资源分组内包含的资源来源的企业项目ID，type为EPS时必传

        :return: The association_ep_ids of this ShowResourceGroupResponse.
        :rtype: list[str]
        """
        return self._association_ep_ids

    @association_ep_ids.setter
    def association_ep_ids(self, association_ep_ids):
        r"""Sets the association_ep_ids of this ShowResourceGroupResponse.

        该资源分组内包含的资源来源的企业项目ID，type为EPS时必传

        :param association_ep_ids: The association_ep_ids of this ShowResourceGroupResponse.
        :type association_ep_ids: list[str]
        """
        self._association_ep_ids = association_ep_ids

    @property
    def tags(self):
        r"""Gets the tags of this ShowResourceGroupResponse.

        当资源匹配规则为匹配标签时,所指定的标签规则

        :return: The tags of this ShowResourceGroupResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowResourceGroupResponse.

        当资源匹配规则为匹配标签时,所指定的标签规则

        :param tags: The tags of this ShowResourceGroupResponse.
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        self._tags = tags

    @property
    def instances(self):
        r"""Gets the instances of this ShowResourceGroupResponse.

        实例名称匹配参数

        :return: The instances of this ShowResourceGroupResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.Instance`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ShowResourceGroupResponse.

        实例名称匹配参数

        :param instances: The instances of this ShowResourceGroupResponse.
        :type instances: list[:class:`huaweicloudsdkces.v2.Instance`]
        """
        self._instances = instances

    @property
    def comb_relation(self):
        r"""Gets the comb_relation of this ShowResourceGroupResponse.

        :return: The comb_relation of this ShowResourceGroupResponse.
        :rtype: :class:`huaweicloudsdkces.v2.CombRelation`
        """
        return self._comb_relation

    @comb_relation.setter
    def comb_relation(self, comb_relation):
        r"""Sets the comb_relation of this ShowResourceGroupResponse.

        :param comb_relation: The comb_relation of this ShowResourceGroupResponse.
        :type comb_relation: :class:`huaweicloudsdkces.v2.CombRelation`
        """
        self._comb_relation = comb_relation

    @property
    def related_ep_ids(self):
        r"""Gets the related_ep_ids of this ShowResourceGroupResponse.

        当资源匹配规则为匹配企业项目时，指定的企业项目列表

        :return: The related_ep_ids of this ShowResourceGroupResponse.
        :rtype: list[str]
        """
        return self._related_ep_ids

    @related_ep_ids.setter
    def related_ep_ids(self, related_ep_ids):
        r"""Sets the related_ep_ids of this ShowResourceGroupResponse.

        当资源匹配规则为匹配企业项目时，指定的企业项目列表

        :param related_ep_ids: The related_ep_ids of this ShowResourceGroupResponse.
        :type related_ep_ids: list[str]
        """
        self._related_ep_ids = related_ep_ids

    @property
    def enterprise_project_id_and_tags(self):
        r"""Gets the enterprise_project_id_and_tags of this ShowResourceGroupResponse.

        匹配企业项目或匹配标签参数

        :return: The enterprise_project_id_and_tags of this ShowResourceGroupResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.EnterpriseProjectIdAndTags`]
        """
        return self._enterprise_project_id_and_tags

    @enterprise_project_id_and_tags.setter
    def enterprise_project_id_and_tags(self, enterprise_project_id_and_tags):
        r"""Sets the enterprise_project_id_and_tags of this ShowResourceGroupResponse.

        匹配企业项目或匹配标签参数

        :param enterprise_project_id_and_tags: The enterprise_project_id_and_tags of this ShowResourceGroupResponse.
        :type enterprise_project_id_and_tags: list[:class:`huaweicloudsdkces.v2.EnterpriseProjectIdAndTags`]
        """
        self._enterprise_project_id_and_tags = enterprise_project_id_and_tags

    @property
    def status(self):
        r"""Gets the status of this ShowResourceGroupResponse.

        指标告警状态，取值为health（告警中）、unhealthy（已触发）、no_alarm_rule（未设置告警规则）

        :return: The status of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowResourceGroupResponse.

        指标告警状态，取值为health（告警中）、unhealthy（已触发）、no_alarm_rule（未设置告警规则）

        :param status: The status of this ShowResourceGroupResponse.
        :type status: str
        """
        self._status = status

    @property
    def event_status(self):
        r"""Gets the event_status of this ShowResourceGroupResponse.

        事件告警状态，取值为health（告警中）、unhealthy（已触发）、no_alarm_rule（未设置告警规则）

        :return: The event_status of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        r"""Sets the event_status of this ShowResourceGroupResponse.

        事件告警状态，取值为health（告警中）、unhealthy（已触发）、no_alarm_rule（未设置告警规则）

        :param event_status: The event_status of this ShowResourceGroupResponse.
        :type event_status: str
        """
        self._event_status = event_status

    @property
    def resource_statistics(self):
        r"""Gets the resource_statistics of this ShowResourceGroupResponse.

        :return: The resource_statistics of this ShowResourceGroupResponse.
        :rtype: :class:`huaweicloudsdkces.v2.OneResourceGroupRespResourceStatistics`
        """
        return self._resource_statistics

    @resource_statistics.setter
    def resource_statistics(self, resource_statistics):
        r"""Sets the resource_statistics of this ShowResourceGroupResponse.

        :param resource_statistics: The resource_statistics of this ShowResourceGroupResponse.
        :type resource_statistics: :class:`huaweicloudsdkces.v2.OneResourceGroupRespResourceStatistics`
        """
        self._resource_statistics = resource_statistics

    @property
    def resource_level(self):
        r"""Gets the resource_level of this ShowResourceGroupResponse.

        dimension: 子维度,product: 云产品

        :return: The resource_level of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this ShowResourceGroupResponse.

        dimension: 子维度,product: 云产品

        :param resource_level: The resource_level of this ShowResourceGroupResponse.
        :type resource_level: str
        """
        self._resource_level = resource_level

    @property
    def product_names(self):
        r"""Gets the product_names of this ShowResourceGroupResponse.

        创建资源层级为云产品时的云产品的取值，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"。多个云产品则用“;”隔开，如\"SERVICE.BMS,instance_id;SYS.ECS,instance_id\"。

        :return: The product_names of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._product_names

    @product_names.setter
    def product_names(self, product_names):
        r"""Sets the product_names of this ShowResourceGroupResponse.

        创建资源层级为云产品时的云产品的取值，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"。多个云产品则用“;”隔开，如\"SERVICE.BMS,instance_id;SYS.ECS,instance_id\"。

        :param product_names: The product_names of this ShowResourceGroupResponse.
        :type product_names: str
        """
        self._product_names = product_names

    @property
    def ep_resource_statistics(self):
        r"""Gets the ep_resource_statistics of this ShowResourceGroupResponse.

        每个企业项目关联的资源状态

        :return: The ep_resource_statistics of this ShowResourceGroupResponse.
        :rtype: list[:class:`huaweicloudsdkces.v2.EpResourceStatistics`]
        """
        return self._ep_resource_statistics

    @ep_resource_statistics.setter
    def ep_resource_statistics(self, ep_resource_statistics):
        r"""Sets the ep_resource_statistics of this ShowResourceGroupResponse.

        每个企业项目关联的资源状态

        :param ep_resource_statistics: The ep_resource_statistics of this ShowResourceGroupResponse.
        :type ep_resource_statistics: list[:class:`huaweicloudsdkces.v2.EpResourceStatistics`]
        """
        self._ep_resource_statistics = ep_resource_statistics

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
        if not isinstance(other, ShowResourceGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
