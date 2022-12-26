# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmWhiteListResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_name': 'str',
        'hash': 'str',
        'description': 'str',
        'event_type': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'enterprise_project_name': 'enterprise_project_name',
        'hash': 'hash',
        'description': 'description',
        'event_type': 'event_type',
        'update_time': 'update_time'
    }

    def __init__(self, enterprise_project_name=None, hash=None, description=None, event_type=None, update_time=None):
        """AlarmWhiteListResponseInfo

        The model defined in huaweicloud sdk

        :param enterprise_project_name: 企业项目名称
        :type enterprise_project_name: str
        :param hash: SHA256
        :type hash: str
        :param description: 描述信息
        :type description: str
        :param event_type: 事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号
        :type event_type: int
        :param update_time: 更新时间，毫秒
        :type update_time: int
        """
        
        

        self._enterprise_project_name = None
        self._hash = None
        self._description = None
        self._event_type = None
        self._update_time = None
        self.discriminator = None

        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if hash is not None:
            self.hash = hash
        if description is not None:
            self.description = description
        if event_type is not None:
            self.event_type = event_type
        if update_time is not None:
            self.update_time = update_time

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this AlarmWhiteListResponseInfo.

        企业项目名称

        :return: The enterprise_project_name of this AlarmWhiteListResponseInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this AlarmWhiteListResponseInfo.

        企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this AlarmWhiteListResponseInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def hash(self):
        """Gets the hash of this AlarmWhiteListResponseInfo.

        SHA256

        :return: The hash of this AlarmWhiteListResponseInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this AlarmWhiteListResponseInfo.

        SHA256

        :param hash: The hash of this AlarmWhiteListResponseInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def description(self):
        """Gets the description of this AlarmWhiteListResponseInfo.

        描述信息

        :return: The description of this AlarmWhiteListResponseInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AlarmWhiteListResponseInfo.

        描述信息

        :param description: The description of this AlarmWhiteListResponseInfo.
        :type description: str
        """
        self._description = description

    @property
    def event_type(self):
        """Gets the event_type of this AlarmWhiteListResponseInfo.

        事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号

        :return: The event_type of this AlarmWhiteListResponseInfo.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this AlarmWhiteListResponseInfo.

        事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号

        :param event_type: The event_type of this AlarmWhiteListResponseInfo.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def update_time(self):
        """Gets the update_time of this AlarmWhiteListResponseInfo.

        更新时间，毫秒

        :return: The update_time of this AlarmWhiteListResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AlarmWhiteListResponseInfo.

        更新时间，毫秒

        :param update_time: The update_time of this AlarmWhiteListResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, AlarmWhiteListResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
