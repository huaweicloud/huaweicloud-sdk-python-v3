# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsModelTuningTasksByTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'body': 'ListOpsModelTuningTasksByTagsRequestBody'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'body': 'body'
    }

    def __init__(self, offset=None, limit=None, body=None):
        r"""ListOpsModelTuningTasksByTagsRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 
        :type offset: int
        :param limit: **参数解释：** 查询记录数，表示单页返回的最大任务数，单位：条。 **约束限制：** 不涉及  **取值范围：** 1到1000的正整数。  **默认取值：** 无
        :type limit: int
        :param body: Body of the ListOpsModelTuningTasksByTagsRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.ListOpsModelTuningTasksByTagsRequestBody`
        """
        
        

        self._offset = None
        self._limit = None
        self._body = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if body is not None:
            self.body = body

    @property
    def offset(self):
        r"""Gets the offset of this ListOpsModelTuningTasksByTagsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :return: The offset of this ListOpsModelTuningTasksByTagsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpsModelTuningTasksByTagsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 必须为非负整数。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :param offset: The offset of this ListOpsModelTuningTasksByTagsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsModelTuningTasksByTagsRequest.

        **参数解释：** 查询记录数，表示单页返回的最大任务数，单位：条。 **约束限制：** 不涉及  **取值范围：** 1到1000的正整数。  **默认取值：** 无

        :return: The limit of this ListOpsModelTuningTasksByTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsModelTuningTasksByTagsRequest.

        **参数解释：** 查询记录数，表示单页返回的最大任务数，单位：条。 **约束限制：** 不涉及  **取值范围：** 1到1000的正整数。  **默认取值：** 无

        :param limit: The limit of this ListOpsModelTuningTasksByTagsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def body(self):
        r"""Gets the body of this ListOpsModelTuningTasksByTagsRequest.

        :return: The body of this ListOpsModelTuningTasksByTagsRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.ListOpsModelTuningTasksByTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListOpsModelTuningTasksByTagsRequest.

        :param body: The body of this ListOpsModelTuningTasksByTagsRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.ListOpsModelTuningTasksByTagsRequestBody`
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
        if not isinstance(other, ListOpsModelTuningTasksByTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
