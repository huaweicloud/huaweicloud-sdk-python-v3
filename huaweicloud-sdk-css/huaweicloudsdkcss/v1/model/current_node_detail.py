# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CurrentNodeDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order': 'int',
        'name': 'str',
        'status': 'str',
        'desc': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'order': 'order',
        'name': 'name',
        'status': 'status',
        'desc': 'desc',
        'begin_time': 'beginTime',
        'end_time': 'endTime'
    }

    def __init__(self, order=None, name=None, status=None, desc=None, begin_time=None, end_time=None):
        """CurrentNodeDetail

        The model defined in huaweicloud sdk

        :param order: 升级任务序号。
        :type order: int
        :param name: 升级任务名称。
        :type name: str
        :param status: 当前任务状态。
        :type status: str
        :param desc: 当前任务描述。
        :type desc: str
        :param begin_time: 当前任务开始时间。
        :type begin_time: str
        :param end_time: 当前任务结束时间。
        :type end_time: str
        """
        
        

        self._order = None
        self._name = None
        self._status = None
        self._desc = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if order is not None:
            self.order = order
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if desc is not None:
            self.desc = desc
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def order(self):
        """Gets the order of this CurrentNodeDetail.

        升级任务序号。

        :return: The order of this CurrentNodeDetail.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CurrentNodeDetail.

        升级任务序号。

        :param order: The order of this CurrentNodeDetail.
        :type order: int
        """
        self._order = order

    @property
    def name(self):
        """Gets the name of this CurrentNodeDetail.

        升级任务名称。

        :return: The name of this CurrentNodeDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CurrentNodeDetail.

        升级任务名称。

        :param name: The name of this CurrentNodeDetail.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this CurrentNodeDetail.

        当前任务状态。

        :return: The status of this CurrentNodeDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CurrentNodeDetail.

        当前任务状态。

        :param status: The status of this CurrentNodeDetail.
        :type status: str
        """
        self._status = status

    @property
    def desc(self):
        """Gets the desc of this CurrentNodeDetail.

        当前任务描述。

        :return: The desc of this CurrentNodeDetail.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this CurrentNodeDetail.

        当前任务描述。

        :param desc: The desc of this CurrentNodeDetail.
        :type desc: str
        """
        self._desc = desc

    @property
    def begin_time(self):
        """Gets the begin_time of this CurrentNodeDetail.

        当前任务开始时间。

        :return: The begin_time of this CurrentNodeDetail.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this CurrentNodeDetail.

        当前任务开始时间。

        :param begin_time: The begin_time of this CurrentNodeDetail.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this CurrentNodeDetail.

        当前任务结束时间。

        :return: The end_time of this CurrentNodeDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CurrentNodeDetail.

        当前任务结束时间。

        :param end_time: The end_time of this CurrentNodeDetail.
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
        if not isinstance(other, CurrentNodeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
