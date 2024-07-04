# coding: utf-8

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

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param hash: 事件白名单SHA256
        :type hash: str
        :param event_type: 事件类型，包含如下:   - 1001 : 通用恶意软件   - 1002 : 病毒   - 1003 : 蠕虫   - 1004 : 木马   - 1005 : 僵尸网络   - 1006 : 后门   - 1010 : Rootkit   - 1011 : 勒索软件   - 1012 ：黑客工具   - 1015 : Webshell   - 1016 : 挖矿   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2012 : 远程代码执行   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 3029 ：系统安全防护被禁用   - 3030 ：备份删除   - 3031 ：异常注册表操作   - 3036 : 容器镜像阻断   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号   - 4014 : 用户账号添加   - 4020 : 用户密码窃取   - 6002 : 端口扫描   - 6003 : 主机扫描   - 13001 : Kubernetes事件删除   - 13002 : Pod异常行为   - 13003 : 枚举用户信息   - 13004 : 绑定集群用户角色
        :type event_type: int
        :param offset: 偏移量：指定返回记录的开始位置
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

        Region ID

        :return: The region of this ListAlarmWhiteListRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListAlarmWhiteListRequest.

        Region ID

        :param region: The region of this ListAlarmWhiteListRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAlarmWhiteListRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListAlarmWhiteListRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAlarmWhiteListRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListAlarmWhiteListRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def hash(self):
        """Gets the hash of this ListAlarmWhiteListRequest.

        事件白名单SHA256

        :return: The hash of this ListAlarmWhiteListRequest.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this ListAlarmWhiteListRequest.

        事件白名单SHA256

        :param hash: The hash of this ListAlarmWhiteListRequest.
        :type hash: str
        """
        self._hash = hash

    @property
    def event_type(self):
        """Gets the event_type of this ListAlarmWhiteListRequest.

        事件类型，包含如下:   - 1001 : 通用恶意软件   - 1002 : 病毒   - 1003 : 蠕虫   - 1004 : 木马   - 1005 : 僵尸网络   - 1006 : 后门   - 1010 : Rootkit   - 1011 : 勒索软件   - 1012 ：黑客工具   - 1015 : Webshell   - 1016 : 挖矿   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2012 : 远程代码执行   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 3029 ：系统安全防护被禁用   - 3030 ：备份删除   - 3031 ：异常注册表操作   - 3036 : 容器镜像阻断   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号   - 4014 : 用户账号添加   - 4020 : 用户密码窃取   - 6002 : 端口扫描   - 6003 : 主机扫描   - 13001 : Kubernetes事件删除   - 13002 : Pod异常行为   - 13003 : 枚举用户信息   - 13004 : 绑定集群用户角色

        :return: The event_type of this ListAlarmWhiteListRequest.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ListAlarmWhiteListRequest.

        事件类型，包含如下:   - 1001 : 通用恶意软件   - 1002 : 病毒   - 1003 : 蠕虫   - 1004 : 木马   - 1005 : 僵尸网络   - 1006 : 后门   - 1010 : Rootkit   - 1011 : 勒索软件   - 1012 ：黑客工具   - 1015 : Webshell   - 1016 : 挖矿   - 1017 : 反弹Shell   - 2001 : 一般漏洞利用   - 2012 : 远程代码执行   - 2047 : Redis漏洞利用   - 2048 : Hadoop漏洞利用   - 2049 : MySQL漏洞利用   - 3002 : 文件提权   - 3003 : 进程提权   - 3004 : 关键文件变更   - 3005 : 文件/目录变更   - 3007 : 进程异常行为   - 3015 : 高危命令执行   - 3018 : 异常Shell   - 3027 : Crontab可疑任务   - 3029 ：系统安全防护被禁用   - 3030 ：备份删除   - 3031 ：异常注册表操作   - 3036 : 容器镜像阻断   - 4002 : 暴力破解   - 4004 : 异常登录   - 4006 : 非法系统账号   - 4014 : 用户账号添加   - 4020 : 用户密码窃取   - 6002 : 端口扫描   - 6003 : 主机扫描   - 13001 : Kubernetes事件删除   - 13002 : Pod异常行为   - 13003 : 枚举用户信息   - 13004 : 绑定集群用户角色

        :param event_type: The event_type of this ListAlarmWhiteListRequest.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def offset(self):
        """Gets the offset of this ListAlarmWhiteListRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListAlarmWhiteListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAlarmWhiteListRequest.

        偏移量：指定返回记录的开始位置

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
