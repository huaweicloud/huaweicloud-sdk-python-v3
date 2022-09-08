# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlinkJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_type': 'str',
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'order': 'str',
        'queue_name': 'str',
        'root_job_id': 'int',
        'show_detail': 'bool',
        'status': 'str',
        'sys_enterprise_project_name': 'str',
        'tags': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'job_type': 'job_type',
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'order': 'order',
        'queue_name': 'queue_name',
        'root_job_id': 'root_job_id',
        'show_detail': 'show_detail',
        'status': 'status',
        'sys_enterprise_project_name': 'sys_enterprise_project_name',
        'tags': 'tags',
        'user_name': 'user_name'
    }

    def __init__(self, job_type=None, limit=None, name=None, offset=None, order=None, queue_name=None, root_job_id=None, show_detail=None, status=None, sys_enterprise_project_name=None, tags=None, user_name=None):
        """ListFlinkJobsRequest

        The model defined in huaweicloud sdk

        :param job_type: 作业类型
        :type job_type: str
        :param limit: 返回的数据条数。默认为10。
        :type limit: int
        :param name: 作业名称。长度限制：0-57个字符。
        :type name: str
        :param offset: 作业偏移量。
        :type offset: int
        :param order: 查询结果排序，升序asc和降序desc两种可选，默认降序。
        :type order: str
        :param queue_name: 队列名称。
        :type queue_name: str
        :param root_job_id: 边缘父作业ID, 用于查询指定边缘作业的子作业。不带该参数时, 查询所有非边缘作业和边缘父作业, 不包括边缘子作业。
        :type root_job_id: int
        :param show_detail: 是否返回作业详情信息。默认为false。
        :type show_detail: bool
        :param status: 作业状态码。
        :type status: str
        :param sys_enterprise_project_name: 
        :type sys_enterprise_project_name: str
        :param tags: 
        :type tags: str
        :param user_name: 用户名，可作为筛选条件
        :type user_name: str
        """
        
        

        self._job_type = None
        self._limit = None
        self._name = None
        self._offset = None
        self._order = None
        self._queue_name = None
        self._root_job_id = None
        self._show_detail = None
        self._status = None
        self._sys_enterprise_project_name = None
        self._tags = None
        self._user_name = None
        self.discriminator = None

        if job_type is not None:
            self.job_type = job_type
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if order is not None:
            self.order = order
        if queue_name is not None:
            self.queue_name = queue_name
        if root_job_id is not None:
            self.root_job_id = root_job_id
        if show_detail is not None:
            self.show_detail = show_detail
        if status is not None:
            self.status = status
        if sys_enterprise_project_name is not None:
            self.sys_enterprise_project_name = sys_enterprise_project_name
        if tags is not None:
            self.tags = tags
        if user_name is not None:
            self.user_name = user_name

    @property
    def job_type(self):
        """Gets the job_type of this ListFlinkJobsRequest.

        作业类型

        :return: The job_type of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ListFlinkJobsRequest.

        作业类型

        :param job_type: The job_type of this ListFlinkJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def limit(self):
        """Gets the limit of this ListFlinkJobsRequest.

        返回的数据条数。默认为10。

        :return: The limit of this ListFlinkJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFlinkJobsRequest.

        返回的数据条数。默认为10。

        :param limit: The limit of this ListFlinkJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListFlinkJobsRequest.

        作业名称。长度限制：0-57个字符。

        :return: The name of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListFlinkJobsRequest.

        作业名称。长度限制：0-57个字符。

        :param name: The name of this ListFlinkJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListFlinkJobsRequest.

        作业偏移量。

        :return: The offset of this ListFlinkJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFlinkJobsRequest.

        作业偏移量。

        :param offset: The offset of this ListFlinkJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def order(self):
        """Gets the order of this ListFlinkJobsRequest.

        查询结果排序，升序asc和降序desc两种可选，默认降序。

        :return: The order of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListFlinkJobsRequest.

        查询结果排序，升序asc和降序desc两种可选，默认降序。

        :param order: The order of this ListFlinkJobsRequest.
        :type order: str
        """
        self._order = order

    @property
    def queue_name(self):
        """Gets the queue_name of this ListFlinkJobsRequest.

        队列名称。

        :return: The queue_name of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ListFlinkJobsRequest.

        队列名称。

        :param queue_name: The queue_name of this ListFlinkJobsRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def root_job_id(self):
        """Gets the root_job_id of this ListFlinkJobsRequest.

        边缘父作业ID, 用于查询指定边缘作业的子作业。不带该参数时, 查询所有非边缘作业和边缘父作业, 不包括边缘子作业。

        :return: The root_job_id of this ListFlinkJobsRequest.
        :rtype: int
        """
        return self._root_job_id

    @root_job_id.setter
    def root_job_id(self, root_job_id):
        """Sets the root_job_id of this ListFlinkJobsRequest.

        边缘父作业ID, 用于查询指定边缘作业的子作业。不带该参数时, 查询所有非边缘作业和边缘父作业, 不包括边缘子作业。

        :param root_job_id: The root_job_id of this ListFlinkJobsRequest.
        :type root_job_id: int
        """
        self._root_job_id = root_job_id

    @property
    def show_detail(self):
        """Gets the show_detail of this ListFlinkJobsRequest.

        是否返回作业详情信息。默认为false。

        :return: The show_detail of this ListFlinkJobsRequest.
        :rtype: bool
        """
        return self._show_detail

    @show_detail.setter
    def show_detail(self, show_detail):
        """Sets the show_detail of this ListFlinkJobsRequest.

        是否返回作业详情信息。默认为false。

        :param show_detail: The show_detail of this ListFlinkJobsRequest.
        :type show_detail: bool
        """
        self._show_detail = show_detail

    @property
    def status(self):
        """Gets the status of this ListFlinkJobsRequest.

        作业状态码。

        :return: The status of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListFlinkJobsRequest.

        作业状态码。

        :param status: The status of this ListFlinkJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def sys_enterprise_project_name(self):
        """Gets the sys_enterprise_project_name of this ListFlinkJobsRequest.


        :return: The sys_enterprise_project_name of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._sys_enterprise_project_name

    @sys_enterprise_project_name.setter
    def sys_enterprise_project_name(self, sys_enterprise_project_name):
        """Sets the sys_enterprise_project_name of this ListFlinkJobsRequest.


        :param sys_enterprise_project_name: The sys_enterprise_project_name of this ListFlinkJobsRequest.
        :type sys_enterprise_project_name: str
        """
        self._sys_enterprise_project_name = sys_enterprise_project_name

    @property
    def tags(self):
        """Gets the tags of this ListFlinkJobsRequest.


        :return: The tags of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListFlinkJobsRequest.


        :param tags: The tags of this ListFlinkJobsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def user_name(self):
        """Gets the user_name of this ListFlinkJobsRequest.

        用户名，可作为筛选条件

        :return: The user_name of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListFlinkJobsRequest.

        用户名，可作为筛选条件

        :param user_name: The user_name of this ListFlinkJobsRequest.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, ListFlinkJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
