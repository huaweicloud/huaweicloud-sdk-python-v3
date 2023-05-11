# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppChangeResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'variation_type': 'str',
        'host_id': 'str',
        'app_name': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'version': 'str',
        'update_time': 'int',
        'recent_scan_time': 'int'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'variation_type': 'variation_type',
        'host_id': 'host_id',
        'app_name': 'app_name',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'version': 'version',
        'update_time': 'update_time',
        'recent_scan_time': 'recent_scan_time'
    }

    def __init__(self, agent_id=None, variation_type=None, host_id=None, app_name=None, host_name=None, host_ip=None, version=None, update_time=None, recent_scan_time=None):
        """AppChangeResponseInfo

        The model defined in huaweicloud sdk

        :param agent_id: agent_id
        :type agent_id: str
        :param variation_type: the type of change   - add ：新建   - delete ：删除   - modify ：修改
        :type variation_type: str
        :param host_id: host_id
        :type host_id: str
        :param app_name: 软件名称
        :type app_name: str
        :param host_name: 弹性服务器名称
        :type host_name: str
        :param host_ip: 服务器ip
        :type host_ip: str
        :param version: 版本号
        :type version: str
        :param update_time: 更新时间
        :type update_time: int
        :param recent_scan_time: 变更时间
        :type recent_scan_time: int
        """
        
        

        self._agent_id = None
        self._variation_type = None
        self._host_id = None
        self._app_name = None
        self._host_name = None
        self._host_ip = None
        self._version = None
        self._update_time = None
        self._recent_scan_time = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if variation_type is not None:
            self.variation_type = variation_type
        if host_id is not None:
            self.host_id = host_id
        if app_name is not None:
            self.app_name = app_name
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if version is not None:
            self.version = version
        if update_time is not None:
            self.update_time = update_time
        if recent_scan_time is not None:
            self.recent_scan_time = recent_scan_time

    @property
    def agent_id(self):
        """Gets the agent_id of this AppChangeResponseInfo.

        agent_id

        :return: The agent_id of this AppChangeResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AppChangeResponseInfo.

        agent_id

        :param agent_id: The agent_id of this AppChangeResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def variation_type(self):
        """Gets the variation_type of this AppChangeResponseInfo.

        the type of change   - add ：新建   - delete ：删除   - modify ：修改

        :return: The variation_type of this AppChangeResponseInfo.
        :rtype: str
        """
        return self._variation_type

    @variation_type.setter
    def variation_type(self, variation_type):
        """Sets the variation_type of this AppChangeResponseInfo.

        the type of change   - add ：新建   - delete ：删除   - modify ：修改

        :param variation_type: The variation_type of this AppChangeResponseInfo.
        :type variation_type: str
        """
        self._variation_type = variation_type

    @property
    def host_id(self):
        """Gets the host_id of this AppChangeResponseInfo.

        host_id

        :return: The host_id of this AppChangeResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this AppChangeResponseInfo.

        host_id

        :param host_id: The host_id of this AppChangeResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def app_name(self):
        """Gets the app_name of this AppChangeResponseInfo.

        软件名称

        :return: The app_name of this AppChangeResponseInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AppChangeResponseInfo.

        软件名称

        :param app_name: The app_name of this AppChangeResponseInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def host_name(self):
        """Gets the host_name of this AppChangeResponseInfo.

        弹性服务器名称

        :return: The host_name of this AppChangeResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this AppChangeResponseInfo.

        弹性服务器名称

        :param host_name: The host_name of this AppChangeResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this AppChangeResponseInfo.

        服务器ip

        :return: The host_ip of this AppChangeResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this AppChangeResponseInfo.

        服务器ip

        :param host_ip: The host_ip of this AppChangeResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def version(self):
        """Gets the version of this AppChangeResponseInfo.

        版本号

        :return: The version of this AppChangeResponseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AppChangeResponseInfo.

        版本号

        :param version: The version of this AppChangeResponseInfo.
        :type version: str
        """
        self._version = version

    @property
    def update_time(self):
        """Gets the update_time of this AppChangeResponseInfo.

        更新时间

        :return: The update_time of this AppChangeResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AppChangeResponseInfo.

        更新时间

        :param update_time: The update_time of this AppChangeResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def recent_scan_time(self):
        """Gets the recent_scan_time of this AppChangeResponseInfo.

        变更时间

        :return: The recent_scan_time of this AppChangeResponseInfo.
        :rtype: int
        """
        return self._recent_scan_time

    @recent_scan_time.setter
    def recent_scan_time(self, recent_scan_time):
        """Sets the recent_scan_time of this AppChangeResponseInfo.

        变更时间

        :param recent_scan_time: The recent_scan_time of this AppChangeResponseInfo.
        :type recent_scan_time: int
        """
        self._recent_scan_time = recent_scan_time

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
        if not isinstance(other, AppChangeResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
