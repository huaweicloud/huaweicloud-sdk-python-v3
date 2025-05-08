# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptResourceTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[ScriptTag]',
        'total': 'int'
    }

    attribute_map = {
        'tags': 'tags',
        'total': 'total'
    }

    def __init__(self, tags=None, total=None):
        r"""ListScriptResourceTagsResponse

        The model defined in huaweicloud sdk

        :param tags: 
        :type tags: list[:class:`huaweicloudsdkcoc.v1.ScriptTag`]
        :param total: 总条数。
        :type total: int
        """
        
        super(ListScriptResourceTagsResponse, self).__init__()

        self._tags = None
        self._total = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if total is not None:
            self.total = total

    @property
    def tags(self):
        r"""Gets the tags of this ListScriptResourceTagsResponse.

        :return: The tags of this ListScriptResourceTagsResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScriptTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListScriptResourceTagsResponse.

        :param tags: The tags of this ListScriptResourceTagsResponse.
        :type tags: list[:class:`huaweicloudsdkcoc.v1.ScriptTag`]
        """
        self._tags = tags

    @property
    def total(self):
        r"""Gets the total of this ListScriptResourceTagsResponse.

        总条数。

        :return: The total of this ListScriptResourceTagsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListScriptResourceTagsResponse.

        总条数。

        :param total: The total of this ListScriptResourceTagsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListScriptResourceTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
