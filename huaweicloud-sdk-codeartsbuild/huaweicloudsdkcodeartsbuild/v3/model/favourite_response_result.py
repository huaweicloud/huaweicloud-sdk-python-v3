# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FavouriteResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'favorite': 'bool'
    }

    attribute_map = {
        'favorite': 'favorite'
    }

    def __init__(self, favorite=None):
        r"""FavouriteResponseResult

        The model defined in huaweicloud sdk

        :param favorite: 是否收藏任务
        :type favorite: bool
        """
        
        

        self._favorite = None
        self.discriminator = None

        if favorite is not None:
            self.favorite = favorite

    @property
    def favorite(self):
        r"""Gets the favorite of this FavouriteResponseResult.

        是否收藏任务

        :return: The favorite of this FavouriteResponseResult.
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        r"""Sets the favorite of this FavouriteResponseResult.

        是否收藏任务

        :param favorite: The favorite of this FavouriteResponseResult.
        :type favorite: bool
        """
        self._favorite = favorite

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
        if not isinstance(other, FavouriteResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
