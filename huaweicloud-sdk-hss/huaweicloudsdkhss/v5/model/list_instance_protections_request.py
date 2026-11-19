# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceProtectionsRequest:

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
        'type': 'str',
        'instance_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, type=None, instance_id=None, limit=None, offset=None):
        r"""ListInstanceProtectionsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param type: **参数解释**： 列表展示维度 **约束限制**： 不涉及 **取值范围**： - instance：实例维度。 - deployment：无状态负载维度。 - stateful：有状态负载维度。 - cronjob：定时任务维度。 - job：普通任务维度。 - cluster：集群维度。  **默认取值**： instance 
        :type type: str
        :param instance_id: **参数解释**： 实例ID，type类型为instance时，传入实例ID **约束限制**： type值为instance，传入实例ID。 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 
        :type instance_id: str
        :param limit: **参数解释**： 每页显示数量，默认10 **约束限制**： 不涉及 **取值范围**： 整数取值[10,200]  **默认取值**： 10 
        :type limit: int
        :param offset: **参数解释**： 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0 **约束限制**： 不涉及 **取值范围**： 取值[0,2000000]  **默认取值**： 0 
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._type = None
        self._instance_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.type = type
        if instance_id is not None:
            self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListInstanceProtectionsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListInstanceProtectionsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListInstanceProtectionsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListInstanceProtectionsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ListInstanceProtectionsRequest.

        **参数解释**： 列表展示维度 **约束限制**： 不涉及 **取值范围**： - instance：实例维度。 - deployment：无状态负载维度。 - stateful：有状态负载维度。 - cronjob：定时任务维度。 - job：普通任务维度。 - cluster：集群维度。  **默认取值**： instance 

        :return: The type of this ListInstanceProtectionsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListInstanceProtectionsRequest.

        **参数解释**： 列表展示维度 **约束限制**： 不涉及 **取值范围**： - instance：实例维度。 - deployment：无状态负载维度。 - stateful：有状态负载维度。 - cronjob：定时任务维度。 - job：普通任务维度。 - cluster：集群维度。  **默认取值**： instance 

        :param type: The type of this ListInstanceProtectionsRequest.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceProtectionsRequest.

        **参数解释**： 实例ID，type类型为instance时，传入实例ID **约束限制**： type值为instance，传入实例ID。 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :return: The instance_id of this ListInstanceProtectionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceProtectionsRequest.

        **参数解释**： 实例ID，type类型为instance时，传入实例ID **约束限制**： type值为instance，传入实例ID。 **取值范围**： 字符长度1-256位  **默认取值**： 不涉及 

        :param instance_id: The instance_id of this ListInstanceProtectionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceProtectionsRequest.

        **参数解释**： 每页显示数量，默认10 **约束限制**： 不涉及 **取值范围**： 整数取值[10,200]  **默认取值**： 10 

        :return: The limit of this ListInstanceProtectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceProtectionsRequest.

        **参数解释**： 每页显示数量，默认10 **约束限制**： 不涉及 **取值范围**： 整数取值[10,200]  **默认取值**： 10 

        :param limit: The limit of this ListInstanceProtectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceProtectionsRequest.

        **参数解释**： 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0 **约束限制**： 不涉及 **取值范围**： 取值[0,2000000]  **默认取值**： 0 

        :return: The offset of this ListInstanceProtectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceProtectionsRequest.

        **参数解释**： 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0 **约束限制**： 不涉及 **取值范围**： 取值[0,2000000]  **默认取值**： 0 

        :param offset: The offset of this ListInstanceProtectionsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListInstanceProtectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
