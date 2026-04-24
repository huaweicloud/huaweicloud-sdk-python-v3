# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSearchFactoryEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'x_project_id': 'str',
        'workspace': 'str',
        'workspace_id': 'str',
        'name': 'str',
        'task_name': 'str',
        'owner_name': 'str',
        'type': 'str',
        'status': 'str',
        'order_by': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_project_id': 'X-Project-Id',
        'workspace': 'workspace',
        'workspace_id': 'workspace_id',
        'name': 'name',
        'task_name': 'task_name',
        'owner_name': 'owner_name',
        'type': 'type',
        'status': 'status',
        'order_by': 'order_by',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, x_project_id=None, workspace=None, workspace_id=None, name=None, task_name=None, owner_name=None, type=None, status=None, order_by=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ListSearchFactoryEventsRequest

        The model defined in huaweicloud sdk

        :param instance_id: DataArts Studio实例ID。
        :type instance_id: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param workspace_id: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace_id: str
        :param name: 基线任务名称。
        :type name: str
        :param task_name: 作业名称
        :type task_name: str
        :param owner_name: 责任人名称。
        :type owner_name: str
        :param type: 事件类型:  - ERROR: 出错 - SLOW_DOWN: 变慢  默认查询全部事件类型。
        :type type: str
        :param status: 事件状态: - NEW_DISCOVERY: 新发现 - PROCESSING: 处理中 - RESTORED: 已恢复 - IGNORED: 已忽略
        :type status: str
        :param order_by: 排序规则，示例 happen_time_ms asc asc，表示按照优先级升序排序，有如下取值： - happen_time_ms asc asc: 按照触发事件升序。 - happen_time_ms asc desc: 按照触发事件降序。  默认不排序。
        :type order_by: str
        :param start_time: 创建时间检索区间，起始时间戳，单位毫秒。默认为当天0点0分0秒，当end_time有值时，该值不能为空。
        :type start_time: int
        :param end_time: 创建时间检索区间，终止时间戳，单位毫秒。默认为当天23点59分59秒，当start_time有值时，该值不能为空，最大查询范围为180天。
        :type end_time: int
        :param offset: 分页列表的页数，默认值为1。取值范围大于等于1。
        :type offset: int
        :param limit: 分页返回结果，指定每页最大记录数。范围[1,100] 默认值：10
        :type limit: int
        """
        
        

        self._instance_id = None
        self._x_project_id = None
        self._workspace = None
        self._workspace_id = None
        self._name = None
        self._task_name = None
        self._owner_name = None
        self._type = None
        self._status = None
        self._order_by = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.workspace = workspace
        self.workspace_id = workspace_id
        if name is not None:
            self.name = name
        if task_name is not None:
            self.task_name = task_name
        if owner_name is not None:
            self.owner_name = owner_name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if order_by is not None:
            self.order_by = order_by
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSearchFactoryEventsRequest.

        DataArts Studio实例ID。

        :return: The instance_id of this ListSearchFactoryEventsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSearchFactoryEventsRequest.

        DataArts Studio实例ID。

        :param instance_id: The instance_id of this ListSearchFactoryEventsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListSearchFactoryEventsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ListSearchFactoryEventsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListSearchFactoryEventsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ListSearchFactoryEventsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSearchFactoryEventsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListSearchFactoryEventsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSearchFactoryEventsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListSearchFactoryEventsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListSearchFactoryEventsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace_id of this ListSearchFactoryEventsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListSearchFactoryEventsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace_id: The workspace_id of this ListSearchFactoryEventsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def name(self):
        r"""Gets the name of this ListSearchFactoryEventsRequest.

        基线任务名称。

        :return: The name of this ListSearchFactoryEventsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSearchFactoryEventsRequest.

        基线任务名称。

        :param name: The name of this ListSearchFactoryEventsRequest.
        :type name: str
        """
        self._name = name

    @property
    def task_name(self):
        r"""Gets the task_name of this ListSearchFactoryEventsRequest.

        作业名称

        :return: The task_name of this ListSearchFactoryEventsRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListSearchFactoryEventsRequest.

        作业名称

        :param task_name: The task_name of this ListSearchFactoryEventsRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def owner_name(self):
        r"""Gets the owner_name of this ListSearchFactoryEventsRequest.

        责任人名称。

        :return: The owner_name of this ListSearchFactoryEventsRequest.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this ListSearchFactoryEventsRequest.

        责任人名称。

        :param owner_name: The owner_name of this ListSearchFactoryEventsRequest.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def type(self):
        r"""Gets the type of this ListSearchFactoryEventsRequest.

        事件类型:  - ERROR: 出错 - SLOW_DOWN: 变慢  默认查询全部事件类型。

        :return: The type of this ListSearchFactoryEventsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListSearchFactoryEventsRequest.

        事件类型:  - ERROR: 出错 - SLOW_DOWN: 变慢  默认查询全部事件类型。

        :param type: The type of this ListSearchFactoryEventsRequest.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ListSearchFactoryEventsRequest.

        事件状态: - NEW_DISCOVERY: 新发现 - PROCESSING: 处理中 - RESTORED: 已恢复 - IGNORED: 已忽略

        :return: The status of this ListSearchFactoryEventsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSearchFactoryEventsRequest.

        事件状态: - NEW_DISCOVERY: 新发现 - PROCESSING: 处理中 - RESTORED: 已恢复 - IGNORED: 已忽略

        :param status: The status of this ListSearchFactoryEventsRequest.
        :type status: str
        """
        self._status = status

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSearchFactoryEventsRequest.

        排序规则，示例 happen_time_ms asc asc，表示按照优先级升序排序，有如下取值： - happen_time_ms asc asc: 按照触发事件升序。 - happen_time_ms asc desc: 按照触发事件降序。  默认不排序。

        :return: The order_by of this ListSearchFactoryEventsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSearchFactoryEventsRequest.

        排序规则，示例 happen_time_ms asc asc，表示按照优先级升序排序，有如下取值： - happen_time_ms asc asc: 按照触发事件升序。 - happen_time_ms asc desc: 按照触发事件降序。  默认不排序。

        :param order_by: The order_by of this ListSearchFactoryEventsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def start_time(self):
        r"""Gets the start_time of this ListSearchFactoryEventsRequest.

        创建时间检索区间，起始时间戳，单位毫秒。默认为当天0点0分0秒，当end_time有值时，该值不能为空。

        :return: The start_time of this ListSearchFactoryEventsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListSearchFactoryEventsRequest.

        创建时间检索区间，起始时间戳，单位毫秒。默认为当天0点0分0秒，当end_time有值时，该值不能为空。

        :param start_time: The start_time of this ListSearchFactoryEventsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSearchFactoryEventsRequest.

        创建时间检索区间，终止时间戳，单位毫秒。默认为当天23点59分59秒，当start_time有值时，该值不能为空，最大查询范围为180天。

        :return: The end_time of this ListSearchFactoryEventsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSearchFactoryEventsRequest.

        创建时间检索区间，终止时间戳，单位毫秒。默认为当天23点59分59秒，当start_time有值时，该值不能为空，最大查询范围为180天。

        :param end_time: The end_time of this ListSearchFactoryEventsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListSearchFactoryEventsRequest.

        分页列表的页数，默认值为1。取值范围大于等于1。

        :return: The offset of this ListSearchFactoryEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSearchFactoryEventsRequest.

        分页列表的页数，默认值为1。取值范围大于等于1。

        :param offset: The offset of this ListSearchFactoryEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSearchFactoryEventsRequest.

        分页返回结果，指定每页最大记录数。范围[1,100] 默认值：10

        :return: The limit of this ListSearchFactoryEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSearchFactoryEventsRequest.

        分页返回结果，指定每页最大记录数。范围[1,100] 默认值：10

        :param limit: The limit of this ListSearchFactoryEventsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSearchFactoryEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
