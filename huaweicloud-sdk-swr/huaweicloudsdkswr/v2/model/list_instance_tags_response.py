# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[RepositoryTag]',
        'total': 'int'
    }

    attribute_map = {
        'tags': 'tags',
        'total': 'total'
    }

    def __init__(self, tags=None, total=None):
        r"""ListInstanceTagsResponse

        The model defined in huaweicloud sdk

        :param tags: 制品Tag列表
        :type tags: list[:class:`huaweicloudsdkswr.v2.RepositoryTag`]
        :param total: 制品总数
        :type total: int
        """
        
        super(ListInstanceTagsResponse, self).__init__()

        self._tags = None
        self._total = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if total is not None:
            self.total = total

    @property
    def tags(self):
        r"""Gets the tags of this ListInstanceTagsResponse.

        制品Tag列表

        :return: The tags of this ListInstanceTagsResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.RepositoryTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListInstanceTagsResponse.

        制品Tag列表

        :param tags: The tags of this ListInstanceTagsResponse.
        :type tags: list[:class:`huaweicloudsdkswr.v2.RepositoryTag`]
        """
        self._tags = tags

    @property
    def total(self):
        r"""Gets the total of this ListInstanceTagsResponse.

        制品总数

        :return: The total of this ListInstanceTagsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceTagsResponse.

        制品总数

        :param total: The total of this ListInstanceTagsResponse.
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
        if not isinstance(other, ListInstanceTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
