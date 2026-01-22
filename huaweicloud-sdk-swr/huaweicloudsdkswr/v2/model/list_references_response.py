# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReferencesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'next_marker': 'str',
        'has_more': 'bool',
        'tags': 'list[str]'
    }

    attribute_map = {
        'next_marker': 'next_marker',
        'has_more': 'has_more',
        'tags': 'tags'
    }

    def __init__(self, next_marker=None, has_more=None, tags=None):
        r"""ListReferencesResponse

        The model defined in huaweicloud sdk

        :param next_marker: 下一次分页查询的起始ID。如果未返回该值，则表示数据已查询完毕
        :type next_marker: str
        :param has_more: 分页查询时表示是否还有下一页的数据
        :type has_more: bool
        :param tags: 镜像版本列表
        :type tags: list[str]
        """
        
        super().__init__()

        self._next_marker = None
        self._has_more = None
        self._tags = None
        self.discriminator = None

        if next_marker is not None:
            self.next_marker = next_marker
        if has_more is not None:
            self.has_more = has_more
        if tags is not None:
            self.tags = tags

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListReferencesResponse.

        下一次分页查询的起始ID。如果未返回该值，则表示数据已查询完毕

        :return: The next_marker of this ListReferencesResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListReferencesResponse.

        下一次分页查询的起始ID。如果未返回该值，则表示数据已查询完毕

        :param next_marker: The next_marker of this ListReferencesResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def has_more(self):
        r"""Gets the has_more of this ListReferencesResponse.

        分页查询时表示是否还有下一页的数据

        :return: The has_more of this ListReferencesResponse.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        r"""Sets the has_more of this ListReferencesResponse.

        分页查询时表示是否还有下一页的数据

        :param has_more: The has_more of this ListReferencesResponse.
        :type has_more: bool
        """
        self._has_more = has_more

    @property
    def tags(self):
        r"""Gets the tags of this ListReferencesResponse.

        镜像版本列表

        :return: The tags of this ListReferencesResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListReferencesResponse.

        镜像版本列表

        :param tags: The tags of this ListReferencesResponse.
        :type tags: list[str]
        """
        self._tags = tags

    def to_dict(self):
        import warnings
        warnings.warn("ListReferencesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListReferencesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
