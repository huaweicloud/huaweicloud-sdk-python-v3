# coding: utf-8

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
        'resources': 'list[ResourceGroup]',
        'status': 'str',
        'create_time': 'int',
        'meta_data': 'MetaData',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'resources': 'resources',
        'status': 'status',
        'create_time': 'create_time',
        'meta_data': 'meta_data',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, group_name=None, group_id=None, resources=None, status=None, create_time=None, meta_data=None, enterprise_project_id=None):
        r"""ShowResourceGroupResponse

        The model defined in huaweicloud sdk

        :param group_name: **参数解释** 资源分组的名称 **约束限制** 不涉及 **取值范围** 只能为字母、数字、汉字、-或_，长度为[1,128]个字符 **默认取值** 不涉及 
        :type group_name: str
        :param group_id: **参数解释**： 资源分组ID     **约束限制**： 不涉及。  **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串。长度为[2,24]个字符。       **默认取值**： 不涉及。 
        :type group_id: str
        :param resources: **参数解释** 创建的资源分组选择一个或者多个资源。 **约束限制** 不超过1000个资源。 
        :type resources: list[:class:`huaweicloudsdkces.v1.ResourceGroup`]
        :param status: **参数解释** 资源分组健康状态 **约束限制** 不涉及 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及 
        :type status: str
        :param create_time: **参数解释**： 资源分组的创建时间，UNIX时间戳，单位毫秒；如：1603819753000。     **约束限制**： 不涉及。  **取值范围**： 在[1,9223372036854775807]区间内 **默认取值**： 不涉及。 
        :type create_time: int
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkces.v1.MetaData`
        :param enterprise_project_id: **参数解释**： 创建资源分组时关联的企业项目，默认值为0，表示企业项目为default。     **约束限制**： 不涉及。  **取值范围**： 由数字、字母和-组成，或者为0（默认企业项目ID）。 **默认取值**： 不涉及。 
        :type enterprise_project_id: str
        """
        
        super().__init__()

        self._group_name = None
        self._group_id = None
        self._resources = None
        self._status = None
        self._create_time = None
        self._meta_data = None
        self._enterprise_project_id = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if resources is not None:
            self.resources = resources
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if meta_data is not None:
            self.meta_data = meta_data
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ShowResourceGroupResponse.

        **参数解释** 资源分组的名称 **约束限制** 不涉及 **取值范围** 只能为字母、数字、汉字、-或_，长度为[1,128]个字符 **默认取值** 不涉及 

        :return: The group_name of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ShowResourceGroupResponse.

        **参数解释** 资源分组的名称 **约束限制** 不涉及 **取值范围** 只能为字母、数字、汉字、-或_，长度为[1,128]个字符 **默认取值** 不涉及 

        :param group_name: The group_name of this ShowResourceGroupResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowResourceGroupResponse.

        **参数解释**： 资源分组ID     **约束限制**： 不涉及。  **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串。长度为[2,24]个字符。       **默认取值**： 不涉及。 

        :return: The group_id of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowResourceGroupResponse.

        **参数解释**： 资源分组ID     **约束限制**： 不涉及。  **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串。长度为[2,24]个字符。       **默认取值**： 不涉及。 

        :param group_id: The group_id of this ShowResourceGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def resources(self):
        r"""Gets the resources of this ShowResourceGroupResponse.

        **参数解释** 创建的资源分组选择一个或者多个资源。 **约束限制** 不超过1000个资源。 

        :return: The resources of this ShowResourceGroupResponse.
        :rtype: list[:class:`huaweicloudsdkces.v1.ResourceGroup`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ShowResourceGroupResponse.

        **参数解释** 创建的资源分组选择一个或者多个资源。 **约束限制** 不超过1000个资源。 

        :param resources: The resources of this ShowResourceGroupResponse.
        :type resources: list[:class:`huaweicloudsdkces.v1.ResourceGroup`]
        """
        self._resources = resources

    @property
    def status(self):
        r"""Gets the status of this ShowResourceGroupResponse.

        **参数解释** 资源分组健康状态 **约束限制** 不涉及 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及 

        :return: The status of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowResourceGroupResponse.

        **参数解释** 资源分组健康状态 **约束限制** 不涉及 **取值范围** - health: 表示健康 - unhealth: 表示不健康 - no_alarm_rule: 表示未配置告警规则 **默认取值** 不涉及 

        :param status: The status of this ShowResourceGroupResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowResourceGroupResponse.

        **参数解释**： 资源分组的创建时间，UNIX时间戳，单位毫秒；如：1603819753000。     **约束限制**： 不涉及。  **取值范围**： 在[1,9223372036854775807]区间内 **默认取值**： 不涉及。 

        :return: The create_time of this ShowResourceGroupResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowResourceGroupResponse.

        **参数解释**： 资源分组的创建时间，UNIX时间戳，单位毫秒；如：1603819753000。     **约束限制**： 不涉及。  **取值范围**： 在[1,9223372036854775807]区间内 **默认取值**： 不涉及。 

        :param create_time: The create_time of this ShowResourceGroupResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def meta_data(self):
        r"""Gets the meta_data of this ShowResourceGroupResponse.

        :return: The meta_data of this ShowResourceGroupResponse.
        :rtype: :class:`huaweicloudsdkces.v1.MetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        r"""Sets the meta_data of this ShowResourceGroupResponse.

        :param meta_data: The meta_data of this ShowResourceGroupResponse.
        :type meta_data: :class:`huaweicloudsdkces.v1.MetaData`
        """
        self._meta_data = meta_data

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowResourceGroupResponse.

        **参数解释**： 创建资源分组时关联的企业项目，默认值为0，表示企业项目为default。     **约束限制**： 不涉及。  **取值范围**： 由数字、字母和-组成，或者为0（默认企业项目ID）。 **默认取值**： 不涉及。 

        :return: The enterprise_project_id of this ShowResourceGroupResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowResourceGroupResponse.

        **参数解释**： 创建资源分组时关联的企业项目，默认值为0，表示企业项目为default。     **约束限制**： 不涉及。  **取值范围**： 由数字、字母和-组成，或者为0（默认企业项目ID）。 **默认取值**： 不涉及。 

        :param enterprise_project_id: The enterprise_project_id of this ShowResourceGroupResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowResourceGroupResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowResourceGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
