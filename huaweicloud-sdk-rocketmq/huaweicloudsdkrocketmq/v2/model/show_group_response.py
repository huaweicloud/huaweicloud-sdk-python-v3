# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'broadcast': 'bool',
        'brokers': 'list[str]',
        'name': 'str',
        'group_desc': 'str',
        'retry_max_time': 'int',
        'app_id': 'str',
        'app_name': 'str',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'broadcast': 'broadcast',
        'brokers': 'brokers',
        'name': 'name',
        'group_desc': 'group_desc',
        'retry_max_time': 'retry_max_time',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'permissions': 'permissions'
    }

    def __init__(self, enabled=None, broadcast=None, brokers=None, name=None, group_desc=None, retry_max_time=None, app_id=None, app_name=None, permissions=None):
        r"""ShowGroupResponse

        The model defined in huaweicloud sdk

        :param enabled: 是否可以消费。
        :type enabled: bool
        :param broadcast: 是否广播。
        :type broadcast: bool
        :param brokers: 关联的代理列表。
        :type brokers: list[str]
        :param name: 消费组名称。
        :type name: str
        :param group_desc: 消费组描述。
        :type group_desc: str
        :param retry_max_time: 最大重试次数。
        :type retry_max_time: int
        :param app_id: 应用ID。
        :type app_id: str
        :param app_name: 应用名称。
        :type app_name: str
        :param permissions: 权限。
        :type permissions: list[str]
        """
        
        super(ShowGroupResponse, self).__init__()

        self._enabled = None
        self._broadcast = None
        self._brokers = None
        self._name = None
        self._group_desc = None
        self._retry_max_time = None
        self._app_id = None
        self._app_name = None
        self._permissions = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if broadcast is not None:
            self.broadcast = broadcast
        if brokers is not None:
            self.brokers = brokers
        if name is not None:
            self.name = name
        if group_desc is not None:
            self.group_desc = group_desc
        if retry_max_time is not None:
            self.retry_max_time = retry_max_time
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if permissions is not None:
            self.permissions = permissions

    @property
    def enabled(self):
        r"""Gets the enabled of this ShowGroupResponse.

        是否可以消费。

        :return: The enabled of this ShowGroupResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ShowGroupResponse.

        是否可以消费。

        :param enabled: The enabled of this ShowGroupResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def broadcast(self):
        r"""Gets the broadcast of this ShowGroupResponse.

        是否广播。

        :return: The broadcast of this ShowGroupResponse.
        :rtype: bool
        """
        return self._broadcast

    @broadcast.setter
    def broadcast(self, broadcast):
        r"""Sets the broadcast of this ShowGroupResponse.

        是否广播。

        :param broadcast: The broadcast of this ShowGroupResponse.
        :type broadcast: bool
        """
        self._broadcast = broadcast

    @property
    def brokers(self):
        r"""Gets the brokers of this ShowGroupResponse.

        关联的代理列表。

        :return: The brokers of this ShowGroupResponse.
        :rtype: list[str]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        r"""Sets the brokers of this ShowGroupResponse.

        关联的代理列表。

        :param brokers: The brokers of this ShowGroupResponse.
        :type brokers: list[str]
        """
        self._brokers = brokers

    @property
    def name(self):
        r"""Gets the name of this ShowGroupResponse.

        消费组名称。

        :return: The name of this ShowGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowGroupResponse.

        消费组名称。

        :param name: The name of this ShowGroupResponse.
        :type name: str
        """
        self._name = name

    @property
    def group_desc(self):
        r"""Gets the group_desc of this ShowGroupResponse.

        消费组描述。

        :return: The group_desc of this ShowGroupResponse.
        :rtype: str
        """
        return self._group_desc

    @group_desc.setter
    def group_desc(self, group_desc):
        r"""Sets the group_desc of this ShowGroupResponse.

        消费组描述。

        :param group_desc: The group_desc of this ShowGroupResponse.
        :type group_desc: str
        """
        self._group_desc = group_desc

    @property
    def retry_max_time(self):
        r"""Gets the retry_max_time of this ShowGroupResponse.

        最大重试次数。

        :return: The retry_max_time of this ShowGroupResponse.
        :rtype: int
        """
        return self._retry_max_time

    @retry_max_time.setter
    def retry_max_time(self, retry_max_time):
        r"""Sets the retry_max_time of this ShowGroupResponse.

        最大重试次数。

        :param retry_max_time: The retry_max_time of this ShowGroupResponse.
        :type retry_max_time: int
        """
        self._retry_max_time = retry_max_time

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowGroupResponse.

        应用ID。

        :return: The app_id of this ShowGroupResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowGroupResponse.

        应用ID。

        :param app_id: The app_id of this ShowGroupResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this ShowGroupResponse.

        应用名称。

        :return: The app_name of this ShowGroupResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ShowGroupResponse.

        应用名称。

        :param app_name: The app_name of this ShowGroupResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def permissions(self):
        r"""Gets the permissions of this ShowGroupResponse.

        权限。

        :return: The permissions of this ShowGroupResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this ShowGroupResponse.

        权限。

        :param permissions: The permissions of this ShowGroupResponse.
        :type permissions: list[str]
        """
        self._permissions = permissions

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
        if not isinstance(other, ShowGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
