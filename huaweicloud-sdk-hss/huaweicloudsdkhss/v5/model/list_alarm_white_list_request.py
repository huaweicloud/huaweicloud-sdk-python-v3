# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmWhiteListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'hash': 'str',
        'event_type': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'hash': 'hash',
        'event_type': 'event_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, region=None, enterprise_project_id=None, hash=None, event_type=None, offset=None, limit=None):
        """ListAlarmWhiteListRequest

        The model defined in huaweicloud sdk

        :param region: region id
        :type region: str
        :param enterprise_project_id: 租户企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param hash: SHA256
        :type hash: str
        :param event_type: 事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号
        :type event_type: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._hash = None
        self._event_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if hash is not None:
            self.hash = hash
        if event_type is not None:
            self.event_type = event_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def region(self):
        """Gets the region of this ListAlarmWhiteListRequest.

        region id

        :return: The region of this ListAlarmWhiteListRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListAlarmWhiteListRequest.

        region id

        :param region: The region of this ListAlarmWhiteListRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAlarmWhiteListRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListAlarmWhiteListRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAlarmWhiteListRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListAlarmWhiteListRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def hash(self):
        """Gets the hash of this ListAlarmWhiteListRequest.

        SHA256

        :return: The hash of this ListAlarmWhiteListRequest.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ListAlarmWhiteListRequest.

        SHA256

        :param hash: The hash of this ListAlarmWhiteListRequest.
        :type hash: str
        """
        self._hash = hash

    @property
    def event_type(self):
        """Gets the event_type of this ListAlarmWhiteListRequest.

        事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号

        :return: The event_type of this ListAlarmWhiteListRequest.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ListAlarmWhiteListRequest.

        事件类型，包含如下:   - 1001 : 恶意软件   - 1010 : Rootkit   - 1011 : 勒索软件   - 1015 : Webshell   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号

        :param event_type: The event_type of this ListAlarmWhiteListRequest.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def offset(self):
        """Gets the offset of this ListAlarmWhiteListRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListAlarmWhiteListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAlarmWhiteListRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListAlarmWhiteListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAlarmWhiteListRequest.

        每页显示个数

        :return: The limit of this ListAlarmWhiteListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlarmWhiteListRequest.

        每页显示个数

        :param limit: The limit of this ListAlarmWhiteListRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAlarmWhiteListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
