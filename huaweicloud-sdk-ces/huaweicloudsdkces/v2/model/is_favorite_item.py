# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsFavoriteItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_favorite': 'bool'
    }

    attribute_map = {
        'is_favorite': 'is_favorite'
    }

    def __init__(self, is_favorite=None):
        """IsFavoriteItem

        The model defined in huaweicloud sdk

        :param is_favorite: 监控看板是否标记收藏, true: 收藏, false: 未收藏
        :type is_favorite: bool
        """
        
        

        self._is_favorite = None
        self.discriminator = None

        if is_favorite is not None:
            self.is_favorite = is_favorite

    @property
    def is_favorite(self):
        """Gets the is_favorite of this IsFavoriteItem.

        监控看板是否标记收藏, true: 收藏, false: 未收藏

        :return: The is_favorite of this IsFavoriteItem.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """Sets the is_favorite of this IsFavoriteItem.

        监控看板是否标记收藏, true: 收藏, false: 未收藏

        :param is_favorite: The is_favorite of this IsFavoriteItem.
        :type is_favorite: bool
        """
        self._is_favorite = is_favorite

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
        if not isinstance(other, IsFavoriteItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
