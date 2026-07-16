# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferServicesRequest:

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
        'pool_id': 'str',
        'pool_name': 'str',
        'sort_key': 'str',
        'status': 'str',
        'name': 'str',
        'auth_type': 'str',
        'type': 'str',
        'description': 'str',
        'workspace_id': 'str',
        'user_name': 'str',
        'tags': 'str',
        'asset_id': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'id': 'id',
        'pool_id': 'pool_id',
        'pool_name': 'pool_name',
        'sort_key': 'sort_key',
        'status': 'status',
        'name': 'name',
        'auth_type': 'auth_type',
        'type': 'type',
        'description': 'description',
        'workspace_id': 'workspace_id',
        'user_name': 'user_name',
        'tags': 'tags',
        'asset_id': 'asset_id',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, id=None, pool_id=None, pool_name=None, sort_key=None, status=None, name=None, auth_type=None, type=None, description=None, workspace_id=None, user_name=None, tags=None, asset_id=None, sort_dir=None, limit=None, offset=None):
        r"""ListInferServicesRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。
        :type id: str
        :param pool_id: **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type pool_id: str
        :param pool_name: **参数解释：** 资源池name，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type pool_name: str
        :param sort_key: **参数解释：** 排序字段，多个字段以\&quot;,\&quot;分隔，支持create_at, update_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。
        :type sort_key: str
        :param status: **参数解释：** 服务当前状态，查询指定状态的过滤。默认不过滤。 **约束限制：** 不涉及。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。 **默认取值：** 不涉及。
        :type status: str
        :param name: **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义。 **约束限制：** 服务在删除之前名字不能重复。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。
        :type name: str
        :param auth_type: **参数解释：** 认证类型，默认不过滤。 **约束限制：** 不涉及。 **取值范围：** - TOKEN：IAM Token认证。 - API_KEY：API Key认证。 - NONE：无认证。 **默认取值：** 不涉及。
        :type auth_type: str
        :param type: **参数解释：** 推理服务类型。 **约束限制：** 不涉及。 **取值范围：** - REAL_TIME：在线服务。 - ASYNC_REAL_TIME：异步服务。 **默认取值：** 不涉及。
        :type type: str
        :param description: **参数解释：** 服务描述，模糊查询，默认不过滤。由用户[创建服务](CreateInferService.xml)时自行填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type description: str
        :param workspace_id: **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml) **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type workspace_id: str
        :param user_name: **参数解释：** 创建者，即创建服务的用户名。 **约束限制：** 不涉及。 **取值范围：** 创建服务的用户名。 **默认取值：** 不涉及。
        :type user_name: str
        :param tags: **参数解释：** 标签，查询指定标签的服务，默认不过滤。根据标签过滤service参数，格式：每组tag之间使用英文逗号分隔，每个标签内的key和value使用英文竖划线分隔，例：tag_key1|tag_value1,tag_key2|tag_value2 **约束限制：** 不以逗号，竖划线开头，不以逗号结尾，不出现连续的竖划线和逗号，允许中文、西文、葡文等语言以及空格_.:/&#x3D;+-@特殊字符，且字符间以逗号或者竖划线分隔。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tags: str
        :param asset_id: **参数解释：** 资产ID，查询使用了指定资产的服务，默认不过滤。可通过[资产管理][模型列表]获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type asset_id: str
        :param sort_dir: **参数解释：** 排序方式 **约束限制：** 不涉及。 **取值范围：** - ASC: 递增排序。 - DESC: 递减排序。 **默认取值：** DESC。
        :type sort_dir: str
        :param limit: **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。
        :type limit: int
        :param offset: **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。
        :type offset: int
        """
        
        

        self._id = None
        self._pool_id = None
        self._pool_name = None
        self._sort_key = None
        self._status = None
        self._name = None
        self._auth_type = None
        self._type = None
        self._description = None
        self._workspace_id = None
        self._user_name = None
        self._tags = None
        self._asset_id = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if pool_id is not None:
            self.pool_id = pool_id
        if pool_name is not None:
            self.pool_name = pool_name
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if auth_type is not None:
            self.auth_type = auth_type
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if user_name is not None:
            self.user_name = user_name
        if tags is not None:
            self.tags = tags
        if asset_id is not None:
            self.asset_id = asset_id
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def id(self):
        r"""Gets the id of this ListInferServicesRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :return: The id of this ListInferServicesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListInferServicesRequest.

        **参数解释：** 服务ID，在[创建服务](CreateInferService.xml)时即可在返回体中获取，也可通过[查询服务列表](ListInferServices.xml)获取当前用户拥有的服务，其中service_id字段即为服务ID。 **约束限制：** 不涉及。 **取值范围：** 服务ID。 **默认取值：** 不涉及。

        :param id: The id of this ListInferServicesRequest.
        :type id: str
        """
        self._id = id

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ListInferServicesRequest.

        **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The pool_id of this ListInferServicesRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ListInferServicesRequest.

        **参数解释：** 资源池ID，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param pool_id: The pool_id of this ListInferServicesRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def pool_name(self):
        r"""Gets the pool_name of this ListInferServicesRequest.

        **参数解释：** 资源池name，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The pool_name of this ListInferServicesRequest.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this ListInferServicesRequest.

        **参数解释：** 资源池name，查询指定资源池下的服务，默认不过滤。可通过[查询资源池列表](ShowPool.xml)获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param pool_name: The pool_name of this ListInferServicesRequest.
        :type pool_name: str
        """
        self._pool_name = pool_name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListInferServicesRequest.

        **参数解释：** 排序字段，多个字段以\",\"分隔，支持create_at, update_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。

        :return: The sort_key of this ListInferServicesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListInferServicesRequest.

        **参数解释：** 排序字段，多个字段以\",\"分隔，支持create_at, update_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。

        :param sort_key: The sort_key of this ListInferServicesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        r"""Gets the status of this ListInferServicesRequest.

        **参数解释：** 服务当前状态，查询指定状态的过滤。默认不过滤。 **约束限制：** 不涉及。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。 **默认取值：** 不涉及。

        :return: The status of this ListInferServicesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListInferServicesRequest.

        **参数解释：** 服务当前状态，查询指定状态的过滤。默认不过滤。 **约束限制：** 不涉及。 **取值范围：** - DEPLOYING：部署中。 - FAILED：失败。 - STOPPED：停止。 - RUNNING：运行中。 - DELETING：删除中。 - STOPPING：停止中。 - CONCERNING：告警。 - UPGRADING：升级中。 - ERROR：异常。 - INTERRUPTING：中断中。 **默认取值：** 不涉及。

        :param status: The status of this ListInferServicesRequest.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ListInferServicesRequest.

        **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义。 **约束限制：** 服务在删除之前名字不能重复。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。

        :return: The name of this ListInferServicesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListInferServicesRequest.

        **参数解释：** 服务名，用户在[创建服务](CreateInferService.xml)时自定义。 **约束限制：** 服务在删除之前名字不能重复。 **取值范围：** 支持1-128个字符，可以包含字母、汉字、数字、连字符和下划线。 **默认取值：** 不涉及。

        :param name: The name of this ListInferServicesRequest.
        :type name: str
        """
        self._name = name

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ListInferServicesRequest.

        **参数解释：** 认证类型，默认不过滤。 **约束限制：** 不涉及。 **取值范围：** - TOKEN：IAM Token认证。 - API_KEY：API Key认证。 - NONE：无认证。 **默认取值：** 不涉及。

        :return: The auth_type of this ListInferServicesRequest.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ListInferServicesRequest.

        **参数解释：** 认证类型，默认不过滤。 **约束限制：** 不涉及。 **取值范围：** - TOKEN：IAM Token认证。 - API_KEY：API Key认证。 - NONE：无认证。 **默认取值：** 不涉及。

        :param auth_type: The auth_type of this ListInferServicesRequest.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def type(self):
        r"""Gets the type of this ListInferServicesRequest.

        **参数解释：** 推理服务类型。 **约束限制：** 不涉及。 **取值范围：** - REAL_TIME：在线服务。 - ASYNC_REAL_TIME：异步服务。 **默认取值：** 不涉及。

        :return: The type of this ListInferServicesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListInferServicesRequest.

        **参数解释：** 推理服务类型。 **约束限制：** 不涉及。 **取值范围：** - REAL_TIME：在线服务。 - ASYNC_REAL_TIME：异步服务。 **默认取值：** 不涉及。

        :param type: The type of this ListInferServicesRequest.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this ListInferServicesRequest.

        **参数解释：** 服务描述，模糊查询，默认不过滤。由用户[创建服务](CreateInferService.xml)时自行填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The description of this ListInferServicesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListInferServicesRequest.

        **参数解释：** 服务描述，模糊查询，默认不过滤。由用户[创建服务](CreateInferService.xml)时自行填写。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param description: The description of this ListInferServicesRequest.
        :type description: str
        """
        self._description = description

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListInferServicesRequest.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml) **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The workspace_id of this ListInferServicesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListInferServicesRequest.

        **参数解释：** 工作空间ID。 **取值范围：** - 0：默认空间ID - 由数字和小写字母组成的32位字符：其他空间ID，可参考[工作空间创建](CreateWorkspace.xml) **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param workspace_id: The workspace_id of this ListInferServicesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ListInferServicesRequest.

        **参数解释：** 创建者，即创建服务的用户名。 **约束限制：** 不涉及。 **取值范围：** 创建服务的用户名。 **默认取值：** 不涉及。

        :return: The user_name of this ListInferServicesRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListInferServicesRequest.

        **参数解释：** 创建者，即创建服务的用户名。 **约束限制：** 不涉及。 **取值范围：** 创建服务的用户名。 **默认取值：** 不涉及。

        :param user_name: The user_name of this ListInferServicesRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def tags(self):
        r"""Gets the tags of this ListInferServicesRequest.

        **参数解释：** 标签，查询指定标签的服务，默认不过滤。根据标签过滤service参数，格式：每组tag之间使用英文逗号分隔，每个标签内的key和value使用英文竖划线分隔，例：tag_key1|tag_value1,tag_key2|tag_value2 **约束限制：** 不以逗号，竖划线开头，不以逗号结尾，不出现连续的竖划线和逗号，允许中文、西文、葡文等语言以及空格_.:/=+-@特殊字符，且字符间以逗号或者竖划线分隔。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tags of this ListInferServicesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListInferServicesRequest.

        **参数解释：** 标签，查询指定标签的服务，默认不过滤。根据标签过滤service参数，格式：每组tag之间使用英文逗号分隔，每个标签内的key和value使用英文竖划线分隔，例：tag_key1|tag_value1,tag_key2|tag_value2 **约束限制：** 不以逗号，竖划线开头，不以逗号结尾，不出现连续的竖划线和逗号，允许中文、西文、葡文等语言以及空格_.:/=+-@特殊字符，且字符间以逗号或者竖划线分隔。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tags: The tags of this ListInferServicesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ListInferServicesRequest.

        **参数解释：** 资产ID，查询使用了指定资产的服务，默认不过滤。可通过[资产管理][模型列表]获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The asset_id of this ListInferServicesRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ListInferServicesRequest.

        **参数解释：** 资产ID，查询使用了指定资产的服务，默认不过滤。可通过[资产管理][模型列表]获取。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param asset_id: The asset_id of this ListInferServicesRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListInferServicesRequest.

        **参数解释：** 排序方式 **约束限制：** 不涉及。 **取值范围：** - ASC: 递增排序。 - DESC: 递减排序。 **默认取值：** DESC。

        :return: The sort_dir of this ListInferServicesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListInferServicesRequest.

        **参数解释：** 排序方式 **约束限制：** 不涉及。 **取值范围：** - ASC: 递增排序。 - DESC: 递减排序。 **默认取值：** DESC。

        :param sort_dir: The sort_dir of this ListInferServicesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListInferServicesRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :return: The limit of this ListInferServicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInferServicesRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :param limit: The limit of this ListInferServicesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInferServicesRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。

        :return: The offset of this ListInferServicesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInferServicesRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。

        :param offset: The offset of this ListInferServicesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListInferServicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
