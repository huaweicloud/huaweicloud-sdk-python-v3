# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OfflineTaskInfo:

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
        'status': 'str',
        'engine_type': 'str',
        'error_log': 'str',
        'description': 'str',
        'create_time': 'str',
        'finish_time': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'engine_type': 'engine_type',
        'error_log': 'error_log',
        'description': 'description',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, status=None, engine_type=None, error_log=None, description=None, create_time=None, finish_time=None, enterprise_project_id=None):
        r"""OfflineTaskInfo

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务状态。 - TRANSFERRING：恢复中 - SUCCESS：成功 - FAILED：失败 - PRECHECK FAILED：预检查失败
        :type status: str
        :param engine_type: 数据库引擎。 - sqlserver：RDS for SQL Server引擎
        :type engine_type: str
        :param error_log: 错误日志。
        :type error_log: str
        :param description: 描述。
        :type description: str
        :param create_time: 任务创建时间。
        :type create_time: str
        :param finish_time: 任务完成时间。
        :type finish_time: str
        :param enterprise_project_id: 企业项目。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._engine_type = None
        self._error_log = None
        self._description = None
        self._create_time = None
        self._finish_time = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.engine_type = engine_type
        if error_log is not None:
            self.error_log = error_log
        if description is not None:
            self.description = description
        self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this OfflineTaskInfo.

        任务ID。

        :return: The id of this OfflineTaskInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OfflineTaskInfo.

        任务ID。

        :param id: The id of this OfflineTaskInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this OfflineTaskInfo.

        任务名称。

        :return: The name of this OfflineTaskInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OfflineTaskInfo.

        任务名称。

        :param name: The name of this OfflineTaskInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this OfflineTaskInfo.

        任务状态。 - TRANSFERRING：恢复中 - SUCCESS：成功 - FAILED：失败 - PRECHECK FAILED：预检查失败

        :return: The status of this OfflineTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OfflineTaskInfo.

        任务状态。 - TRANSFERRING：恢复中 - SUCCESS：成功 - FAILED：失败 - PRECHECK FAILED：预检查失败

        :param status: The status of this OfflineTaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def engine_type(self):
        r"""Gets the engine_type of this OfflineTaskInfo.

        数据库引擎。 - sqlserver：RDS for SQL Server引擎

        :return: The engine_type of this OfflineTaskInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this OfflineTaskInfo.

        数据库引擎。 - sqlserver：RDS for SQL Server引擎

        :param engine_type: The engine_type of this OfflineTaskInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def error_log(self):
        r"""Gets the error_log of this OfflineTaskInfo.

        错误日志。

        :return: The error_log of this OfflineTaskInfo.
        :rtype: str
        """
        return self._error_log

    @error_log.setter
    def error_log(self, error_log):
        r"""Sets the error_log of this OfflineTaskInfo.

        错误日志。

        :param error_log: The error_log of this OfflineTaskInfo.
        :type error_log: str
        """
        self._error_log = error_log

    @property
    def description(self):
        r"""Gets the description of this OfflineTaskInfo.

        描述。

        :return: The description of this OfflineTaskInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OfflineTaskInfo.

        描述。

        :param description: The description of this OfflineTaskInfo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this OfflineTaskInfo.

        任务创建时间。

        :return: The create_time of this OfflineTaskInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this OfflineTaskInfo.

        任务创建时间。

        :param create_time: The create_time of this OfflineTaskInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this OfflineTaskInfo.

        任务完成时间。

        :return: The finish_time of this OfflineTaskInfo.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this OfflineTaskInfo.

        任务完成时间。

        :param finish_time: The finish_time of this OfflineTaskInfo.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this OfflineTaskInfo.

        企业项目。

        :return: The enterprise_project_id of this OfflineTaskInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this OfflineTaskInfo.

        企业项目。

        :param enterprise_project_id: The enterprise_project_id of this OfflineTaskInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, OfflineTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
