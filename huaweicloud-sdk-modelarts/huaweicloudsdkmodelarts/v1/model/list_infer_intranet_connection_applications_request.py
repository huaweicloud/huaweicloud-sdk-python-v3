# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferIntranetConnectionApplicationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scene': 'str',
        'status': 'str',
        'id': 'str',
        'service_id': 'str',
        'service_name': 'str',
        'vpc_id': 'str',
        'vpc_name': 'str',
        'pool_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'workspace_id': 'str',
        'sort_dir': 'str',
        'sort_key': 'str'
    }

    attribute_map = {
        'scene': 'scene',
        'status': 'status',
        'id': 'id',
        'service_id': 'service_id',
        'service_name': 'service_name',
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name',
        'pool_id': 'pool_id',
        'offset': 'offset',
        'limit': 'limit',
        'workspace_id': 'workspace_id',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key'
    }

    def __init__(self, scene=None, status=None, id=None, service_id=None, service_name=None, vpc_id=None, vpc_name=None, pool_id=None, offset=None, limit=None, workspace_id=None, sort_dir=None, sort_key=None):
        r"""ListInferIntranetConnectionApplicationsRequest

        The model defined in huaweicloud sdk

        :param scene: **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - POOL：用户资源池接入场景 - VPC：用户VPC网络接入场景 **默认取值：** 不涉及。
        :type scene: str
        :param status: **参数解释：** 内网接入状态，支持列表查询。 **约束限制：** 不涉及。 **取值范围：** - APPROVING：审批中 - REJECTED：拒绝 - CONNECTING：接入中 - CONNECTED：已接入 - CANCELED：已取消 - FAILED：失败 - DELETING：删除中 **默认取值：** 不涉及。
        :type status: str
        :param id: **参数解释：** 内网接入ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param service_id: **参数解释：** 服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type service_id: str
        :param service_name: **参数解释：** 服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type service_name: str
        :param vpc_id: **参数解释：** VPC网络的id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type vpc_id: str
        :param vpc_name: **参数解释：** VPC网络的名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type vpc_name: str
        :param pool_id: **参数解释：** 资源池的id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type pool_id: str
        :param offset: **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。
        :type offset: int
        :param limit: **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。
        :type limit: int
        :param workspace_id: **参数解释：** 工作空间ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type workspace_id: str
        :param sort_dir: **参数解释：** 排序方式 **约束限制：** 不涉及。 **取值范围：** - ASC: 递增排序。 - DESC: 递减排序。 **默认取值：** DESC。
        :type sort_dir: str
        :param sort_key: **参数解释：** 排序字段，多个字段以\&quot;,\&quot;分隔，支持create_at, update_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。
        :type sort_key: str
        """
        
        

        self._scene = None
        self._status = None
        self._id = None
        self._service_id = None
        self._service_name = None
        self._vpc_id = None
        self._vpc_name = None
        self._pool_id = None
        self._offset = None
        self._limit = None
        self._workspace_id = None
        self._sort_dir = None
        self._sort_key = None
        self.discriminator = None

        if scene is not None:
            self.scene = scene
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if service_id is not None:
            self.service_id = service_id
        if service_name is not None:
            self.service_name = service_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if pool_id is not None:
            self.pool_id = pool_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key

    @property
    def scene(self):
        r"""Gets the scene of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - POOL：用户资源池接入场景 - VPC：用户VPC网络接入场景 **默认取值：** 不涉及。

        :return: The scene of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - POOL：用户资源池接入场景 - VPC：用户VPC网络接入场景 **默认取值：** 不涉及。

        :param scene: The scene of this ListInferIntranetConnectionApplicationsRequest.
        :type scene: str
        """
        self._scene = scene

    @property
    def status(self):
        r"""Gets the status of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 内网接入状态，支持列表查询。 **约束限制：** 不涉及。 **取值范围：** - APPROVING：审批中 - REJECTED：拒绝 - CONNECTING：接入中 - CONNECTED：已接入 - CANCELED：已取消 - FAILED：失败 - DELETING：删除中 **默认取值：** 不涉及。

        :return: The status of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 内网接入状态，支持列表查询。 **约束限制：** 不涉及。 **取值范围：** - APPROVING：审批中 - REJECTED：拒绝 - CONNECTING：接入中 - CONNECTED：已接入 - CANCELED：已取消 - FAILED：失败 - DELETING：删除中 **默认取值：** 不涉及。

        :param status: The status of this ListInferIntranetConnectionApplicationsRequest.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        r"""Gets the id of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 内网接入ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 内网接入ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this ListInferIntranetConnectionApplicationsRequest.
        :type id: str
        """
        self._id = id

    @property
    def service_id(self):
        r"""Gets the service_id of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The service_id of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param service_id: The service_id of this ListInferIntranetConnectionApplicationsRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def service_name(self):
        r"""Gets the service_name of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The service_name of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param service_name: The service_name of this ListInferIntranetConnectionApplicationsRequest.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** VPC网络的id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The vpc_id of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** VPC网络的id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param vpc_id: The vpc_id of this ListInferIntranetConnectionApplicationsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** VPC网络的名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The vpc_name of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** VPC网络的名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param vpc_name: The vpc_name of this ListInferIntranetConnectionApplicationsRequest.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 资源池的id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The pool_id of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 资源池的id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param pool_id: The pool_id of this ListInferIntranetConnectionApplicationsRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。

        :return: The offset of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。

        :param offset: The offset of this ListInferIntranetConnectionApplicationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :return: The limit of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :param limit: The limit of this ListInferIntranetConnectionApplicationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 工作空间ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The workspace_id of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 工作空间ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param workspace_id: The workspace_id of this ListInferIntranetConnectionApplicationsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 排序方式 **约束限制：** 不涉及。 **取值范围：** - ASC: 递增排序。 - DESC: 递减排序。 **默认取值：** DESC。

        :return: The sort_dir of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 排序方式 **约束限制：** 不涉及。 **取值范围：** - ASC: 递增排序。 - DESC: 递减排序。 **默认取值：** DESC。

        :param sort_dir: The sort_dir of this ListInferIntranetConnectionApplicationsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 排序字段，多个字段以\",\"分隔，支持create_at, update_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。

        :return: The sort_key of this ListInferIntranetConnectionApplicationsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListInferIntranetConnectionApplicationsRequest.

        **参数解释：** 排序字段，多个字段以\",\"分隔，支持create_at, update_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - create_at：按创建时间排序。 - update_at：按更新时间排序。 **默认取值：** update_at。

        :param sort_key: The sort_key of this ListInferIntranetConnectionApplicationsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

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
        if not isinstance(other, ListInferIntranetConnectionApplicationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
