# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'job_type': 'str',
        'name': 'str',
        'status': 'str',
        'engine_type': 'str',
        'net_type': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_type': 'job_type',
        'name': 'name',
        'status': 'status',
        'engine_type': 'engine_type',
        'net_type': 'net_type',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, x_language=None, job_type=None, name=None, status=None, engine_type=None, net_type=None, enterprise_project_id=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        """ListJobsRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param job_type: 任务场景。取值： - migration：实时迁移。 - sync：实时同步。 - cloudDataGuard：实时灾备。
        :type job_type: str
        :param name: 任务ID或名称。
        :type name: str
        :param status: 任务状态。取值： - CREATING：创建中。 - CREATE_FAILED：创建失败。 - CONFIGURATION：配置中。 - STARTJOBING：启动中。 - WAITING_FOR_START：等待启动中。 - START_JOB_FAILED：任务启动失败。 - FULL_TRANSFER_STARTED：全量迁移中，灾备场景为初始化。 - FULL_TRANSFER_FAILED：全量迁移失败，灾备场景为初始化失败。 - FULL_TRANSFER_COMPLETE：全量迁移完成，灾备场景为初始化完成。 - INCRE_TRANSFER_STARTED：增量迁移中，灾备场景为灾备中。 - INCRE_TRANSFER_FAILED：增量迁移失败，灾备场景为灾备异常。 - RELEASE_RESOURCE_STARTED：结束任务中。 - RELEASE_RESOURCE_FAILED：结束任务失败。 - RELEASE_RESOURCE_COMPLETE：已结束。 - CHANGE_JOB_STARTED：任务变更中。 - CHANGE_JOB_FAILED：任务变更失败。 - CHILD_TRANSFER_STARTING：子任务启动中。 - CHILD_TRANSFER_STARTED：子任务迁移中。 - CHILD_TRANSFER_COMPLETE：子任务迁移完成。 - CHILD_TRANSFER_FAILED：子任务迁移失败。 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中。 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束。 其中，异常状态可单独查询，也可以通过以下方式查询全部异常任务： CREATE_FAILED,START_JOB_FAILED,FULL_TRANSFER_FAILED,INCRE_TRANSFER_FAILED,RELEASE_RESOURCE_FAILED,CHANGE_JOB_FAILED,CHILD_TRANSFER_FAILED
        :type status: str
        :param engine_type: 引擎类型。取值： - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用。
        :type engine_type: str
        :param net_type: 网络类型。取值： - eip：公网网络。 - vpc：VPC网络。 - vpn：VPN、专线网络。
        :type net_type: str
        :param enterprise_project_id: 企业项目ID。 缺省值：\&quot;\&quot;，表示查询所有企业项目任务。
        :type enterprise_project_id: str
        :param offset: 偏移量，表示查询该偏移量后面的记录。
        :type offset: int
        :param limit: 查询返回记录的数量限制。
        :type limit: int
        :param sort_key: 返回结果按该关键字排序，默认为“create_time”。
        :type sort_key: str
        :param sort_dir: 降序或升序（分别对应desc和asc，默认为“desc”）
        :type sort_dir: str
        """
        
        

        self._x_language = None
        self._job_type = None
        self._name = None
        self._status = None
        self._engine_type = None
        self._net_type = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_type = job_type
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if engine_type is not None:
            self.engine_type = engine_type
        if net_type is not None:
            self.net_type = net_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def x_language(self):
        """Gets the x_language of this ListJobsRequest.

        请求语言类型。

        :return: The x_language of this ListJobsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListJobsRequest.

        请求语言类型。

        :param x_language: The x_language of this ListJobsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_type(self):
        """Gets the job_type of this ListJobsRequest.

        任务场景。取值： - migration：实时迁移。 - sync：实时同步。 - cloudDataGuard：实时灾备。

        :return: The job_type of this ListJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ListJobsRequest.

        任务场景。取值： - migration：实时迁移。 - sync：实时同步。 - cloudDataGuard：实时灾备。

        :param job_type: The job_type of this ListJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def name(self):
        """Gets the name of this ListJobsRequest.

        任务ID或名称。

        :return: The name of this ListJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListJobsRequest.

        任务ID或名称。

        :param name: The name of this ListJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListJobsRequest.

        任务状态。取值： - CREATING：创建中。 - CREATE_FAILED：创建失败。 - CONFIGURATION：配置中。 - STARTJOBING：启动中。 - WAITING_FOR_START：等待启动中。 - START_JOB_FAILED：任务启动失败。 - FULL_TRANSFER_STARTED：全量迁移中，灾备场景为初始化。 - FULL_TRANSFER_FAILED：全量迁移失败，灾备场景为初始化失败。 - FULL_TRANSFER_COMPLETE：全量迁移完成，灾备场景为初始化完成。 - INCRE_TRANSFER_STARTED：增量迁移中，灾备场景为灾备中。 - INCRE_TRANSFER_FAILED：增量迁移失败，灾备场景为灾备异常。 - RELEASE_RESOURCE_STARTED：结束任务中。 - RELEASE_RESOURCE_FAILED：结束任务失败。 - RELEASE_RESOURCE_COMPLETE：已结束。 - CHANGE_JOB_STARTED：任务变更中。 - CHANGE_JOB_FAILED：任务变更失败。 - CHILD_TRANSFER_STARTING：子任务启动中。 - CHILD_TRANSFER_STARTED：子任务迁移中。 - CHILD_TRANSFER_COMPLETE：子任务迁移完成。 - CHILD_TRANSFER_FAILED：子任务迁移失败。 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中。 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束。 其中，异常状态可单独查询，也可以通过以下方式查询全部异常任务： CREATE_FAILED,START_JOB_FAILED,FULL_TRANSFER_FAILED,INCRE_TRANSFER_FAILED,RELEASE_RESOURCE_FAILED,CHANGE_JOB_FAILED,CHILD_TRANSFER_FAILED

        :return: The status of this ListJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListJobsRequest.

        任务状态。取值： - CREATING：创建中。 - CREATE_FAILED：创建失败。 - CONFIGURATION：配置中。 - STARTJOBING：启动中。 - WAITING_FOR_START：等待启动中。 - START_JOB_FAILED：任务启动失败。 - FULL_TRANSFER_STARTED：全量迁移中，灾备场景为初始化。 - FULL_TRANSFER_FAILED：全量迁移失败，灾备场景为初始化失败。 - FULL_TRANSFER_COMPLETE：全量迁移完成，灾备场景为初始化完成。 - INCRE_TRANSFER_STARTED：增量迁移中，灾备场景为灾备中。 - INCRE_TRANSFER_FAILED：增量迁移失败，灾备场景为灾备异常。 - RELEASE_RESOURCE_STARTED：结束任务中。 - RELEASE_RESOURCE_FAILED：结束任务失败。 - RELEASE_RESOURCE_COMPLETE：已结束。 - CHANGE_JOB_STARTED：任务变更中。 - CHANGE_JOB_FAILED：任务变更失败。 - CHILD_TRANSFER_STARTING：子任务启动中。 - CHILD_TRANSFER_STARTED：子任务迁移中。 - CHILD_TRANSFER_COMPLETE：子任务迁移完成。 - CHILD_TRANSFER_FAILED：子任务迁移失败。 - RELEASE_CHILD_TRANSFER_STARTED：子任务结束中。 - RELEASE_CHILD_TRANSFER_COMPLETE：子任务已结束。 其中，异常状态可单独查询，也可以通过以下方式查询全部异常任务： CREATE_FAILED,START_JOB_FAILED,FULL_TRANSFER_FAILED,INCRE_TRANSFER_FAILED,RELEASE_RESOURCE_FAILED,CHANGE_JOB_FAILED,CHILD_TRANSFER_FAILED

        :param status: The status of this ListJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def engine_type(self):
        """Gets the engine_type of this ListJobsRequest.

        引擎类型。取值： - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用。

        :return: The engine_type of this ListJobsRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this ListJobsRequest.

        引擎类型。取值： - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用。

        :param engine_type: The engine_type of this ListJobsRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def net_type(self):
        """Gets the net_type of this ListJobsRequest.

        网络类型。取值： - eip：公网网络。 - vpc：VPC网络。 - vpn：VPN、专线网络。

        :return: The net_type of this ListJobsRequest.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        """Sets the net_type of this ListJobsRequest.

        网络类型。取值： - eip：公网网络。 - vpc：VPC网络。 - vpn：VPN、专线网络。

        :param net_type: The net_type of this ListJobsRequest.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListJobsRequest.

        企业项目ID。 缺省值：\"\"，表示查询所有企业项目任务。

        :return: The enterprise_project_id of this ListJobsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListJobsRequest.

        企业项目ID。 缺省值：\"\"，表示查询所有企业项目任务。

        :param enterprise_project_id: The enterprise_project_id of this ListJobsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ListJobsRequest.

        偏移量，表示查询该偏移量后面的记录。

        :return: The offset of this ListJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListJobsRequest.

        偏移量，表示查询该偏移量后面的记录。

        :param offset: The offset of this ListJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListJobsRequest.

        查询返回记录的数量限制。

        :return: The limit of this ListJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListJobsRequest.

        查询返回记录的数量限制。

        :param limit: The limit of this ListJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        """Gets the sort_key of this ListJobsRequest.

        返回结果按该关键字排序，默认为“create_time”。

        :return: The sort_key of this ListJobsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListJobsRequest.

        返回结果按该关键字排序，默认为“create_time”。

        :param sort_key: The sort_key of this ListJobsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListJobsRequest.

        降序或升序（分别对应desc和asc，默认为“desc”）

        :return: The sort_dir of this ListJobsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListJobsRequest.

        降序或升序（分别对应desc和asc，默认为“desc”）

        :param sort_dir: The sort_dir of this ListJobsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
