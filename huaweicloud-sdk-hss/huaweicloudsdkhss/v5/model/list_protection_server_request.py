# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectionServerRequest:

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
        'offset': 'int',
        'limit': 'int',
        'host_name': 'str',
        'os_type': 'str',
        'host_ip': 'str',
        'host_status': 'str',
        'last_days': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_name': 'host_name',
        'os_type': 'os_type',
        'host_ip': 'host_ip',
        'host_status': 'host_status',
        'last_days': 'last_days'
    }

    def __init__(self, region=None, enterprise_project_id=None, offset=None, limit=None, host_name=None, os_type=None, host_ip=None, host_status=None, last_days=None):
        """ListProtectionServerRequest

        The model defined in huaweicloud sdk

        :param region: region id
        :type region: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param host_name: 服务器名称
        :type host_name: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。
        :type os_type: str
        :param host_ip: 服务器IP地址
        :type host_ip: str
        :param host_status: 主机状态，包含如下3种。   - 不传参默认为全部。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。
        :type host_status: str
        :param last_days: 查询时间范围天数，最近7天为last_days&#x3D;7，若不填，则默认查询一天内的防护事件和已有备份数
        :type last_days: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_name = None
        self._os_type = None
        self._host_ip = None
        self._host_status = None
        self._last_days = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if host_name is not None:
            self.host_name = host_name
        if os_type is not None:
            self.os_type = os_type
        if host_ip is not None:
            self.host_ip = host_ip
        if host_status is not None:
            self.host_status = host_status
        if last_days is not None:
            self.last_days = last_days

    @property
    def region(self):
        """Gets the region of this ListProtectionServerRequest.

        region id

        :return: The region of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListProtectionServerRequest.

        region id

        :param region: The region of this ListProtectionServerRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListProtectionServerRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListProtectionServerRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListProtectionServerRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ListProtectionServerRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListProtectionServerRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProtectionServerRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListProtectionServerRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListProtectionServerRequest.

        每页显示个数

        :return: The limit of this ListProtectionServerRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProtectionServerRequest.

        每页显示个数

        :param limit: The limit of this ListProtectionServerRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_name(self):
        """Gets the host_name of this ListProtectionServerRequest.

        服务器名称

        :return: The host_name of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListProtectionServerRequest.

        服务器名称

        :param host_name: The host_name of this ListProtectionServerRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def os_type(self):
        """Gets the os_type of this ListProtectionServerRequest.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :return: The os_type of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListProtectionServerRequest.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :param os_type: The os_type of this ListProtectionServerRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def host_ip(self):
        """Gets the host_ip of this ListProtectionServerRequest.

        服务器IP地址

        :return: The host_ip of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this ListProtectionServerRequest.

        服务器IP地址

        :param host_ip: The host_ip of this ListProtectionServerRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def host_status(self):
        """Gets the host_status of this ListProtectionServerRequest.

        主机状态，包含如下3种。   - 不传参默认为全部。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。

        :return: The host_status of this ListProtectionServerRequest.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this ListProtectionServerRequest.

        主机状态，包含如下3种。   - 不传参默认为全部。   - ACTIVE ：正在运行。   - SHUTOFF ：关机。

        :param host_status: The host_status of this ListProtectionServerRequest.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def last_days(self):
        """Gets the last_days of this ListProtectionServerRequest.

        查询时间范围天数，最近7天为last_days=7，若不填，则默认查询一天内的防护事件和已有备份数

        :return: The last_days of this ListProtectionServerRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        """Sets the last_days of this ListProtectionServerRequest.

        查询时间范围天数，最近7天为last_days=7，若不填，则默认查询一天内的防护事件和已有备份数

        :param last_days: The last_days of this ListProtectionServerRequest.
        :type last_days: int
        """
        self._last_days = last_days

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
        if not isinstance(other, ListProtectionServerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
