# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpComingWebinarsResponse(SdkResponse):

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
        'count': 'int',
        'data': 'list[OpenWebinarUpcomingInfo]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'count': 'count',
        'data': 'data'
    }

    def __init__(self, offset=None, limit=None, count=None, data=None):
        r"""ListUpComingWebinarsResponse

        The model defined in huaweicloud sdk

        :param offset: 偏移量。
        :type offset: int
        :param limit: 每页的记录数。
        :type limit: int
        :param count: 总记录数。
        :type count: int
        :param data: 即将召开研讨会信息列表。
        :type data: list[:class:`huaweicloudsdkmeeting.v1.OpenWebinarUpcomingInfo`]
        """
        
        super(ListUpComingWebinarsResponse, self).__init__()

        self._offset = None
        self._limit = None
        self._count = None
        self._data = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        self.count = count
        if data is not None:
            self.data = data

    @property
    def offset(self):
        r"""Gets the offset of this ListUpComingWebinarsResponse.

        偏移量。

        :return: The offset of this ListUpComingWebinarsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUpComingWebinarsResponse.

        偏移量。

        :param offset: The offset of this ListUpComingWebinarsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListUpComingWebinarsResponse.

        每页的记录数。

        :return: The limit of this ListUpComingWebinarsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUpComingWebinarsResponse.

        每页的记录数。

        :param limit: The limit of this ListUpComingWebinarsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def count(self):
        r"""Gets the count of this ListUpComingWebinarsResponse.

        总记录数。

        :return: The count of this ListUpComingWebinarsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListUpComingWebinarsResponse.

        总记录数。

        :param count: The count of this ListUpComingWebinarsResponse.
        :type count: int
        """
        self._count = count

    @property
    def data(self):
        r"""Gets the data of this ListUpComingWebinarsResponse.

        即将召开研讨会信息列表。

        :return: The data of this ListUpComingWebinarsResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.OpenWebinarUpcomingInfo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListUpComingWebinarsResponse.

        即将召开研讨会信息列表。

        :param data: The data of this ListUpComingWebinarsResponse.
        :type data: list[:class:`huaweicloudsdkmeeting.v1.OpenWebinarUpcomingInfo`]
        """
        self._data = data

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
        if not isinstance(other, ListUpComingWebinarsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
