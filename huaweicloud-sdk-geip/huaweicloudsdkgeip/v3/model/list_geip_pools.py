# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGeipPools:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'en_name': 'str',
        'cn_name': 'str',
        'status': 'str',
        'isp': 'str',
        'ip_version': 'int',
        'access_site': 'str',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'allowed_bandwidth_types': 'list[AllowedBandwidthTypes]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'en_name': 'en_name',
        'cn_name': 'cn_name',
        'status': 'status',
        'isp': 'isp',
        'ip_version': 'ip_version',
        'access_site': 'access_site',
        'type': 'type',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'allowed_bandwidth_types': 'allowed_bandwidth_types'
    }

    def __init__(self, id=None, name=None, en_name=None, cn_name=None, status=None, isp=None, ip_version=None, access_site=None, type=None, created_at=None, updated_at=None, allowed_bandwidth_types=None):
        """ListGeipPools

        The model defined in huaweicloud sdk

        :param id: 全域弹性公网IP池的ID
        :type id: str
        :param name: - 功能说明：全域弹性公网IP池名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param en_name: 英文名称
        :type en_name: str
        :param cn_name: 中文名称
        :type cn_name: str
        :param status: 状态
        :type status: str
        :param isp: 全域弹性公网IP所属线路
        :type isp: str
        :param ip_version: - 功能说明：全域弹性公网IP池的版本 - 取值范围：4、6
        :type ip_version: int
        :param access_site: 接入点信息
        :type access_site: str
        :param type: 类型
        :type type: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param allowed_bandwidth_types: 地址池支持的全域公网带宽类型资源
        :type allowed_bandwidth_types: list[:class:`huaweicloudsdkgeip.v3.AllowedBandwidthTypes`]
        """
        
        

        self._id = None
        self._name = None
        self._en_name = None
        self._cn_name = None
        self._status = None
        self._isp = None
        self._ip_version = None
        self._access_site = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._allowed_bandwidth_types = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if en_name is not None:
            self.en_name = en_name
        if cn_name is not None:
            self.cn_name = cn_name
        if status is not None:
            self.status = status
        if isp is not None:
            self.isp = isp
        if ip_version is not None:
            self.ip_version = ip_version
        if access_site is not None:
            self.access_site = access_site
        if type is not None:
            self.type = type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if allowed_bandwidth_types is not None:
            self.allowed_bandwidth_types = allowed_bandwidth_types

    @property
    def id(self):
        """Gets the id of this ListGeipPools.

        全域弹性公网IP池的ID

        :return: The id of this ListGeipPools.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListGeipPools.

        全域弹性公网IP池的ID

        :param id: The id of this ListGeipPools.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListGeipPools.

        - 功能说明：全域弹性公网IP池名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this ListGeipPools.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListGeipPools.

        - 功能说明：全域弹性公网IP池名称 - 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this ListGeipPools.
        :type name: str
        """
        self._name = name

    @property
    def en_name(self):
        """Gets the en_name of this ListGeipPools.

        英文名称

        :return: The en_name of this ListGeipPools.
        :rtype: str
        """
        return self._en_name

    @en_name.setter
    def en_name(self, en_name):
        """Sets the en_name of this ListGeipPools.

        英文名称

        :param en_name: The en_name of this ListGeipPools.
        :type en_name: str
        """
        self._en_name = en_name

    @property
    def cn_name(self):
        """Gets the cn_name of this ListGeipPools.

        中文名称

        :return: The cn_name of this ListGeipPools.
        :rtype: str
        """
        return self._cn_name

    @cn_name.setter
    def cn_name(self, cn_name):
        """Sets the cn_name of this ListGeipPools.

        中文名称

        :param cn_name: The cn_name of this ListGeipPools.
        :type cn_name: str
        """
        self._cn_name = cn_name

    @property
    def status(self):
        """Gets the status of this ListGeipPools.

        状态

        :return: The status of this ListGeipPools.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListGeipPools.

        状态

        :param status: The status of this ListGeipPools.
        :type status: str
        """
        self._status = status

    @property
    def isp(self):
        """Gets the isp of this ListGeipPools.

        全域弹性公网IP所属线路

        :return: The isp of this ListGeipPools.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListGeipPools.

        全域弹性公网IP所属线路

        :param isp: The isp of this ListGeipPools.
        :type isp: str
        """
        self._isp = isp

    @property
    def ip_version(self):
        """Gets the ip_version of this ListGeipPools.

        - 功能说明：全域弹性公网IP池的版本 - 取值范围：4、6

        :return: The ip_version of this ListGeipPools.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListGeipPools.

        - 功能说明：全域弹性公网IP池的版本 - 取值范围：4、6

        :param ip_version: The ip_version of this ListGeipPools.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def access_site(self):
        """Gets the access_site of this ListGeipPools.

        接入点信息

        :return: The access_site of this ListGeipPools.
        :rtype: str
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        """Sets the access_site of this ListGeipPools.

        接入点信息

        :param access_site: The access_site of this ListGeipPools.
        :type access_site: str
        """
        self._access_site = access_site

    @property
    def type(self):
        """Gets the type of this ListGeipPools.

        类型

        :return: The type of this ListGeipPools.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListGeipPools.

        类型

        :param type: The type of this ListGeipPools.
        :type type: str
        """
        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this ListGeipPools.

        创建时间

        :return: The created_at of this ListGeipPools.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListGeipPools.

        创建时间

        :param created_at: The created_at of this ListGeipPools.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ListGeipPools.

        更新时间

        :return: The updated_at of this ListGeipPools.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListGeipPools.

        更新时间

        :param updated_at: The updated_at of this ListGeipPools.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def allowed_bandwidth_types(self):
        """Gets the allowed_bandwidth_types of this ListGeipPools.

        地址池支持的全域公网带宽类型资源

        :return: The allowed_bandwidth_types of this ListGeipPools.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.AllowedBandwidthTypes`]
        """
        return self._allowed_bandwidth_types

    @allowed_bandwidth_types.setter
    def allowed_bandwidth_types(self, allowed_bandwidth_types):
        """Sets the allowed_bandwidth_types of this ListGeipPools.

        地址池支持的全域公网带宽类型资源

        :param allowed_bandwidth_types: The allowed_bandwidth_types of this ListGeipPools.
        :type allowed_bandwidth_types: list[:class:`huaweicloudsdkgeip.v3.AllowedBandwidthTypes`]
        """
        self._allowed_bandwidth_types = allowed_bandwidth_types

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
        if not isinstance(other, ListGeipPools):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
