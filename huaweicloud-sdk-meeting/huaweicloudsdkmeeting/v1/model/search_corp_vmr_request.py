# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchCorpVmrRequest:

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
        'vmr_mode': 'int',
        'status': 'int'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'vmr_mode': 'vmrMode',
        'status': 'status'
    }

    def __init__(self, x_request_id=None, accept_language=None, offset=None, limit=None, search_key=None, vmr_mode=None, status=None):
        r"""SearchCorpVmrRequest

        The model defined in huaweicloud sdk

        :param x_request_id: 请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。
        :type x_request_id: str
        :param accept_language: 语言参数，默认为中文zh-CN，英文为en-US。
        :type accept_language: str
        :param offset: 查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 
        :type offset: int
        :param limit: 查询数量。 默认值：10。 
        :type limit: int
        :param search_key: 搜索条件。支持云会议室名称、ID及分配的用户、硬终端名称模糊搜索。
        :type search_key: str
        :param vmr_mode: VMR模式。不填则默认为云会议室。 - 1：云会议室 - 2：网络研讨会 
        :type vmr_mode: int
        :param status: 云会议室状态。不填则查询所有。 * 0：正常 * 1：停用 * 2：未分配 
        :type status: int
        """
        
        

        self._x_request_id = None
        self._accept_language = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._vmr_mode = None
        self._status = None
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
        if vmr_mode is not None:
            self.vmr_mode = vmr_mode
        if status is not None:
            self.status = status

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this SearchCorpVmrRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :return: The x_request_id of this SearchCorpVmrRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this SearchCorpVmrRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用UUID，若不携带，则后台自动生成。

        :param x_request_id: The x_request_id of this SearchCorpVmrRequest.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        r"""Gets the accept_language of this SearchCorpVmrRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :return: The accept_language of this SearchCorpVmrRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        r"""Sets the accept_language of this SearchCorpVmrRequest.

        语言参数，默认为中文zh-CN，英文为en-US。

        :param accept_language: The accept_language of this SearchCorpVmrRequest.
        :type accept_language: str
        """
        self._accept_language = accept_language

    @property
    def offset(self):
        r"""Gets the offset of this SearchCorpVmrRequest.

        查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 

        :return: The offset of this SearchCorpVmrRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchCorpVmrRequest.

        查询偏移量,若超过最大数量，则返回最后一页的数据。 默认值：0。 

        :param offset: The offset of this SearchCorpVmrRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this SearchCorpVmrRequest.

        查询数量。 默认值：10。 

        :return: The limit of this SearchCorpVmrRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchCorpVmrRequest.

        查询数量。 默认值：10。 

        :param limit: The limit of this SearchCorpVmrRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_key(self):
        r"""Gets the search_key of this SearchCorpVmrRequest.

        搜索条件。支持云会议室名称、ID及分配的用户、硬终端名称模糊搜索。

        :return: The search_key of this SearchCorpVmrRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        r"""Sets the search_key of this SearchCorpVmrRequest.

        搜索条件。支持云会议室名称、ID及分配的用户、硬终端名称模糊搜索。

        :param search_key: The search_key of this SearchCorpVmrRequest.
        :type search_key: str
        """
        self._search_key = search_key

    @property
    def vmr_mode(self):
        r"""Gets the vmr_mode of this SearchCorpVmrRequest.

        VMR模式。不填则默认为云会议室。 - 1：云会议室 - 2：网络研讨会 

        :return: The vmr_mode of this SearchCorpVmrRequest.
        :rtype: int
        """
        return self._vmr_mode

    @vmr_mode.setter
    def vmr_mode(self, vmr_mode):
        r"""Sets the vmr_mode of this SearchCorpVmrRequest.

        VMR模式。不填则默认为云会议室。 - 1：云会议室 - 2：网络研讨会 

        :param vmr_mode: The vmr_mode of this SearchCorpVmrRequest.
        :type vmr_mode: int
        """
        self._vmr_mode = vmr_mode

    @property
    def status(self):
        r"""Gets the status of this SearchCorpVmrRequest.

        云会议室状态。不填则查询所有。 * 0：正常 * 1：停用 * 2：未分配 

        :return: The status of this SearchCorpVmrRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SearchCorpVmrRequest.

        云会议室状态。不填则查询所有。 * 0：正常 * 1：停用 * 2：未分配 

        :param status: The status of this SearchCorpVmrRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, SearchCorpVmrRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
