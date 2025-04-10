# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_name': 'str',
        'env_id': 'int',
        'app_name': 'str',
        'app_id': 'int',
        'online_count': 'int',
        'disable_count': 'int',
        'offline_count': 'int'
    }

    attribute_map = {
        'env_name': 'env_name',
        'env_id': 'env_id',
        'app_name': 'app_name',
        'app_id': 'app_id',
        'online_count': 'online_count',
        'disable_count': 'disable_count',
        'offline_count': 'offline_count'
    }

    def __init__(self, env_name=None, env_id=None, app_name=None, app_id=None, online_count=None, disable_count=None, offline_count=None):
        r"""AppInfo

        The model defined in huaweicloud sdk

        :param env_name: 环境名称。
        :type env_name: str
        :param env_id: 环境id。
        :type env_id: int
        :param app_name: 组件名称。
        :type app_name: str
        :param app_id: 组件id。
        :type app_id: int
        :param online_count: 在线探针数。
        :type online_count: int
        :param disable_count: 手动停止探针数。
        :type disable_count: int
        :param offline_count: 离线探针数。
        :type offline_count: int
        """
        
        

        self._env_name = None
        self._env_id = None
        self._app_name = None
        self._app_id = None
        self._online_count = None
        self._disable_count = None
        self._offline_count = None
        self.discriminator = None

        if env_name is not None:
            self.env_name = env_name
        if env_id is not None:
            self.env_id = env_id
        if app_name is not None:
            self.app_name = app_name
        if app_id is not None:
            self.app_id = app_id
        if online_count is not None:
            self.online_count = online_count
        if disable_count is not None:
            self.disable_count = disable_count
        if offline_count is not None:
            self.offline_count = offline_count

    @property
    def env_name(self):
        r"""Gets the env_name of this AppInfo.

        环境名称。

        :return: The env_name of this AppInfo.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        r"""Sets the env_name of this AppInfo.

        环境名称。

        :param env_name: The env_name of this AppInfo.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def env_id(self):
        r"""Gets the env_id of this AppInfo.

        环境id。

        :return: The env_id of this AppInfo.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this AppInfo.

        环境id。

        :param env_id: The env_id of this AppInfo.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def app_name(self):
        r"""Gets the app_name of this AppInfo.

        组件名称。

        :return: The app_name of this AppInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this AppInfo.

        组件名称。

        :param app_name: The app_name of this AppInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_id(self):
        r"""Gets the app_id of this AppInfo.

        组件id。

        :return: The app_id of this AppInfo.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this AppInfo.

        组件id。

        :param app_id: The app_id of this AppInfo.
        :type app_id: int
        """
        self._app_id = app_id

    @property
    def online_count(self):
        r"""Gets the online_count of this AppInfo.

        在线探针数。

        :return: The online_count of this AppInfo.
        :rtype: int
        """
        return self._online_count

    @online_count.setter
    def online_count(self, online_count):
        r"""Sets the online_count of this AppInfo.

        在线探针数。

        :param online_count: The online_count of this AppInfo.
        :type online_count: int
        """
        self._online_count = online_count

    @property
    def disable_count(self):
        r"""Gets the disable_count of this AppInfo.

        手动停止探针数。

        :return: The disable_count of this AppInfo.
        :rtype: int
        """
        return self._disable_count

    @disable_count.setter
    def disable_count(self, disable_count):
        r"""Sets the disable_count of this AppInfo.

        手动停止探针数。

        :param disable_count: The disable_count of this AppInfo.
        :type disable_count: int
        """
        self._disable_count = disable_count

    @property
    def offline_count(self):
        r"""Gets the offline_count of this AppInfo.

        离线探针数。

        :return: The offline_count of this AppInfo.
        :rtype: int
        """
        return self._offline_count

    @offline_count.setter
    def offline_count(self, offline_count):
        r"""Sets the offline_count of this AppInfo.

        离线探针数。

        :param offline_count: The offline_count of this AppInfo.
        :type offline_count: int
        """
        self._offline_count = offline_count

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
        if not isinstance(other, AppInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
