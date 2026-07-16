# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInferDeploymentVersionRequest:

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
        'version': 'str',
        'deployment_id': 'str'
    }

    attribute_map = {
        'service_id': 'service_id',
        'version': 'version',
        'deployment_id': 'deployment_id'
    }

    def __init__(self, service_id=None, version=None, deployment_id=None):
        r"""ShowInferDeploymentVersionRequest

        The model defined in huaweicloud sdk

        :param service_id: **参数解释：** 服务ID，在创建服务时即可在返回体中获取，也可通过查询服务列表接口获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type service_id: str
        :param version: 版本
        :type version: str
        :param deployment_id: 部署id
        :type deployment_id: str
        """
        
        

        self._service_id = None
        self._version = None
        self._deployment_id = None
        self.discriminator = None

        self.service_id = service_id
        self.version = version
        self.deployment_id = deployment_id

    @property
    def service_id(self):
        r"""Gets the service_id of this ShowInferDeploymentVersionRequest.

        **参数解释：** 服务ID，在创建服务时即可在返回体中获取，也可通过查询服务列表接口获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The service_id of this ShowInferDeploymentVersionRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ShowInferDeploymentVersionRequest.

        **参数解释：** 服务ID，在创建服务时即可在返回体中获取，也可通过查询服务列表接口获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param service_id: The service_id of this ShowInferDeploymentVersionRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def version(self):
        r"""Gets the version of this ShowInferDeploymentVersionRequest.

        版本

        :return: The version of this ShowInferDeploymentVersionRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowInferDeploymentVersionRequest.

        版本

        :param version: The version of this ShowInferDeploymentVersionRequest.
        :type version: str
        """
        self._version = version

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this ShowInferDeploymentVersionRequest.

        部署id

        :return: The deployment_id of this ShowInferDeploymentVersionRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this ShowInferDeploymentVersionRequest.

        部署id

        :param deployment_id: The deployment_id of this ShowInferDeploymentVersionRequest.
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
        if not isinstance(other, ShowInferDeploymentVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
