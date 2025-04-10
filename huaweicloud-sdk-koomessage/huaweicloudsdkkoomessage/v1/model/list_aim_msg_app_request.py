# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimMsgAppRequest:

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
        'app_name': 'str',
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'app_name': 'app_name',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, offset=None, limit=None, app_name=None, status=None, begin_time=None, end_time=None):
        r"""ListAimMsgAppRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param app_name: 应用名称。
        :type app_name: str
        :param status: 应用状态。
        :type status: str
        :param begin_time: 创建时间筛选-开始时间。格式为：2019-10-12T07:20:50Z。
        :type begin_time: str
        :param end_time: 创建时间筛选-结束时间。格式为：2019-10-12T07:20:50Z。
        :type end_time: str
        """
        
        

        self._offset = None
        self._limit = None
        self._app_name = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if app_name is not None:
            self.app_name = app_name
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListAimMsgAppRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ListAimMsgAppRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAimMsgAppRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListAimMsgAppRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAimMsgAppRequest.

        每页显示的条目数量。

        :return: The limit of this ListAimMsgAppRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAimMsgAppRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListAimMsgAppRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def app_name(self):
        r"""Gets the app_name of this ListAimMsgAppRequest.

        应用名称。

        :return: The app_name of this ListAimMsgAppRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListAimMsgAppRequest.

        应用名称。

        :param app_name: The app_name of this ListAimMsgAppRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def status(self):
        r"""Gets the status of this ListAimMsgAppRequest.

        应用状态。

        :return: The status of this ListAimMsgAppRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAimMsgAppRequest.

        应用状态。

        :param status: The status of this ListAimMsgAppRequest.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListAimMsgAppRequest.

        创建时间筛选-开始时间。格式为：2019-10-12T07:20:50Z。

        :return: The begin_time of this ListAimMsgAppRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListAimMsgAppRequest.

        创建时间筛选-开始时间。格式为：2019-10-12T07:20:50Z。

        :param begin_time: The begin_time of this ListAimMsgAppRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAimMsgAppRequest.

        创建时间筛选-结束时间。格式为：2019-10-12T07:20:50Z。

        :return: The end_time of this ListAimMsgAppRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAimMsgAppRequest.

        创建时间筛选-结束时间。格式为：2019-10-12T07:20:50Z。

        :param end_time: The end_time of this ListAimMsgAppRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListAimMsgAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
