# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeploymentFormRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'solution': 'str',
        'instance_id': 'str',
        'consistency': 'str',
        'consistency_protocol': 'str',
        'engine_version': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'solution': 'solution',
        'instance_id': 'instance_id',
        'consistency': 'consistency',
        'consistency_protocol': 'consistency_protocol',
        'engine_version': 'engine_version'
    }

    def __init__(self, x_language=None, solution=None, instance_id=None, consistency=None, consistency_protocol=None, engine_version=None):
        r"""ShowDeploymentFormRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**:   - zh-cn   - en-us  **默认取值**: en-us
        :type x_language: str
        :param solution: 解决方案模板名称。
        :type solution: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param consistency: **参数解释**: 事务一致性类型。 **约束限制**: 不涉及。 **取值范围**: - strong - eventual **默认取值**: 不涉及。
        :type consistency: str
        :param consistency_protocol: **参数解释**: 副本一致性协议类型。 **约束限制**: 不涉及。 **取值范围**: - quorum - paxos **默认取值**: 不涉及。
        :type consistency_protocol: str
        :param engine_version: **参数解释**: 引擎版本号。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type engine_version: str
        """
        
        

        self._x_language = None
        self._solution = None
        self._instance_id = None
        self._consistency = None
        self._consistency_protocol = None
        self._engine_version = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if solution is not None:
            self.solution = solution
        if instance_id is not None:
            self.instance_id = instance_id
        if consistency is not None:
            self.consistency = consistency
        if consistency_protocol is not None:
            self.consistency_protocol = consistency_protocol
        if engine_version is not None:
            self.engine_version = engine_version

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowDeploymentFormRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**:   - zh-cn   - en-us  **默认取值**: en-us

        :return: The x_language of this ShowDeploymentFormRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowDeploymentFormRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**:   - zh-cn   - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ShowDeploymentFormRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def solution(self):
        r"""Gets the solution of this ShowDeploymentFormRequest.

        解决方案模板名称。

        :return: The solution of this ShowDeploymentFormRequest.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this ShowDeploymentFormRequest.

        解决方案模板名称。

        :param solution: The solution of this ShowDeploymentFormRequest.
        :type solution: str
        """
        self._solution = solution

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDeploymentFormRequest.

        实例ID。

        :return: The instance_id of this ShowDeploymentFormRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDeploymentFormRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowDeploymentFormRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def consistency(self):
        r"""Gets the consistency of this ShowDeploymentFormRequest.

        **参数解释**: 事务一致性类型。 **约束限制**: 不涉及。 **取值范围**: - strong - eventual **默认取值**: 不涉及。

        :return: The consistency of this ShowDeploymentFormRequest.
        :rtype: str
        """
        return self._consistency

    @consistency.setter
    def consistency(self, consistency):
        r"""Sets the consistency of this ShowDeploymentFormRequest.

        **参数解释**: 事务一致性类型。 **约束限制**: 不涉及。 **取值范围**: - strong - eventual **默认取值**: 不涉及。

        :param consistency: The consistency of this ShowDeploymentFormRequest.
        :type consistency: str
        """
        self._consistency = consistency

    @property
    def consistency_protocol(self):
        r"""Gets the consistency_protocol of this ShowDeploymentFormRequest.

        **参数解释**: 副本一致性协议类型。 **约束限制**: 不涉及。 **取值范围**: - quorum - paxos **默认取值**: 不涉及。

        :return: The consistency_protocol of this ShowDeploymentFormRequest.
        :rtype: str
        """
        return self._consistency_protocol

    @consistency_protocol.setter
    def consistency_protocol(self, consistency_protocol):
        r"""Sets the consistency_protocol of this ShowDeploymentFormRequest.

        **参数解释**: 副本一致性协议类型。 **约束限制**: 不涉及。 **取值范围**: - quorum - paxos **默认取值**: 不涉及。

        :param consistency_protocol: The consistency_protocol of this ShowDeploymentFormRequest.
        :type consistency_protocol: str
        """
        self._consistency_protocol = consistency_protocol

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ShowDeploymentFormRequest.

        **参数解释**: 引擎版本号。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The engine_version of this ShowDeploymentFormRequest.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ShowDeploymentFormRequest.

        **参数解释**: 引擎版本号。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param engine_version: The engine_version of this ShowDeploymentFormRequest.
        :type engine_version: str
        """
        self._engine_version = engine_version

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
        if not isinstance(other, ShowDeploymentFormRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
