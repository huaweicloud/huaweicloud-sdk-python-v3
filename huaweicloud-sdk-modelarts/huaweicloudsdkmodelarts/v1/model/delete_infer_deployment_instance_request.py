# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteInferDeploymentInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'deployment_name': 'str',
        'name': 'str',
        'force': 'bool',
        'operation': 'str'
    }

    attribute_map = {
        'id': 'id',
        'deployment_name': 'deployment_name',
        'name': 'name',
        'force': 'force',
        'operation': 'operation'
    }

    def __init__(self, id=None, deployment_name=None, name=None, force=None, operation=None):
        r"""DeleteInferDeploymentInstanceRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。
        :type id: str
        :param deployment_name: **参数解释：** 部署名称。
        :type deployment_name: str
        :param name: **参数解释：** 服务实例名字，可以为all，为all时去查询所有的服务实例。 **约束限制：** 不涉及。 **取值范围：** 服务实例名字。 **默认取值：** 不涉及。
        :type name: str
        :param force: **参数解释：** 是否强制删除。 **约束限制：** 不涉及。 **取值范围：** - true：强制删除。 - false：不强制删除。 **默认取值：** false。
        :type force: bool
        :param operation: **参数解释：** 删除操作类型。 **约束限制：** 枚举值。 **取值范围：** - DELETE：直接删除，释放资源。 - RECREATE：删除后重建。 **默认取值：** RECREATE。
        :type operation: str
        """
        
        

        self._id = None
        self._deployment_name = None
        self._name = None
        self._force = None
        self._operation = None
        self.discriminator = None

        self.id = id
        self.deployment_name = deployment_name
        self.name = name
        if force is not None:
            self.force = force
        if operation is not None:
            self.operation = operation

    @property
    def id(self):
        r"""Gets the id of this DeleteInferDeploymentInstanceRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :return: The id of this DeleteInferDeploymentInstanceRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteInferDeploymentInstanceRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :param id: The id of this DeleteInferDeploymentInstanceRequest.
        :type id: str
        """
        self._id = id

    @property
    def deployment_name(self):
        r"""Gets the deployment_name of this DeleteInferDeploymentInstanceRequest.

        **参数解释：** 部署名称。

        :return: The deployment_name of this DeleteInferDeploymentInstanceRequest.
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        r"""Sets the deployment_name of this DeleteInferDeploymentInstanceRequest.

        **参数解释：** 部署名称。

        :param deployment_name: The deployment_name of this DeleteInferDeploymentInstanceRequest.
        :type deployment_name: str
        """
        self._deployment_name = deployment_name

    @property
    def name(self):
        r"""Gets the name of this DeleteInferDeploymentInstanceRequest.

        **参数解释：** 服务实例名字，可以为all，为all时去查询所有的服务实例。 **约束限制：** 不涉及。 **取值范围：** 服务实例名字。 **默认取值：** 不涉及。

        :return: The name of this DeleteInferDeploymentInstanceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DeleteInferDeploymentInstanceRequest.

        **参数解释：** 服务实例名字，可以为all，为all时去查询所有的服务实例。 **约束限制：** 不涉及。 **取值范围：** 服务实例名字。 **默认取值：** 不涉及。

        :param name: The name of this DeleteInferDeploymentInstanceRequest.
        :type name: str
        """
        self._name = name

    @property
    def force(self):
        r"""Gets the force of this DeleteInferDeploymentInstanceRequest.

        **参数解释：** 是否强制删除。 **约束限制：** 不涉及。 **取值范围：** - true：强制删除。 - false：不强制删除。 **默认取值：** false。

        :return: The force of this DeleteInferDeploymentInstanceRequest.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        r"""Sets the force of this DeleteInferDeploymentInstanceRequest.

        **参数解释：** 是否强制删除。 **约束限制：** 不涉及。 **取值范围：** - true：强制删除。 - false：不强制删除。 **默认取值：** false。

        :param force: The force of this DeleteInferDeploymentInstanceRequest.
        :type force: bool
        """
        self._force = force

    @property
    def operation(self):
        r"""Gets the operation of this DeleteInferDeploymentInstanceRequest.

        **参数解释：** 删除操作类型。 **约束限制：** 枚举值。 **取值范围：** - DELETE：直接删除，释放资源。 - RECREATE：删除后重建。 **默认取值：** RECREATE。

        :return: The operation of this DeleteInferDeploymentInstanceRequest.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this DeleteInferDeploymentInstanceRequest.

        **参数解释：** 删除操作类型。 **约束限制：** 枚举值。 **取值范围：** - DELETE：直接删除，释放资源。 - RECREATE：删除后重建。 **默认取值：** RECREATE。

        :param operation: The operation of this DeleteInferDeploymentInstanceRequest.
        :type operation: str
        """
        self._operation = operation

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
        if not isinstance(other, DeleteInferDeploymentInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
