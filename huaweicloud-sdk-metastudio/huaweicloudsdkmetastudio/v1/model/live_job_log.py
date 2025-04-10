# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveJobLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interaction_records_url': 'str',
        'job_config_records_url': 'str',
        'scripts_records_url': 'str',
        'command_reviced_records_url': 'str',
        'command_exec_records_url': 'str'
    }

    attribute_map = {
        'interaction_records_url': 'interaction_records_url',
        'job_config_records_url': 'job_config_records_url',
        'scripts_records_url': 'scripts_records_url',
        'command_reviced_records_url': 'command_reviced_records_url',
        'command_exec_records_url': 'command_exec_records_url'
    }

    def __init__(self, interaction_records_url=None, job_config_records_url=None, scripts_records_url=None, command_reviced_records_url=None, command_exec_records_url=None):
        r"""LiveJobLog

        The model defined in huaweicloud sdk

        :param interaction_records_url: 直播互动记录文件地址
        :type interaction_records_url: str
        :param job_config_records_url: 任务配置记录文件地址
        :type job_config_records_url: str
        :param scripts_records_url: 剧本播放记录文件地址
        :type scripts_records_url: str
        :param command_reviced_records_url: 命令接受记录文件地址
        :type command_reviced_records_url: str
        :param command_exec_records_url: 命令执行记录文件地址
        :type command_exec_records_url: str
        """
        
        

        self._interaction_records_url = None
        self._job_config_records_url = None
        self._scripts_records_url = None
        self._command_reviced_records_url = None
        self._command_exec_records_url = None
        self.discriminator = None

        if interaction_records_url is not None:
            self.interaction_records_url = interaction_records_url
        if job_config_records_url is not None:
            self.job_config_records_url = job_config_records_url
        if scripts_records_url is not None:
            self.scripts_records_url = scripts_records_url
        if command_reviced_records_url is not None:
            self.command_reviced_records_url = command_reviced_records_url
        if command_exec_records_url is not None:
            self.command_exec_records_url = command_exec_records_url

    @property
    def interaction_records_url(self):
        r"""Gets the interaction_records_url of this LiveJobLog.

        直播互动记录文件地址

        :return: The interaction_records_url of this LiveJobLog.
        :rtype: str
        """
        return self._interaction_records_url

    @interaction_records_url.setter
    def interaction_records_url(self, interaction_records_url):
        r"""Sets the interaction_records_url of this LiveJobLog.

        直播互动记录文件地址

        :param interaction_records_url: The interaction_records_url of this LiveJobLog.
        :type interaction_records_url: str
        """
        self._interaction_records_url = interaction_records_url

    @property
    def job_config_records_url(self):
        r"""Gets the job_config_records_url of this LiveJobLog.

        任务配置记录文件地址

        :return: The job_config_records_url of this LiveJobLog.
        :rtype: str
        """
        return self._job_config_records_url

    @job_config_records_url.setter
    def job_config_records_url(self, job_config_records_url):
        r"""Sets the job_config_records_url of this LiveJobLog.

        任务配置记录文件地址

        :param job_config_records_url: The job_config_records_url of this LiveJobLog.
        :type job_config_records_url: str
        """
        self._job_config_records_url = job_config_records_url

    @property
    def scripts_records_url(self):
        r"""Gets the scripts_records_url of this LiveJobLog.

        剧本播放记录文件地址

        :return: The scripts_records_url of this LiveJobLog.
        :rtype: str
        """
        return self._scripts_records_url

    @scripts_records_url.setter
    def scripts_records_url(self, scripts_records_url):
        r"""Sets the scripts_records_url of this LiveJobLog.

        剧本播放记录文件地址

        :param scripts_records_url: The scripts_records_url of this LiveJobLog.
        :type scripts_records_url: str
        """
        self._scripts_records_url = scripts_records_url

    @property
    def command_reviced_records_url(self):
        r"""Gets the command_reviced_records_url of this LiveJobLog.

        命令接受记录文件地址

        :return: The command_reviced_records_url of this LiveJobLog.
        :rtype: str
        """
        return self._command_reviced_records_url

    @command_reviced_records_url.setter
    def command_reviced_records_url(self, command_reviced_records_url):
        r"""Sets the command_reviced_records_url of this LiveJobLog.

        命令接受记录文件地址

        :param command_reviced_records_url: The command_reviced_records_url of this LiveJobLog.
        :type command_reviced_records_url: str
        """
        self._command_reviced_records_url = command_reviced_records_url

    @property
    def command_exec_records_url(self):
        r"""Gets the command_exec_records_url of this LiveJobLog.

        命令执行记录文件地址

        :return: The command_exec_records_url of this LiveJobLog.
        :rtype: str
        """
        return self._command_exec_records_url

    @command_exec_records_url.setter
    def command_exec_records_url(self, command_exec_records_url):
        r"""Sets the command_exec_records_url of this LiveJobLog.

        命令执行记录文件地址

        :param command_exec_records_url: The command_exec_records_url of this LiveJobLog.
        :type command_exec_records_url: str
        """
        self._command_exec_records_url = command_exec_records_url

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
        if not isinstance(other, LiveJobLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
