# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Category:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_meta_list': 'list[str]',
        'item_meta_list': 'list[str]'
    }

    attribute_map = {
        'user_meta_list': 'user_meta_list',
        'item_meta_list': 'item_meta_list'
    }

    def __init__(self, user_meta_list=None, item_meta_list=None):
        r"""Category

        The model defined in huaweicloud sdk

        :param user_meta_list: 用户特征。
        :type user_meta_list: list[str]
        :param item_meta_list: 物品特征。
        :type item_meta_list: list[str]
        """
        
        

        self._user_meta_list = None
        self._item_meta_list = None
        self.discriminator = None

        if user_meta_list is not None:
            self.user_meta_list = user_meta_list
        if item_meta_list is not None:
            self.item_meta_list = item_meta_list

    @property
    def user_meta_list(self):
        r"""Gets the user_meta_list of this Category.

        用户特征。

        :return: The user_meta_list of this Category.
        :rtype: list[str]
        """
        return self._user_meta_list

    @user_meta_list.setter
    def user_meta_list(self, user_meta_list):
        r"""Sets the user_meta_list of this Category.

        用户特征。

        :param user_meta_list: The user_meta_list of this Category.
        :type user_meta_list: list[str]
        """
        self._user_meta_list = user_meta_list

    @property
    def item_meta_list(self):
        r"""Gets the item_meta_list of this Category.

        物品特征。

        :return: The item_meta_list of this Category.
        :rtype: list[str]
        """
        return self._item_meta_list

    @item_meta_list.setter
    def item_meta_list(self, item_meta_list):
        r"""Sets the item_meta_list of this Category.

        物品特征。

        :param item_meta_list: The item_meta_list of this Category.
        :type item_meta_list: list[str]
        """
        self._item_meta_list = item_meta_list

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
        if not isinstance(other, Category):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
