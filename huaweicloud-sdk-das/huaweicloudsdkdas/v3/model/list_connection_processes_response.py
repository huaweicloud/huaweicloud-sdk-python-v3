# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectionProcessesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_info_list': 'list[ProcessInfo]',
        'total': 'int',
        'user_info_list': 'list[str]',
        'db_info_list': 'list[str]',
        'host_info_list': 'list[str]',
        'state_info_list': 'list[str]',
        'command_info_list': 'list[str]',
        'session_exec_time': 'object',
        'idle_session': 'int',
        'active_session': 'int',
        'summary': 'list[ProcessSummary]',
        'user_stats': 'list[ProcessStats]',
        'host_stats': 'list[ProcessStats]',
        'db_stats': 'list[ProcessStats]',
        'show_version_support_message': 'bool',
        'show_warn_message': 'bool'
    }

    attribute_map = {
        'process_info_list': 'process_info_list',
        'total': 'total',
        'user_info_list': 'user_info_list',
        'db_info_list': 'db_info_list',
        'host_info_list': 'host_info_list',
        'state_info_list': 'state_info_list',
        'command_info_list': 'command_info_list',
        'session_exec_time': 'session_exec_time',
        'idle_session': 'idle_session',
        'active_session': 'active_session',
        'summary': 'summary',
        'user_stats': 'user_stats',
        'host_stats': 'host_stats',
        'db_stats': 'db_stats',
        'show_version_support_message': 'show_version_support_message',
        'show_warn_message': 'show_warn_message'
    }

    def __init__(self, process_info_list=None, total=None, user_info_list=None, db_info_list=None, host_info_list=None, state_info_list=None, command_info_list=None, session_exec_time=None, idle_session=None, active_session=None, summary=None, user_stats=None, host_stats=None, db_stats=None, show_version_support_message=None, show_warn_message=None):
        r"""ListConnectionProcessesResponse

        The model defined in huaweicloud sdk

        :param process_info_list: 会话信息列表
        :type process_info_list: list[:class:`huaweicloudsdkdas.v3.ProcessInfo`]
        :param total: 根据条件筛选的总会话数
        :type total: int
        :param user_info_list: 用户列表
        :type user_info_list: list[str]
        :param db_info_list: 数据库列表
        :type db_info_list: list[str]
        :param host_info_list: 来源IP列表
        :type host_info_list: list[str]
        :param state_info_list: 状态列表
        :type state_info_list: list[str]
        :param command_info_list: 命令列表
        :type command_info_list: list[str]
        :param session_exec_time: 会话执行时间比例
        :type session_exec_time: object
        :param idle_session: 空闲会话数
        :type idle_session: int
        :param active_session: 运行会话数
        :type active_session: int
        :param summary: 概要
        :type summary: list[:class:`huaweicloudsdkdas.v3.ProcessSummary`]
        :param user_stats: 按用户统计信息
        :type user_stats: list[:class:`huaweicloudsdkdas.v3.ProcessStats`]
        :param host_stats: 按访问来源统计
        :type host_stats: list[:class:`huaweicloudsdkdas.v3.ProcessStats`]
        :param db_stats: 按数据库统计
        :type db_stats: list[:class:`huaweicloudsdkdas.v3.ProcessStats`]
        :param show_version_support_message: 是否显示版本支持信息
        :type show_version_support_message: bool
        :param show_warn_message: 是否告警信息
        :type show_warn_message: bool
        """
        
        super().__init__()

        self._process_info_list = None
        self._total = None
        self._user_info_list = None
        self._db_info_list = None
        self._host_info_list = None
        self._state_info_list = None
        self._command_info_list = None
        self._session_exec_time = None
        self._idle_session = None
        self._active_session = None
        self._summary = None
        self._user_stats = None
        self._host_stats = None
        self._db_stats = None
        self._show_version_support_message = None
        self._show_warn_message = None
        self.discriminator = None

        if process_info_list is not None:
            self.process_info_list = process_info_list
        if total is not None:
            self.total = total
        if user_info_list is not None:
            self.user_info_list = user_info_list
        if db_info_list is not None:
            self.db_info_list = db_info_list
        if host_info_list is not None:
            self.host_info_list = host_info_list
        if state_info_list is not None:
            self.state_info_list = state_info_list
        if command_info_list is not None:
            self.command_info_list = command_info_list
        if session_exec_time is not None:
            self.session_exec_time = session_exec_time
        if idle_session is not None:
            self.idle_session = idle_session
        if active_session is not None:
            self.active_session = active_session
        if summary is not None:
            self.summary = summary
        if user_stats is not None:
            self.user_stats = user_stats
        if host_stats is not None:
            self.host_stats = host_stats
        if db_stats is not None:
            self.db_stats = db_stats
        if show_version_support_message is not None:
            self.show_version_support_message = show_version_support_message
        if show_warn_message is not None:
            self.show_warn_message = show_warn_message

    @property
    def process_info_list(self):
        r"""Gets the process_info_list of this ListConnectionProcessesResponse.

        会话信息列表

        :return: The process_info_list of this ListConnectionProcessesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ProcessInfo`]
        """
        return self._process_info_list

    @process_info_list.setter
    def process_info_list(self, process_info_list):
        r"""Sets the process_info_list of this ListConnectionProcessesResponse.

        会话信息列表

        :param process_info_list: The process_info_list of this ListConnectionProcessesResponse.
        :type process_info_list: list[:class:`huaweicloudsdkdas.v3.ProcessInfo`]
        """
        self._process_info_list = process_info_list

    @property
    def total(self):
        r"""Gets the total of this ListConnectionProcessesResponse.

        根据条件筛选的总会话数

        :return: The total of this ListConnectionProcessesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListConnectionProcessesResponse.

        根据条件筛选的总会话数

        :param total: The total of this ListConnectionProcessesResponse.
        :type total: int
        """
        self._total = total

    @property
    def user_info_list(self):
        r"""Gets the user_info_list of this ListConnectionProcessesResponse.

        用户列表

        :return: The user_info_list of this ListConnectionProcessesResponse.
        :rtype: list[str]
        """
        return self._user_info_list

    @user_info_list.setter
    def user_info_list(self, user_info_list):
        r"""Sets the user_info_list of this ListConnectionProcessesResponse.

        用户列表

        :param user_info_list: The user_info_list of this ListConnectionProcessesResponse.
        :type user_info_list: list[str]
        """
        self._user_info_list = user_info_list

    @property
    def db_info_list(self):
        r"""Gets the db_info_list of this ListConnectionProcessesResponse.

        数据库列表

        :return: The db_info_list of this ListConnectionProcessesResponse.
        :rtype: list[str]
        """
        return self._db_info_list

    @db_info_list.setter
    def db_info_list(self, db_info_list):
        r"""Sets the db_info_list of this ListConnectionProcessesResponse.

        数据库列表

        :param db_info_list: The db_info_list of this ListConnectionProcessesResponse.
        :type db_info_list: list[str]
        """
        self._db_info_list = db_info_list

    @property
    def host_info_list(self):
        r"""Gets the host_info_list of this ListConnectionProcessesResponse.

        来源IP列表

        :return: The host_info_list of this ListConnectionProcessesResponse.
        :rtype: list[str]
        """
        return self._host_info_list

    @host_info_list.setter
    def host_info_list(self, host_info_list):
        r"""Sets the host_info_list of this ListConnectionProcessesResponse.

        来源IP列表

        :param host_info_list: The host_info_list of this ListConnectionProcessesResponse.
        :type host_info_list: list[str]
        """
        self._host_info_list = host_info_list

    @property
    def state_info_list(self):
        r"""Gets the state_info_list of this ListConnectionProcessesResponse.

        状态列表

        :return: The state_info_list of this ListConnectionProcessesResponse.
        :rtype: list[str]
        """
        return self._state_info_list

    @state_info_list.setter
    def state_info_list(self, state_info_list):
        r"""Sets the state_info_list of this ListConnectionProcessesResponse.

        状态列表

        :param state_info_list: The state_info_list of this ListConnectionProcessesResponse.
        :type state_info_list: list[str]
        """
        self._state_info_list = state_info_list

    @property
    def command_info_list(self):
        r"""Gets the command_info_list of this ListConnectionProcessesResponse.

        命令列表

        :return: The command_info_list of this ListConnectionProcessesResponse.
        :rtype: list[str]
        """
        return self._command_info_list

    @command_info_list.setter
    def command_info_list(self, command_info_list):
        r"""Sets the command_info_list of this ListConnectionProcessesResponse.

        命令列表

        :param command_info_list: The command_info_list of this ListConnectionProcessesResponse.
        :type command_info_list: list[str]
        """
        self._command_info_list = command_info_list

    @property
    def session_exec_time(self):
        r"""Gets the session_exec_time of this ListConnectionProcessesResponse.

        会话执行时间比例

        :return: The session_exec_time of this ListConnectionProcessesResponse.
        :rtype: object
        """
        return self._session_exec_time

    @session_exec_time.setter
    def session_exec_time(self, session_exec_time):
        r"""Sets the session_exec_time of this ListConnectionProcessesResponse.

        会话执行时间比例

        :param session_exec_time: The session_exec_time of this ListConnectionProcessesResponse.
        :type session_exec_time: object
        """
        self._session_exec_time = session_exec_time

    @property
    def idle_session(self):
        r"""Gets the idle_session of this ListConnectionProcessesResponse.

        空闲会话数

        :return: The idle_session of this ListConnectionProcessesResponse.
        :rtype: int
        """
        return self._idle_session

    @idle_session.setter
    def idle_session(self, idle_session):
        r"""Sets the idle_session of this ListConnectionProcessesResponse.

        空闲会话数

        :param idle_session: The idle_session of this ListConnectionProcessesResponse.
        :type idle_session: int
        """
        self._idle_session = idle_session

    @property
    def active_session(self):
        r"""Gets the active_session of this ListConnectionProcessesResponse.

        运行会话数

        :return: The active_session of this ListConnectionProcessesResponse.
        :rtype: int
        """
        return self._active_session

    @active_session.setter
    def active_session(self, active_session):
        r"""Sets the active_session of this ListConnectionProcessesResponse.

        运行会话数

        :param active_session: The active_session of this ListConnectionProcessesResponse.
        :type active_session: int
        """
        self._active_session = active_session

    @property
    def summary(self):
        r"""Gets the summary of this ListConnectionProcessesResponse.

        概要

        :return: The summary of this ListConnectionProcessesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ProcessSummary`]
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this ListConnectionProcessesResponse.

        概要

        :param summary: The summary of this ListConnectionProcessesResponse.
        :type summary: list[:class:`huaweicloudsdkdas.v3.ProcessSummary`]
        """
        self._summary = summary

    @property
    def user_stats(self):
        r"""Gets the user_stats of this ListConnectionProcessesResponse.

        按用户统计信息

        :return: The user_stats of this ListConnectionProcessesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ProcessStats`]
        """
        return self._user_stats

    @user_stats.setter
    def user_stats(self, user_stats):
        r"""Sets the user_stats of this ListConnectionProcessesResponse.

        按用户统计信息

        :param user_stats: The user_stats of this ListConnectionProcessesResponse.
        :type user_stats: list[:class:`huaweicloudsdkdas.v3.ProcessStats`]
        """
        self._user_stats = user_stats

    @property
    def host_stats(self):
        r"""Gets the host_stats of this ListConnectionProcessesResponse.

        按访问来源统计

        :return: The host_stats of this ListConnectionProcessesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ProcessStats`]
        """
        return self._host_stats

    @host_stats.setter
    def host_stats(self, host_stats):
        r"""Sets the host_stats of this ListConnectionProcessesResponse.

        按访问来源统计

        :param host_stats: The host_stats of this ListConnectionProcessesResponse.
        :type host_stats: list[:class:`huaweicloudsdkdas.v3.ProcessStats`]
        """
        self._host_stats = host_stats

    @property
    def db_stats(self):
        r"""Gets the db_stats of this ListConnectionProcessesResponse.

        按数据库统计

        :return: The db_stats of this ListConnectionProcessesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ProcessStats`]
        """
        return self._db_stats

    @db_stats.setter
    def db_stats(self, db_stats):
        r"""Sets the db_stats of this ListConnectionProcessesResponse.

        按数据库统计

        :param db_stats: The db_stats of this ListConnectionProcessesResponse.
        :type db_stats: list[:class:`huaweicloudsdkdas.v3.ProcessStats`]
        """
        self._db_stats = db_stats

    @property
    def show_version_support_message(self):
        r"""Gets the show_version_support_message of this ListConnectionProcessesResponse.

        是否显示版本支持信息

        :return: The show_version_support_message of this ListConnectionProcessesResponse.
        :rtype: bool
        """
        return self._show_version_support_message

    @show_version_support_message.setter
    def show_version_support_message(self, show_version_support_message):
        r"""Sets the show_version_support_message of this ListConnectionProcessesResponse.

        是否显示版本支持信息

        :param show_version_support_message: The show_version_support_message of this ListConnectionProcessesResponse.
        :type show_version_support_message: bool
        """
        self._show_version_support_message = show_version_support_message

    @property
    def show_warn_message(self):
        r"""Gets the show_warn_message of this ListConnectionProcessesResponse.

        是否告警信息

        :return: The show_warn_message of this ListConnectionProcessesResponse.
        :rtype: bool
        """
        return self._show_warn_message

    @show_warn_message.setter
    def show_warn_message(self, show_warn_message):
        r"""Sets the show_warn_message of this ListConnectionProcessesResponse.

        是否告警信息

        :param show_warn_message: The show_warn_message of this ListConnectionProcessesResponse.
        :type show_warn_message: bool
        """
        self._show_warn_message = show_warn_message

    def to_dict(self):
        import warnings
        warnings.warn("ListConnectionProcessesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListConnectionProcessesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
