# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSessionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'user_name': 'str',
        'query_begin_time': 'str',
        'query_end_time': 'str',
        'app_server_group_id': 'str',
        'vm_ip': 'str',
        'machine_name': 'str',
        'session_state': 'str',
        'is_success': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'user_name': 'user_name',
        'query_begin_time': 'query_begin_time',
        'query_end_time': 'query_end_time',
        'app_server_group_id': 'app_server_group_id',
        'vm_ip': 'vm_ip',
        'machine_name': 'machine_name',
        'session_state': 'session_state',
        'is_success': 'is_success'
    }

    def __init__(self, limit=None, offset=None, user_name=None, query_begin_time=None, query_end_time=None, app_server_group_id=None, vm_ip=None, machine_name=None, session_state=None, is_success=None):
        """ListSessionsRequest

        The model defined in huaweicloud sdk

        :param limit: 单次查询的大小[1-100]。
        :type limit: int
        :param offset: 查询的偏移量。
        :type offset: int
        :param user_name: 用户名。
        :type user_name: str
        :param query_begin_time: 搜索开始时间，以会话开始时间为条件查询，格式2024-02-27T03:47:51.182Z。
        :type query_begin_time: str
        :param query_end_time: 搜索结束时间，以会话开始时间为条件查询，格式2024-02-27T03:47:51.182Z。
        :type query_end_time: str
        :param app_server_group_id: AppServer组ID。
        :type app_server_group_id: str
        :param vm_ip: 服务器IP。
        :type vm_ip: str
        :param machine_name: 应用服务器名称。
        :type machine_name: str
        :param session_state: 应用状态： * &#x60;Active&#x60; - 会话当前处于活动状态，有用户登录并且正在使用。 * &#x60;Disconnected&#x60; - 用户已经登录但会话处于断开连接状态。 * &#x60;AppcInit&#x60; - 会话正在初始化。 * &#x60;SignedOut&#x60; - 会话已注销。 * &#x60;InitFail&#x60; - 会话初始化失败。
        :type session_state: str
        :param is_success: 会话是否创建成功,默认不填则查询全部 * &#39;true&#39; - 会话创建成功 * &#39;false&#39; - 会话创建失败
        :type is_success: str
        """
        
        

        self._limit = None
        self._offset = None
        self._user_name = None
        self._query_begin_time = None
        self._query_end_time = None
        self._app_server_group_id = None
        self._vm_ip = None
        self._machine_name = None
        self._session_state = None
        self._is_success = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if user_name is not None:
            self.user_name = user_name
        self.query_begin_time = query_begin_time
        self.query_end_time = query_end_time
        if app_server_group_id is not None:
            self.app_server_group_id = app_server_group_id
        if vm_ip is not None:
            self.vm_ip = vm_ip
        if machine_name is not None:
            self.machine_name = machine_name
        if session_state is not None:
            self.session_state = session_state
        if is_success is not None:
            self.is_success = is_success

    @property
    def limit(self):
        """Gets the limit of this ListSessionsRequest.

        单次查询的大小[1-100]。

        :return: The limit of this ListSessionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSessionsRequest.

        单次查询的大小[1-100]。

        :param limit: The limit of this ListSessionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSessionsRequest.

        查询的偏移量。

        :return: The offset of this ListSessionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSessionsRequest.

        查询的偏移量。

        :param offset: The offset of this ListSessionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def user_name(self):
        """Gets the user_name of this ListSessionsRequest.

        用户名。

        :return: The user_name of this ListSessionsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListSessionsRequest.

        用户名。

        :param user_name: The user_name of this ListSessionsRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def query_begin_time(self):
        """Gets the query_begin_time of this ListSessionsRequest.

        搜索开始时间，以会话开始时间为条件查询，格式2024-02-27T03:47:51.182Z。

        :return: The query_begin_time of this ListSessionsRequest.
        :rtype: str
        """
        return self._query_begin_time

    @query_begin_time.setter
    def query_begin_time(self, query_begin_time):
        """Sets the query_begin_time of this ListSessionsRequest.

        搜索开始时间，以会话开始时间为条件查询，格式2024-02-27T03:47:51.182Z。

        :param query_begin_time: The query_begin_time of this ListSessionsRequest.
        :type query_begin_time: str
        """
        self._query_begin_time = query_begin_time

    @property
    def query_end_time(self):
        """Gets the query_end_time of this ListSessionsRequest.

        搜索结束时间，以会话开始时间为条件查询，格式2024-02-27T03:47:51.182Z。

        :return: The query_end_time of this ListSessionsRequest.
        :rtype: str
        """
        return self._query_end_time

    @query_end_time.setter
    def query_end_time(self, query_end_time):
        """Sets the query_end_time of this ListSessionsRequest.

        搜索结束时间，以会话开始时间为条件查询，格式2024-02-27T03:47:51.182Z。

        :param query_end_time: The query_end_time of this ListSessionsRequest.
        :type query_end_time: str
        """
        self._query_end_time = query_end_time

    @property
    def app_server_group_id(self):
        """Gets the app_server_group_id of this ListSessionsRequest.

        AppServer组ID。

        :return: The app_server_group_id of this ListSessionsRequest.
        :rtype: str
        """
        return self._app_server_group_id

    @app_server_group_id.setter
    def app_server_group_id(self, app_server_group_id):
        """Sets the app_server_group_id of this ListSessionsRequest.

        AppServer组ID。

        :param app_server_group_id: The app_server_group_id of this ListSessionsRequest.
        :type app_server_group_id: str
        """
        self._app_server_group_id = app_server_group_id

    @property
    def vm_ip(self):
        """Gets the vm_ip of this ListSessionsRequest.

        服务器IP。

        :return: The vm_ip of this ListSessionsRequest.
        :rtype: str
        """
        return self._vm_ip

    @vm_ip.setter
    def vm_ip(self, vm_ip):
        """Sets the vm_ip of this ListSessionsRequest.

        服务器IP。

        :param vm_ip: The vm_ip of this ListSessionsRequest.
        :type vm_ip: str
        """
        self._vm_ip = vm_ip

    @property
    def machine_name(self):
        """Gets the machine_name of this ListSessionsRequest.

        应用服务器名称。

        :return: The machine_name of this ListSessionsRequest.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this ListSessionsRequest.

        应用服务器名称。

        :param machine_name: The machine_name of this ListSessionsRequest.
        :type machine_name: str
        """
        self._machine_name = machine_name

    @property
    def session_state(self):
        """Gets the session_state of this ListSessionsRequest.

        应用状态： * `Active` - 会话当前处于活动状态，有用户登录并且正在使用。 * `Disconnected` - 用户已经登录但会话处于断开连接状态。 * `AppcInit` - 会话正在初始化。 * `SignedOut` - 会话已注销。 * `InitFail` - 会话初始化失败。

        :return: The session_state of this ListSessionsRequest.
        :rtype: str
        """
        return self._session_state

    @session_state.setter
    def session_state(self, session_state):
        """Sets the session_state of this ListSessionsRequest.

        应用状态： * `Active` - 会话当前处于活动状态，有用户登录并且正在使用。 * `Disconnected` - 用户已经登录但会话处于断开连接状态。 * `AppcInit` - 会话正在初始化。 * `SignedOut` - 会话已注销。 * `InitFail` - 会话初始化失败。

        :param session_state: The session_state of this ListSessionsRequest.
        :type session_state: str
        """
        self._session_state = session_state

    @property
    def is_success(self):
        """Gets the is_success of this ListSessionsRequest.

        会话是否创建成功,默认不填则查询全部 * 'true' - 会话创建成功 * 'false' - 会话创建失败

        :return: The is_success of this ListSessionsRequest.
        :rtype: str
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListSessionsRequest.

        会话是否创建成功,默认不填则查询全部 * 'true' - 会话创建成功 * 'false' - 会话创建失败

        :param is_success: The is_success of this ListSessionsRequest.
        :type is_success: str
        """
        self._is_success = is_success

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
        if not isinstance(other, ListSessionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
