# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSearchFactoryBaselinesRequest:

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
        'owner_name': 'str',
        'priority': 'int',
        'order_by': 'str',
        'enable': 'bool',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_project_id': 'X-Project-Id',
        'workspace': 'workspace',
        'workspace_id': 'workspace_id',
        'name': 'name',
        'owner_name': 'owner_name',
        'priority': 'priority',
        'order_by': 'order_by',
        'enable': 'enable',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, x_project_id=None, workspace=None, workspace_id=None, name=None, owner_name=None, priority=None, order_by=None, enable=None, offset=None, limit=None):
        r"""ListSearchFactoryBaselinesRequest

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
        :param owner_name: 责任人名称。
        :type owner_name: str
        :param priority: 优先级，取值有1/2/3/4/5，默认查询所有优先级。当同时查询优先级为1/2/3时，样例如下：priority&#x3D;1&amp;priority&#x3D;2&amp;priority&#x3D;3。
        :type priority: int
        :param order_by: 排序规则，取值如下： - priority asc: 按照优先级升序。 - priority desc: 按照优先级降序。 默认不排序。
        :type order_by: str
        :param enable: 开启基线任务。 true: 开启基线任务，系统将会监控基线任务以及其依赖链上游的所有任务。 false: 关闭基线任务，系统不会监控基线任务以及其依赖链上游的所有任务。 默认查询全部。
        :type enable: bool
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
        self._owner_name = None
        self._priority = None
        self._order_by = None
        self._enable = None
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
        if owner_name is not None:
            self.owner_name = owner_name
        if priority is not None:
            self.priority = priority
        if order_by is not None:
            self.order_by = order_by
        if enable is not None:
            self.enable = enable
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSearchFactoryBaselinesRequest.

        DataArts Studio实例ID。

        :return: The instance_id of this ListSearchFactoryBaselinesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSearchFactoryBaselinesRequest.

        DataArts Studio实例ID。

        :param instance_id: The instance_id of this ListSearchFactoryBaselinesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListSearchFactoryBaselinesRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ListSearchFactoryBaselinesRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListSearchFactoryBaselinesRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ListSearchFactoryBaselinesRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSearchFactoryBaselinesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListSearchFactoryBaselinesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSearchFactoryBaselinesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListSearchFactoryBaselinesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListSearchFactoryBaselinesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace_id of this ListSearchFactoryBaselinesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListSearchFactoryBaselinesRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace_id: The workspace_id of this ListSearchFactoryBaselinesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def name(self):
        r"""Gets the name of this ListSearchFactoryBaselinesRequest.

        基线任务名称。

        :return: The name of this ListSearchFactoryBaselinesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSearchFactoryBaselinesRequest.

        基线任务名称。

        :param name: The name of this ListSearchFactoryBaselinesRequest.
        :type name: str
        """
        self._name = name

    @property
    def owner_name(self):
        r"""Gets the owner_name of this ListSearchFactoryBaselinesRequest.

        责任人名称。

        :return: The owner_name of this ListSearchFactoryBaselinesRequest.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this ListSearchFactoryBaselinesRequest.

        责任人名称。

        :param owner_name: The owner_name of this ListSearchFactoryBaselinesRequest.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def priority(self):
        r"""Gets the priority of this ListSearchFactoryBaselinesRequest.

        优先级，取值有1/2/3/4/5，默认查询所有优先级。当同时查询优先级为1/2/3时，样例如下：priority=1&priority=2&priority=3。

        :return: The priority of this ListSearchFactoryBaselinesRequest.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ListSearchFactoryBaselinesRequest.

        优先级，取值有1/2/3/4/5，默认查询所有优先级。当同时查询优先级为1/2/3时，样例如下：priority=1&priority=2&priority=3。

        :param priority: The priority of this ListSearchFactoryBaselinesRequest.
        :type priority: int
        """
        self._priority = priority

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSearchFactoryBaselinesRequest.

        排序规则，取值如下： - priority asc: 按照优先级升序。 - priority desc: 按照优先级降序。 默认不排序。

        :return: The order_by of this ListSearchFactoryBaselinesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSearchFactoryBaselinesRequest.

        排序规则，取值如下： - priority asc: 按照优先级升序。 - priority desc: 按照优先级降序。 默认不排序。

        :param order_by: The order_by of this ListSearchFactoryBaselinesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def enable(self):
        r"""Gets the enable of this ListSearchFactoryBaselinesRequest.

        开启基线任务。 true: 开启基线任务，系统将会监控基线任务以及其依赖链上游的所有任务。 false: 关闭基线任务，系统不会监控基线任务以及其依赖链上游的所有任务。 默认查询全部。

        :return: The enable of this ListSearchFactoryBaselinesRequest.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ListSearchFactoryBaselinesRequest.

        开启基线任务。 true: 开启基线任务，系统将会监控基线任务以及其依赖链上游的所有任务。 false: 关闭基线任务，系统不会监控基线任务以及其依赖链上游的所有任务。 默认查询全部。

        :param enable: The enable of this ListSearchFactoryBaselinesRequest.
        :type enable: bool
        """
        self._enable = enable

    @property
    def offset(self):
        r"""Gets the offset of this ListSearchFactoryBaselinesRequest.

        分页列表的页数，默认值为1。取值范围大于等于1。

        :return: The offset of this ListSearchFactoryBaselinesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSearchFactoryBaselinesRequest.

        分页列表的页数，默认值为1。取值范围大于等于1。

        :param offset: The offset of this ListSearchFactoryBaselinesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSearchFactoryBaselinesRequest.

        分页返回结果，指定每页最大记录数。范围[1,100] 默认值：10

        :return: The limit of this ListSearchFactoryBaselinesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSearchFactoryBaselinesRequest.

        分页返回结果，指定每页最大记录数。范围[1,100] 默认值：10

        :param limit: The limit of this ListSearchFactoryBaselinesRequest.
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
        if not isinstance(other, ListSearchFactoryBaselinesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
