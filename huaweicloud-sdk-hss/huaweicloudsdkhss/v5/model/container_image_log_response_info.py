# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerImageLogResponseInfo:

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
        'event_name': 'str',
        'event_id': 'str',
        'event_type': 'str',
        'source_ip': 'str',
        'user_name': 'str',
        'time': 'int',
        'content': 'str'
    }

    attribute_map = {
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'event_name': 'event_name',
        'event_id': 'event_id',
        'event_type': 'event_type',
        'source_ip': 'source_ip',
        'user_name': 'user_name',
        'time': 'time',
        'content': 'content'
    }

    def __init__(self, resource_name=None, resource_type=None, event_name=None, event_id=None, event_type=None, source_ip=None, user_name=None, time=None, content=None):
        r"""ContainerImageLogResponseInfo

        The model defined in huaweicloud sdk

        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param event_name: 事件名称
        :type event_name: str
        :param event_id: 事件id
        :type event_id: str
        :param event_type: 事件类型
        :type event_type: str
        :param source_ip: 触发事件的源ip
        :type source_ip: str
        :param user_name: 触发事件的用户
        :type user_name: str
        :param time: 日志产生的时间
        :type time: int
        :param content: 日志内容
        :type content: str
        """
        
        

        self._resource_name = None
        self._resource_type = None
        self._event_name = None
        self._event_id = None
        self._event_type = None
        self._source_ip = None
        self._user_name = None
        self._time = None
        self._content = None
        self.discriminator = None

        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if event_name is not None:
            self.event_name = event_name
        if event_id is not None:
            self.event_id = event_id
        if event_type is not None:
            self.event_type = event_type
        if source_ip is not None:
            self.source_ip = source_ip
        if user_name is not None:
            self.user_name = user_name
        if time is not None:
            self.time = time
        if content is not None:
            self.content = content

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ContainerImageLogResponseInfo.

        资源名称

        :return: The resource_name of this ContainerImageLogResponseInfo.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ContainerImageLogResponseInfo.

        资源名称

        :param resource_name: The resource_name of this ContainerImageLogResponseInfo.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ContainerImageLogResponseInfo.

        资源类型

        :return: The resource_type of this ContainerImageLogResponseInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ContainerImageLogResponseInfo.

        资源类型

        :param resource_type: The resource_type of this ContainerImageLogResponseInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def event_name(self):
        r"""Gets the event_name of this ContainerImageLogResponseInfo.

        事件名称

        :return: The event_name of this ContainerImageLogResponseInfo.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this ContainerImageLogResponseInfo.

        事件名称

        :param event_name: The event_name of this ContainerImageLogResponseInfo.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_id(self):
        r"""Gets the event_id of this ContainerImageLogResponseInfo.

        事件id

        :return: The event_id of this ContainerImageLogResponseInfo.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this ContainerImageLogResponseInfo.

        事件id

        :param event_id: The event_id of this ContainerImageLogResponseInfo.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_type(self):
        r"""Gets the event_type of this ContainerImageLogResponseInfo.

        事件类型

        :return: The event_type of this ContainerImageLogResponseInfo.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ContainerImageLogResponseInfo.

        事件类型

        :param event_type: The event_type of this ContainerImageLogResponseInfo.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def source_ip(self):
        r"""Gets the source_ip of this ContainerImageLogResponseInfo.

        触发事件的源ip

        :return: The source_ip of this ContainerImageLogResponseInfo.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        r"""Sets the source_ip of this ContainerImageLogResponseInfo.

        触发事件的源ip

        :param source_ip: The source_ip of this ContainerImageLogResponseInfo.
        :type source_ip: str
        """
        self._source_ip = source_ip

    @property
    def user_name(self):
        r"""Gets the user_name of this ContainerImageLogResponseInfo.

        触发事件的用户

        :return: The user_name of this ContainerImageLogResponseInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ContainerImageLogResponseInfo.

        触发事件的用户

        :param user_name: The user_name of this ContainerImageLogResponseInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def time(self):
        r"""Gets the time of this ContainerImageLogResponseInfo.

        日志产生的时间

        :return: The time of this ContainerImageLogResponseInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ContainerImageLogResponseInfo.

        日志产生的时间

        :param time: The time of this ContainerImageLogResponseInfo.
        :type time: int
        """
        self._time = time

    @property
    def content(self):
        r"""Gets the content of this ContainerImageLogResponseInfo.

        日志内容

        :return: The content of this ContainerImageLogResponseInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ContainerImageLogResponseInfo.

        日志内容

        :param content: The content of this ContainerImageLogResponseInfo.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, ContainerImageLogResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
