# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortalInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pub_name': 'str',
        'begin_time': 'datetime',
        'end_time': 'datetime',
        'state': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'pub_name': 'pub_name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'state': 'state',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, pub_name=None, begin_time=None, end_time=None, state=None, limit=None, offset=None):
        r"""ListPortalInfosRequest

        The model defined in huaweicloud sdk

        :param pub_name: 服务号名称。
        :type pub_name: str
        :param begin_time: 起始上线时间。格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type begin_time: datetime
        :param end_time: 截止上线时间。格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type end_time: datetime
        :param state: 主页状态。 - 1：未生效  - 2：已生效  - 3：已失效  - 4：服务号已冻结 
        :type state: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        """
        
        

        self._pub_name = None
        self._begin_time = None
        self._end_time = None
        self._state = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if pub_name is not None:
            self.pub_name = pub_name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if state is not None:
            self.state = state
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def pub_name(self):
        r"""Gets the pub_name of this ListPortalInfosRequest.

        服务号名称。

        :return: The pub_name of this ListPortalInfosRequest.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        r"""Sets the pub_name of this ListPortalInfosRequest.

        服务号名称。

        :param pub_name: The pub_name of this ListPortalInfosRequest.
        :type pub_name: str
        """
        self._pub_name = pub_name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListPortalInfosRequest.

        起始上线时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The begin_time of this ListPortalInfosRequest.
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListPortalInfosRequest.

        起始上线时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param begin_time: The begin_time of this ListPortalInfosRequest.
        :type begin_time: datetime
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListPortalInfosRequest.

        截止上线时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The end_time of this ListPortalInfosRequest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListPortalInfosRequest.

        截止上线时间。格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param end_time: The end_time of this ListPortalInfosRequest.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def state(self):
        r"""Gets the state of this ListPortalInfosRequest.

        主页状态。 - 1：未生效  - 2：已生效  - 3：已失效  - 4：服务号已冻结 

        :return: The state of this ListPortalInfosRequest.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListPortalInfosRequest.

        主页状态。 - 1：未生效  - 2：已生效  - 3：已失效  - 4：服务号已冻结 

        :param state: The state of this ListPortalInfosRequest.
        :type state: int
        """
        self._state = state

    @property
    def limit(self):
        r"""Gets the limit of this ListPortalInfosRequest.

        每页显示的条目数量。

        :return: The limit of this ListPortalInfosRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPortalInfosRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListPortalInfosRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPortalInfosRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ListPortalInfosRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPortalInfosRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListPortalInfosRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListPortalInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
