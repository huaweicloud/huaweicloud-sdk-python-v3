# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TagResponse]',
        'errors': 'list[TagListErrorItem]'
    }

    attribute_map = {
        'tags': 'tags',
        'errors': 'errors'
    }

    def __init__(self, tags=None, errors=None):
        r"""ListTagsResponse

        The model defined in huaweicloud sdk

        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdktms.v1.TagResponse`]
        :param errors: 错误列表
        :type errors: list[:class:`huaweicloudsdktms.v1.TagListErrorItem`]
        """
        
        super(ListTagsResponse, self).__init__()

        self._tags = None
        self._errors = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if errors is not None:
            self.errors = errors

    @property
    def tags(self):
        r"""Gets the tags of this ListTagsResponse.

        标签列表

        :return: The tags of this ListTagsResponse.
        :rtype: list[:class:`huaweicloudsdktms.v1.TagResponse`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListTagsResponse.

        标签列表

        :param tags: The tags of this ListTagsResponse.
        :type tags: list[:class:`huaweicloudsdktms.v1.TagResponse`]
        """
        self._tags = tags

    @property
    def errors(self):
        r"""Gets the errors of this ListTagsResponse.

        错误列表

        :return: The errors of this ListTagsResponse.
        :rtype: list[:class:`huaweicloudsdktms.v1.TagListErrorItem`]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        r"""Sets the errors of this ListTagsResponse.

        错误列表

        :param errors: The errors of this ListTagsResponse.
        :type errors: list[:class:`huaweicloudsdktms.v1.TagListErrorItem`]
        """
        self._errors = errors

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
        if not isinstance(other, ListTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
