# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceProcessesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_sync_time': 'int',
        'total': 'int',
        'data': 'list[object]',
        'user_info_list': 'list[str]',
        'db_info_list': 'list[str]',
        'host_info_list': 'list[str]',
        'state_info_list': 'list[str]',
        'command_info_list': 'list[str]'
    }

    attribute_map = {
        'data_sync_time': 'data_sync_time',
        'total': 'total',
        'data': 'data',
        'user_info_list': 'user_info_list',
        'db_info_list': 'db_info_list',
        'host_info_list': 'host_info_list',
        'state_info_list': 'state_info_list',
        'command_info_list': 'command_info_list'
    }

    def __init__(self, data_sync_time=None, total=None, data=None, user_info_list=None, db_info_list=None, host_info_list=None, state_info_list=None, command_info_list=None):
        r"""ListInstanceProcessesResponse

        The model defined in huaweicloud sdk

        :param data_sync_time: 同步时间
        :type data_sync_time: int
        :param total: 总数
        :type total: int
        :param data: 数据列表
        :type data: list[object]
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
        """
        
        super().__init__()

        self._data_sync_time = None
        self._total = None
        self._data = None
        self._user_info_list = None
        self._db_info_list = None
        self._host_info_list = None
        self._state_info_list = None
        self._command_info_list = None
        self.discriminator = None

        if data_sync_time is not None:
            self.data_sync_time = data_sync_time
        if total is not None:
            self.total = total
        if data is not None:
            self.data = data
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

    @property
    def data_sync_time(self):
        r"""Gets the data_sync_time of this ListInstanceProcessesResponse.

        同步时间

        :return: The data_sync_time of this ListInstanceProcessesResponse.
        :rtype: int
        """
        return self._data_sync_time

    @data_sync_time.setter
    def data_sync_time(self, data_sync_time):
        r"""Sets the data_sync_time of this ListInstanceProcessesResponse.

        同步时间

        :param data_sync_time: The data_sync_time of this ListInstanceProcessesResponse.
        :type data_sync_time: int
        """
        self._data_sync_time = data_sync_time

    @property
    def total(self):
        r"""Gets the total of this ListInstanceProcessesResponse.

        总数

        :return: The total of this ListInstanceProcessesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceProcessesResponse.

        总数

        :param total: The total of this ListInstanceProcessesResponse.
        :type total: int
        """
        self._total = total

    @property
    def data(self):
        r"""Gets the data of this ListInstanceProcessesResponse.

        数据列表

        :return: The data of this ListInstanceProcessesResponse.
        :rtype: list[object]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListInstanceProcessesResponse.

        数据列表

        :param data: The data of this ListInstanceProcessesResponse.
        :type data: list[object]
        """
        self._data = data

    @property
    def user_info_list(self):
        r"""Gets the user_info_list of this ListInstanceProcessesResponse.

        用户列表

        :return: The user_info_list of this ListInstanceProcessesResponse.
        :rtype: list[str]
        """
        return self._user_info_list

    @user_info_list.setter
    def user_info_list(self, user_info_list):
        r"""Sets the user_info_list of this ListInstanceProcessesResponse.

        用户列表

        :param user_info_list: The user_info_list of this ListInstanceProcessesResponse.
        :type user_info_list: list[str]
        """
        self._user_info_list = user_info_list

    @property
    def db_info_list(self):
        r"""Gets the db_info_list of this ListInstanceProcessesResponse.

        数据库列表

        :return: The db_info_list of this ListInstanceProcessesResponse.
        :rtype: list[str]
        """
        return self._db_info_list

    @db_info_list.setter
    def db_info_list(self, db_info_list):
        r"""Sets the db_info_list of this ListInstanceProcessesResponse.

        数据库列表

        :param db_info_list: The db_info_list of this ListInstanceProcessesResponse.
        :type db_info_list: list[str]
        """
        self._db_info_list = db_info_list

    @property
    def host_info_list(self):
        r"""Gets the host_info_list of this ListInstanceProcessesResponse.

        来源IP列表

        :return: The host_info_list of this ListInstanceProcessesResponse.
        :rtype: list[str]
        """
        return self._host_info_list

    @host_info_list.setter
    def host_info_list(self, host_info_list):
        r"""Sets the host_info_list of this ListInstanceProcessesResponse.

        来源IP列表

        :param host_info_list: The host_info_list of this ListInstanceProcessesResponse.
        :type host_info_list: list[str]
        """
        self._host_info_list = host_info_list

    @property
    def state_info_list(self):
        r"""Gets the state_info_list of this ListInstanceProcessesResponse.

        状态列表

        :return: The state_info_list of this ListInstanceProcessesResponse.
        :rtype: list[str]
        """
        return self._state_info_list

    @state_info_list.setter
    def state_info_list(self, state_info_list):
        r"""Sets the state_info_list of this ListInstanceProcessesResponse.

        状态列表

        :param state_info_list: The state_info_list of this ListInstanceProcessesResponse.
        :type state_info_list: list[str]
        """
        self._state_info_list = state_info_list

    @property
    def command_info_list(self):
        r"""Gets the command_info_list of this ListInstanceProcessesResponse.

        命令列表

        :return: The command_info_list of this ListInstanceProcessesResponse.
        :rtype: list[str]
        """
        return self._command_info_list

    @command_info_list.setter
    def command_info_list(self, command_info_list):
        r"""Sets the command_info_list of this ListInstanceProcessesResponse.

        命令列表

        :param command_info_list: The command_info_list of this ListInstanceProcessesResponse.
        :type command_info_list: list[str]
        """
        self._command_info_list = command_info_list

    def to_dict(self):
        import warnings
        warnings.warn("ListInstanceProcessesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInstanceProcessesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
