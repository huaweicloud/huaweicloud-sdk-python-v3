# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInferServicesByTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'workspace_id': 'str',
        'body': 'QueryTmsResourceRequest'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'workspace_id': 'workspace_id',
        'body': 'body'
    }

    def __init__(self, limit=None, offset=None, workspace_id=None, body=None):
        r"""ListInferServicesByTagsRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。
        :type limit: int
        :param offset: **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。
        :type offset: int
        :param workspace_id: **参数解释：** 工作空间ID，workspaceId将会被设置为null。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type workspace_id: str
        :param body: Body of the ListInferServicesByTagsRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.QueryTmsResourceRequest`
        """
        
        

        self._limit = None
        self._offset = None
        self._workspace_id = None
        self._body = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def limit(self):
        r"""Gets the limit of this ListInferServicesByTagsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :return: The limit of this ListInferServicesByTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInferServicesByTagsRequest.

        **参数解释：** 指定返回的最大条目数。 **约束限制：** 不涉及。 **取值范围：** [1,500] **默认取值：** 10。

        :param limit: The limit of this ListInferServicesByTagsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInferServicesByTagsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。

        :return: The offset of this ListInferServicesByTagsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInferServicesByTagsRequest.

        **参数解释：** 分页列表查询的偏移量。 **约束限制：** offset必须是limit的整数倍。 **取值范围：** 不涉及。 **默认取值：** 0。

        :param offset: The offset of this ListInferServicesByTagsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListInferServicesByTagsRequest.

        **参数解释：** 工作空间ID，workspaceId将会被设置为null。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The workspace_id of this ListInferServicesByTagsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListInferServicesByTagsRequest.

        **参数解释：** 工作空间ID，workspaceId将会被设置为null。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param workspace_id: The workspace_id of this ListInferServicesByTagsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        r"""Gets the body of this ListInferServicesByTagsRequest.

        :return: The body of this ListInferServicesByTagsRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.QueryTmsResourceRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListInferServicesByTagsRequest.

        :param body: The body of this ListInferServicesByTagsRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.QueryTmsResourceRequest`
        """
        self._body = body

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
        if not isinstance(other, ListInferServicesByTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
