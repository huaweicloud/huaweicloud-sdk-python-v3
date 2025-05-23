# coding: utf-8

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
        'offset': 'int',
        'category': 'str',
        'part_match': 'bool'
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
        'offset': 'offset',
        'category': 'category',
        'part_match': 'part_match'
    }

    def __init__(self, host_id=None, host_name=None, app_name=None, host_ip=None, version=None, install_dir=None, enterprise_project_id=None, limit=None, offset=None, category=None, part_match=None):
        r"""ListAppsRequest

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param app_name: 软件名称
        :type app_name: str
        :param host_ip: 主机ip
        :type host_ip: str
        :param version: 软件版本号
        :type version: str
        :param install_dir: 安装目录
        :type install_dir: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param limit: 每页显示数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param category: 类别，默认为host，包含如下： - host：主机 - container：容器
        :type category: str
        :param part_match: 是否模糊匹配，默认false表示精确匹配
        :type part_match: bool
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
        self._category = None
        self._part_match = None
        self.discriminator = None

        if host_id is not None:
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
        if category is not None:
            self.category = category
        if part_match is not None:
            self.part_match = part_match

    @property
    def host_id(self):
        r"""Gets the host_id of this ListAppsRequest.

        主机id

        :return: The host_id of this ListAppsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListAppsRequest.

        主机id

        :param host_id: The host_id of this ListAppsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListAppsRequest.

        主机名称

        :return: The host_name of this ListAppsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListAppsRequest.

        主机名称

        :param host_name: The host_name of this ListAppsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def app_name(self):
        r"""Gets the app_name of this ListAppsRequest.

        软件名称

        :return: The app_name of this ListAppsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListAppsRequest.

        软件名称

        :param app_name: The app_name of this ListAppsRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListAppsRequest.

        主机ip

        :return: The host_ip of this ListAppsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListAppsRequest.

        主机ip

        :param host_ip: The host_ip of this ListAppsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def version(self):
        r"""Gets the version of this ListAppsRequest.

        软件版本号

        :return: The version of this ListAppsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListAppsRequest.

        软件版本号

        :param version: The version of this ListAppsRequest.
        :type version: str
        """
        self._version = version

    @property
    def install_dir(self):
        r"""Gets the install_dir of this ListAppsRequest.

        安装目录

        :return: The install_dir of this ListAppsRequest.
        :rtype: str
        """
        return self._install_dir

    @install_dir.setter
    def install_dir(self, install_dir):
        r"""Sets the install_dir of this ListAppsRequest.

        安装目录

        :param install_dir: The install_dir of this ListAppsRequest.
        :type install_dir: str
        """
        self._install_dir = install_dir

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAppsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListAppsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAppsRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListAppsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAppsRequest.

        每页显示数量

        :return: The limit of this ListAppsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAppsRequest.

        每页显示数量

        :param limit: The limit of this ListAppsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAppsRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListAppsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAppsRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListAppsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def category(self):
        r"""Gets the category of this ListAppsRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :return: The category of this ListAppsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListAppsRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :param category: The category of this ListAppsRequest.
        :type category: str
        """
        self._category = category

    @property
    def part_match(self):
        r"""Gets the part_match of this ListAppsRequest.

        是否模糊匹配，默认false表示精确匹配

        :return: The part_match of this ListAppsRequest.
        :rtype: bool
        """
        return self._part_match

    @part_match.setter
    def part_match(self, part_match):
        r"""Sets the part_match of this ListAppsRequest.

        是否模糊匹配，默认false表示精确匹配

        :param part_match: The part_match of this ListAppsRequest.
        :type part_match: bool
        """
        self._part_match = part_match

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
