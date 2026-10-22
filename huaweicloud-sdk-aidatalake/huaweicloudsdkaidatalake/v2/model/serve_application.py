# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServeApplication:

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
        'import_path': 'str',
        'route_prefix': 'str',
        'runtime_env': 'ServeRuntimeEnv',
        'deployments': 'list[ServeDeployment]'
    }

    attribute_map = {
        'name': 'name',
        'import_path': 'import_path',
        'route_prefix': 'route_prefix',
        'runtime_env': 'runtime_env',
        'deployments': 'deployments'
    }

    def __init__(self, name=None, import_path=None, route_prefix=None, runtime_env=None, deployments=None):
        r"""ServeApplication

        The model defined in huaweicloud sdk

        :param name: **参数解释**：应用名（L7 路由/计费维度）。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param import_path: **参数解释**：Python 导入路径（模块:对象），如 voc_deepseek_server_v4:app。 **约束限制**：不能包含空格。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type import_path: str
        :param route_prefix: **参数解释**：路由前缀，端点内不可重复。 **约束限制**：必须以 / 开头，不能包含空格，且同一端点内多个应用的 route_prefix 不可重复。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type route_prefix: str
        :param runtime_env: 
        :type runtime_env: :class:`huaweicloudsdkaidatalake.v2.ServeRuntimeEnv`
        :param deployments: 
        :type deployments: list[:class:`huaweicloudsdkaidatalake.v2.ServeDeployment`]
        """
        
        

        self._name = None
        self._import_path = None
        self._route_prefix = None
        self._runtime_env = None
        self._deployments = None
        self.discriminator = None

        self.name = name
        self.import_path = import_path
        self.route_prefix = route_prefix
        self.runtime_env = runtime_env
        self.deployments = deployments

    @property
    def name(self):
        r"""Gets the name of this ServeApplication.

        **参数解释**：应用名（L7 路由/计费维度）。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this ServeApplication.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServeApplication.

        **参数解释**：应用名（L7 路由/计费维度）。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this ServeApplication.
        :type name: str
        """
        self._name = name

    @property
    def import_path(self):
        r"""Gets the import_path of this ServeApplication.

        **参数解释**：Python 导入路径（模块:对象），如 voc_deepseek_server_v4:app。 **约束限制**：不能包含空格。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The import_path of this ServeApplication.
        :rtype: str
        """
        return self._import_path

    @import_path.setter
    def import_path(self, import_path):
        r"""Sets the import_path of this ServeApplication.

        **参数解释**：Python 导入路径（模块:对象），如 voc_deepseek_server_v4:app。 **约束限制**：不能包含空格。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param import_path: The import_path of this ServeApplication.
        :type import_path: str
        """
        self._import_path = import_path

    @property
    def route_prefix(self):
        r"""Gets the route_prefix of this ServeApplication.

        **参数解释**：路由前缀，端点内不可重复。 **约束限制**：必须以 / 开头，不能包含空格，且同一端点内多个应用的 route_prefix 不可重复。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The route_prefix of this ServeApplication.
        :rtype: str
        """
        return self._route_prefix

    @route_prefix.setter
    def route_prefix(self, route_prefix):
        r"""Sets the route_prefix of this ServeApplication.

        **参数解释**：路由前缀，端点内不可重复。 **约束限制**：必须以 / 开头，不能包含空格，且同一端点内多个应用的 route_prefix 不可重复。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param route_prefix: The route_prefix of this ServeApplication.
        :type route_prefix: str
        """
        self._route_prefix = route_prefix

    @property
    def runtime_env(self):
        r"""Gets the runtime_env of this ServeApplication.

        :return: The runtime_env of this ServeApplication.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ServeRuntimeEnv`
        """
        return self._runtime_env

    @runtime_env.setter
    def runtime_env(self, runtime_env):
        r"""Sets the runtime_env of this ServeApplication.

        :param runtime_env: The runtime_env of this ServeApplication.
        :type runtime_env: :class:`huaweicloudsdkaidatalake.v2.ServeRuntimeEnv`
        """
        self._runtime_env = runtime_env

    @property
    def deployments(self):
        r"""Gets the deployments of this ServeApplication.

        :return: The deployments of this ServeApplication.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ServeDeployment`]
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        r"""Sets the deployments of this ServeApplication.

        :param deployments: The deployments of this ServeApplication.
        :type deployments: list[:class:`huaweicloudsdkaidatalake.v2.ServeDeployment`]
        """
        self._deployments = deployments

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
        if not isinstance(other, ServeApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
