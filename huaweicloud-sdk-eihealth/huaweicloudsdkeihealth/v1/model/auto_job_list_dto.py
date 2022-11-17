# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoJobListDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'priority': 'int',
        'timeout': 'int',
        'status': 'str',
        'create_time': 'str',
        'finish_time': 'str',
        'failed_reason': 'str',
        'user_name': 'str',
        'tool_info': 'ToolInfoDto',
        'database_id': 'str',
        'database_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'labels': 'labels',
        'priority': 'priority',
        'timeout': 'timeout',
        'status': 'status',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'failed_reason': 'failed_reason',
        'user_name': 'user_name',
        'tool_info': 'tool_info',
        'database_id': 'database_id',
        'database_name': 'database_name'
    }

    def __init__(self, id=None, name=None, description=None, labels=None, priority=None, timeout=None, status=None, create_time=None, finish_time=None, failed_reason=None, user_name=None, tool_info=None, database_id=None, database_name=None):
        """AutoJobListDto

        The model defined in huaweicloud sdk

        :param id: 自动作业id
        :type id: str
        :param name: 自动作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)
        :type name: str
        :param description: 自动作业的描述, 取值范围：输入字符最大长度为255
        :type description: str
        :param labels: 自动作业标签
        :type labels: list[str]
        :param priority: 自动作业优先级，[0,9]，0表示最低，默认0
        :type priority: int
        :param timeout: 作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440
        :type timeout: int
        :param status: 自动作业状态
        :type status: str
        :param create_time: 自动作业创建时间
        :type create_time: str
        :param finish_time: 自动作业结束时间
        :type finish_time: str
        :param failed_reason: 失败原因，当自动作业执行失败时会返回，比如依赖的数据表，流程不存在等等
        :type failed_reason: str
        :param user_name: 自动作业的创建者
        :type user_name: str
        :param tool_info: 
        :type tool_info: :class:`huaweicloudsdkeihealth.v1.ToolInfoDto`
        :param database_id: 自动作业依赖的数据表ID
        :type database_id: str
        :param database_name: 自动作业依赖的数据表名称
        :type database_name: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._labels = None
        self._priority = None
        self._timeout = None
        self._status = None
        self._create_time = None
        self._finish_time = None
        self._failed_reason = None
        self._user_name = None
        self._tool_info = None
        self._database_id = None
        self._database_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if priority is not None:
            self.priority = priority
        if timeout is not None:
            self.timeout = timeout
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if user_name is not None:
            self.user_name = user_name
        if tool_info is not None:
            self.tool_info = tool_info
        if database_id is not None:
            self.database_id = database_id
        if database_name is not None:
            self.database_name = database_name

    @property
    def id(self):
        """Gets the id of this AutoJobListDto.

        自动作业id

        :return: The id of this AutoJobListDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AutoJobListDto.

        自动作业id

        :param id: The id of this AutoJobListDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AutoJobListDto.

        自动作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :return: The name of this AutoJobListDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AutoJobListDto.

        自动作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :param name: The name of this AutoJobListDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AutoJobListDto.

        自动作业的描述, 取值范围：输入字符最大长度为255

        :return: The description of this AutoJobListDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AutoJobListDto.

        自动作业的描述, 取值范围：输入字符最大长度为255

        :param description: The description of this AutoJobListDto.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this AutoJobListDto.

        自动作业标签

        :return: The labels of this AutoJobListDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this AutoJobListDto.

        自动作业标签

        :param labels: The labels of this AutoJobListDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def priority(self):
        """Gets the priority of this AutoJobListDto.

        自动作业优先级，[0,9]，0表示最低，默认0

        :return: The priority of this AutoJobListDto.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this AutoJobListDto.

        自动作业优先级，[0,9]，0表示最低，默认0

        :param priority: The priority of this AutoJobListDto.
        :type priority: int
        """
        self._priority = priority

    @property
    def timeout(self):
        """Gets the timeout of this AutoJobListDto.

        作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440

        :return: The timeout of this AutoJobListDto.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this AutoJobListDto.

        作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440

        :param timeout: The timeout of this AutoJobListDto.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def status(self):
        """Gets the status of this AutoJobListDto.

        自动作业状态

        :return: The status of this AutoJobListDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AutoJobListDto.

        自动作业状态

        :param status: The status of this AutoJobListDto.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this AutoJobListDto.

        自动作业创建时间

        :return: The create_time of this AutoJobListDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AutoJobListDto.

        自动作业创建时间

        :param create_time: The create_time of this AutoJobListDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        """Gets the finish_time of this AutoJobListDto.

        自动作业结束时间

        :return: The finish_time of this AutoJobListDto.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this AutoJobListDto.

        自动作业结束时间

        :param finish_time: The finish_time of this AutoJobListDto.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def failed_reason(self):
        """Gets the failed_reason of this AutoJobListDto.

        失败原因，当自动作业执行失败时会返回，比如依赖的数据表，流程不存在等等

        :return: The failed_reason of this AutoJobListDto.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this AutoJobListDto.

        失败原因，当自动作业执行失败时会返回，比如依赖的数据表，流程不存在等等

        :param failed_reason: The failed_reason of this AutoJobListDto.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def user_name(self):
        """Gets the user_name of this AutoJobListDto.

        自动作业的创建者

        :return: The user_name of this AutoJobListDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AutoJobListDto.

        自动作业的创建者

        :param user_name: The user_name of this AutoJobListDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def tool_info(self):
        """Gets the tool_info of this AutoJobListDto.

        :return: The tool_info of this AutoJobListDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ToolInfoDto`
        """
        return self._tool_info

    @tool_info.setter
    def tool_info(self, tool_info):
        """Sets the tool_info of this AutoJobListDto.

        :param tool_info: The tool_info of this AutoJobListDto.
        :type tool_info: :class:`huaweicloudsdkeihealth.v1.ToolInfoDto`
        """
        self._tool_info = tool_info

    @property
    def database_id(self):
        """Gets the database_id of this AutoJobListDto.

        自动作业依赖的数据表ID

        :return: The database_id of this AutoJobListDto.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """Sets the database_id of this AutoJobListDto.

        自动作业依赖的数据表ID

        :param database_id: The database_id of this AutoJobListDto.
        :type database_id: str
        """
        self._database_id = database_id

    @property
    def database_name(self):
        """Gets the database_name of this AutoJobListDto.

        自动作业依赖的数据表名称

        :return: The database_name of this AutoJobListDto.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this AutoJobListDto.

        自动作业依赖的数据表名称

        :param database_name: The database_name of this AutoJobListDto.
        :type database_name: str
        """
        self._database_name = database_name

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
        if not isinstance(other, AutoJobListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
