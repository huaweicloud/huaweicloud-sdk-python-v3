# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchVisionActiveCodeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str',
        'dev_type': 'str'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'dev_type': 'devType'
    }

    def __init__(self, x_request_id=None, accept_language=None, offset=None, limit=None, search_key=None, dev_type=None):
        """SearchVisionActiveCodeRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param accept_language: 语言参数，默认为中文zh-CN，英文为en-US。
        :type accept_language: str
        :param offset: 查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 
        :type offset: int
        :param limit: 查询数量。 默认值：10。 
        :type limit: int
        :param search_key: 搜索条件,支持激活码、终端名称模糊搜索。
        :type search_key: str
        :param dev_type: 终端类型。 - idea-hub:智能协作大屏 - huawei-vision:智慧屏TV - welink-desktop(iwb):SmartRooms会议版 - smart-rooms：SmartRooms完整版 
        :type dev_type: str
        """
        
        

        self._x_request_id = None
        self._accept_language = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._dev_type = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key
        if dev_type is not None:
            self.dev_type = dev_type

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SearchVisionActiveCodeRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this SearchVisionActiveCodeRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchVisionActiveCodeRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this SearchVisionActiveCodeRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this SearchVisionActiveCodeRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :return: The accept_language of this SearchVisionActiveCodeRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this SearchVisionActiveCodeRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :param accept_language: The accept_language of this SearchVisionActiveCodeRequest.
        :type accept_language: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        """Gets the offset of this SearchVisionActiveCodeRequest.

        查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 

        :return: The offset of this SearchVisionActiveCodeRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchVisionActiveCodeRequest.

        查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 

        :param offset: The offset of this SearchVisionActiveCodeRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchVisionActiveCodeRequest.

        查询数量。 默认值：10。 

        :return: The limit of this SearchVisionActiveCodeRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchVisionActiveCodeRequest.

        查询数量。 默认值：10。 

        :param limit: The limit of this SearchVisionActiveCodeRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchVisionActiveCodeRequest.

        搜索条件,支持激活码、终端名称模糊搜索。

        :return: The search_key of this SearchVisionActiveCodeRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchVisionActiveCodeRequest.

        搜索条件,支持激活码、终端名称模糊搜索。

        :param search_key: The search_key of this SearchVisionActiveCodeRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def dev_type(self):
        """Gets the dev_type of this SearchVisionActiveCodeRequest.

        终端类型。 - idea-hub:智能协作大屏 - huawei-vision:智慧屏TV - welink-desktop(iwb):SmartRooms会议版 - smart-rooms：SmartRooms完整版 

        :return: The dev_type of this SearchVisionActiveCodeRequest.
        :rtype: str
        """
        return self._dev_type

    @dev_type.setter
    def dev_type(self, dev_type):
        """Sets the dev_type of this SearchVisionActiveCodeRequest.

        终端类型。 - idea-hub:智能协作大屏 - huawei-vision:智慧屏TV - welink-desktop(iwb):SmartRooms会议版 - smart-rooms：SmartRooms完整版 

        :param dev_type: The dev_type of this SearchVisionActiveCodeRequest.
        :type dev_type: str
        """
        self._dev_type = dev_type

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
        if not isinstance(other, SearchVisionActiveCodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
