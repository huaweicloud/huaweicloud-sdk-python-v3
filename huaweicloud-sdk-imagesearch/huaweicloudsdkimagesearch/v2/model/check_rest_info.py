# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'existed': 'bool',
        'item_info': 'ItemSource',
        'items': 'list[SearchItem]',
        'check_info': 'CheckInfo'
    }

    attribute_map = {
        'existed': 'existed',
        'item_info': 'item_info',
        'items': 'items',
        'check_info': 'check_info'
    }

    def __init__(self, existed=None, item_info=None, items=None, check_info=None):
        """CheckRestInfo

        The model defined in huaweicloud sdk

        :param existed: 数据是否存在，存在返回true，不存在返回false。仅在指定ID检查时包含该字段。
        :type existed: bool
        :param item_info: 
        :type item_info: :class:`huaweicloudsdkimagesearch.v2.ItemSource`
        :param items: 检查结果列表，仅在条件检查时包含该字段。
        :type items: list[:class:`huaweicloudsdkimagesearch.v2.SearchItem`]
        :param check_info: 
        :type check_info: :class:`huaweicloudsdkimagesearch.v2.CheckInfo`
        """
        
        

        self._existed = None
        self._item_info = None
        self._items = None
        self._check_info = None
        self.discriminator = None

        if existed is not None:
            self.existed = existed
        if item_info is not None:
            self.item_info = item_info
        if items is not None:
            self.items = items
        if check_info is not None:
            self.check_info = check_info

    @property
    def existed(self):
        """Gets the existed of this CheckRestInfo.

        数据是否存在，存在返回true，不存在返回false。仅在指定ID检查时包含该字段。

        :return: The existed of this CheckRestInfo.
        :rtype: bool
        """
        return self._existed

    @existed.setter
    def existed(self, existed):
        """Sets the existed of this CheckRestInfo.

        数据是否存在，存在返回true，不存在返回false。仅在指定ID检查时包含该字段。

        :param existed: The existed of this CheckRestInfo.
        :type existed: bool
        """
        self._existed = existed

    @property
    def item_info(self):
        """Gets the item_info of this CheckRestInfo.

        :return: The item_info of this CheckRestInfo.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.ItemSource`
        """
        return self._item_info

    @item_info.setter
    def item_info(self, item_info):
        """Sets the item_info of this CheckRestInfo.

        :param item_info: The item_info of this CheckRestInfo.
        :type item_info: :class:`huaweicloudsdkimagesearch.v2.ItemSource`
        """
        self._item_info = item_info

    @property
    def items(self):
        """Gets the items of this CheckRestInfo.

        检查结果列表，仅在条件检查时包含该字段。

        :return: The items of this CheckRestInfo.
        :rtype: list[:class:`huaweicloudsdkimagesearch.v2.SearchItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CheckRestInfo.

        检查结果列表，仅在条件检查时包含该字段。

        :param items: The items of this CheckRestInfo.
        :type items: list[:class:`huaweicloudsdkimagesearch.v2.SearchItem`]
        """
        self._items = items

    @property
    def check_info(self):
        """Gets the check_info of this CheckRestInfo.

        :return: The check_info of this CheckRestInfo.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.CheckInfo`
        """
        return self._check_info

    @check_info.setter
    def check_info(self, check_info):
        """Sets the check_info of this CheckRestInfo.

        :param check_info: The check_info of this CheckRestInfo.
        :type check_info: :class:`huaweicloudsdkimagesearch.v2.CheckInfo`
        """
        self._check_info = check_info

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
        if not isinstance(other, CheckRestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
