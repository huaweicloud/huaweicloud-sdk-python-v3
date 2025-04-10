# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[DeleteRestInfoItems]',
        'delete_info': 'DeleteInfo'
    }

    attribute_map = {
        'items': 'items',
        'delete_info': 'delete_info'
    }

    def __init__(self, items=None, delete_info=None):
        r"""DeleteRestInfo

        The model defined in huaweicloud sdk

        :param items: 删除数据列表。
        :type items: list[:class:`huaweicloudsdkimagesearch.v2.DeleteRestInfoItems`]
        :param delete_info: 
        :type delete_info: :class:`huaweicloudsdkimagesearch.v2.DeleteInfo`
        """
        
        

        self._items = None
        self._delete_info = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if delete_info is not None:
            self.delete_info = delete_info

    @property
    def items(self):
        r"""Gets the items of this DeleteRestInfo.

        删除数据列表。

        :return: The items of this DeleteRestInfo.
        :rtype: list[:class:`huaweicloudsdkimagesearch.v2.DeleteRestInfoItems`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this DeleteRestInfo.

        删除数据列表。

        :param items: The items of this DeleteRestInfo.
        :type items: list[:class:`huaweicloudsdkimagesearch.v2.DeleteRestInfoItems`]
        """
        self._items = items

    @property
    def delete_info(self):
        r"""Gets the delete_info of this DeleteRestInfo.

        :return: The delete_info of this DeleteRestInfo.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.DeleteInfo`
        """
        return self._delete_info

    @delete_info.setter
    def delete_info(self, delete_info):
        r"""Sets the delete_info of this DeleteRestInfo.

        :param delete_info: The delete_info of this DeleteRestInfo.
        :type delete_info: :class:`huaweicloudsdkimagesearch.v2.DeleteInfo`
        """
        self._delete_info = delete_info

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
        if not isinstance(other, DeleteRestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
