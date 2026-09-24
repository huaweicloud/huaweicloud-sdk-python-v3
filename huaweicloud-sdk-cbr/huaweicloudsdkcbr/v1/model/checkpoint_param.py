# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckpointParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_trigger': 'bool',
        'description': 'str',
        'incremental': 'bool',
        'name': 'str',
        'resources': 'list[str]',
        'resource_details': 'list[Resource]',
        'policy_id': 'str',
        'retention_duration_days': 'int'
    }

    attribute_map = {
        'auto_trigger': 'auto_trigger',
        'description': 'description',
        'incremental': 'incremental',
        'name': 'name',
        'resources': 'resources',
        'resource_details': 'resource_details',
        'policy_id': 'policy_id',
        'retention_duration_days': 'retention_duration_days'
    }

    def __init__(self, auto_trigger=None, description=None, incremental=None, name=None, resources=None, resource_details=None, policy_id=None, retention_duration_days=None):
        r"""CheckpointParam

        The model defined in huaweicloud sdk

        :param auto_trigger: 是否自动触发,true：自动触发，false：非自动触发。
        :type auto_trigger: bool
        :param description: 备份描述
        :type description: str
        :param incremental: 是否增量备份，true：增量备份，false：非增量备份。
        :type incremental: bool
        :param name: 备份名称
        :type name: str
        :param resources: 待备份的资源id列表:uuid
        :type resources: list[str]
        :param resource_details: 资源详情
        :type resource_details: list[:class:`huaweicloudsdkcbr.v1.Resource`]
        :param policy_id: 自动备份时的策略id
        :type policy_id: str
        :param retention_duration_days: **参数解释**： 手动备份的保留时长，单位为天。设置该参数后，备份副本将在保留时长到期后自动删除。用于为手动备份设置自动过期时间，避免手动备份堆积导致存储容量浪费。不设置此参数时，备份将永久保留。 **约束限制**： 当auto_trigger为true时不支持传此参数，自动备份的保留时间由关联的备份策略指定。auto_trigger不传或为false时支持指定此参数。 **取值范围**： -  1~36500：指定保留天数，备份将在创建时间 + 该天数后到期并自动删除。 - -1：永久保留，备份不会自动过期。  **默认取值**： -1 &gt; 该特性目前处于公测阶段，部分Region可能无法使用
        :type retention_duration_days: int
        """
        
        

        self._auto_trigger = None
        self._description = None
        self._incremental = None
        self._name = None
        self._resources = None
        self._resource_details = None
        self._policy_id = None
        self._retention_duration_days = None
        self.discriminator = None

        if auto_trigger is not None:
            self.auto_trigger = auto_trigger
        if description is not None:
            self.description = description
        if incremental is not None:
            self.incremental = incremental
        if name is not None:
            self.name = name
        if resources is not None:
            self.resources = resources
        if resource_details is not None:
            self.resource_details = resource_details
        if policy_id is not None:
            self.policy_id = policy_id
        if retention_duration_days is not None:
            self.retention_duration_days = retention_duration_days

    @property
    def auto_trigger(self):
        r"""Gets the auto_trigger of this CheckpointParam.

        是否自动触发,true：自动触发，false：非自动触发。

        :return: The auto_trigger of this CheckpointParam.
        :rtype: bool
        """
        return self._auto_trigger

    @auto_trigger.setter
    def auto_trigger(self, auto_trigger):
        r"""Sets the auto_trigger of this CheckpointParam.

        是否自动触发,true：自动触发，false：非自动触发。

        :param auto_trigger: The auto_trigger of this CheckpointParam.
        :type auto_trigger: bool
        """
        self._auto_trigger = auto_trigger

    @property
    def description(self):
        r"""Gets the description of this CheckpointParam.

        备份描述

        :return: The description of this CheckpointParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CheckpointParam.

        备份描述

        :param description: The description of this CheckpointParam.
        :type description: str
        """
        self._description = description

    @property
    def incremental(self):
        r"""Gets the incremental of this CheckpointParam.

        是否增量备份，true：增量备份，false：非增量备份。

        :return: The incremental of this CheckpointParam.
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        r"""Sets the incremental of this CheckpointParam.

        是否增量备份，true：增量备份，false：非增量备份。

        :param incremental: The incremental of this CheckpointParam.
        :type incremental: bool
        """
        self._incremental = incremental

    @property
    def name(self):
        r"""Gets the name of this CheckpointParam.

        备份名称

        :return: The name of this CheckpointParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CheckpointParam.

        备份名称

        :param name: The name of this CheckpointParam.
        :type name: str
        """
        self._name = name

    @property
    def resources(self):
        r"""Gets the resources of this CheckpointParam.

        待备份的资源id列表:uuid

        :return: The resources of this CheckpointParam.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this CheckpointParam.

        待备份的资源id列表:uuid

        :param resources: The resources of this CheckpointParam.
        :type resources: list[str]
        """
        self._resources = resources

    @property
    def resource_details(self):
        r"""Gets the resource_details of this CheckpointParam.

        资源详情

        :return: The resource_details of this CheckpointParam.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Resource`]
        """
        return self._resource_details

    @resource_details.setter
    def resource_details(self, resource_details):
        r"""Sets the resource_details of this CheckpointParam.

        资源详情

        :param resource_details: The resource_details of this CheckpointParam.
        :type resource_details: list[:class:`huaweicloudsdkcbr.v1.Resource`]
        """
        self._resource_details = resource_details

    @property
    def policy_id(self):
        r"""Gets the policy_id of this CheckpointParam.

        自动备份时的策略id

        :return: The policy_id of this CheckpointParam.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this CheckpointParam.

        自动备份时的策略id

        :param policy_id: The policy_id of this CheckpointParam.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def retention_duration_days(self):
        r"""Gets the retention_duration_days of this CheckpointParam.

        **参数解释**： 手动备份的保留时长，单位为天。设置该参数后，备份副本将在保留时长到期后自动删除。用于为手动备份设置自动过期时间，避免手动备份堆积导致存储容量浪费。不设置此参数时，备份将永久保留。 **约束限制**： 当auto_trigger为true时不支持传此参数，自动备份的保留时间由关联的备份策略指定。auto_trigger不传或为false时支持指定此参数。 **取值范围**： -  1~36500：指定保留天数，备份将在创建时间 + 该天数后到期并自动删除。 - -1：永久保留，备份不会自动过期。  **默认取值**： -1 > 该特性目前处于公测阶段，部分Region可能无法使用

        :return: The retention_duration_days of this CheckpointParam.
        :rtype: int
        """
        return self._retention_duration_days

    @retention_duration_days.setter
    def retention_duration_days(self, retention_duration_days):
        r"""Sets the retention_duration_days of this CheckpointParam.

        **参数解释**： 手动备份的保留时长，单位为天。设置该参数后，备份副本将在保留时长到期后自动删除。用于为手动备份设置自动过期时间，避免手动备份堆积导致存储容量浪费。不设置此参数时，备份将永久保留。 **约束限制**： 当auto_trigger为true时不支持传此参数，自动备份的保留时间由关联的备份策略指定。auto_trigger不传或为false时支持指定此参数。 **取值范围**： -  1~36500：指定保留天数，备份将在创建时间 + 该天数后到期并自动删除。 - -1：永久保留，备份不会自动过期。  **默认取值**： -1 > 该特性目前处于公测阶段，部分Region可能无法使用

        :param retention_duration_days: The retention_duration_days of this CheckpointParam.
        :type retention_duration_days: int
        """
        self._retention_duration_days = retention_duration_days

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
        if not isinstance(other, CheckpointParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
