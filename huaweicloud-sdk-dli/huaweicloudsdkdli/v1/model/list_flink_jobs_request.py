# coding: utf-8

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
        r"""ListFlinkJobsRequest

        The model defined in huaweicloud sdk

        :param job_type: 参数解释:  作业类型 示例: flink_jar_job 约束限制:  无 取值范围: flink_sql_job（flink sql作业） flink_opensource_sql_job（flink opensource sql作业） flink_sql_edge_job（flink sql边缘作业） flink_jar_job（flink自定义作业） 默认取值: 无
        :type job_type: str
        :param limit: 参数解释:  返回的数据条数。默认为10 示例: 100 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 10
        :type limit: int
        :param name: 参数解释:  作业名称 示例: myjob 约束限制:  长度在[0,57]的字符串 取值范围: 无 默认取值: 无
        :type name: str
        :param offset: 参数解释:  作业偏移量 示例: 10000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 0
        :type offset: int
        :param order: 参数解释:  查询结果排序 示例: asc 约束限制:  无 取值范围: asc desc 默认取值: desc
        :type order: str
        :param queue_name: 参数解释:  队列名称 示例: queue1 约束限制:  无 取值范围: 无 默认取值: 无
        :type queue_name: str
        :param root_job_id: 参数解释:  边缘父作业ID, 用于查询指定边缘作业的子作业。不带该参数时, 查询所有非边缘作业和边缘父作业, 不包括边缘子作业 示例: 548483 约束限制:  无 取值范围: 无 默认取值: 无
        :type root_job_id: int
        :param show_detail: 参数解释:  是否返回作业详情信息 示例: false 约束限制:  无 取值范围: true,false 默认取值: false
        :type show_detail: bool
        :param status: 参数解释:  作业状态 示例: job_submitting 约束限制:  无 取值范围: job_init（草稿） job_submitting（提交中） job_submit_fail（提交失败） job_running（运行中） job_running_exception（运行异常） job_downloading（下载中） job_idle（空闲） job_canceling（停止中） job_cancel_success（已停止） job_cancel_fail（停止失败） job_savepointing（保存点创建中） job_arrearage_stopped（因欠费被停止） job_arrearage_recovering（欠费作业恢复中） job_finish（已完成） 默认取值: 无
        :type status: str
        :param sys_enterprise_project_name: 参数解释:  企业项目名称 示例: DLI 约束限制:  无 取值范围: 无 默认取值: 无
        :type sys_enterprise_project_name: str
        :param tags: 参数解释:  标签列表 示例: key_zy1&#x3D;zy01,AA&#x3D;aa 约束限制:  符合键值对格式(如“key&#x3D;value”)的字符串 取值范围: 无 默认取值: 无
        :type tags: str
        :param user_name: 参数解释:  用户名，可作为筛选条件 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无
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
        r"""Gets the job_type of this ListFlinkJobsRequest.

        参数解释:  作业类型 示例: flink_jar_job 约束限制:  无 取值范围: flink_sql_job（flink sql作业） flink_opensource_sql_job（flink opensource sql作业） flink_sql_edge_job（flink sql边缘作业） flink_jar_job（flink自定义作业） 默认取值: 无

        :return: The job_type of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListFlinkJobsRequest.

        参数解释:  作业类型 示例: flink_jar_job 约束限制:  无 取值范围: flink_sql_job（flink sql作业） flink_opensource_sql_job（flink opensource sql作业） flink_sql_edge_job（flink sql边缘作业） flink_jar_job（flink自定义作业） 默认取值: 无

        :param job_type: The job_type of this ListFlinkJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def limit(self):
        r"""Gets the limit of this ListFlinkJobsRequest.

        参数解释:  返回的数据条数。默认为10 示例: 100 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 10

        :return: The limit of this ListFlinkJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFlinkJobsRequest.

        参数解释:  返回的数据条数。默认为10 示例: 100 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 10

        :param limit: The limit of this ListFlinkJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListFlinkJobsRequest.

        参数解释:  作业名称 示例: myjob 约束限制:  长度在[0,57]的字符串 取值范围: 无 默认取值: 无

        :return: The name of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFlinkJobsRequest.

        参数解释:  作业名称 示例: myjob 约束限制:  长度在[0,57]的字符串 取值范围: 无 默认取值: 无

        :param name: The name of this ListFlinkJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListFlinkJobsRequest.

        参数解释:  作业偏移量 示例: 10000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 0

        :return: The offset of this ListFlinkJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFlinkJobsRequest.

        参数解释:  作业偏移量 示例: 10000 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 0

        :param offset: The offset of this ListFlinkJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def order(self):
        r"""Gets the order of this ListFlinkJobsRequest.

        参数解释:  查询结果排序 示例: asc 约束限制:  无 取值范围: asc desc 默认取值: desc

        :return: The order of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListFlinkJobsRequest.

        参数解释:  查询结果排序 示例: asc 约束限制:  无 取值范围: asc desc 默认取值: desc

        :param order: The order of this ListFlinkJobsRequest.
        :type order: str
        """
        self._order = order

    @property
    def queue_name(self):
        r"""Gets the queue_name of this ListFlinkJobsRequest.

        参数解释:  队列名称 示例: queue1 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The queue_name of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this ListFlinkJobsRequest.

        参数解释:  队列名称 示例: queue1 约束限制:  无 取值范围: 无 默认取值: 无

        :param queue_name: The queue_name of this ListFlinkJobsRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def root_job_id(self):
        r"""Gets the root_job_id of this ListFlinkJobsRequest.

        参数解释:  边缘父作业ID, 用于查询指定边缘作业的子作业。不带该参数时, 查询所有非边缘作业和边缘父作业, 不包括边缘子作业 示例: 548483 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The root_job_id of this ListFlinkJobsRequest.
        :rtype: int
        """
        return self._root_job_id

    @root_job_id.setter
    def root_job_id(self, root_job_id):
        r"""Sets the root_job_id of this ListFlinkJobsRequest.

        参数解释:  边缘父作业ID, 用于查询指定边缘作业的子作业。不带该参数时, 查询所有非边缘作业和边缘父作业, 不包括边缘子作业 示例: 548483 约束限制:  无 取值范围: 无 默认取值: 无

        :param root_job_id: The root_job_id of this ListFlinkJobsRequest.
        :type root_job_id: int
        """
        self._root_job_id = root_job_id

    @property
    def show_detail(self):
        r"""Gets the show_detail of this ListFlinkJobsRequest.

        参数解释:  是否返回作业详情信息 示例: false 约束限制:  无 取值范围: true,false 默认取值: false

        :return: The show_detail of this ListFlinkJobsRequest.
        :rtype: bool
        """
        return self._show_detail

    @show_detail.setter
    def show_detail(self, show_detail):
        r"""Sets the show_detail of this ListFlinkJobsRequest.

        参数解释:  是否返回作业详情信息 示例: false 约束限制:  无 取值范围: true,false 默认取值: false

        :param show_detail: The show_detail of this ListFlinkJobsRequest.
        :type show_detail: bool
        """
        self._show_detail = show_detail

    @property
    def status(self):
        r"""Gets the status of this ListFlinkJobsRequest.

        参数解释:  作业状态 示例: job_submitting 约束限制:  无 取值范围: job_init（草稿） job_submitting（提交中） job_submit_fail（提交失败） job_running（运行中） job_running_exception（运行异常） job_downloading（下载中） job_idle（空闲） job_canceling（停止中） job_cancel_success（已停止） job_cancel_fail（停止失败） job_savepointing（保存点创建中） job_arrearage_stopped（因欠费被停止） job_arrearage_recovering（欠费作业恢复中） job_finish（已完成） 默认取值: 无

        :return: The status of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListFlinkJobsRequest.

        参数解释:  作业状态 示例: job_submitting 约束限制:  无 取值范围: job_init（草稿） job_submitting（提交中） job_submit_fail（提交失败） job_running（运行中） job_running_exception（运行异常） job_downloading（下载中） job_idle（空闲） job_canceling（停止中） job_cancel_success（已停止） job_cancel_fail（停止失败） job_savepointing（保存点创建中） job_arrearage_stopped（因欠费被停止） job_arrearage_recovering（欠费作业恢复中） job_finish（已完成） 默认取值: 无

        :param status: The status of this ListFlinkJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def sys_enterprise_project_name(self):
        r"""Gets the sys_enterprise_project_name of this ListFlinkJobsRequest.

        参数解释:  企业项目名称 示例: DLI 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The sys_enterprise_project_name of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._sys_enterprise_project_name

    @sys_enterprise_project_name.setter
    def sys_enterprise_project_name(self, sys_enterprise_project_name):
        r"""Sets the sys_enterprise_project_name of this ListFlinkJobsRequest.

        参数解释:  企业项目名称 示例: DLI 约束限制:  无 取值范围: 无 默认取值: 无

        :param sys_enterprise_project_name: The sys_enterprise_project_name of this ListFlinkJobsRequest.
        :type sys_enterprise_project_name: str
        """
        self._sys_enterprise_project_name = sys_enterprise_project_name

    @property
    def tags(self):
        r"""Gets the tags of this ListFlinkJobsRequest.

        参数解释:  标签列表 示例: key_zy1=zy01,AA=aa 约束限制:  符合键值对格式(如“key=value”)的字符串 取值范围: 无 默认取值: 无

        :return: The tags of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListFlinkJobsRequest.

        参数解释:  标签列表 示例: key_zy1=zy01,AA=aa 约束限制:  符合键值对格式(如“key=value”)的字符串 取值范围: 无 默认取值: 无

        :param tags: The tags of this ListFlinkJobsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def user_name(self):
        r"""Gets the user_name of this ListFlinkJobsRequest.

        参数解释:  用户名，可作为筛选条件 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The user_name of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListFlinkJobsRequest.

        参数解释:  用户名，可作为筛选条件 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

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
