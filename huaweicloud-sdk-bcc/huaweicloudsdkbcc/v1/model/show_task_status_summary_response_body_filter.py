# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskStatusSummaryResponseBodyFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'task_type': 'str',
        'resource_type': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'task_type': 'task_type',
        'resource_type': 'resource_type',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, region_id=None, task_type=None, resource_type=None, start_time=None, end_time=None):
        r"""ShowTaskStatusSummaryResponseBodyFilter

        The model defined in huaweicloud sdk

        :param region_id: 区域ID
        :type region_id: str
        :param task_type: 任务类型枚举
        :type task_type: str
        :param resource_type: Server：云服务器 Volume：云硬盘 Sfs-Turbo：高性能文件系统 Workspace：云桌面 MySQL：云数据库RDS(MySQL) PostgreSQL：云数据库RDS(PostgreSQL) SQLServer：云数据库RDS(SQLServer) MariaDB：云数据库RDS(MariaDB) GaussDB：云数据库GaussDB
        :type resource_type: str
        :param start_time: 起始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        """
        
        

        self._region_id = None
        self._task_type = None
        self._resource_type = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if task_type is not None:
            self.task_type = task_type
        if resource_type is not None:
            self.resource_type = resource_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowTaskStatusSummaryResponseBodyFilter.

        区域ID

        :return: The region_id of this ShowTaskStatusSummaryResponseBodyFilter.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowTaskStatusSummaryResponseBodyFilter.

        区域ID

        :param region_id: The region_id of this ShowTaskStatusSummaryResponseBodyFilter.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def task_type(self):
        r"""Gets the task_type of this ShowTaskStatusSummaryResponseBodyFilter.

        任务类型枚举

        :return: The task_type of this ShowTaskStatusSummaryResponseBodyFilter.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ShowTaskStatusSummaryResponseBodyFilter.

        任务类型枚举

        :param task_type: The task_type of this ShowTaskStatusSummaryResponseBodyFilter.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowTaskStatusSummaryResponseBodyFilter.

        Server：云服务器 Volume：云硬盘 Sfs-Turbo：高性能文件系统 Workspace：云桌面 MySQL：云数据库RDS(MySQL) PostgreSQL：云数据库RDS(PostgreSQL) SQLServer：云数据库RDS(SQLServer) MariaDB：云数据库RDS(MariaDB) GaussDB：云数据库GaussDB

        :return: The resource_type of this ShowTaskStatusSummaryResponseBodyFilter.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowTaskStatusSummaryResponseBodyFilter.

        Server：云服务器 Volume：云硬盘 Sfs-Turbo：高性能文件系统 Workspace：云桌面 MySQL：云数据库RDS(MySQL) PostgreSQL：云数据库RDS(PostgreSQL) SQLServer：云数据库RDS(SQLServer) MariaDB：云数据库RDS(MariaDB) GaussDB：云数据库GaussDB

        :param resource_type: The resource_type of this ShowTaskStatusSummaryResponseBodyFilter.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowTaskStatusSummaryResponseBodyFilter.

        起始时间

        :return: The start_time of this ShowTaskStatusSummaryResponseBodyFilter.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowTaskStatusSummaryResponseBodyFilter.

        起始时间

        :param start_time: The start_time of this ShowTaskStatusSummaryResponseBodyFilter.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowTaskStatusSummaryResponseBodyFilter.

        结束时间

        :return: The end_time of this ShowTaskStatusSummaryResponseBodyFilter.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowTaskStatusSummaryResponseBodyFilter.

        结束时间

        :param end_time: The end_time of this ShowTaskStatusSummaryResponseBodyFilter.
        :type end_time: str
        """
        self._end_time = end_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowTaskStatusSummaryResponseBodyFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
