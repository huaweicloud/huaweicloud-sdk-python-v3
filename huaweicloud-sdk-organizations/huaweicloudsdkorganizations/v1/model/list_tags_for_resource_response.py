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
        'tags': 'list[TagDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'tags': 'tags',
        'page_info': 'page_info'
    }

    def __init__(self, tags=None, page_info=None):
        """ListTagsForResourceResponse

        The model defined in huaweicloud sdk

        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        
        super(ListTagsForResourceResponse, self).__init__()

        self._tags = None
        self._page_info = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if page_info is not None:
            self.page_info = page_info

    @property
    def tags(self):
        """Gets the tags of this ListTagsForResourceResponse.

        标签列表。

        :return: The tags of this ListTagsForResourceResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListTagsForResourceResponse.

        标签列表。

        :param tags: The tags of this ListTagsForResourceResponse.
        :type tags: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        self._tags = tags

    @property
    def page_info(self):
        """Gets the page_info of this ListTagsForResourceResponse.

        :return: The page_info of this ListTagsForResourceResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListTagsForResourceResponse.

        :param page_info: The page_info of this ListTagsForResourceResponse.
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        self._page_info = page_info

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
