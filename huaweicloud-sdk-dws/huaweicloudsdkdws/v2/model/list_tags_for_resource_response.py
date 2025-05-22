# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagsForResourceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sys_tags': 'list[Tag]',
        'count': 'int'
    }

    attribute_map = {
        'sys_tags': 'sys_tags',
        'count': 'count'
    }

    def __init__(self, sys_tags=None, count=None):
        r"""ListTagsForResourceResponse

        The model defined in huaweicloud sdk

        :param sys_tags: **参数解释**： 标签列表。 **取值范围**： 不涉及。
        :type sys_tags: list[:class:`huaweicloudsdkdws.v2.Tag`]
        :param count: **参数解释**： 标签数量。 **取值范围**： 不涉及。
        :type count: int
        """
        
        super(ListTagsForResourceResponse, self).__init__()

        self._sys_tags = None
        self._count = None
        self.discriminator = None

        if sys_tags is not None:
            self.sys_tags = sys_tags
        if count is not None:
            self.count = count

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ListTagsForResourceResponse.

        **参数解释**： 标签列表。 **取值范围**： 不涉及。

        :return: The sys_tags of this ListTagsForResourceResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Tag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ListTagsForResourceResponse.

        **参数解释**： 标签列表。 **取值范围**： 不涉及。

        :param sys_tags: The sys_tags of this ListTagsForResourceResponse.
        :type sys_tags: list[:class:`huaweicloudsdkdws.v2.Tag`]
        """
        self._sys_tags = sys_tags

    @property
    def count(self):
        r"""Gets the count of this ListTagsForResourceResponse.

        **参数解释**： 标签数量。 **取值范围**： 不涉及。

        :return: The count of this ListTagsForResourceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListTagsForResourceResponse.

        **参数解释**： 标签数量。 **取值范围**： 不涉及。

        :param count: The count of this ListTagsForResourceResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListTagsForResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
