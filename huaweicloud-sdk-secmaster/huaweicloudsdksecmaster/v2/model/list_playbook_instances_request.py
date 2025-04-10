# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlaybookInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'workspace_id': 'str',
        'status': 'str',
        'name': 'str',
        'playbook_name': 'str',
        'dataclass_name': 'str',
        'dataobject_name': 'str',
        'trigger_type': 'str',
        'from_date': 'str',
        'to_date': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'status': 'status',
        'name': 'name',
        'playbook_name': 'playbook_name',
        'dataclass_name': 'dataclass_name',
        'dataobject_name': 'dataobject_name',
        'trigger_type': 'trigger_type',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, project_id=None, workspace_id=None, status=None, name=None, playbook_name=None, dataclass_name=None, dataobject_name=None, trigger_type=None, from_date=None, to_date=None, limit=None, offset=None):
        r"""ListPlaybookInstancesRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param status: 剧本实例状态. (RUNNING--运行中、FINISHED--成功、FAILED--失败、RETRYING--重试中、TERMINATING--终止中、TERMINATED--已终止)
        :type status: str
        :param name: 实例名称
        :type name: str
        :param playbook_name: 剧本名称
        :type playbook_name: str
        :param dataclass_name: 数据类名称
        :type dataclass_name: str
        :param dataobject_name: 数据对象名称
        :type dataobject_name: str
        :param trigger_type: 触发类型. TIMER--定时触发, EVENT--事件触发
        :type trigger_type: str
        :param from_date: 查询起始时间
        :type from_date: str
        :param to_date: 查询结束时间
        :type to_date: str
        :param limit: 分页查询参数，用于指定一次查询最多的结果数，从1开始
        :type limit: int
        :param offset: 分页查询参数。用于指定查询结果的起始位置，从0开始
        :type offset: int
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._status = None
        self._name = None
        self._playbook_name = None
        self._dataclass_name = None
        self._dataobject_name = None
        self._trigger_type = None
        self._from_date = None
        self._to_date = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if playbook_name is not None:
            self.playbook_name = playbook_name
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if dataobject_name is not None:
            self.dataobject_name = dataobject_name
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        self.limit = limit
        self.offset = offset

    @property
    def project_id(self):
        r"""Gets the project_id of this ListPlaybookInstancesRequest.

        项目ID

        :return: The project_id of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListPlaybookInstancesRequest.

        项目ID

        :param project_id: The project_id of this ListPlaybookInstancesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListPlaybookInstancesRequest.

        工作空间ID

        :return: The workspace_id of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListPlaybookInstancesRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListPlaybookInstancesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def status(self):
        r"""Gets the status of this ListPlaybookInstancesRequest.

        剧本实例状态. (RUNNING--运行中、FINISHED--成功、FAILED--失败、RETRYING--重试中、TERMINATING--终止中、TERMINATED--已终止)

        :return: The status of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPlaybookInstancesRequest.

        剧本实例状态. (RUNNING--运行中、FINISHED--成功、FAILED--失败、RETRYING--重试中、TERMINATING--终止中、TERMINATED--已终止)

        :param status: The status of this ListPlaybookInstancesRequest.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ListPlaybookInstancesRequest.

        实例名称

        :return: The name of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPlaybookInstancesRequest.

        实例名称

        :param name: The name of this ListPlaybookInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def playbook_name(self):
        r"""Gets the playbook_name of this ListPlaybookInstancesRequest.

        剧本名称

        :return: The playbook_name of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._playbook_name

    @playbook_name.setter
    def playbook_name(self, playbook_name):
        r"""Sets the playbook_name of this ListPlaybookInstancesRequest.

        剧本名称

        :param playbook_name: The playbook_name of this ListPlaybookInstancesRequest.
        :type playbook_name: str
        """
        self._playbook_name = playbook_name

    @property
    def dataclass_name(self):
        r"""Gets the dataclass_name of this ListPlaybookInstancesRequest.

        数据类名称

        :return: The dataclass_name of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        r"""Sets the dataclass_name of this ListPlaybookInstancesRequest.

        数据类名称

        :param dataclass_name: The dataclass_name of this ListPlaybookInstancesRequest.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def dataobject_name(self):
        r"""Gets the dataobject_name of this ListPlaybookInstancesRequest.

        数据对象名称

        :return: The dataobject_name of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._dataobject_name

    @dataobject_name.setter
    def dataobject_name(self, dataobject_name):
        r"""Sets the dataobject_name of this ListPlaybookInstancesRequest.

        数据对象名称

        :param dataobject_name: The dataobject_name of this ListPlaybookInstancesRequest.
        :type dataobject_name: str
        """
        self._dataobject_name = dataobject_name

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ListPlaybookInstancesRequest.

        触发类型. TIMER--定时触发, EVENT--事件触发

        :return: The trigger_type of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ListPlaybookInstancesRequest.

        触发类型. TIMER--定时触发, EVENT--事件触发

        :param trigger_type: The trigger_type of this ListPlaybookInstancesRequest.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def from_date(self):
        r"""Gets the from_date of this ListPlaybookInstancesRequest.

        查询起始时间

        :return: The from_date of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        r"""Sets the from_date of this ListPlaybookInstancesRequest.

        查询起始时间

        :param from_date: The from_date of this ListPlaybookInstancesRequest.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        r"""Gets the to_date of this ListPlaybookInstancesRequest.

        查询结束时间

        :return: The to_date of this ListPlaybookInstancesRequest.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        r"""Sets the to_date of this ListPlaybookInstancesRequest.

        查询结束时间

        :param to_date: The to_date of this ListPlaybookInstancesRequest.
        :type to_date: str
        """
        self._to_date = to_date

    @property
    def limit(self):
        r"""Gets the limit of this ListPlaybookInstancesRequest.

        分页查询参数，用于指定一次查询最多的结果数，从1开始

        :return: The limit of this ListPlaybookInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPlaybookInstancesRequest.

        分页查询参数，用于指定一次查询最多的结果数，从1开始

        :param limit: The limit of this ListPlaybookInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPlaybookInstancesRequest.

        分页查询参数。用于指定查询结果的起始位置，从0开始

        :return: The offset of this ListPlaybookInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPlaybookInstancesRequest.

        分页查询参数。用于指定查询结果的起始位置，从0开始

        :param offset: The offset of this ListPlaybookInstancesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListPlaybookInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
