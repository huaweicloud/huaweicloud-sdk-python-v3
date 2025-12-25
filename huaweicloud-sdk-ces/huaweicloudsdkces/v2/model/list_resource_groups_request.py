# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'group_name': 'str',
        'group_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'group_name': 'group_name',
        'group_id': 'group_id',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'status': 'status'
    }

    def __init__(self, enterprise_project_id=None, group_name=None, group_id=None, offset=None, limit=None, type=None, status=None):
        r"""ListResourceGroupsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 归属企业项目ID。 **约束限制**: 不涉及。 **取值范围**: 只能包含小写字母、数字、“-”、“_”，长度为36个字符。或者为0（代表默认企业项目ID），或者为all_granted_eps（代表所有企业项目ID）。 **默认取值**: 不涉及。
        :type enterprise_project_id: str
        :param group_name: **参数解释** 资源分组名称，支持模糊查询。 **约束限制** 不涉及。 **取值范围** 包含字母、数字、_、-或汉字，长度为[1,128]个字符。 **默认取值** 不涉及。
        :type group_name: str
        :param group_id: **参数解释** 资源分组ID。 **约束限制** 不涉及。 **取值范围** 以\&quot;rg\&quot;开头，后跟22位由字母或数字组成的字符串。 **默认取值** 不涉及。
        :type group_id: str
        :param offset: **参数解释** 分页起始值。 **约束限制** 不涉及。 **取值范围** 在[0,10000]区间内。 **默认取值** 0
        :type offset: int
        :param limit: **参数解释** 分页查询时每页的条目数。 **约束限制** 不涉及。 **取值范围** 在[1,100]区间内。 **默认取值** 100
        :type limit: int
        :param type: **参数解释** 资源分组添加资源方式，不传代表查询所有资源分组类型。 **约束限制** 不涉及。 **取值范围** - EPS: 表示匹配企业项目 - TAG: 表示匹配标签 - Manual: 表示手动添加 - COMB: 表示组合匹配 - NAME: 表示匹配实例名称 **默认取值** 不涉及。
        :type type: str
        :param status: **参数解释** 资源分组健康状态。 **约束限制** 不涉及。 **取值范围** - health: 表示健康 - unhealthy: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及。
        :type status: str
        """
        
        

        self._enterprise_project_id = None
        self._group_name = None
        self._group_id = None
        self._offset = None
        self._limit = None
        self._type = None
        self._status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListResourceGroupsRequest.

        **参数解释**: 归属企业项目ID。 **约束限制**: 不涉及。 **取值范围**: 只能包含小写字母、数字、“-”、“_”，长度为36个字符。或者为0（代表默认企业项目ID），或者为all_granted_eps（代表所有企业项目ID）。 **默认取值**: 不涉及。

        :return: The enterprise_project_id of this ListResourceGroupsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListResourceGroupsRequest.

        **参数解释**: 归属企业项目ID。 **约束限制**: 不涉及。 **取值范围**: 只能包含小写字母、数字、“-”、“_”，长度为36个字符。或者为0（代表默认企业项目ID），或者为all_granted_eps（代表所有企业项目ID）。 **默认取值**: 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this ListResourceGroupsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ListResourceGroupsRequest.

        **参数解释** 资源分组名称，支持模糊查询。 **约束限制** 不涉及。 **取值范围** 包含字母、数字、_、-或汉字，长度为[1,128]个字符。 **默认取值** 不涉及。

        :return: The group_name of this ListResourceGroupsRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ListResourceGroupsRequest.

        **参数解释** 资源分组名称，支持模糊查询。 **约束限制** 不涉及。 **取值范围** 包含字母、数字、_、-或汉字，长度为[1,128]个字符。 **默认取值** 不涉及。

        :param group_name: The group_name of this ListResourceGroupsRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        r"""Gets the group_id of this ListResourceGroupsRequest.

        **参数解释** 资源分组ID。 **约束限制** 不涉及。 **取值范围** 以\"rg\"开头，后跟22位由字母或数字组成的字符串。 **默认取值** 不涉及。

        :return: The group_id of this ListResourceGroupsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListResourceGroupsRequest.

        **参数解释** 资源分组ID。 **约束限制** 不涉及。 **取值范围** 以\"rg\"开头，后跟22位由字母或数字组成的字符串。 **默认取值** 不涉及。

        :param group_id: The group_id of this ListResourceGroupsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def offset(self):
        r"""Gets the offset of this ListResourceGroupsRequest.

        **参数解释** 分页起始值。 **约束限制** 不涉及。 **取值范围** 在[0,10000]区间内。 **默认取值** 0

        :return: The offset of this ListResourceGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListResourceGroupsRequest.

        **参数解释** 分页起始值。 **约束限制** 不涉及。 **取值范围** 在[0,10000]区间内。 **默认取值** 0

        :param offset: The offset of this ListResourceGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListResourceGroupsRequest.

        **参数解释** 分页查询时每页的条目数。 **约束限制** 不涉及。 **取值范围** 在[1,100]区间内。 **默认取值** 100

        :return: The limit of this ListResourceGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourceGroupsRequest.

        **参数解释** 分页查询时每页的条目数。 **约束限制** 不涉及。 **取值范围** 在[1,100]区间内。 **默认取值** 100

        :param limit: The limit of this ListResourceGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        r"""Gets the type of this ListResourceGroupsRequest.

        **参数解释** 资源分组添加资源方式，不传代表查询所有资源分组类型。 **约束限制** 不涉及。 **取值范围** - EPS: 表示匹配企业项目 - TAG: 表示匹配标签 - Manual: 表示手动添加 - COMB: 表示组合匹配 - NAME: 表示匹配实例名称 **默认取值** 不涉及。

        :return: The type of this ListResourceGroupsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListResourceGroupsRequest.

        **参数解释** 资源分组添加资源方式，不传代表查询所有资源分组类型。 **约束限制** 不涉及。 **取值范围** - EPS: 表示匹配企业项目 - TAG: 表示匹配标签 - Manual: 表示手动添加 - COMB: 表示组合匹配 - NAME: 表示匹配实例名称 **默认取值** 不涉及。

        :param type: The type of this ListResourceGroupsRequest.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ListResourceGroupsRequest.

        **参数解释** 资源分组健康状态。 **约束限制** 不涉及。 **取值范围** - health: 表示健康 - unhealthy: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及。

        :return: The status of this ListResourceGroupsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListResourceGroupsRequest.

        **参数解释** 资源分组健康状态。 **约束限制** 不涉及。 **取值范围** - health: 表示健康 - unhealthy: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及。

        :param status: The status of this ListResourceGroupsRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListResourceGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
