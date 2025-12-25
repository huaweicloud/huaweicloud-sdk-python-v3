# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceGroupInfo:

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
        'type': 'str',
        'relation_ids': 'list[str]',
        'group_id': 'str',
        'create_time': 'int',
        'instance_statistics': 'InstanceStatistics',
        'status': 'str',
        'enterprise_project_id': 'str',
        'resources': 'list[Resource]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'type': 'type',
        'relation_ids': 'relation_ids',
        'group_id': 'group_id',
        'create_time': 'create_time',
        'instance_statistics': 'instance_statistics',
        'status': 'status',
        'enterprise_project_id': 'enterprise_project_id',
        'resources': 'resources'
    }

    def __init__(self, group_name=None, type=None, relation_ids=None, group_id=None, create_time=None, instance_statistics=None, status=None, enterprise_project_id=None, resources=None):
        r"""ResourceGroupInfo

        The model defined in huaweicloud sdk

        :param group_name: **参数解释** 资源分组名称。 **取值范围** 包含字母、数字、_、-或汉字，长度为[1,128]个字符。
        :type group_name: str
        :param type: **参数解释** 资源添加/匹配方式。 **取值范围** 取值只能为EPS（匹配企业项目），TAG（匹配标签），NAME（匹配实例名称），COMB（组合匹配），Manual/空值（手动添加）。
        :type type: str
        :param relation_ids: **参数解释** 企业项目ID列表。
        :type relation_ids: list[str]
        :param group_id: **参数解释**： 资源分组ID。  **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串。长度为[2,24]个字符。
        :type group_id: str
        :param create_time: **参数解释** 资源分组的创建时间，UNIX时间戳，单位毫秒；如：1603819753000。 **取值范围** 在[0,9223372036854775807]区间内
        :type create_time: int
        :param instance_statistics: 
        :type instance_statistics: :class:`huaweicloudsdkces.v1.InstanceStatistics`
        :param status: **参数解释** 资源分组健康状态 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 
        :type status: str
        :param enterprise_project_id: **参数解释** 资源分组归属企业项目ID。 **取值范围** 由数字、字母和-组成，或者为0（默认企业项目ID）。
        :type enterprise_project_id: str
        :param resources: **参数解释** 一组或者多个资源信息，默认为空。
        :type resources: list[:class:`huaweicloudsdkces.v1.Resource`]
        """
        
        

        self._group_name = None
        self._type = None
        self._relation_ids = None
        self._group_id = None
        self._create_time = None
        self._instance_statistics = None
        self._status = None
        self._enterprise_project_id = None
        self._resources = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if type is not None:
            self.type = type
        if relation_ids is not None:
            self.relation_ids = relation_ids
        if group_id is not None:
            self.group_id = group_id
        if create_time is not None:
            self.create_time = create_time
        if instance_statistics is not None:
            self.instance_statistics = instance_statistics
        if status is not None:
            self.status = status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if resources is not None:
            self.resources = resources

    @property
    def group_name(self):
        r"""Gets the group_name of this ResourceGroupInfo.

        **参数解释** 资源分组名称。 **取值范围** 包含字母、数字、_、-或汉字，长度为[1,128]个字符。

        :return: The group_name of this ResourceGroupInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ResourceGroupInfo.

        **参数解释** 资源分组名称。 **取值范围** 包含字母、数字、_、-或汉字，长度为[1,128]个字符。

        :param group_name: The group_name of this ResourceGroupInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def type(self):
        r"""Gets the type of this ResourceGroupInfo.

        **参数解释** 资源添加/匹配方式。 **取值范围** 取值只能为EPS（匹配企业项目），TAG（匹配标签），NAME（匹配实例名称），COMB（组合匹配），Manual/空值（手动添加）。

        :return: The type of this ResourceGroupInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceGroupInfo.

        **参数解释** 资源添加/匹配方式。 **取值范围** 取值只能为EPS（匹配企业项目），TAG（匹配标签），NAME（匹配实例名称），COMB（组合匹配），Manual/空值（手动添加）。

        :param type: The type of this ResourceGroupInfo.
        :type type: str
        """
        self._type = type

    @property
    def relation_ids(self):
        r"""Gets the relation_ids of this ResourceGroupInfo.

        **参数解释** 企业项目ID列表。

        :return: The relation_ids of this ResourceGroupInfo.
        :rtype: list[str]
        """
        return self._relation_ids

    @relation_ids.setter
    def relation_ids(self, relation_ids):
        r"""Sets the relation_ids of this ResourceGroupInfo.

        **参数解释** 企业项目ID列表。

        :param relation_ids: The relation_ids of this ResourceGroupInfo.
        :type relation_ids: list[str]
        """
        self._relation_ids = relation_ids

    @property
    def group_id(self):
        r"""Gets the group_id of this ResourceGroupInfo.

        **参数解释**： 资源分组ID。  **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串。长度为[2,24]个字符。

        :return: The group_id of this ResourceGroupInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ResourceGroupInfo.

        **参数解释**： 资源分组ID。  **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串。长度为[2,24]个字符。

        :param group_id: The group_id of this ResourceGroupInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ResourceGroupInfo.

        **参数解释** 资源分组的创建时间，UNIX时间戳，单位毫秒；如：1603819753000。 **取值范围** 在[0,9223372036854775807]区间内

        :return: The create_time of this ResourceGroupInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ResourceGroupInfo.

        **参数解释** 资源分组的创建时间，UNIX时间戳，单位毫秒；如：1603819753000。 **取值范围** 在[0,9223372036854775807]区间内

        :param create_time: The create_time of this ResourceGroupInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def instance_statistics(self):
        r"""Gets the instance_statistics of this ResourceGroupInfo.

        :return: The instance_statistics of this ResourceGroupInfo.
        :rtype: :class:`huaweicloudsdkces.v1.InstanceStatistics`
        """
        return self._instance_statistics

    @instance_statistics.setter
    def instance_statistics(self, instance_statistics):
        r"""Sets the instance_statistics of this ResourceGroupInfo.

        :param instance_statistics: The instance_statistics of this ResourceGroupInfo.
        :type instance_statistics: :class:`huaweicloudsdkces.v1.InstanceStatistics`
        """
        self._instance_statistics = instance_statistics

    @property
    def status(self):
        r"""Gets the status of this ResourceGroupInfo.

        **参数解释** 资源分组健康状态 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 

        :return: The status of this ResourceGroupInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResourceGroupInfo.

        **参数解释** 资源分组健康状态 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 

        :param status: The status of this ResourceGroupInfo.
        :type status: str
        """
        self._status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ResourceGroupInfo.

        **参数解释** 资源分组归属企业项目ID。 **取值范围** 由数字、字母和-组成，或者为0（默认企业项目ID）。

        :return: The enterprise_project_id of this ResourceGroupInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ResourceGroupInfo.

        **参数解释** 资源分组归属企业项目ID。 **取值范围** 由数字、字母和-组成，或者为0（默认企业项目ID）。

        :param enterprise_project_id: The enterprise_project_id of this ResourceGroupInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def resources(self):
        r"""Gets the resources of this ResourceGroupInfo.

        **参数解释** 一组或者多个资源信息，默认为空。

        :return: The resources of this ResourceGroupInfo.
        :rtype: list[:class:`huaweicloudsdkces.v1.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ResourceGroupInfo.

        **参数解释** 一组或者多个资源信息，默认为空。

        :param resources: The resources of this ResourceGroupInfo.
        :type resources: list[:class:`huaweicloudsdkces.v1.Resource`]
        """
        self._resources = resources

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
