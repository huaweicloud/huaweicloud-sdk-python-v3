# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateApplicationViewRequestBodyGroupList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'region_id': 'str',
        'cmdb_resource_id_list': 'list[str]',
        'parent_name': 'str',
        'sync_mode': 'str',
        'sync_rules': 'list[BatchCreateApplicationViewRequestBodySyncRules]',
        'application_name': 'str',
        'component_name': 'str',
        'vendor': 'str',
        'relation_configurations': 'list[GroupRelationConfiguration]',
        'related_domain_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'region_id': 'region_id',
        'cmdb_resource_id_list': 'cmdb_resource_id_list',
        'parent_name': 'parent_name',
        'sync_mode': 'sync_mode',
        'sync_rules': 'sync_rules',
        'application_name': 'application_name',
        'component_name': 'component_name',
        'vendor': 'vendor',
        'relation_configurations': 'relation_configurations',
        'related_domain_id': 'related_domain_id'
    }

    def __init__(self, name=None, region_id=None, cmdb_resource_id_list=None, parent_name=None, sync_mode=None, sync_rules=None, application_name=None, component_name=None, vendor=None, relation_configurations=None, related_domain_id=None):
        r"""BatchCreateApplicationViewRequestBodyGroupList

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 分组名称。 **约束限制：** 不涉及。 **取值范围：** 由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。
        :type name: str
        :param region_id: **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type region_id: str
        :param cmdb_resource_id_list: **参数解释：** 关联的资源id列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type cmdb_resource_id_list: list[str]
        :param parent_name: **参数解释：** 父节点名称。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度3到50个字符。 **默认取值：** 不涉及。
        :type parent_name: str
        :param sync_mode: **参数解释：** 同步模式。 **约束限制：** 不涉及。 **取值范围：** - MANUAL：表示手动关联：用户在对应分组下，手动将对应资源数据关联至分组内进行管理。 - AUTO：表示智能关联：用户通过企业项目和标签的形式，将企业项目下的相同标签资源创建至同一资源分组。 **默认取值：** 不涉及。
        :type sync_mode: str
        :param sync_rules: **参数解释：** 智能关联规则。 **约束限制：** 不涉及。 **取值范围：** 智能关联已选择的企业项目和对应标签的现存及未来创建的资源。 **默认取值：** 不涉及。
        :type sync_rules: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodySyncRules`]
        :param application_name: **参数解释：** 分组关联的应用名称。 **约束限制：** 不涉及。 **取值范围：**  由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。
        :type application_name: str
        :param component_name: **参数解释：** 分组关联的组件名称。 **约束限制：** 不涉及。 **取值范围：**  由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。
        :type component_name: str
        :param vendor: **参数解释：** 云广商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。
        :type vendor: str
        :param relation_configurations: **参数解释：** 分组配置信息。 **约束限制：** 不涉及。 **取值范围：** 分组的关联配置信息，比如对应的APM的配置信息。 **默认取值：** 不涉及。
        :type relation_configurations: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        :param related_domain_id: **参数解释：** 关联的租户id。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度32个字符。 **默认取值：** 不涉及。
        :type related_domain_id: str
        """
        
        

        self._name = None
        self._region_id = None
        self._cmdb_resource_id_list = None
        self._parent_name = None
        self._sync_mode = None
        self._sync_rules = None
        self._application_name = None
        self._component_name = None
        self._vendor = None
        self._relation_configurations = None
        self._related_domain_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id
        if cmdb_resource_id_list is not None:
            self.cmdb_resource_id_list = cmdb_resource_id_list
        if parent_name is not None:
            self.parent_name = parent_name
        if sync_mode is not None:
            self.sync_mode = sync_mode
        if sync_rules is not None:
            self.sync_rules = sync_rules
        if application_name is not None:
            self.application_name = application_name
        if component_name is not None:
            self.component_name = component_name
        if vendor is not None:
            self.vendor = vendor
        if relation_configurations is not None:
            self.relation_configurations = relation_configurations
        if related_domain_id is not None:
            self.related_domain_id = related_domain_id

    @property
    def name(self):
        r"""Gets the name of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 分组名称。 **约束限制：** 不涉及。 **取值范围：** 由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。

        :return: The name of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 分组名称。 **约束限制：** 不涉及。 **取值范围：** 由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。

        :param name: The name of this BatchCreateApplicationViewRequestBodyGroupList.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The region_id of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param region_id: The region_id of this BatchCreateApplicationViewRequestBodyGroupList.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def cmdb_resource_id_list(self):
        r"""Gets the cmdb_resource_id_list of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 关联的资源id列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The cmdb_resource_id_list of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: list[str]
        """
        return self._cmdb_resource_id_list

    @cmdb_resource_id_list.setter
    def cmdb_resource_id_list(self, cmdb_resource_id_list):
        r"""Sets the cmdb_resource_id_list of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 关联的资源id列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param cmdb_resource_id_list: The cmdb_resource_id_list of this BatchCreateApplicationViewRequestBodyGroupList.
        :type cmdb_resource_id_list: list[str]
        """
        self._cmdb_resource_id_list = cmdb_resource_id_list

    @property
    def parent_name(self):
        r"""Gets the parent_name of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 父节点名称。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度3到50个字符。 **默认取值：** 不涉及。

        :return: The parent_name of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        r"""Sets the parent_name of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 父节点名称。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度3到50个字符。 **默认取值：** 不涉及。

        :param parent_name: The parent_name of this BatchCreateApplicationViewRequestBodyGroupList.
        :type parent_name: str
        """
        self._parent_name = parent_name

    @property
    def sync_mode(self):
        r"""Gets the sync_mode of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 同步模式。 **约束限制：** 不涉及。 **取值范围：** - MANUAL：表示手动关联：用户在对应分组下，手动将对应资源数据关联至分组内进行管理。 - AUTO：表示智能关联：用户通过企业项目和标签的形式，将企业项目下的相同标签资源创建至同一资源分组。 **默认取值：** 不涉及。

        :return: The sync_mode of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, sync_mode):
        r"""Sets the sync_mode of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 同步模式。 **约束限制：** 不涉及。 **取值范围：** - MANUAL：表示手动关联：用户在对应分组下，手动将对应资源数据关联至分组内进行管理。 - AUTO：表示智能关联：用户通过企业项目和标签的形式，将企业项目下的相同标签资源创建至同一资源分组。 **默认取值：** 不涉及。

        :param sync_mode: The sync_mode of this BatchCreateApplicationViewRequestBodyGroupList.
        :type sync_mode: str
        """
        self._sync_mode = sync_mode

    @property
    def sync_rules(self):
        r"""Gets the sync_rules of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 智能关联规则。 **约束限制：** 不涉及。 **取值范围：** 智能关联已选择的企业项目和对应标签的现存及未来创建的资源。 **默认取值：** 不涉及。

        :return: The sync_rules of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodySyncRules`]
        """
        return self._sync_rules

    @sync_rules.setter
    def sync_rules(self, sync_rules):
        r"""Sets the sync_rules of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 智能关联规则。 **约束限制：** 不涉及。 **取值范围：** 智能关联已选择的企业项目和对应标签的现存及未来创建的资源。 **默认取值：** 不涉及。

        :param sync_rules: The sync_rules of this BatchCreateApplicationViewRequestBodyGroupList.
        :type sync_rules: list[:class:`huaweicloudsdkcoc.v1.BatchCreateApplicationViewRequestBodySyncRules`]
        """
        self._sync_rules = sync_rules

    @property
    def application_name(self):
        r"""Gets the application_name of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 分组关联的应用名称。 **约束限制：** 不涉及。 **取值范围：**  由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。

        :return: The application_name of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 分组关联的应用名称。 **约束限制：** 不涉及。 **取值范围：**  由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。

        :param application_name: The application_name of this BatchCreateApplicationViewRequestBodyGroupList.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def component_name(self):
        r"""Gets the component_name of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 分组关联的组件名称。 **约束限制：** 不涉及。 **取值范围：**  由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。

        :return: The component_name of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 分组关联的组件名称。 **约束限制：** 不涉及。 **取值范围：**  由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。

        :param component_name: The component_name of this BatchCreateApplicationViewRequestBodyGroupList.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def vendor(self):
        r"""Gets the vendor of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 云广商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。

        :return: The vendor of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 云广商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS： 华为云。 - AWS：亚马逊。 - AZURE：微软。 - ALI：阿里云。 - VMWARE：VMware。 - OPENSTACK：openstack云平台。 - HCS：Huawei Cloud Stack。 - OTHER：其他云广商。 **默认取值：** 不涉及。

        :param vendor: The vendor of this BatchCreateApplicationViewRequestBodyGroupList.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def relation_configurations(self):
        r"""Gets the relation_configurations of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 分组配置信息。 **约束限制：** 不涉及。 **取值范围：** 分组的关联配置信息，比如对应的APM的配置信息。 **默认取值：** 不涉及。

        :return: The relation_configurations of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        return self._relation_configurations

    @relation_configurations.setter
    def relation_configurations(self, relation_configurations):
        r"""Sets the relation_configurations of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 分组配置信息。 **约束限制：** 不涉及。 **取值范围：** 分组的关联配置信息，比如对应的APM的配置信息。 **默认取值：** 不涉及。

        :param relation_configurations: The relation_configurations of this BatchCreateApplicationViewRequestBodyGroupList.
        :type relation_configurations: list[:class:`huaweicloudsdkcoc.v1.GroupRelationConfiguration`]
        """
        self._relation_configurations = relation_configurations

    @property
    def related_domain_id(self):
        r"""Gets the related_domain_id of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 关联的租户id。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度32个字符。 **默认取值：** 不涉及。

        :return: The related_domain_id of this BatchCreateApplicationViewRequestBodyGroupList.
        :rtype: str
        """
        return self._related_domain_id

    @related_domain_id.setter
    def related_domain_id(self, related_domain_id):
        r"""Sets the related_domain_id of this BatchCreateApplicationViewRequestBodyGroupList.

        **参数解释：** 关联的租户id。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度32个字符。 **默认取值：** 不涉及。

        :param related_domain_id: The related_domain_id of this BatchCreateApplicationViewRequestBodyGroupList.
        :type related_domain_id: str
        """
        self._related_domain_id = related_domain_id

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
        if not isinstance(other, BatchCreateApplicationViewRequestBodyGroupList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
