# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterSecurityCheckAppInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'app_version': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'update_time': 'int',
        'recent_scan_time': 'int'
    }

    attribute_map = {
        'app_name': 'app_name',
        'app_version': 'app_version',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'update_time': 'update_time',
        'recent_scan_time': 'recent_scan_time'
    }

    def __init__(self, app_name=None, app_version=None, container_id=None, container_name=None, host_name=None, private_ip=None, public_ip=None, update_time=None, recent_scan_time=None):
        r"""ClusterSecurityCheckAppInfo

        The model defined in huaweicloud sdk

        :param app_name: **参数解释**： 软件名称 **取值范围**： 不涉及 
        :type app_name: str
        :param app_version: **参数解释**： 软件版本 **取值范围**： 不涉及 
        :type app_version: str
        :param container_id: **参数解释**： 容器ID **取值范围**： 不涉及 
        :type container_id: str
        :param container_name: **参数解释**： 容器名称 **取值范围**： 不涉及 
        :type container_name: str
        :param host_name: **参数解释**： 节点名称 **取值范围**： 不涉及 
        :type host_name: str
        :param private_ip: **参数解释**： 私有IP地址 **取值范围**： 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**： 公有IP地址 **取值范围**： 不涉及 
        :type public_ip: str
        :param update_time: **参数解释**： 更新时间 **取值范围**： 不涉及 
        :type update_time: int
        :param recent_scan_time: **参数解释**： 最近扫描时间 **取值范围**： 不涉及 
        :type recent_scan_time: int
        """
        
        

        self._app_name = None
        self._app_version = None
        self._container_id = None
        self._container_name = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._update_time = None
        self._recent_scan_time = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        if app_version is not None:
            self.app_version = app_version
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if update_time is not None:
            self.update_time = update_time
        if recent_scan_time is not None:
            self.recent_scan_time = recent_scan_time

    @property
    def app_name(self):
        r"""Gets the app_name of this ClusterSecurityCheckAppInfo.

        **参数解释**： 软件名称 **取值范围**： 不涉及 

        :return: The app_name of this ClusterSecurityCheckAppInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ClusterSecurityCheckAppInfo.

        **参数解释**： 软件名称 **取值范围**： 不涉及 

        :param app_name: The app_name of this ClusterSecurityCheckAppInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_version(self):
        r"""Gets the app_version of this ClusterSecurityCheckAppInfo.

        **参数解释**： 软件版本 **取值范围**： 不涉及 

        :return: The app_version of this ClusterSecurityCheckAppInfo.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this ClusterSecurityCheckAppInfo.

        **参数解释**： 软件版本 **取值范围**： 不涉及 

        :param app_version: The app_version of this ClusterSecurityCheckAppInfo.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def container_id(self):
        r"""Gets the container_id of this ClusterSecurityCheckAppInfo.

        **参数解释**： 容器ID **取值范围**： 不涉及 

        :return: The container_id of this ClusterSecurityCheckAppInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ClusterSecurityCheckAppInfo.

        **参数解释**： 容器ID **取值范围**： 不涉及 

        :param container_id: The container_id of this ClusterSecurityCheckAppInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this ClusterSecurityCheckAppInfo.

        **参数解释**： 容器名称 **取值范围**： 不涉及 

        :return: The container_name of this ClusterSecurityCheckAppInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ClusterSecurityCheckAppInfo.

        **参数解释**： 容器名称 **取值范围**： 不涉及 

        :param container_name: The container_name of this ClusterSecurityCheckAppInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ClusterSecurityCheckAppInfo.

        **参数解释**： 节点名称 **取值范围**： 不涉及 

        :return: The host_name of this ClusterSecurityCheckAppInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ClusterSecurityCheckAppInfo.

        **参数解释**： 节点名称 **取值范围**： 不涉及 

        :param host_name: The host_name of this ClusterSecurityCheckAppInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ClusterSecurityCheckAppInfo.

        **参数解释**： 私有IP地址 **取值范围**： 不涉及 

        :return: The private_ip of this ClusterSecurityCheckAppInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ClusterSecurityCheckAppInfo.

        **参数解释**： 私有IP地址 **取值范围**： 不涉及 

        :param private_ip: The private_ip of this ClusterSecurityCheckAppInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ClusterSecurityCheckAppInfo.

        **参数解释**： 公有IP地址 **取值范围**： 不涉及 

        :return: The public_ip of this ClusterSecurityCheckAppInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ClusterSecurityCheckAppInfo.

        **参数解释**： 公有IP地址 **取值范围**： 不涉及 

        :param public_ip: The public_ip of this ClusterSecurityCheckAppInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def update_time(self):
        r"""Gets the update_time of this ClusterSecurityCheckAppInfo.

        **参数解释**： 更新时间 **取值范围**： 不涉及 

        :return: The update_time of this ClusterSecurityCheckAppInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ClusterSecurityCheckAppInfo.

        **参数解释**： 更新时间 **取值范围**： 不涉及 

        :param update_time: The update_time of this ClusterSecurityCheckAppInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def recent_scan_time(self):
        r"""Gets the recent_scan_time of this ClusterSecurityCheckAppInfo.

        **参数解释**： 最近扫描时间 **取值范围**： 不涉及 

        :return: The recent_scan_time of this ClusterSecurityCheckAppInfo.
        :rtype: int
        """
        return self._recent_scan_time

    @recent_scan_time.setter
    def recent_scan_time(self, recent_scan_time):
        r"""Sets the recent_scan_time of this ClusterSecurityCheckAppInfo.

        **参数解释**： 最近扫描时间 **取值范围**： 不涉及 

        :param recent_scan_time: The recent_scan_time of this ClusterSecurityCheckAppInfo.
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
        if not isinstance(other, ClusterSecurityCheckAppInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
