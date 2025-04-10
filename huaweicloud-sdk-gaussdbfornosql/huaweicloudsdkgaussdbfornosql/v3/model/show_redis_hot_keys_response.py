# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRedisHotKeysResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keys': 'list[HotKeysInfoResponseBody]',
        'count': 'int'
    }

    attribute_map = {
        'keys': 'keys',
        'count': 'count'
    }

    def __init__(self, keys=None, count=None):
        r"""ShowRedisHotKeysResponse

        The model defined in huaweicloud sdk

        :param keys: 查询到的热Key列表。
        :type keys: list[:class:`huaweicloudsdkgaussdbfornosql.v3.HotKeysInfoResponseBody`]
        :param count: 总数。
        :type count: int
        """
        
        super(ShowRedisHotKeysResponse, self).__init__()

        self._keys = None
        self._count = None
        self.discriminator = None

        if keys is not None:
            self.keys = keys
        if count is not None:
            self.count = count

    @property
    def keys(self):
        r"""Gets the keys of this ShowRedisHotKeysResponse.

        查询到的热Key列表。

        :return: The keys of this ShowRedisHotKeysResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.HotKeysInfoResponseBody`]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        r"""Sets the keys of this ShowRedisHotKeysResponse.

        查询到的热Key列表。

        :param keys: The keys of this ShowRedisHotKeysResponse.
        :type keys: list[:class:`huaweicloudsdkgaussdbfornosql.v3.HotKeysInfoResponseBody`]
        """
        self._keys = keys

    @property
    def count(self):
        r"""Gets the count of this ShowRedisHotKeysResponse.

        总数。

        :return: The count of this ShowRedisHotKeysResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowRedisHotKeysResponse.

        总数。

        :param count: The count of this ShowRedisHotKeysResponse.
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
        if not isinstance(other, ShowRedisHotKeysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
