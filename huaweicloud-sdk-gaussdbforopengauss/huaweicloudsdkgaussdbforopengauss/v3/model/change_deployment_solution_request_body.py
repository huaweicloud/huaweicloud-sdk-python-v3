# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeDeploymentSolutionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'solution': 'str',
        'availability_zone': 'str',
        'master_az': 'str',
        'logger_az': 'str'
    }

    attribute_map = {
        'solution': 'solution',
        'availability_zone': 'availability_zone',
        'master_az': 'master_az',
        'logger_az': 'logger_az'
    }

    def __init__(self, solution=None, availability_zone=None, master_az=None, logger_az=None):
        r"""ChangeDeploymentSolutionRequestBody

        The model defined in huaweicloud sdk

        :param solution: **参数解释**: 变更后的目标部署形态。 **约束限制**: 必填。取值需为当前实例允许变更的目标形态。 **取值范围**: - logger：一主一备一日志节点 - triset：一主两备三节点  **默认取值**: 不涉及。
        :type solution: str
        :param availability_zone: **参数解释**: 部署可用区，多个可用区以英文逗号\&quot;,\&quot;隔开。 **约束限制**: 必填。不可包含 []()^%&amp;\\\\&#39;&#x60;|\&quot;;&#x3D;?$&lt;&gt; 等特殊字符。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type availability_zone: str
        :param master_az: **参数解释**: 主可用区。 **约束限制**: 不填时默认使用当前主可用区。 **取值范围**: 不涉及。 **默认取值**: 当前实例的主可用区。
        :type master_az: str
        :param logger_az: **参数解释**: 日志可用区。 **约束限制**: 带日志节点的部署形态（如 logger）需要传该参数。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type logger_az: str
        """
        
        

        self._solution = None
        self._availability_zone = None
        self._master_az = None
        self._logger_az = None
        self.discriminator = None

        self.solution = solution
        self.availability_zone = availability_zone
        if master_az is not None:
            self.master_az = master_az
        if logger_az is not None:
            self.logger_az = logger_az

    @property
    def solution(self):
        r"""Gets the solution of this ChangeDeploymentSolutionRequestBody.

        **参数解释**: 变更后的目标部署形态。 **约束限制**: 必填。取值需为当前实例允许变更的目标形态。 **取值范围**: - logger：一主一备一日志节点 - triset：一主两备三节点  **默认取值**: 不涉及。

        :return: The solution of this ChangeDeploymentSolutionRequestBody.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this ChangeDeploymentSolutionRequestBody.

        **参数解释**: 变更后的目标部署形态。 **约束限制**: 必填。取值需为当前实例允许变更的目标形态。 **取值范围**: - logger：一主一备一日志节点 - triset：一主两备三节点  **默认取值**: 不涉及。

        :param solution: The solution of this ChangeDeploymentSolutionRequestBody.
        :type solution: str
        """
        self._solution = solution

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ChangeDeploymentSolutionRequestBody.

        **参数解释**: 部署可用区，多个可用区以英文逗号\",\"隔开。 **约束限制**: 必填。不可包含 []()^%&\\\\'`|\";=?$<> 等特殊字符。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The availability_zone of this ChangeDeploymentSolutionRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ChangeDeploymentSolutionRequestBody.

        **参数解释**: 部署可用区，多个可用区以英文逗号\",\"隔开。 **约束限制**: 必填。不可包含 []()^%&\\\\'`|\";=?$<> 等特殊字符。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param availability_zone: The availability_zone of this ChangeDeploymentSolutionRequestBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def master_az(self):
        r"""Gets the master_az of this ChangeDeploymentSolutionRequestBody.

        **参数解释**: 主可用区。 **约束限制**: 不填时默认使用当前主可用区。 **取值范围**: 不涉及。 **默认取值**: 当前实例的主可用区。

        :return: The master_az of this ChangeDeploymentSolutionRequestBody.
        :rtype: str
        """
        return self._master_az

    @master_az.setter
    def master_az(self, master_az):
        r"""Sets the master_az of this ChangeDeploymentSolutionRequestBody.

        **参数解释**: 主可用区。 **约束限制**: 不填时默认使用当前主可用区。 **取值范围**: 不涉及。 **默认取值**: 当前实例的主可用区。

        :param master_az: The master_az of this ChangeDeploymentSolutionRequestBody.
        :type master_az: str
        """
        self._master_az = master_az

    @property
    def logger_az(self):
        r"""Gets the logger_az of this ChangeDeploymentSolutionRequestBody.

        **参数解释**: 日志可用区。 **约束限制**: 带日志节点的部署形态（如 logger）需要传该参数。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The logger_az of this ChangeDeploymentSolutionRequestBody.
        :rtype: str
        """
        return self._logger_az

    @logger_az.setter
    def logger_az(self, logger_az):
        r"""Sets the logger_az of this ChangeDeploymentSolutionRequestBody.

        **参数解释**: 日志可用区。 **约束限制**: 带日志节点的部署形态（如 logger）需要传该参数。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param logger_az: The logger_az of this ChangeDeploymentSolutionRequestBody.
        :type logger_az: str
        """
        self._logger_az = logger_az

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
        if not isinstance(other, ChangeDeploymentSolutionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
