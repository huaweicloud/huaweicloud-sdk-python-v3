# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IntranetConnectionRequest:

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
        'scene': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'pool_id': 'str',
        'type': 'str',
        'dispatcher_group_id': 'str',
        'custom_urls': 'list[str]'
    }

    attribute_map = {
        'service_id': 'service_id',
        'scene': 'scene',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'pool_id': 'pool_id',
        'type': 'type',
        'dispatcher_group_id': 'dispatcher_group_id',
        'custom_urls': 'custom_urls'
    }

    def __init__(self, service_id=None, scene=None, vpc_id=None, subnet_id=None, pool_id=None, type=None, dispatcher_group_id=None, custom_urls=None):
        r"""IntranetConnectionRequest

        The model defined in huaweicloud sdk

        :param service_id: **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** type为SERVICE时，必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type service_id: str
        :param scene: **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - VPC：用户VPC网络接入场景 - POOL：用户资源池网络接入场景 **默认取值：** 不涉及。
        :type scene: str
        :param vpc_id: **参数解释：** VPC ID，VPC场景需要填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type vpc_id: str
        :param subnet_id: **参数解释：** 子网 ID，VPC场景需要填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type subnet_id: str
        :param pool_id: **参数解释：** 资源池id POOL场景需要填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type pool_id: str
        :param type: **参数解释：** 内网访问接入粒度，不填默认为SERVICE **约束限制：** 不涉及。 **取值范围：** - SERVICE：服务粒度。 - GLOBAL：global粒度。 **默认取值：** 默认为SERVICE。
        :type type: str
        :param dispatcher_group_id: **参数解释：** 服务绑定的dispatcher组ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type dispatcher_group_id: str
        :param custom_urls: **参数解释：** 自定义URL，格式为：{协议}://{域名}{路径} **约束限制：** url个数不超过10个，单个url长度不超过1024。 **取值范围：** - 协议范围：http，https，wss，ws。 - 域名范围：支持域名或IP:端口。域名长度不超过63，包含字母、数字、中划线（-)且不能以中划线（-)开头或结尾，顶级域名不能包含数字；端口范围为1-65535。 - 路径范围：斜杠（/）开头，仅包含字母、数字、点号（.）、中划线（-)、下划线（_）、斜杠（/）的路径。 **默认取值：** 不涉及。
        :type custom_urls: list[str]
        """
        
        

        self._service_id = None
        self._scene = None
        self._vpc_id = None
        self._subnet_id = None
        self._pool_id = None
        self._type = None
        self._dispatcher_group_id = None
        self._custom_urls = None
        self.discriminator = None

        if service_id is not None:
            self.service_id = service_id
        self.scene = scene
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if pool_id is not None:
            self.pool_id = pool_id
        if type is not None:
            self.type = type
        if dispatcher_group_id is not None:
            self.dispatcher_group_id = dispatcher_group_id
        if custom_urls is not None:
            self.custom_urls = custom_urls

    @property
    def service_id(self):
        r"""Gets the service_id of this IntranetConnectionRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** type为SERVICE时，必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The service_id of this IntranetConnectionRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this IntranetConnectionRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** type为SERVICE时，必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param service_id: The service_id of this IntranetConnectionRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def scene(self):
        r"""Gets the scene of this IntranetConnectionRequest.

        **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - VPC：用户VPC网络接入场景 - POOL：用户资源池网络接入场景 **默认取值：** 不涉及。

        :return: The scene of this IntranetConnectionRequest.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this IntranetConnectionRequest.

        **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - VPC：用户VPC网络接入场景 - POOL：用户资源池网络接入场景 **默认取值：** 不涉及。

        :param scene: The scene of this IntranetConnectionRequest.
        :type scene: str
        """
        self._scene = scene

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this IntranetConnectionRequest.

        **参数解释：** VPC ID，VPC场景需要填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The vpc_id of this IntranetConnectionRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this IntranetConnectionRequest.

        **参数解释：** VPC ID，VPC场景需要填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param vpc_id: The vpc_id of this IntranetConnectionRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this IntranetConnectionRequest.

        **参数解释：** 子网 ID，VPC场景需要填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The subnet_id of this IntranetConnectionRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this IntranetConnectionRequest.

        **参数解释：** 子网 ID，VPC场景需要填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param subnet_id: The subnet_id of this IntranetConnectionRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def pool_id(self):
        r"""Gets the pool_id of this IntranetConnectionRequest.

        **参数解释：** 资源池id POOL场景需要填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The pool_id of this IntranetConnectionRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this IntranetConnectionRequest.

        **参数解释：** 资源池id POOL场景需要填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param pool_id: The pool_id of this IntranetConnectionRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def type(self):
        r"""Gets the type of this IntranetConnectionRequest.

        **参数解释：** 内网访问接入粒度，不填默认为SERVICE **约束限制：** 不涉及。 **取值范围：** - SERVICE：服务粒度。 - GLOBAL：global粒度。 **默认取值：** 默认为SERVICE。

        :return: The type of this IntranetConnectionRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IntranetConnectionRequest.

        **参数解释：** 内网访问接入粒度，不填默认为SERVICE **约束限制：** 不涉及。 **取值范围：** - SERVICE：服务粒度。 - GLOBAL：global粒度。 **默认取值：** 默认为SERVICE。

        :param type: The type of this IntranetConnectionRequest.
        :type type: str
        """
        self._type = type

    @property
    def dispatcher_group_id(self):
        r"""Gets the dispatcher_group_id of this IntranetConnectionRequest.

        **参数解释：** 服务绑定的dispatcher组ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The dispatcher_group_id of this IntranetConnectionRequest.
        :rtype: str
        """
        return self._dispatcher_group_id

    @dispatcher_group_id.setter
    def dispatcher_group_id(self, dispatcher_group_id):
        r"""Sets the dispatcher_group_id of this IntranetConnectionRequest.

        **参数解释：** 服务绑定的dispatcher组ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param dispatcher_group_id: The dispatcher_group_id of this IntranetConnectionRequest.
        :type dispatcher_group_id: str
        """
        self._dispatcher_group_id = dispatcher_group_id

    @property
    def custom_urls(self):
        r"""Gets the custom_urls of this IntranetConnectionRequest.

        **参数解释：** 自定义URL，格式为：{协议}://{域名}{路径} **约束限制：** url个数不超过10个，单个url长度不超过1024。 **取值范围：** - 协议范围：http，https，wss，ws。 - 域名范围：支持域名或IP:端口。域名长度不超过63，包含字母、数字、中划线（-)且不能以中划线（-)开头或结尾，顶级域名不能包含数字；端口范围为1-65535。 - 路径范围：斜杠（/）开头，仅包含字母、数字、点号（.）、中划线（-)、下划线（_）、斜杠（/）的路径。 **默认取值：** 不涉及。

        :return: The custom_urls of this IntranetConnectionRequest.
        :rtype: list[str]
        """
        return self._custom_urls

    @custom_urls.setter
    def custom_urls(self, custom_urls):
        r"""Sets the custom_urls of this IntranetConnectionRequest.

        **参数解释：** 自定义URL，格式为：{协议}://{域名}{路径} **约束限制：** url个数不超过10个，单个url长度不超过1024。 **取值范围：** - 协议范围：http，https，wss，ws。 - 域名范围：支持域名或IP:端口。域名长度不超过63，包含字母、数字、中划线（-)且不能以中划线（-)开头或结尾，顶级域名不能包含数字；端口范围为1-65535。 - 路径范围：斜杠（/）开头，仅包含字母、数字、点号（.）、中划线（-)、下划线（_）、斜杠（/）的路径。 **默认取值：** 不涉及。

        :param custom_urls: The custom_urls of this IntranetConnectionRequest.
        :type custom_urls: list[str]
        """
        self._custom_urls = custom_urls

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
        if not isinstance(other, IntranetConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
