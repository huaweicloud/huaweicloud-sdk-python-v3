# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWebAppAndServicesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'category': 'str',
        'catalogue': 'str',
        'host_name': 'str',
        'host_id': 'str',
        'host_ip': 'str',
        'version': 'str',
        'install_dir': 'str',
        'part_match': 'bool'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'category': 'category',
        'catalogue': 'catalogue',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'host_ip': 'host_ip',
        'version': 'version',
        'install_dir': 'install_dir',
        'part_match': 'part_match'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, name=None, category=None, catalogue=None, host_name=None, host_id=None, host_ip=None, version=None, install_dir=None, part_match=None):
        r"""ListWebAppAndServicesRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param name: WebAppAndService资产的名称
        :type name: str
        :param category: 返回的资产类别 - 0: 主机 - 1: 容器
        :type category: str
        :param catalogue: 资产类型 - web-app：web应用 - web-service：web服务 - database：数据库
        :type catalogue: str
        :param host_name: 服务器名称(可选)，可让用户根据主机名字搜索
        :type host_name: str
        :param host_id: 服务器id(可选)，可让用户根据主机id搜索
        :type host_id: str
        :param host_ip: 服务器ip(可选)，可让用户根据主机ip搜索
        :type host_ip: str
        :param version: WebAppAndService资产版本，可让用户根据版本搜索
        :type version: str
        :param install_dir: WebAppAndService资产安装目录，可让用户根据安装目录搜索
        :type install_dir: str
        :param part_match: 是否模糊匹配，默认false表示精确匹配
        :type part_match: bool
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._category = None
        self._catalogue = None
        self._host_name = None
        self._host_id = None
        self._host_ip = None
        self._version = None
        self._install_dir = None
        self._part_match = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.name = name
        self.category = category
        self.catalogue = catalogue
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if host_ip is not None:
            self.host_ip = host_ip
        if version is not None:
            self.version = version
        if install_dir is not None:
            self.install_dir = install_dir
        if part_match is not None:
            self.part_match = part_match

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWebAppAndServicesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListWebAppAndServicesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWebAppAndServicesRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListWebAppAndServicesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWebAppAndServicesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListWebAppAndServicesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWebAppAndServicesRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListWebAppAndServicesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWebAppAndServicesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListWebAppAndServicesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWebAppAndServicesRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListWebAppAndServicesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListWebAppAndServicesRequest.

        WebAppAndService资产的名称

        :return: The name of this ListWebAppAndServicesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListWebAppAndServicesRequest.

        WebAppAndService资产的名称

        :param name: The name of this ListWebAppAndServicesRequest.
        :type name: str
        """
        self._name = name

    @property
    def category(self):
        r"""Gets the category of this ListWebAppAndServicesRequest.

        返回的资产类别 - 0: 主机 - 1: 容器

        :return: The category of this ListWebAppAndServicesRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListWebAppAndServicesRequest.

        返回的资产类别 - 0: 主机 - 1: 容器

        :param category: The category of this ListWebAppAndServicesRequest.
        :type category: str
        """
        self._category = category

    @property
    def catalogue(self):
        r"""Gets the catalogue of this ListWebAppAndServicesRequest.

        资产类型 - web-app：web应用 - web-service：web服务 - database：数据库

        :return: The catalogue of this ListWebAppAndServicesRequest.
        :rtype: str
        """
        return self._catalogue

    @catalogue.setter
    def catalogue(self, catalogue):
        r"""Sets the catalogue of this ListWebAppAndServicesRequest.

        资产类型 - web-app：web应用 - web-service：web服务 - database：数据库

        :param catalogue: The catalogue of this ListWebAppAndServicesRequest.
        :type catalogue: str
        """
        self._catalogue = catalogue

    @property
    def host_name(self):
        r"""Gets the host_name of this ListWebAppAndServicesRequest.

        服务器名称(可选)，可让用户根据主机名字搜索

        :return: The host_name of this ListWebAppAndServicesRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListWebAppAndServicesRequest.

        服务器名称(可选)，可让用户根据主机名字搜索

        :param host_name: The host_name of this ListWebAppAndServicesRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        r"""Gets the host_id of this ListWebAppAndServicesRequest.

        服务器id(可选)，可让用户根据主机id搜索

        :return: The host_id of this ListWebAppAndServicesRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListWebAppAndServicesRequest.

        服务器id(可选)，可让用户根据主机id搜索

        :param host_id: The host_id of this ListWebAppAndServicesRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ListWebAppAndServicesRequest.

        服务器ip(可选)，可让用户根据主机ip搜索

        :return: The host_ip of this ListWebAppAndServicesRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ListWebAppAndServicesRequest.

        服务器ip(可选)，可让用户根据主机ip搜索

        :param host_ip: The host_ip of this ListWebAppAndServicesRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def version(self):
        r"""Gets the version of this ListWebAppAndServicesRequest.

        WebAppAndService资产版本，可让用户根据版本搜索

        :return: The version of this ListWebAppAndServicesRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListWebAppAndServicesRequest.

        WebAppAndService资产版本，可让用户根据版本搜索

        :param version: The version of this ListWebAppAndServicesRequest.
        :type version: str
        """
        self._version = version

    @property
    def install_dir(self):
        r"""Gets the install_dir of this ListWebAppAndServicesRequest.

        WebAppAndService资产安装目录，可让用户根据安装目录搜索

        :return: The install_dir of this ListWebAppAndServicesRequest.
        :rtype: str
        """
        return self._install_dir

    @install_dir.setter
    def install_dir(self, install_dir):
        r"""Sets the install_dir of this ListWebAppAndServicesRequest.

        WebAppAndService资产安装目录，可让用户根据安装目录搜索

        :param install_dir: The install_dir of this ListWebAppAndServicesRequest.
        :type install_dir: str
        """
        self._install_dir = install_dir

    @property
    def part_match(self):
        r"""Gets the part_match of this ListWebAppAndServicesRequest.

        是否模糊匹配，默认false表示精确匹配

        :return: The part_match of this ListWebAppAndServicesRequest.
        :rtype: bool
        """
        return self._part_match

    @part_match.setter
    def part_match(self, part_match):
        r"""Sets the part_match of this ListWebAppAndServicesRequest.

        是否模糊匹配，默认false表示精确匹配

        :param part_match: The part_match of this ListWebAppAndServicesRequest.
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
        if not isinstance(other, ListWebAppAndServicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
