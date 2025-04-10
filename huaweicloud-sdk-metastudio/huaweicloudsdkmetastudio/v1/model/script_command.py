# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptCommand:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'room_id': 'str',
        'job_id': 'str',
        'command_id': 'str',
        'command_time': 'str',
        'scene_scripts': 'list[LivePlayingScriptInfo]'
    }

    attribute_map = {
        'room_id': 'room_id',
        'job_id': 'job_id',
        'command_id': 'command_id',
        'command_time': 'command_time',
        'scene_scripts': 'scene_scripts'
    }

    def __init__(self, room_id=None, job_id=None, command_id=None, command_time=None, scene_scripts=None):
        r"""ScriptCommand

        The model defined in huaweicloud sdk

        :param room_id: 直播间ID
        :type room_id: str
        :param job_id: 直播任务ID。
        :type job_id: str
        :param command_id: 命令ID。
        :type command_id: str
        :param command_time: 命令时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type command_time: str
        :param scene_scripts: 直播剧本列表。
        :type scene_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LivePlayingScriptInfo`]
        """
        
        

        self._room_id = None
        self._job_id = None
        self._command_id = None
        self._command_time = None
        self._scene_scripts = None
        self.discriminator = None

        if room_id is not None:
            self.room_id = room_id
        if job_id is not None:
            self.job_id = job_id
        if command_id is not None:
            self.command_id = command_id
        if command_time is not None:
            self.command_time = command_time
        if scene_scripts is not None:
            self.scene_scripts = scene_scripts

    @property
    def room_id(self):
        r"""Gets the room_id of this ScriptCommand.

        直播间ID

        :return: The room_id of this ScriptCommand.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this ScriptCommand.

        直播间ID

        :param room_id: The room_id of this ScriptCommand.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ScriptCommand.

        直播任务ID。

        :return: The job_id of this ScriptCommand.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ScriptCommand.

        直播任务ID。

        :param job_id: The job_id of this ScriptCommand.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def command_id(self):
        r"""Gets the command_id of this ScriptCommand.

        命令ID。

        :return: The command_id of this ScriptCommand.
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        r"""Sets the command_id of this ScriptCommand.

        命令ID。

        :param command_id: The command_id of this ScriptCommand.
        :type command_id: str
        """
        self._command_id = command_id

    @property
    def command_time(self):
        r"""Gets the command_time of this ScriptCommand.

        命令时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The command_time of this ScriptCommand.
        :rtype: str
        """
        return self._command_time

    @command_time.setter
    def command_time(self, command_time):
        r"""Sets the command_time of this ScriptCommand.

        命令时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param command_time: The command_time of this ScriptCommand.
        :type command_time: str
        """
        self._command_time = command_time

    @property
    def scene_scripts(self):
        r"""Gets the scene_scripts of this ScriptCommand.

        直播剧本列表。

        :return: The scene_scripts of this ScriptCommand.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LivePlayingScriptInfo`]
        """
        return self._scene_scripts

    @scene_scripts.setter
    def scene_scripts(self, scene_scripts):
        r"""Sets the scene_scripts of this ScriptCommand.

        直播剧本列表。

        :param scene_scripts: The scene_scripts of this ScriptCommand.
        :type scene_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LivePlayingScriptInfo`]
        """
        self._scene_scripts = scene_scripts

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
        if not isinstance(other, ScriptCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
