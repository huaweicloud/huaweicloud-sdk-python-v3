# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFavoriteResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'favorites': 'list[FavoriteDto]',
        'count': 'int'
    }

    attribute_map = {
        'favorites': 'favorites',
        'count': 'count'
    }

    def __init__(self, favorites=None, count=None):
        r"""ListFavoriteResponse

        The model defined in huaweicloud sdk

        :param favorites: 收藏列表。
        :type favorites: list[:class:`huaweicloudsdkeihealth.v1.FavoriteDto`]
        :param count: 收藏总数。
        :type count: int
        """
        
        super(ListFavoriteResponse, self).__init__()

        self._favorites = None
        self._count = None
        self.discriminator = None

        if favorites is not None:
            self.favorites = favorites
        if count is not None:
            self.count = count

    @property
    def favorites(self):
        r"""Gets the favorites of this ListFavoriteResponse.

        收藏列表。

        :return: The favorites of this ListFavoriteResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.FavoriteDto`]
        """
        return self._favorites

    @favorites.setter
    def favorites(self, favorites):
        r"""Sets the favorites of this ListFavoriteResponse.

        收藏列表。

        :param favorites: The favorites of this ListFavoriteResponse.
        :type favorites: list[:class:`huaweicloudsdkeihealth.v1.FavoriteDto`]
        """
        self._favorites = favorites

    @property
    def count(self):
        r"""Gets the count of this ListFavoriteResponse.

        收藏总数。

        :return: The count of this ListFavoriteResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListFavoriteResponse.

        收藏总数。

        :param count: The count of this ListFavoriteResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListFavoriteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
