# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'sid': 'str',
        'desktop_name': 'str',
        'username': 'str',
        'status': 'str',
        'task_status': 'str'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'sid': 'sid',
        'desktop_name': 'desktop_name',
        'username': 'username',
        'status': 'status',
        'task_status': 'task_status'
    }

    def __init__(self, desktop_id=None, sid=None, desktop_name=None, username=None, status=None, task_status=None):
        r"""DesktopVersionInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面id。
        :type desktop_id: str
        :param sid: 桌面sid。
        :type sid: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param username: 用户名。
        :type username: str
        :param status: 桌面状态。
        :type status: str
        :param task_status: 桌面执行任务状态。
        :type task_status: str
        """
        
        

        self._desktop_id = None
        self._sid = None
        self._desktop_name = None
        self._username = None
        self._status = None
        self._task_status = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if sid is not None:
            self.sid = sid
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if username is not None:
            self.username = username
        if status is not None:
            self.status = status
        if task_status is not None:
            self.task_status = task_status

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this DesktopVersionInfo.

        桌面id。

        :return: The desktop_id of this DesktopVersionInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this DesktopVersionInfo.

        桌面id。

        :param desktop_id: The desktop_id of this DesktopVersionInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def sid(self):
        r"""Gets the sid of this DesktopVersionInfo.

        桌面sid。

        :return: The sid of this DesktopVersionInfo.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        r"""Sets the sid of this DesktopVersionInfo.

        桌面sid。

        :param sid: The sid of this DesktopVersionInfo.
        :type sid: str
        """
        self._sid = sid

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this DesktopVersionInfo.

        桌面名称。

        :return: The desktop_name of this DesktopVersionInfo.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this DesktopVersionInfo.

        桌面名称。

        :param desktop_name: The desktop_name of this DesktopVersionInfo.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def username(self):
        r"""Gets the username of this DesktopVersionInfo.

        用户名。

        :return: The username of this DesktopVersionInfo.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this DesktopVersionInfo.

        用户名。

        :param username: The username of this DesktopVersionInfo.
        :type username: str
        """
        self._username = username

    @property
    def status(self):
        r"""Gets the status of this DesktopVersionInfo.

        桌面状态。

        :return: The status of this DesktopVersionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DesktopVersionInfo.

        桌面状态。

        :param status: The status of this DesktopVersionInfo.
        :type status: str
        """
        self._status = status

    @property
    def task_status(self):
        r"""Gets the task_status of this DesktopVersionInfo.

        桌面执行任务状态。

        :return: The task_status of this DesktopVersionInfo.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this DesktopVersionInfo.

        桌面执行任务状态。

        :param task_status: The task_status of this DesktopVersionInfo.
        :type task_status: str
        """
        self._task_status = task_status

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
        if not isinstance(other, DesktopVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
