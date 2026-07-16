# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchInferDeploymentVersionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'target_deployment_version': 'str',
        'infer_name': 'str'
    }

    attribute_map = {
        'service_id': 'service_id',
        'target_deployment_version': 'target_deployment_version',
        'infer_name': 'infer_name'
    }

    def __init__(self, service_id=None, target_deployment_version=None, infer_name=None):
        r"""SwitchInferDeploymentVersionRequestBody

        The model defined in huaweicloud sdk

        :param service_id: **参数解释：** 服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type service_id: str
        :param target_deployment_version: **参数解释：** 待切换的目标版本。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type target_deployment_version: str
        :param infer_name: **参数解释：** 部署ID。
        :type infer_name: str
        """
        
        

        self._service_id = None
        self._target_deployment_version = None
        self._infer_name = None
        self.discriminator = None

        if service_id is not None:
            self.service_id = service_id
        if target_deployment_version is not None:
            self.target_deployment_version = target_deployment_version
        self.infer_name = infer_name

    @property
    def service_id(self):
        r"""Gets the service_id of this SwitchInferDeploymentVersionRequestBody.

        **参数解释：** 服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The service_id of this SwitchInferDeploymentVersionRequestBody.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this SwitchInferDeploymentVersionRequestBody.

        **参数解释：** 服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param service_id: The service_id of this SwitchInferDeploymentVersionRequestBody.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def target_deployment_version(self):
        r"""Gets the target_deployment_version of this SwitchInferDeploymentVersionRequestBody.

        **参数解释：** 待切换的目标版本。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The target_deployment_version of this SwitchInferDeploymentVersionRequestBody.
        :rtype: str
        """
        return self._target_deployment_version

    @target_deployment_version.setter
    def target_deployment_version(self, target_deployment_version):
        r"""Sets the target_deployment_version of this SwitchInferDeploymentVersionRequestBody.

        **参数解释：** 待切换的目标版本。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param target_deployment_version: The target_deployment_version of this SwitchInferDeploymentVersionRequestBody.
        :type target_deployment_version: str
        """
        self._target_deployment_version = target_deployment_version

    @property
    def infer_name(self):
        r"""Gets the infer_name of this SwitchInferDeploymentVersionRequestBody.

        **参数解释：** 部署ID。

        :return: The infer_name of this SwitchInferDeploymentVersionRequestBody.
        :rtype: str
        """
        return self._infer_name

    @infer_name.setter
    def infer_name(self, infer_name):
        r"""Sets the infer_name of this SwitchInferDeploymentVersionRequestBody.

        **参数解释：** 部署ID。

        :param infer_name: The infer_name of this SwitchInferDeploymentVersionRequestBody.
        :type infer_name: str
        """
        self._infer_name = infer_name

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
        if not isinstance(other, SwitchInferDeploymentVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
