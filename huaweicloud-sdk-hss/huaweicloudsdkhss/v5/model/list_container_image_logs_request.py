# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListContainerImageLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_name': 'str',
        'resource_type': 'str',
        'event_type': 'str',
        'event_name': 'str',
        'source_ip': 'str',
        'user_name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'event_type': 'event_type',
        'event_name': 'event_name',
        'source_ip': 'source_ip',
        'user_name': 'user_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, resource_name=None, resource_type=None, event_type=None, event_name=None, source_ip=None, user_name=None, start_time=None, end_time=None, limit=None, offset=None):
        r"""ListContainerImageLogsRequest

        The model defined in huaweicloud sdk

        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param event_type: 事件类型
        :type event_type: str
        :param event_name: 事件名称
        :type event_name: str
        :param source_ip: 触发事件的源ip
        :type source_ip: str
        :param user_name: 操作用户
        :type user_name: str
        :param start_time: 查询日志范围的最小时间
        :type start_time: int
        :param end_time: 查询日志范围的最大时间
        :type end_time: int
        :param limit: 每页显示个数，默认为10
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        """
        
        

        self._resource_name = None
        self._resource_type = None
        self._event_type = None
        self._event_name = None
        self._source_ip = None
        self._user_name = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if event_type is not None:
            self.event_type = event_type
        if event_name is not None:
            self.event_name = event_name
        if source_ip is not None:
            self.source_ip = source_ip
        if user_name is not None:
            self.user_name = user_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListContainerImageLogsRequest.

        资源名称

        :return: The resource_name of this ListContainerImageLogsRequest.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListContainerImageLogsRequest.

        资源名称

        :param resource_name: The resource_name of this ListContainerImageLogsRequest.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListContainerImageLogsRequest.

        资源类型

        :return: The resource_type of this ListContainerImageLogsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListContainerImageLogsRequest.

        资源类型

        :param resource_type: The resource_type of this ListContainerImageLogsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def event_type(self):
        r"""Gets the event_type of this ListContainerImageLogsRequest.

        事件类型

        :return: The event_type of this ListContainerImageLogsRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ListContainerImageLogsRequest.

        事件类型

        :param event_type: The event_type of this ListContainerImageLogsRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_name(self):
        r"""Gets the event_name of this ListContainerImageLogsRequest.

        事件名称

        :return: The event_name of this ListContainerImageLogsRequest.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ListContainerImageLogsRequest.

        事件名称

        :param event_name: The event_name of this ListContainerImageLogsRequest.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def source_ip(self):
        r"""Gets the source_ip of this ListContainerImageLogsRequest.

        触发事件的源ip

        :return: The source_ip of this ListContainerImageLogsRequest.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        r"""Sets the source_ip of this ListContainerImageLogsRequest.

        触发事件的源ip

        :param source_ip: The source_ip of this ListContainerImageLogsRequest.
        :type source_ip: str
        """
        self._source_ip = source_ip

    @property
    def user_name(self):
        r"""Gets the user_name of this ListContainerImageLogsRequest.

        操作用户

        :return: The user_name of this ListContainerImageLogsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListContainerImageLogsRequest.

        操作用户

        :param user_name: The user_name of this ListContainerImageLogsRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ListContainerImageLogsRequest.

        查询日志范围的最小时间

        :return: The start_time of this ListContainerImageLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListContainerImageLogsRequest.

        查询日志范围的最小时间

        :param start_time: The start_time of this ListContainerImageLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListContainerImageLogsRequest.

        查询日志范围的最大时间

        :return: The end_time of this ListContainerImageLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListContainerImageLogsRequest.

        查询日志范围的最大时间

        :param end_time: The end_time of this ListContainerImageLogsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListContainerImageLogsRequest.

        每页显示个数，默认为10

        :return: The limit of this ListContainerImageLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListContainerImageLogsRequest.

        每页显示个数，默认为10

        :param limit: The limit of this ListContainerImageLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListContainerImageLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListContainerImageLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListContainerImageLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListContainerImageLogsRequest.
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
        if not isinstance(other, ListContainerImageLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
