# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationForList:

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
        'project_id': 'str',
        'desktop_id': 'str',
        'screen_record_id': 'str',
        'username': 'str',
        'event_type': 'str',
        'event_level': 'str',
        'event_id': 'str',
        'event_data': 'str',
        'operation_time': 'str',
        'relative_start_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'desktop_id': 'desktop_id',
        'screen_record_id': 'screen_record_id',
        'username': 'username',
        'event_type': 'event_type',
        'event_level': 'event_level',
        'event_id': 'event_id',
        'event_data': 'event_data',
        'operation_time': 'operation_time',
        'relative_start_time': 'relative_start_time'
    }

    def __init__(self, id=None, project_id=None, desktop_id=None, screen_record_id=None, username=None, event_type=None, event_level=None, event_id=None, event_data=None, operation_time=None, relative_start_time=None):
        r"""OperationForList

        The model defined in huaweicloud sdk

        :param id: 主键UUID。
        :type id: str
        :param project_id: 项目ID。
        :type project_id: str
        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param screen_record_id: 录屏记录ID。
        :type screen_record_id: str
        :param username: 用户名。
        :type username: str
        :param event_type: 事件类型。 - APP：应用监控。 - FILE：文件监控。 - REG：注册表监控。 - HDP：协议行为监控。
        :type event_type: str
        :param event_level: 事件级别。 - INFO：提示。 - ALARM：告警。 - ERROR：异常。
        :type event_level: str
        :param event_id: 事件ID。 - APP_START：应用程序启动 - APP_STOP：应用程序结束 - APP_CRASH：应用程序异常退出 - APP_HANG：应用程序无响应 - APP_INSTALL：应用安装 - APP_UNINSTALL：应用卸裁 - FILE_CREATE：文件创建 - FILE_DELETE：文件删除 - FILE_RENAME：文件改名 - HDP_FILE：文件重定向 - HDP_USB：USB插拔事件 - HDP_CLIPBOARD：剪切板操作 - HDP_INPUTIDLE：空闲无操作 - HDP_PRINT：文件打印
        :type event_id: str
        :param event_data: 事件内容。
        :type event_data: str
        :param operation_time: 操作时间（2024-10-15T11:04:41.263Z）。
        :type operation_time: str
        :param relative_start_time: 相对于视频开始的时间（秒）。
        :type relative_start_time: int
        """
        
        

        self._id = None
        self._project_id = None
        self._desktop_id = None
        self._screen_record_id = None
        self._username = None
        self._event_type = None
        self._event_level = None
        self._event_id = None
        self._event_data = None
        self._operation_time = None
        self._relative_start_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if screen_record_id is not None:
            self.screen_record_id = screen_record_id
        if username is not None:
            self.username = username
        if event_type is not None:
            self.event_type = event_type
        if event_level is not None:
            self.event_level = event_level
        if event_id is not None:
            self.event_id = event_id
        if event_data is not None:
            self.event_data = event_data
        if operation_time is not None:
            self.operation_time = operation_time
        if relative_start_time is not None:
            self.relative_start_time = relative_start_time

    @property
    def id(self):
        r"""Gets the id of this OperationForList.

        主键UUID。

        :return: The id of this OperationForList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OperationForList.

        主键UUID。

        :param id: The id of this OperationForList.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this OperationForList.

        项目ID。

        :return: The project_id of this OperationForList.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this OperationForList.

        项目ID。

        :param project_id: The project_id of this OperationForList.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this OperationForList.

        桌面ID。

        :return: The desktop_id of this OperationForList.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this OperationForList.

        桌面ID。

        :param desktop_id: The desktop_id of this OperationForList.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def screen_record_id(self):
        r"""Gets the screen_record_id of this OperationForList.

        录屏记录ID。

        :return: The screen_record_id of this OperationForList.
        :rtype: str
        """
        return self._screen_record_id

    @screen_record_id.setter
    def screen_record_id(self, screen_record_id):
        r"""Sets the screen_record_id of this OperationForList.

        录屏记录ID。

        :param screen_record_id: The screen_record_id of this OperationForList.
        :type screen_record_id: str
        """
        self._screen_record_id = screen_record_id

    @property
    def username(self):
        r"""Gets the username of this OperationForList.

        用户名。

        :return: The username of this OperationForList.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this OperationForList.

        用户名。

        :param username: The username of this OperationForList.
        :type username: str
        """
        self._username = username

    @property
    def event_type(self):
        r"""Gets the event_type of this OperationForList.

        事件类型。 - APP：应用监控。 - FILE：文件监控。 - REG：注册表监控。 - HDP：协议行为监控。

        :return: The event_type of this OperationForList.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this OperationForList.

        事件类型。 - APP：应用监控。 - FILE：文件监控。 - REG：注册表监控。 - HDP：协议行为监控。

        :param event_type: The event_type of this OperationForList.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_level(self):
        r"""Gets the event_level of this OperationForList.

        事件级别。 - INFO：提示。 - ALARM：告警。 - ERROR：异常。

        :return: The event_level of this OperationForList.
        :rtype: str
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        r"""Sets the event_level of this OperationForList.

        事件级别。 - INFO：提示。 - ALARM：告警。 - ERROR：异常。

        :param event_level: The event_level of this OperationForList.
        :type event_level: str
        """
        self._event_level = event_level

    @property
    def event_id(self):
        r"""Gets the event_id of this OperationForList.

        事件ID。 - APP_START：应用程序启动 - APP_STOP：应用程序结束 - APP_CRASH：应用程序异常退出 - APP_HANG：应用程序无响应 - APP_INSTALL：应用安装 - APP_UNINSTALL：应用卸裁 - FILE_CREATE：文件创建 - FILE_DELETE：文件删除 - FILE_RENAME：文件改名 - HDP_FILE：文件重定向 - HDP_USB：USB插拔事件 - HDP_CLIPBOARD：剪切板操作 - HDP_INPUTIDLE：空闲无操作 - HDP_PRINT：文件打印

        :return: The event_id of this OperationForList.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this OperationForList.

        事件ID。 - APP_START：应用程序启动 - APP_STOP：应用程序结束 - APP_CRASH：应用程序异常退出 - APP_HANG：应用程序无响应 - APP_INSTALL：应用安装 - APP_UNINSTALL：应用卸裁 - FILE_CREATE：文件创建 - FILE_DELETE：文件删除 - FILE_RENAME：文件改名 - HDP_FILE：文件重定向 - HDP_USB：USB插拔事件 - HDP_CLIPBOARD：剪切板操作 - HDP_INPUTIDLE：空闲无操作 - HDP_PRINT：文件打印

        :param event_id: The event_id of this OperationForList.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_data(self):
        r"""Gets the event_data of this OperationForList.

        事件内容。

        :return: The event_data of this OperationForList.
        :rtype: str
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):
        r"""Sets the event_data of this OperationForList.

        事件内容。

        :param event_data: The event_data of this OperationForList.
        :type event_data: str
        """
        self._event_data = event_data

    @property
    def operation_time(self):
        r"""Gets the operation_time of this OperationForList.

        操作时间（2024-10-15T11:04:41.263Z）。

        :return: The operation_time of this OperationForList.
        :rtype: str
        """
        return self._operation_time

    @operation_time.setter
    def operation_time(self, operation_time):
        r"""Sets the operation_time of this OperationForList.

        操作时间（2024-10-15T11:04:41.263Z）。

        :param operation_time: The operation_time of this OperationForList.
        :type operation_time: str
        """
        self._operation_time = operation_time

    @property
    def relative_start_time(self):
        r"""Gets the relative_start_time of this OperationForList.

        相对于视频开始的时间（秒）。

        :return: The relative_start_time of this OperationForList.
        :rtype: int
        """
        return self._relative_start_time

    @relative_start_time.setter
    def relative_start_time(self, relative_start_time):
        r"""Sets the relative_start_time of this OperationForList.

        相对于视频开始的时间（秒）。

        :param relative_start_time: The relative_start_time of this OperationForList.
        :type relative_start_time: int
        """
        self._relative_start_time = relative_start_time

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
        if not isinstance(other, OperationForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
