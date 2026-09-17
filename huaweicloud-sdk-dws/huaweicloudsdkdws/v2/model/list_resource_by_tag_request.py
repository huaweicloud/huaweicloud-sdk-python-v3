# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceByTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'offset': 'str',
        'body': 'TagFilterRequestBody'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'body': 'body'
    }

    def __init__(self, limit=None, offset=None, body=None):
        r"""ListResourceByTagRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10
        :type limit: str
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0
        :type offset: str
        :param body: Body of the ListResourceByTagRequest
        :type body: :class:`huaweicloudsdkdws.v2.TagFilterRequestBody`
        """
        
        

        self._limit = None
        self._offset = None
        self._body = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if body is not None:
            self.body = body

    @property
    def limit(self):
        r"""Gets the limit of this ListResourceByTagRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10

        :return: The limit of this ListResourceByTagRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourceByTagRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 10

        :param limit: The limit of this ListResourceByTagRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListResourceByTagRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :return: The offset of this ListResourceByTagRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListResourceByTagRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :param offset: The offset of this ListResourceByTagRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def body(self):
        r"""Gets the body of this ListResourceByTagRequest.

        :return: The body of this ListResourceByTagRequest.
        :rtype: :class:`huaweicloudsdkdws.v2.TagFilterRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListResourceByTagRequest.

        :param body: The body of this ListResourceByTagRequest.
        :type body: :class:`huaweicloudsdkdws.v2.TagFilterRequestBody`
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
        if not isinstance(other, ListResourceByTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
