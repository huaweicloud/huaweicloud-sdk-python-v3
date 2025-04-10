# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLivePlatformProductsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'platform_id': 'str',
        'live_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'platform_id': 'platform_id',
        'live_id': 'live_id'
    }

    def __init__(self, offset=None, limit=None, platform_id=None, live_id=None):
        r"""ListLivePlatformProductsRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param platform_id: 第三方直播平台id
        :type platform_id: str
        :param live_id: 第三方直播平台直播Id。
        :type live_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._platform_id = None
        self._live_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.platform_id = platform_id
        self.live_id = live_id

    @property
    def offset(self):
        r"""Gets the offset of this ListLivePlatformProductsRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListLivePlatformProductsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLivePlatformProductsRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListLivePlatformProductsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLivePlatformProductsRequest.

        每页显示的条目数量。

        :return: The limit of this ListLivePlatformProductsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLivePlatformProductsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListLivePlatformProductsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def platform_id(self):
        r"""Gets the platform_id of this ListLivePlatformProductsRequest.

        第三方直播平台id

        :return: The platform_id of this ListLivePlatformProductsRequest.
        :rtype: str
        """
        return self._platform_id

    @platform_id.setter
    def platform_id(self, platform_id):
        r"""Sets the platform_id of this ListLivePlatformProductsRequest.

        第三方直播平台id

        :param platform_id: The platform_id of this ListLivePlatformProductsRequest.
        :type platform_id: str
        """
        self._platform_id = platform_id

    @property
    def live_id(self):
        r"""Gets the live_id of this ListLivePlatformProductsRequest.

        第三方直播平台直播Id。

        :return: The live_id of this ListLivePlatformProductsRequest.
        :rtype: str
        """
        return self._live_id

    @live_id.setter
    def live_id(self, live_id):
        r"""Sets the live_id of this ListLivePlatformProductsRequest.

        第三方直播平台直播Id。

        :param live_id: The live_id of this ListLivePlatformProductsRequest.
        :type live_id: str
        """
        self._live_id = live_id

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
        if not isinstance(other, ListLivePlatformProductsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
