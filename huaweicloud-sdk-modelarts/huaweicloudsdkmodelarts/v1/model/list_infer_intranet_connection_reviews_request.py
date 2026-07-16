# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferIntranetConnectionReviewsRequest:

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
        'id': 'str',
        'applicant_domain_id': 'str',
        'service_id': 'str',
        'applicant_user_name': 'str',
        'service_name': 'str',
        'vpc_name': 'str',
        'vpc_id': 'str',
        'pool_id': 'str',
        'sort_key': 'str',
        'limit': 'int',
        'offset': 'int',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'scene': 'scene',
        'id': 'id',
        'applicant_domain_id': 'applicant_domain_id',
        'service_id': 'service_id',
        'applicant_user_name': 'applicant_user_name',
        'service_name': 'service_name',
        'vpc_name': 'vpc_name',
        'vpc_id': 'vpc_id',
        'pool_id': 'pool_id',
        'sort_key': 'sort_key',
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, scene=None, id=None, applicant_domain_id=None, service_id=None, applicant_user_name=None, service_name=None, vpc_name=None, vpc_id=None, pool_id=None, sort_key=None, limit=None, offset=None, status=None, type=None):
        r"""ListInferIntranetConnectionReviewsRequest

        The model defined in huaweicloud sdk

        :param scene: **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - POOL：用户资源池接入场景 - VPC：用户VPC网络接入场景 **默认取值：** 不涉及。
        :type scene: str
        :param id: **参数解释：** 内网接入id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param applicant_domain_id: **参数解释：** 申请方domain ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type applicant_domain_id: str
        :param service_id: **参数解释：** 服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type service_id: str
        :param applicant_user_name: **参数解释：** 申请方用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type applicant_user_name: str
        :param service_name: **参数解释：** 服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type service_name: str
        :param vpc_name: **参数解释：** VPC名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type vpc_name: str
        :param vpc_id: **参数解释：** VPC ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type vpc_id: str
        :param pool_id: **参数解释：** 资源池ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type pool_id: str
        :param sort_key: **参数解释：** 排序字段，支持update_at、create_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - update_at：按更新时间排序。 - create_at：按创建时间排序。 **默认取值：** update_at。
        :type sort_key: str
        :param limit: **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。
        :type limit: int
        :param offset: **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。
        :type offset: int
        :param status: **参数解释：** 申请状态。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type status: str
        :param type: **参数解释：** 内网申请类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type type: str
        """
        
        

        self._scene = None
        self._id = None
        self._applicant_domain_id = None
        self._service_id = None
        self._applicant_user_name = None
        self._service_name = None
        self._vpc_name = None
        self._vpc_id = None
        self._pool_id = None
        self._sort_key = None
        self._limit = None
        self._offset = None
        self._status = None
        self._type = None
        self.discriminator = None

        if scene is not None:
            self.scene = scene
        if id is not None:
            self.id = id
        if applicant_domain_id is not None:
            self.applicant_domain_id = applicant_domain_id
        if service_id is not None:
            self.service_id = service_id
        if applicant_user_name is not None:
            self.applicant_user_name = applicant_user_name
        if service_name is not None:
            self.service_name = service_name
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if pool_id is not None:
            self.pool_id = pool_id
        if sort_key is not None:
            self.sort_key = sort_key
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def scene(self):
        r"""Gets the scene of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - POOL：用户资源池接入场景 - VPC：用户VPC网络接入场景 **默认取值：** 不涉及。

        :return: The scene of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 内网访问场景。 **约束限制：** 不涉及。 **取值范围：** - POOL：用户资源池接入场景 - VPC：用户VPC网络接入场景 **默认取值：** 不涉及。

        :param scene: The scene of this ListInferIntranetConnectionReviewsRequest.
        :type scene: str
        """
        self._scene = scene

    @property
    def id(self):
        r"""Gets the id of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 内网接入id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 内网接入id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this ListInferIntranetConnectionReviewsRequest.
        :type id: str
        """
        self._id = id

    @property
    def applicant_domain_id(self):
        r"""Gets the applicant_domain_id of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 申请方domain ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The applicant_domain_id of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._applicant_domain_id

    @applicant_domain_id.setter
    def applicant_domain_id(self, applicant_domain_id):
        r"""Sets the applicant_domain_id of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 申请方domain ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param applicant_domain_id: The applicant_domain_id of this ListInferIntranetConnectionReviewsRequest.
        :type applicant_domain_id: str
        """
        self._applicant_domain_id = applicant_domain_id

    @property
    def service_id(self):
        r"""Gets the service_id of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The service_id of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        r"""Sets the service_id of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 服务ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param service_id: The service_id of this ListInferIntranetConnectionReviewsRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def applicant_user_name(self):
        r"""Gets the applicant_user_name of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 申请方用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The applicant_user_name of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._applicant_user_name

    @applicant_user_name.setter
    def applicant_user_name(self, applicant_user_name):
        r"""Sets the applicant_user_name of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 申请方用户名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param applicant_user_name: The applicant_user_name of this ListInferIntranetConnectionReviewsRequest.
        :type applicant_user_name: str
        """
        self._applicant_user_name = applicant_user_name

    @property
    def service_name(self):
        r"""Gets the service_name of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The service_name of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param service_name: The service_name of this ListInferIntranetConnectionReviewsRequest.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** VPC名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The vpc_name of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** VPC名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param vpc_name: The vpc_name of this ListInferIntranetConnectionReviewsRequest.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** VPC ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The vpc_id of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** VPC ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param vpc_id: The vpc_id of this ListInferIntranetConnectionReviewsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 资源池ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The pool_id of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 资源池ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param pool_id: The pool_id of this ListInferIntranetConnectionReviewsRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 排序字段，支持update_at、create_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - update_at：按更新时间排序。 - create_at：按创建时间排序。 **默认取值：** update_at。

        :return: The sort_key of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 排序字段，支持update_at、create_at，默认值update_at。 **约束限制：** 不涉及。 **取值范围：** - update_at：按更新时间排序。 - create_at：按创建时间排序。 **默认取值：** update_at。

        :param sort_key: The sort_key of this ListInferIntranetConnectionReviewsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def limit(self):
        r"""Gets the limit of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :return: The limit of this ListInferIntranetConnectionReviewsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :param limit: The limit of this ListInferIntranetConnectionReviewsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。

        :return: The offset of this ListInferIntranetConnectionReviewsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。

        :param offset: The offset of this ListInferIntranetConnectionReviewsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 申请状态。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The status of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 申请状态。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param status: The status of this ListInferIntranetConnectionReviewsRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 内网申请类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The type of this ListInferIntranetConnectionReviewsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListInferIntranetConnectionReviewsRequest.

        **参数解释：** 内网申请类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param type: The type of this ListInferIntranetConnectionReviewsRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListInferIntranetConnectionReviewsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
