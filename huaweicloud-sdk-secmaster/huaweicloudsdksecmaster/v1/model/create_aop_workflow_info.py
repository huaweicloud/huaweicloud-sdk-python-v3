# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAopWorkflowInfo:

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
        'description': 'str',
        'engine_type': 'str',
        'aop_type': 'str',
        'dataclass_id': 'str',
        'labels': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'engine_type': 'engine_type',
        'aop_type': 'aop_type',
        'dataclass_id': 'dataclass_id',
        'labels': 'labels'
    }

    def __init__(self, name=None, description=None, engine_type=None, aop_type=None, dataclass_id=None, labels=None):
        r"""CreateAopWorkflowInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type name: str
        :param description: **参数解释**: 流程的描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type description: str
        :param engine_type: **参数解释**: 引擎的类型 - public_engine 共享版  **约束限制**: 不涉及         **取值范围**: - public_engine  **默认值**:  不涉及
        :type engine_type: str
        :param aop_type: **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及
        :type aop_type: str
        :param dataclass_id: **参数解释**: 数据类的ID **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type dataclass_id: str
        :param labels: **参数解释**: 流程实体类型 - IP IP - ACCOUNT 账号 - DOMAIN 域名  **约束限制**: 不涉及         **取值范围**: - IP - ACCOUNT - DOMAIN  **默认值**:  不涉及
        :type labels: str
        """
        
        

        self._name = None
        self._description = None
        self._engine_type = None
        self._aop_type = None
        self._dataclass_id = None
        self._labels = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.engine_type = engine_type
        self.aop_type = aop_type
        self.dataclass_id = dataclass_id
        if labels is not None:
            self.labels = labels

    @property
    def name(self):
        r"""Gets the name of this CreateAopWorkflowInfo.

        **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The name of this CreateAopWorkflowInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAopWorkflowInfo.

        **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param name: The name of this CreateAopWorkflowInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateAopWorkflowInfo.

        **参数解释**: 流程的描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The description of this CreateAopWorkflowInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAopWorkflowInfo.

        **参数解释**: 流程的描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param description: The description of this CreateAopWorkflowInfo.
        :type description: str
        """
        self._description = description

    @property
    def engine_type(self):
        r"""Gets the engine_type of this CreateAopWorkflowInfo.

        **参数解释**: 引擎的类型 - public_engine 共享版  **约束限制**: 不涉及         **取值范围**: - public_engine  **默认值**:  不涉及

        :return: The engine_type of this CreateAopWorkflowInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this CreateAopWorkflowInfo.

        **参数解释**: 引擎的类型 - public_engine 共享版  **约束限制**: 不涉及         **取值范围**: - public_engine  **默认值**:  不涉及

        :param engine_type: The engine_type of this CreateAopWorkflowInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def aop_type(self):
        r"""Gets the aop_type of this CreateAopWorkflowInfo.

        **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及

        :return: The aop_type of this CreateAopWorkflowInfo.
        :rtype: str
        """
        return self._aop_type

    @aop_type.setter
    def aop_type(self, aop_type):
        r"""Sets the aop_type of this CreateAopWorkflowInfo.

        **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及

        :param aop_type: The aop_type of this CreateAopWorkflowInfo.
        :type aop_type: str
        """
        self._aop_type = aop_type

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this CreateAopWorkflowInfo.

        **参数解释**: 数据类的ID **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The dataclass_id of this CreateAopWorkflowInfo.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this CreateAopWorkflowInfo.

        **参数解释**: 数据类的ID **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param dataclass_id: The dataclass_id of this CreateAopWorkflowInfo.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def labels(self):
        r"""Gets the labels of this CreateAopWorkflowInfo.

        **参数解释**: 流程实体类型 - IP IP - ACCOUNT 账号 - DOMAIN 域名  **约束限制**: 不涉及         **取值范围**: - IP - ACCOUNT - DOMAIN  **默认值**:  不涉及

        :return: The labels of this CreateAopWorkflowInfo.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateAopWorkflowInfo.

        **参数解释**: 流程实体类型 - IP IP - ACCOUNT 账号 - DOMAIN 域名  **约束限制**: 不涉及         **取值范围**: - IP - ACCOUNT - DOMAIN  **默认值**:  不涉及

        :param labels: The labels of this CreateAopWorkflowInfo.
        :type labels: str
        """
        self._labels = labels

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
        if not isinstance(other, CreateAopWorkflowInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
