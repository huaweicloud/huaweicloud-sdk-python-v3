# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2ProjectTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'tags': 'list[V2ProjectResourceTag]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total_count': 'total_count',
        'tags': 'tags',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, total_count=None, tags=None, x_request_id=None):
        r"""ListV2ProjectTagsResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**：项目标签总记录数。 **取值范围**：0~2147483647。 
        :type total_count: int
        :param tags: **参数解释**：项目标签列表，每个元素为一个V2ProjectResourceTag对象，包含key（标签键）和values（标签值列表）字段。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ProjectResourceTag`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._total_count = None
        self._tags = None
        self._x_request_id = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if tags is not None:
            self.tags = tags
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total_count(self):
        r"""Gets the total_count of this ListV2ProjectTagsResponse.

        **参数解释**：项目标签总记录数。 **取值范围**：0~2147483647。 

        :return: The total_count of this ListV2ProjectTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListV2ProjectTagsResponse.

        **参数解释**：项目标签总记录数。 **取值范围**：0~2147483647。 

        :param total_count: The total_count of this ListV2ProjectTagsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def tags(self):
        r"""Gets the tags of this ListV2ProjectTagsResponse.

        **参数解释**：项目标签列表，每个元素为一个V2ProjectResourceTag对象，包含key（标签键）和values（标签值列表）字段。 

        :return: The tags of this ListV2ProjectTagsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ProjectResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListV2ProjectTagsResponse.

        **参数解释**：项目标签列表，每个元素为一个V2ProjectResourceTag对象，包含key（标签键）和values（标签值列表）字段。 

        :param tags: The tags of this ListV2ProjectTagsResponse.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ProjectResourceTag`]
        """
        self._tags = tags

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListV2ProjectTagsResponse.

        :return: The x_request_id of this ListV2ProjectTagsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListV2ProjectTagsResponse.

        :param x_request_id: The x_request_id of this ListV2ProjectTagsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListV2ProjectTagsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListV2ProjectTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
