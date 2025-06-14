# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostProtectHistoryInfoRequest:

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
        'host_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'limit': 'int',
        'offset': 'int',
        'host_name': 'str',
        'host_ip': 'str',
        'file_path': 'str',
        'file_operation': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'file_path': 'file_path',
        'file_operation': 'file_operation'
    }

    def __init__(self, region=None, enterprise_project_id=None, host_id=None, start_time=None, end_time=None, limit=None, offset=None, host_name=None, host_ip=None, file_path=None, file_operation=None):
        r"""ListHostProtectHistoryInfoRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param host_id: Host Id，为空时查所有主机
        :type host_id: str
        :param start_time: 起始时间(ms)
        :type start_time: int
        :param end_time: 终止时间(ms)
        :type end_time: int
        :param limit: limit
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器ip
        :type host_ip: str
        :param file_path: 防护文件
        :type file_path: str
        :param file_operation: 文件操作类型   - add: 新增   - delete: 删除   - modify: 修改内容   - attribute: 修改属性
        :type file_operation: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._host_id = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._host_name = None
        self._host_ip = None
        self._file_path = None
        self._file_operation = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_id is not None:
            self.host_id = host_id
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        self.offset = offset
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if file_path is not None:
            self.file_path = file_path
        if file_operation is not None:
            self.file_operation = file_operation

    @property
    def region(self):
        r"""Gets the region of this ListHostProtectHistoryInfoRequest.

        Region ID

        :return: The region of this ListHostProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListHostProtectHistoryInfoRequest.

        Region ID

        :param region: The region of this ListHostProtectHistoryInfoRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListHostProtectHistoryInfoRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListHostProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListHostProtectHistoryInfoRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListHostProtectHistoryInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ListHostProtectHistoryInfoRequest.

        Host Id，为空时查所有主机

        :return: The host_id of this ListHostProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListHostProtectHistoryInfoRequest.

        Host Id，为空时查所有主机

        :param host_id: The host_id of this ListHostProtectHistoryInfoRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListHostProtectHistoryInfoRequest.

        起始时间(ms)

        :return: The start_time of this ListHostProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListHostProtectHistoryInfoRequest.

        起始时间(ms)

        :param start_time: The start_time of this ListHostProtectHistoryInfoRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListHostProtectHistoryInfoRequest.

        终止时间(ms)

        :return: The end_time of this ListHostProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListHostProtectHistoryInfoRequest.

        终止时间(ms)

        :param end_time: The end_time of this ListHostProtectHistoryInfoRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListHostProtectHistoryInfoRequest.

        limit

        :return: The limit of this ListHostProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHostProtectHistoryInfoRequest.

        limit

        :param limit: The limit of this ListHostProtectHistoryInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListHostProtectHistoryInfoRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListHostProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHostProtectHistoryInfoRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListHostProtectHistoryInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def host_name(self):
        r"""Gets the host_name of this ListHostProtectHistoryInfoRequest.

        服务器名称

        :return: The host_name of this ListHostProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListHostProtectHistoryInfoRequest.

        服务器名称

        :param host_name: The host_name of this ListHostProtectHistoryInfoRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListHostProtectHistoryInfoRequest.

        服务器ip

        :return: The host_ip of this ListHostProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListHostProtectHistoryInfoRequest.

        服务器ip

        :param host_ip: The host_ip of this ListHostProtectHistoryInfoRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def file_path(self):
        r"""Gets the file_path of this ListHostProtectHistoryInfoRequest.

        防护文件

        :return: The file_path of this ListHostProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ListHostProtectHistoryInfoRequest.

        防护文件

        :param file_path: The file_path of this ListHostProtectHistoryInfoRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_operation(self):
        r"""Gets the file_operation of this ListHostProtectHistoryInfoRequest.

        文件操作类型   - add: 新增   - delete: 删除   - modify: 修改内容   - attribute: 修改属性

        :return: The file_operation of this ListHostProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._file_operation

    @file_operation.setter
    def file_operation(self, file_operation):
        r"""Sets the file_operation of this ListHostProtectHistoryInfoRequest.

        文件操作类型   - add: 新增   - delete: 删除   - modify: 修改内容   - attribute: 修改属性

        :param file_operation: The file_operation of this ListHostProtectHistoryInfoRequest.
        :type file_operation: str
        """
        self._file_operation = file_operation

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
        if not isinstance(other, ListHostProtectHistoryInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
