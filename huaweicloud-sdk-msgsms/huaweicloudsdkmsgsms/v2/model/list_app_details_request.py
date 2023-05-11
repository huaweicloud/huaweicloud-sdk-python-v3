# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'region': 'str',
        'sort_dir': 'str',
        'sort_key': 'str',
        'status': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'region': 'region',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key',
        'status': 'status'
    }

    def __init__(self, app_name=None, start_time=None, end_time=None, limit=None, offset=None, region=None, sort_dir=None, sort_key=None, status=None):
        """ListAppDetailsRequest

        The model defined in huaweicloud sdk

        :param app_name: 应用名称
        :type app_name: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param limit: 数量
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param region: 地域 1. cn：国内 2. intl：国际
        :type region: str
        :param sort_dir: 排序方式 1. desc：降序 2. asc：升序
        :type sort_dir: str
        :param sort_key: 排序字段
        :type sort_key: str
        :param status: 应用状态   1. CREATED：待上线。应用暂未创建成功，请稍候。   2. SUSPENDED：暂停。无法发起业务请求。当客户所发短信内容触发业务违规，或客户申请退订短信业务时，运营经理会将客户短信应用暂停。   3. LAUNCHED：正常。应用添加成功，可以正常使用。
        :type status: str
        """
        
        

        self._app_name = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._region = None
        self._sort_dir = None
        self._sort_key = None
        self._status = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if region is not None:
            self.region = region
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key
        if status is not None:
            self.status = status

    @property
    def app_name(self):
        """Gets the app_name of this ListAppDetailsRequest.

        应用名称

        :return: The app_name of this ListAppDetailsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListAppDetailsRequest.

        应用名称

        :param app_name: The app_name of this ListAppDetailsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def start_time(self):
        """Gets the start_time of this ListAppDetailsRequest.

        开始时间

        :return: The start_time of this ListAppDetailsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListAppDetailsRequest.

        开始时间

        :param start_time: The start_time of this ListAppDetailsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAppDetailsRequest.

        结束时间

        :return: The end_time of this ListAppDetailsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAppDetailsRequest.

        结束时间

        :param end_time: The end_time of this ListAppDetailsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListAppDetailsRequest.

        数量

        :return: The limit of this ListAppDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppDetailsRequest.

        数量

        :param limit: The limit of this ListAppDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAppDetailsRequest.

        偏移量

        :return: The offset of this ListAppDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppDetailsRequest.

        偏移量

        :param offset: The offset of this ListAppDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def region(self):
        """Gets the region of this ListAppDetailsRequest.

        地域 1. cn：国内 2. intl：国际

        :return: The region of this ListAppDetailsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListAppDetailsRequest.

        地域 1. cn：国内 2. intl：国际

        :param region: The region of this ListAppDetailsRequest.
        :type region: str
        """
        self._region = region

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListAppDetailsRequest.

        排序方式 1. desc：降序 2. asc：升序

        :return: The sort_dir of this ListAppDetailsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListAppDetailsRequest.

        排序方式 1. desc：降序 2. asc：升序

        :param sort_dir: The sort_dir of this ListAppDetailsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        """Gets the sort_key of this ListAppDetailsRequest.

        排序字段

        :return: The sort_key of this ListAppDetailsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListAppDetailsRequest.

        排序字段

        :param sort_key: The sort_key of this ListAppDetailsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def status(self):
        """Gets the status of this ListAppDetailsRequest.

        应用状态   1. CREATED：待上线。应用暂未创建成功，请稍候。   2. SUSPENDED：暂停。无法发起业务请求。当客户所发短信内容触发业务违规，或客户申请退订短信业务时，运营经理会将客户短信应用暂停。   3. LAUNCHED：正常。应用添加成功，可以正常使用。

        :return: The status of this ListAppDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAppDetailsRequest.

        应用状态   1. CREATED：待上线。应用暂未创建成功，请稍候。   2. SUSPENDED：暂停。无法发起业务请求。当客户所发短信内容触发业务违规，或客户申请退订短信业务时，运营经理会将客户短信应用暂停。   3. LAUNCHED：正常。应用添加成功，可以正常使用。

        :param status: The status of this ListAppDetailsRequest.
        :type status: str
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
        if not isinstance(other, ListAppDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
