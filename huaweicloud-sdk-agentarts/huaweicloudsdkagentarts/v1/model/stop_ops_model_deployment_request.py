# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopOpsModelDeploymentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deployment_id': 'str'
    }

    attribute_map = {
        'deployment_id': 'deployment_id'
    }

    def __init__(self, deployment_id=None):
        r"""StopOpsModelDeploymentRequest

        The model defined in huaweicloud sdk

        :param deployment_id: **参数解释：** 模型部署任务ID，获取方法请参见查询模型部署列表。  **约束限制：** 不涉及  **取值范围：** 真实存在的部署ID字符串。  **默认取值：** 无
        :type deployment_id: str
        """
        
        

        self._deployment_id = None
        self.discriminator = None

        self.deployment_id = deployment_id

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this StopOpsModelDeploymentRequest.

        **参数解释：** 模型部署任务ID，获取方法请参见查询模型部署列表。  **约束限制：** 不涉及  **取值范围：** 真实存在的部署ID字符串。  **默认取值：** 无

        :return: The deployment_id of this StopOpsModelDeploymentRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this StopOpsModelDeploymentRequest.

        **参数解释：** 模型部署任务ID，获取方法请参见查询模型部署列表。  **约束限制：** 不涉及  **取值范围：** 真实存在的部署ID字符串。  **默认取值：** 无

        :param deployment_id: The deployment_id of this StopOpsModelDeploymentRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

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
        if not isinstance(other, StopOpsModelDeploymentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
