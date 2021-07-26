# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchVisionActiveCodeResponse(SdkResponse):


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
        'data': 'list[QueryVisionActiveCodeResultDTO]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'count': 'count',
        'data': 'data'
    }

    def __init__(self, offset=None, limit=None, count=None, data=None):
        """SearchVisionActiveCodeResponse - a model defined in huaweicloud sdk"""
        
        super(SearchVisionActiveCodeResponse, self).__init__()

        self._offset = None
        self._limit = None
        self._count = None
        self._data = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if count is not None:
            self.count = count
        if data is not None:
            self.data = data

    @property
    def offset(self):
        """Gets the offset of this SearchVisionActiveCodeResponse.

        页面起始页，从0开始

        :return: The offset of this SearchVisionActiveCodeResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchVisionActiveCodeResponse.

        页面起始页，从0开始

        :param offset: The offset of this SearchVisionActiveCodeResponse.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchVisionActiveCodeResponse.

        每页显示的条目数量。 默认值：10。 

        :return: The limit of this SearchVisionActiveCodeResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchVisionActiveCodeResponse.

        每页显示的条目数量。 默认值：10。 

        :param limit: The limit of this SearchVisionActiveCodeResponse.
        :type: int
        """
        self._limit = limit

    @property
    def count(self):
        """Gets the count of this SearchVisionActiveCodeResponse.

        总数量。

        :return: The count of this SearchVisionActiveCodeResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SearchVisionActiveCodeResponse.

        总数量。

        :param count: The count of this SearchVisionActiveCodeResponse.
        :type: int
        """
        self._count = count

    @property
    def data(self):
        """Gets the data of this SearchVisionActiveCodeResponse.


        :return: The data of this SearchVisionActiveCodeResponse.
        :rtype: list[QueryVisionActiveCodeResultDTO]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SearchVisionActiveCodeResponse.


        :param data: The data of this SearchVisionActiveCodeResponse.
        :type: list[QueryVisionActiveCodeResultDTO]
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SearchVisionActiveCodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
