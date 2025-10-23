# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'region_id': 'str',
        'task_status': 'str',
        'task_type': 'str',
        'resource_type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'task_status': 'task_status',
        'task_type': 'task_type',
        'resource_type': 'resource_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, domain_id=None, region_id=None, task_status=None, task_type=None, resource_type=None, start_time=None, end_time=None, marker=None, limit=None):
        r"""ListTasksRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param region_id: RegionID
        :type region_id: str
        :param task_status: 任务状态，取值范围：success,failed,running,skipped,timeout
        :type task_status: str
        :param task_type: 任务类型，取值范围：backup,replication,restore,delete,vault_delete,remove_resource
        :type task_type: str
        :param resource_type: 资源类型，取值范围：Server,Volume,Sfs-Turbo,Workspace,MySQL,PostgreSQL,SQLServer,MariaDB,GaussDB
        :type resource_type: str
        :param start_time: 查询范围起始时间，例如：2025-03-20T09:31:45Z。
        :type start_time: str
        :param end_time: 查询范围结束时间，例如：2025-03-21T09:31:45Z。
        :type end_time: str
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。
        :type marker: str
        :param limit: 单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。
        :type limit: int
        """
        
        

        self._domain_id = None
        self._region_id = None
        self._task_status = None
        self._task_type = None
        self._resource_type = None
        self._start_time = None
        self._end_time = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if task_status is not None:
            self.task_status = task_status
        if task_type is not None:
            self.task_type = task_type
        if resource_type is not None:
            self.resource_type = resource_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListTasksRequest.

        账号ID

        :return: The domain_id of this ListTasksRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListTasksRequest.

        账号ID

        :param domain_id: The domain_id of this ListTasksRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListTasksRequest.

        RegionID

        :return: The region_id of this ListTasksRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListTasksRequest.

        RegionID

        :param region_id: The region_id of this ListTasksRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def task_status(self):
        r"""Gets the task_status of this ListTasksRequest.

        任务状态，取值范围：success,failed,running,skipped,timeout

        :return: The task_status of this ListTasksRequest.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ListTasksRequest.

        任务状态，取值范围：success,failed,running,skipped,timeout

        :param task_status: The task_status of this ListTasksRequest.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def task_type(self):
        r"""Gets the task_type of this ListTasksRequest.

        任务类型，取值范围：backup,replication,restore,delete,vault_delete,remove_resource

        :return: The task_type of this ListTasksRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListTasksRequest.

        任务类型，取值范围：backup,replication,restore,delete,vault_delete,remove_resource

        :param task_type: The task_type of this ListTasksRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListTasksRequest.

        资源类型，取值范围：Server,Volume,Sfs-Turbo,Workspace,MySQL,PostgreSQL,SQLServer,MariaDB,GaussDB

        :return: The resource_type of this ListTasksRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListTasksRequest.

        资源类型，取值范围：Server,Volume,Sfs-Turbo,Workspace,MySQL,PostgreSQL,SQLServer,MariaDB,GaussDB

        :param resource_type: The resource_type of this ListTasksRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTasksRequest.

        查询范围起始时间，例如：2025-03-20T09:31:45Z。

        :return: The start_time of this ListTasksRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTasksRequest.

        查询范围起始时间，例如：2025-03-20T09:31:45Z。

        :param start_time: The start_time of this ListTasksRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTasksRequest.

        查询范围结束时间，例如：2025-03-21T09:31:45Z。

        :return: The end_time of this ListTasksRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTasksRequest.

        查询范围结束时间，例如：2025-03-21T09:31:45Z。

        :param end_time: The end_time of this ListTasksRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def marker(self):
        r"""Gets the marker of this ListTasksRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :return: The marker of this ListTasksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListTasksRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :param marker: The marker of this ListTasksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListTasksRequest.

        单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。

        :return: The limit of this ListTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTasksRequest.

        单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。

        :param limit: The limit of this ListTasksRequest.
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
        if not isinstance(other, ListTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
