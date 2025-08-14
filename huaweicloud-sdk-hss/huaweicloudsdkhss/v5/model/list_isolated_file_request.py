# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIsolatedFileRequest:

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
        'file_path': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'file_hash': 'str',
        'asset_value': 'str',
        'offset': 'int',
        'limit': 'int',
        'isolation_status': 'str',
        'last_days': 'int',
        'begin_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'file_path': 'file_path',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'file_hash': 'file_hash',
        'asset_value': 'asset_value',
        'offset': 'offset',
        'limit': 'limit',
        'isolation_status': 'isolation_status',
        'last_days': 'last_days',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, region=None, enterprise_project_id=None, file_path=None, host_name=None, private_ip=None, public_ip=None, file_hash=None, asset_value=None, offset=None, limit=None, isolation_status=None, last_days=None, begin_time=None, end_time=None):
        r"""ListIsolatedFileRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param file_path: 文件路径
        :type file_path: str
        :param host_name: 服务器名称
        :type host_name: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param file_hash: 文件hash，当前为sha256
        :type file_hash: str
        :param asset_value: 资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产
        :type asset_value: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param isolation_status: 隔离状态，包含如下:   - isolated：已隔离   - restored：已恢复   - isolating：已下发隔离任务   - restoring：已下发恢复任务
        :type isolation_status: str
        :param last_days: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥
        :type last_days: int
        :param begin_time: 自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥
        :type begin_time: int
        :param end_time: 自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥
        :type end_time: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._file_path = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._file_hash = None
        self._asset_value = None
        self._offset = None
        self._limit = None
        self._isolation_status = None
        self._last_days = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if file_path is not None:
            self.file_path = file_path
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if file_hash is not None:
            self.file_hash = file_hash
        if asset_value is not None:
            self.asset_value = asset_value
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if isolation_status is not None:
            self.isolation_status = isolation_status
        if last_days is not None:
            self.last_days = last_days
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def region(self):
        r"""Gets the region of this ListIsolatedFileRequest.

        Region ID

        :return: The region of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListIsolatedFileRequest.

        Region ID

        :param region: The region of this ListIsolatedFileRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListIsolatedFileRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListIsolatedFileRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListIsolatedFileRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def file_path(self):
        r"""Gets the file_path of this ListIsolatedFileRequest.

        文件路径

        :return: The file_path of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ListIsolatedFileRequest.

        文件路径

        :param file_path: The file_path of this ListIsolatedFileRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def host_name(self):
        r"""Gets the host_name of this ListIsolatedFileRequest.

        服务器名称

        :return: The host_name of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListIsolatedFileRequest.

        服务器名称

        :param host_name: The host_name of this ListIsolatedFileRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ListIsolatedFileRequest.

        服务器私有IP

        :return: The private_ip of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ListIsolatedFileRequest.

        服务器私有IP

        :param private_ip: The private_ip of this ListIsolatedFileRequest.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ListIsolatedFileRequest.

        服务器公网IP

        :return: The public_ip of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ListIsolatedFileRequest.

        服务器公网IP

        :param public_ip: The public_ip of this ListIsolatedFileRequest.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def file_hash(self):
        r"""Gets the file_hash of this ListIsolatedFileRequest.

        文件hash，当前为sha256

        :return: The file_hash of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        r"""Sets the file_hash of this ListIsolatedFileRequest.

        文件hash，当前为sha256

        :param file_hash: The file_hash of this ListIsolatedFileRequest.
        :type file_hash: str
        """
        self._file_hash = file_hash

    @property
    def asset_value(self):
        r"""Gets the asset_value of this ListIsolatedFileRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :return: The asset_value of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this ListIsolatedFileRequest.

        资产重要性，包含如下3种   - important ：重要资产   - common ：一般资产   - test ：测试资产

        :param asset_value: The asset_value of this ListIsolatedFileRequest.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def offset(self):
        r"""Gets the offset of this ListIsolatedFileRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListIsolatedFileRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListIsolatedFileRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListIsolatedFileRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListIsolatedFileRequest.

        每页显示个数

        :return: The limit of this ListIsolatedFileRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIsolatedFileRequest.

        每页显示个数

        :param limit: The limit of this ListIsolatedFileRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def isolation_status(self):
        r"""Gets the isolation_status of this ListIsolatedFileRequest.

        隔离状态，包含如下:   - isolated：已隔离   - restored：已恢复   - isolating：已下发隔离任务   - restoring：已下发恢复任务

        :return: The isolation_status of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._isolation_status

    @isolation_status.setter
    def isolation_status(self, isolation_status):
        r"""Sets the isolation_status of this ListIsolatedFileRequest.

        隔离状态，包含如下:   - isolated：已隔离   - restored：已恢复   - isolating：已下发隔离任务   - restoring：已下发恢复任务

        :param isolation_status: The isolation_status of this ListIsolatedFileRequest.
        :type isolation_status: str
        """
        self._isolation_status = isolation_status

    @property
    def last_days(self):
        r"""Gets the last_days of this ListIsolatedFileRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :return: The last_days of this ListIsolatedFileRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListIsolatedFileRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :param last_days: The last_days of this ListIsolatedFileRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListIsolatedFileRequest.

        自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :return: The begin_time of this ListIsolatedFileRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListIsolatedFileRequest.

        自定义查询时间，与查询时间范围天数互斥，查询时间段的起始时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :param begin_time: The begin_time of this ListIsolatedFileRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListIsolatedFileRequest.

        自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :return: The end_time of this ListIsolatedFileRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListIsolatedFileRequest.

        自定义时间，查询时间段的终止时间，毫秒级时间戳，end_time减去begin_time小于等于2天，与查询时间范围天数互斥

        :param end_time: The end_time of this ListIsolatedFileRequest.
        :type end_time: int
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
        if not isinstance(other, ListIsolatedFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
