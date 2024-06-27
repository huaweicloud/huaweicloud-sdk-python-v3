# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubTaskCaseOverstockUsingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'executor_type': 'str',
        'label': 'str',
        'location_id': 'str',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'service_id': 'service_id',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'executor_type': 'executorType',
        'label': 'label',
        'location_id': 'locationId',
        'page_num': 'pageNum',
        'page_size': 'pageSize'
    }

    def __init__(self, service_id=None, start_time=None, end_time=None, executor_type=None, label=None, location_id=None, page_num=None, page_size=None):
        """ListSubTaskCaseOverstockUsingRequest

        The model defined in huaweicloud sdk

        :param service_id: 服务id
        :type service_id: str
        :param start_time: 数据开始时间
        :type start_time: int
        :param end_time: 数据结束时间
        :type end_time: int
        :param executor_type: 执行机类型
        :type executor_type: str
        :param label: 执行机标签
        :type label: str
        :param location_id: 执行机所属区域id
        :type location_id: str
        :param page_num: 分页当前页码
        :type page_num: int
        :param page_size: 分页大小(分页参数只要有一个为空即不做分页)
        :type page_size: int
        """
        
        

        self._service_id = None
        self._start_time = None
        self._end_time = None
        self._executor_type = None
        self._label = None
        self._location_id = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None

        self.service_id = service_id
        self.start_time = start_time
        self.end_time = end_time
        if executor_type is not None:
            self.executor_type = executor_type
        self.label = label
        if location_id is not None:
            self.location_id = location_id
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def service_id(self):
        """Gets the service_id of this ListSubTaskCaseOverstockUsingRequest.

        服务id

        :return: The service_id of this ListSubTaskCaseOverstockUsingRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this ListSubTaskCaseOverstockUsingRequest.

        服务id

        :param service_id: The service_id of this ListSubTaskCaseOverstockUsingRequest.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def start_time(self):
        """Gets the start_time of this ListSubTaskCaseOverstockUsingRequest.

        数据开始时间

        :return: The start_time of this ListSubTaskCaseOverstockUsingRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListSubTaskCaseOverstockUsingRequest.

        数据开始时间

        :param start_time: The start_time of this ListSubTaskCaseOverstockUsingRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListSubTaskCaseOverstockUsingRequest.

        数据结束时间

        :return: The end_time of this ListSubTaskCaseOverstockUsingRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListSubTaskCaseOverstockUsingRequest.

        数据结束时间

        :param end_time: The end_time of this ListSubTaskCaseOverstockUsingRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def executor_type(self):
        """Gets the executor_type of this ListSubTaskCaseOverstockUsingRequest.

        执行机类型

        :return: The executor_type of this ListSubTaskCaseOverstockUsingRequest.
        :rtype: str
        """
        return self._executor_type

    @executor_type.setter
    def executor_type(self, executor_type):
        """Sets the executor_type of this ListSubTaskCaseOverstockUsingRequest.

        执行机类型

        :param executor_type: The executor_type of this ListSubTaskCaseOverstockUsingRequest.
        :type executor_type: str
        """
        self._executor_type = executor_type

    @property
    def label(self):
        """Gets the label of this ListSubTaskCaseOverstockUsingRequest.

        执行机标签

        :return: The label of this ListSubTaskCaseOverstockUsingRequest.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ListSubTaskCaseOverstockUsingRequest.

        执行机标签

        :param label: The label of this ListSubTaskCaseOverstockUsingRequest.
        :type label: str
        """
        self._label = label

    @property
    def location_id(self):
        """Gets the location_id of this ListSubTaskCaseOverstockUsingRequest.

        执行机所属区域id

        :return: The location_id of this ListSubTaskCaseOverstockUsingRequest.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this ListSubTaskCaseOverstockUsingRequest.

        执行机所属区域id

        :param location_id: The location_id of this ListSubTaskCaseOverstockUsingRequest.
        :type location_id: str
        """
        self._location_id = location_id

    @property
    def page_num(self):
        """Gets the page_num of this ListSubTaskCaseOverstockUsingRequest.

        分页当前页码

        :return: The page_num of this ListSubTaskCaseOverstockUsingRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this ListSubTaskCaseOverstockUsingRequest.

        分页当前页码

        :param page_num: The page_num of this ListSubTaskCaseOverstockUsingRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this ListSubTaskCaseOverstockUsingRequest.

        分页大小(分页参数只要有一个为空即不做分页)

        :return: The page_size of this ListSubTaskCaseOverstockUsingRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListSubTaskCaseOverstockUsingRequest.

        分页大小(分页参数只要有一个为空即不做分页)

        :param page_size: The page_size of this ListSubTaskCaseOverstockUsingRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ListSubTaskCaseOverstockUsingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
