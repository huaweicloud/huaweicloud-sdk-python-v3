# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchRestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[SearchItem]',
        'search_info': 'SearchInfo',
        'image_info': 'SearchRestInfoImageInfo'
    }

    attribute_map = {
        'items': 'items',
        'search_info': 'search_info',
        'image_info': 'image_info'
    }

    def __init__(self, items=None, search_info=None, image_info=None):
        """SearchRestInfo

        The model defined in huaweicloud sdk

        :param items: 搜索结果列表。
        :type items: list[:class:`huaweicloudsdkimagesearch.v2.SearchItem`]
        :param search_info: 
        :type search_info: :class:`huaweicloudsdkimagesearch.v2.SearchInfo`
        :param image_info: 
        :type image_info: :class:`huaweicloudsdkimagesearch.v2.SearchRestInfoImageInfo`
        """
        
        

        self._items = None
        self._search_info = None
        self._image_info = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if search_info is not None:
            self.search_info = search_info
        if image_info is not None:
            self.image_info = image_info

    @property
    def items(self):
        """Gets the items of this SearchRestInfo.

        搜索结果列表。

        :return: The items of this SearchRestInfo.
        :rtype: list[:class:`huaweicloudsdkimagesearch.v2.SearchItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this SearchRestInfo.

        搜索结果列表。

        :param items: The items of this SearchRestInfo.
        :type items: list[:class:`huaweicloudsdkimagesearch.v2.SearchItem`]
        """
        self._items = items

    @property
    def search_info(self):
        """Gets the search_info of this SearchRestInfo.

        :return: The search_info of this SearchRestInfo.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.SearchInfo`
        """
        return self._search_info

    @search_info.setter
    def search_info(self, search_info):
        """Sets the search_info of this SearchRestInfo.

        :param search_info: The search_info of this SearchRestInfo.
        :type search_info: :class:`huaweicloudsdkimagesearch.v2.SearchInfo`
        """
        self._search_info = search_info

    @property
    def image_info(self):
        """Gets the image_info of this SearchRestInfo.

        :return: The image_info of this SearchRestInfo.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.SearchRestInfoImageInfo`
        """
        return self._image_info

    @image_info.setter
    def image_info(self, image_info):
        """Sets the image_info of this SearchRestInfo.

        :param image_info: The image_info of this SearchRestInfo.
        :type image_info: :class:`huaweicloudsdkimagesearch.v2.SearchRestInfoImageInfo`
        """
        self._image_info = image_info

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
        if not isinstance(other, SearchRestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
