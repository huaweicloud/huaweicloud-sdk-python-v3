# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateLogGetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'TimeRangeBean',
        'user_name': 'str',
        'operate_name': 'str',
        'result': 'str',
        'page': 'str',
        'size': 'str'
    }

    attribute_map = {
        'time': 'time',
        'user_name': 'user_name',
        'operate_name': 'operate_name',
        'result': 'result',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, time=None, user_name=None, operate_name=None, result=None, page=None, size=None):
        """OperateLogGetRequest

        The model defined in huaweicloud sdk

        :param time: 
        :type time: :class:`huaweicloudsdkdbss.v1.TimeRangeBean`
        :param user_name: 筛选角色用户获取操作日志
        :type user_name: str
        :param operate_name: 筛选操作对象名称获取操作日志
        :type operate_name: str
        :param result: 根据执行结果获取操作日志 [success, fail]
        :type result: str
        :param page: 页数
        :type page: str
        :param size: 每页条数
        :type size: str
        """
        
        

        self._time = None
        self._user_name = None
        self._operate_name = None
        self._result = None
        self._page = None
        self._size = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if user_name is not None:
            self.user_name = user_name
        if operate_name is not None:
            self.operate_name = operate_name
        if result is not None:
            self.result = result
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def time(self):
        """Gets the time of this OperateLogGetRequest.

        :return: The time of this OperateLogGetRequest.
        :rtype: :class:`huaweicloudsdkdbss.v1.TimeRangeBean`
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OperateLogGetRequest.

        :param time: The time of this OperateLogGetRequest.
        :type time: :class:`huaweicloudsdkdbss.v1.TimeRangeBean`
        """
        self._time = time

    @property
    def user_name(self):
        """Gets the user_name of this OperateLogGetRequest.

        筛选角色用户获取操作日志

        :return: The user_name of this OperateLogGetRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this OperateLogGetRequest.

        筛选角色用户获取操作日志

        :param user_name: The user_name of this OperateLogGetRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def operate_name(self):
        """Gets the operate_name of this OperateLogGetRequest.

        筛选操作对象名称获取操作日志

        :return: The operate_name of this OperateLogGetRequest.
        :rtype: str
        """
        return self._operate_name

    @operate_name.setter
    def operate_name(self, operate_name):
        """Sets the operate_name of this OperateLogGetRequest.

        筛选操作对象名称获取操作日志

        :param operate_name: The operate_name of this OperateLogGetRequest.
        :type operate_name: str
        """
        self._operate_name = operate_name

    @property
    def result(self):
        """Gets the result of this OperateLogGetRequest.

        根据执行结果获取操作日志 [success, fail]

        :return: The result of this OperateLogGetRequest.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this OperateLogGetRequest.

        根据执行结果获取操作日志 [success, fail]

        :param result: The result of this OperateLogGetRequest.
        :type result: str
        """
        self._result = result

    @property
    def page(self):
        """Gets the page of this OperateLogGetRequest.

        页数

        :return: The page of this OperateLogGetRequest.
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this OperateLogGetRequest.

        页数

        :param page: The page of this OperateLogGetRequest.
        :type page: str
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this OperateLogGetRequest.

        每页条数

        :return: The size of this OperateLogGetRequest.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this OperateLogGetRequest.

        每页条数

        :param size: The size of this OperateLogGetRequest.
        :type size: str
        """
        self._size = size

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
        if not isinstance(other, OperateLogGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
