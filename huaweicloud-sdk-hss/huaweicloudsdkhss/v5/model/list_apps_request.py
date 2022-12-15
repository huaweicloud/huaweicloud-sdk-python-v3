# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'app_name': 'str',
        'host_ip': 'str',
        'version': 'str',
        'install_dir': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'app_name': 'app_name',
        'host_ip': 'host_ip',
        'version': 'version',
        'install_dir': 'install_dir',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, host_id=None, host_name=None, app_name=None, host_ip=None, version=None, install_dir=None, enterprise_project_id=None, limit=None, offset=None):
        """ListAppsRequest

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param app_name: 软件名称
        :type app_name: str
        :param host_ip: 主机ip
        :type host_ip: str
        :param version: 版本号
        :type version: str
        :param install_dir: 安装目录
        :type install_dir: str
        :param enterprise_project_id: 企业项目
        :type enterprise_project_id: str
        :param limit: 默认10
        :type limit: int
        :param offset: 默认是0
        :type offset: int
        """
        
        

        self._host_id = None
        self._host_name = None
        self._app_name = None
        self._host_ip = None
        self._version = None
        self._install_dir = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if app_name is not None:
            self.app_name = app_name
        if host_ip is not None:
            self.host_ip = host_ip
        if version is not None:
            self.version = version
        if install_dir is not None:
            self.install_dir = install_dir
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def host_id(self):
        """Gets the host_id of this ListAppsRequest.

        主机id

        :return: The host_id of this ListAppsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListAppsRequest.

        主机id

        :param host_id: The host_id of this ListAppsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this ListAppsRequest.

        主机名称

        :return: The host_name of this ListAppsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListAppsRequest.

        主机名称

        :param host_name: The host_name of this ListAppsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def app_name(self):
        """Gets the app_name of this ListAppsRequest.

        软件名称

        :return: The app_name of this ListAppsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListAppsRequest.

        软件名称

        :param app_name: The app_name of this ListAppsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def host_ip(self):
        """Gets the host_ip of this ListAppsRequest.

        主机ip

        :return: The host_ip of this ListAppsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this ListAppsRequest.

        主机ip

        :param host_ip: The host_ip of this ListAppsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def version(self):
        """Gets the version of this ListAppsRequest.

        版本号

        :return: The version of this ListAppsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListAppsRequest.

        版本号

        :param version: The version of this ListAppsRequest.
        :type version: str
        """
        self._version = version

    @property
    def install_dir(self):
        """Gets the install_dir of this ListAppsRequest.

        安装目录

        :return: The install_dir of this ListAppsRequest.
        :rtype: str
        """
        return self._install_dir

    @install_dir.setter
    def install_dir(self, install_dir):
        """Sets the install_dir of this ListAppsRequest.

        安装目录

        :param install_dir: The install_dir of this ListAppsRequest.
        :type install_dir: str
        """
        self._install_dir = install_dir

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAppsRequest.

        企业项目

        :return: The enterprise_project_id of this ListAppsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAppsRequest.

        企业项目

        :param enterprise_project_id: The enterprise_project_id of this ListAppsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListAppsRequest.

        默认10

        :return: The limit of this ListAppsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppsRequest.

        默认10

        :param limit: The limit of this ListAppsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAppsRequest.

        默认是0

        :return: The offset of this ListAppsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppsRequest.

        默认是0

        :param offset: The offset of this ListAppsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListAppsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
