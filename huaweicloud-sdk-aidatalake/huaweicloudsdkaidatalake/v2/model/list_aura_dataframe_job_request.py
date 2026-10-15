# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuraDataframeJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'endpoint_id': 'str',
        'id': 'str',
        'limit': 'int',
        'offset': 'int',
        'status': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'endpoint_id': 'endpoint_id',
        'id': 'id',
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status'
    }

    def __init__(self, workspace_id=None, endpoint_id=None, id=None, limit=None, offset=None, status=None):
        r"""ListAuraDataframeJobRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param endpoint_id: **参数解释**：端点ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。
        :type endpoint_id: str
        :param id: **参数解释**：作业ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。
        :type id: str
        :param limit: **参数解释**：分页数量。 **约束限制**：不涉及。 **取值范围**：长度为1~100。 **默认取值**：不涉及。
        :type limit: int
        :param offset: **参数解释**：分页偏移。 **约束限制**：不涉及。 **取值范围**：长度为0~100。 **默认取值**：不涉及。
        :type offset: int
        :param status: **参数解释**：作业状态。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。
        :type status: str
        """
        
        

        self._workspace_id = None
        self._endpoint_id = None
        self._id = None
        self._limit = None
        self._offset = None
        self._status = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAuraDataframeJobRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ListAuraDataframeJobRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAuraDataframeJobRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListAuraDataframeJobRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ListAuraDataframeJobRequest.

        **参数解释**：端点ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :return: The endpoint_id of this ListAuraDataframeJobRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ListAuraDataframeJobRequest.

        **参数解释**：端点ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :param endpoint_id: The endpoint_id of this ListAuraDataframeJobRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def id(self):
        r"""Gets the id of this ListAuraDataframeJobRequest.

        **参数解释**：作业ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :return: The id of this ListAuraDataframeJobRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAuraDataframeJobRequest.

        **参数解释**：作业ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :param id: The id of this ListAuraDataframeJobRequest.
        :type id: str
        """
        self._id = id

    @property
    def limit(self):
        r"""Gets the limit of this ListAuraDataframeJobRequest.

        **参数解释**：分页数量。 **约束限制**：不涉及。 **取值范围**：长度为1~100。 **默认取值**：不涉及。

        :return: The limit of this ListAuraDataframeJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAuraDataframeJobRequest.

        **参数解释**：分页数量。 **约束限制**：不涉及。 **取值范围**：长度为1~100。 **默认取值**：不涉及。

        :param limit: The limit of this ListAuraDataframeJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAuraDataframeJobRequest.

        **参数解释**：分页偏移。 **约束限制**：不涉及。 **取值范围**：长度为0~100。 **默认取值**：不涉及。

        :return: The offset of this ListAuraDataframeJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAuraDataframeJobRequest.

        **参数解释**：分页偏移。 **约束限制**：不涉及。 **取值范围**：长度为0~100。 **默认取值**：不涉及。

        :param offset: The offset of this ListAuraDataframeJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListAuraDataframeJobRequest.

        **参数解释**：作业状态。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :return: The status of this ListAuraDataframeJobRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAuraDataframeJobRequest.

        **参数解释**：作业状态。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :param status: The status of this ListAuraDataframeJobRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListAuraDataframeJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
