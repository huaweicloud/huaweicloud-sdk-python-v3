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
        'last_days': 'int',
        'host_name': 'str',
        'isolation_status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'last_days': 'last_days',
        'host_name': 'host_name',
        'isolation_status': 'isolation_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, region=None, enterprise_project_id=None, last_days=None, host_name=None, isolation_status=None, offset=None, limit=None):
        """ListIsolatedFileRequest

        The model defined in huaweicloud sdk

        :param region: region id
        :type region: str
        :param enterprise_project_id: 租户企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param last_days: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥
        :type last_days: int
        :param host_name: 服务器名称
        :type host_name: str
        :param isolation_status: 隔离状态，包含如下:   - isolated : 已隔离   - restored : 已恢复   - isolating : 已下发隔离任务   - restoring : 已下发恢复任务
        :type isolation_status: str
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._last_days = None
        self._host_name = None
        self._isolation_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if last_days is not None:
            self.last_days = last_days
        if host_name is not None:
            self.host_name = host_name
        if isolation_status is not None:
            self.isolation_status = isolation_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def region(self):
        """Gets the region of this ListIsolatedFileRequest.

        region id

        :return: The region of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListIsolatedFileRequest.

        region id

        :param region: The region of this ListIsolatedFileRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListIsolatedFileRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListIsolatedFileRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListIsolatedFileRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def last_days(self):
        """Gets the last_days of this ListIsolatedFileRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :return: The last_days of this ListIsolatedFileRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        """Sets the last_days of this ListIsolatedFileRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :param last_days: The last_days of this ListIsolatedFileRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def host_name(self):
        """Gets the host_name of this ListIsolatedFileRequest.

        服务器名称

        :return: The host_name of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListIsolatedFileRequest.

        服务器名称

        :param host_name: The host_name of this ListIsolatedFileRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def isolation_status(self):
        """Gets the isolation_status of this ListIsolatedFileRequest.

        隔离状态，包含如下:   - isolated : 已隔离   - restored : 已恢复   - isolating : 已下发隔离任务   - restoring : 已下发恢复任务

        :return: The isolation_status of this ListIsolatedFileRequest.
        :rtype: str
        """
        return self._isolation_status

    @isolation_status.setter
    def isolation_status(self, isolation_status):
        """Sets the isolation_status of this ListIsolatedFileRequest.

        隔离状态，包含如下:   - isolated : 已隔离   - restored : 已恢复   - isolating : 已下发隔离任务   - restoring : 已下发恢复任务

        :param isolation_status: The isolation_status of this ListIsolatedFileRequest.
        :type isolation_status: str
        """
        self._isolation_status = isolation_status

    @property
    def offset(self):
        """Gets the offset of this ListIsolatedFileRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListIsolatedFileRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIsolatedFileRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListIsolatedFileRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListIsolatedFileRequest.

        每页显示个数

        :return: The limit of this ListIsolatedFileRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIsolatedFileRequest.

        每页显示个数

        :param limit: The limit of this ListIsolatedFileRequest.
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
        if not isinstance(other, ListIsolatedFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
