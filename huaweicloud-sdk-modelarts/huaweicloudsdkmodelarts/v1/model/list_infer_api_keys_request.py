# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferApiKeysRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scope': 'str',
        'service_id': 'str',
        'name': 'str',
        'service_name': 'str',
        'key_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'workspace_id': 'str',
        'with_user_scope': 'bool'
    }

    attribute_map = {
        'scope': 'scope',
        'service_id': 'service_id',
        'name': 'name',
        'service_name': 'service_name',
        'key_id': 'key_id',
        'limit': 'limit',
        'offset': 'offset',
        'workspace_id': 'workspace_id',
        'with_user_scope': 'with_user_scope'
    }

    def __init__(self, scope=None, service_id=None, name=None, service_name=None, key_id=None, limit=None, offset=None, workspace_id=None, with_user_scope=None):
        r"""ListInferApiKeysRequest

        The model defined in huaweicloud sdk

        :param scope: **参数解释：** 生效范围，枚举值，可选值为USER、SERVICE。 **约束限制：** 不涉及。 **取值范围：** - USER：表示生效范围为用户级别，可以访问该用户创建的所有在线服务。 - SERVICE：表示生效范围为单个服务，可以访问绑定该api-key的在线服务。 **默认取值：** 不涉及。
        :type scope: str
        :param service_id: **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。
        :type service_id: str
        :param name: **参数解释：** apikey_name，通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的apikey，其中name字段即为apikey_name。 **约束限制：** 不涉及。 **取值范围：** apikey_name。 **默认取值：** 不涉及。
        :type name: str
        :param service_name: **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义。 **约束限制：** 服务名称不能重复。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。
        :type service_name: str
        :param key_id: **参数解释：** apikey_id，在[创建API_KEY](CreateInferApiKey.xml)时即可在返回体中获取，也可通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的apikey，其中key_id字段即为apikey_id。 **约束限制：** 不涉及。 **取值范围：** apikey_id只能由英文小写字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及。
        :type key_id: str
        :param limit: **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。
        :type limit: int
        :param offset: **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。
        :type offset: int
        :param workspace_id: **参数解释：** 工作空间ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type workspace_id: str
        :param with_user_scope: **参数解释：** 是否查询鉴权范围为USER类型的API KEY，当同时指定service_id时可查询该服务所有可访问的API KEY。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** false。
        :type with_user_scope: bool
        """
        
        

        self._scope = None
        self._service_id = None
        self._name = None
        self._service_name = None
        self._key_id = None
        self._limit = None
        self._offset = None
        self._workspace_id = None
        self._with_user_scope = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope
        if service_id is not None:
            self.service_id = service_id
        if name is not None:
            self.name = name
        if service_name is not None:
            self.service_name = service_name
        if key_id is not None:
            self.key_id = key_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if with_user_scope is not None:
            self.with_user_scope = with_user_scope

    @property
    def scope(self):
        r"""Gets the scope of this ListInferApiKeysRequest.

        **参数解释：** 生效范围，枚举值，可选值为USER、SERVICE。 **约束限制：** 不涉及。 **取值范围：** - USER：表示生效范围为用户级别，可以访问该用户创建的所有在线服务。 - SERVICE：表示生效范围为单个服务，可以访问绑定该api-key的在线服务。 **默认取值：** 不涉及。

        :return: The scope of this ListInferApiKeysRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ListInferApiKeysRequest.

        **参数解释：** 生效范围，枚举值，可选值为USER、SERVICE。 **约束限制：** 不涉及。 **取值范围：** - USER：表示生效范围为用户级别，可以访问该用户创建的所有在线服务。 - SERVICE：表示生效范围为单个服务，可以访问绑定该api-key的在线服务。 **默认取值：** 不涉及。

        :param scope: The scope of this ListInferApiKeysRequest.
        :type scope: str
        """
        self._scope = scope

    @property
    def service_id(self):
        r"""Gets the service_id of this ListInferApiKeysRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :return: The service_id of this ListInferApiKeysRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ListInferApiKeysRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :param service_id: The service_id of this ListInferApiKeysRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def name(self):
        r"""Gets the name of this ListInferApiKeysRequest.

        **参数解释：** apikey_name，通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的apikey，其中name字段即为apikey_name。 **约束限制：** 不涉及。 **取值范围：** apikey_name。 **默认取值：** 不涉及。

        :return: The name of this ListInferApiKeysRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInferApiKeysRequest.

        **参数解释：** apikey_name，通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的apikey，其中name字段即为apikey_name。 **约束限制：** 不涉及。 **取值范围：** apikey_name。 **默认取值：** 不涉及。

        :param name: The name of this ListInferApiKeysRequest.
        :type name: str
        """
        self._name = name

    @property
    def service_name(self):
        r"""Gets the service_name of this ListInferApiKeysRequest.

        **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义。 **约束限制：** 服务名称不能重复。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。

        :return: The service_name of this ListInferApiKeysRequest.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ListInferApiKeysRequest.

        **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义。 **约束限制：** 服务名称不能重复。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。

        :param service_name: The service_name of this ListInferApiKeysRequest.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def key_id(self):
        r"""Gets the key_id of this ListInferApiKeysRequest.

        **参数解释：** apikey_id，在[创建API_KEY](CreateInferApiKey.xml)时即可在返回体中获取，也可通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的apikey，其中key_id字段即为apikey_id。 **约束限制：** 不涉及。 **取值范围：** apikey_id只能由英文小写字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及。

        :return: The key_id of this ListInferApiKeysRequest.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this ListInferApiKeysRequest.

        **参数解释：** apikey_id，在[创建API_KEY](CreateInferApiKey.xml)时即可在返回体中获取，也可通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的apikey，其中key_id字段即为apikey_id。 **约束限制：** 不涉及。 **取值范围：** apikey_id只能由英文小写字母、数字组成，且长度为32个字符。 **默认取值：** 不涉及。

        :param key_id: The key_id of this ListInferApiKeysRequest.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def limit(self):
        r"""Gets the limit of this ListInferApiKeysRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :return: The limit of this ListInferApiKeysRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInferApiKeysRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :param limit: The limit of this ListInferApiKeysRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInferApiKeysRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。

        :return: The offset of this ListInferApiKeysRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInferApiKeysRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。

        :param offset: The offset of this ListInferApiKeysRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListInferApiKeysRequest.

        **参数解释：** 工作空间ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The workspace_id of this ListInferApiKeysRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListInferApiKeysRequest.

        **参数解释：** 工作空间ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param workspace_id: The workspace_id of this ListInferApiKeysRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def with_user_scope(self):
        r"""Gets the with_user_scope of this ListInferApiKeysRequest.

        **参数解释：** 是否查询鉴权范围为USER类型的API KEY，当同时指定service_id时可查询该服务所有可访问的API KEY。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** false。

        :return: The with_user_scope of this ListInferApiKeysRequest.
        :rtype: bool
        """
        return self._with_user_scope

    @with_user_scope.setter
    def with_user_scope(self, with_user_scope):
        r"""Sets the with_user_scope of this ListInferApiKeysRequest.

        **参数解释：** 是否查询鉴权范围为USER类型的API KEY，当同时指定service_id时可查询该服务所有可访问的API KEY。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** false。

        :param with_user_scope: The with_user_scope of this ListInferApiKeysRequest.
        :type with_user_scope: bool
        """
        self._with_user_scope = with_user_scope

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
        if not isinstance(other, ListInferApiKeysRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
