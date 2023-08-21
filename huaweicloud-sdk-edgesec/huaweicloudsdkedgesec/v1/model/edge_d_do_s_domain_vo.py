# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeDDoSDomainVo:

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
        'domain_name': 'str',
        'tenant_id': 'str',
        'area_type': 'str',
        'dispatch_status': 'int',
        'protected_switch': 'int',
        'open_date': 'int',
        'close_date': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain_name': 'domain_name',
        'tenant_id': 'tenant_id',
        'area_type': 'area_type',
        'dispatch_status': 'dispatch_status',
        'protected_switch': 'protected_switch',
        'open_date': 'open_date',
        'close_date': 'close_date',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, domain_name=None, tenant_id=None, area_type=None, dispatch_status=None, protected_switch=None, open_date=None, close_date=None, enterprise_project_id=None):
        """EdgeDDoSDomainVo

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param domain_name: 域名
        :type domain_name: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param area_type: 域名在CDN所属区域
        :type area_type: str
        :param dispatch_status: cdn域名调度情况（0：未防护，1：配置中，2：已防护，3：删除中）
        :type dispatch_status: int
        :param protected_switch: 防护开关（0:关，1:开）
        :type protected_switch: int
        :param open_date: 开启时间
        :type open_date: int
        :param close_date: 关闭时间
        :type close_date: int
        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._domain_name = None
        self._tenant_id = None
        self._area_type = None
        self._dispatch_status = None
        self._protected_switch = None
        self._open_date = None
        self._close_date = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_name is not None:
            self.domain_name = domain_name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if area_type is not None:
            self.area_type = area_type
        if dispatch_status is not None:
            self.dispatch_status = dispatch_status
        if protected_switch is not None:
            self.protected_switch = protected_switch
        if open_date is not None:
            self.open_date = open_date
        if close_date is not None:
            self.close_date = close_date
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this EdgeDDoSDomainVo.

        域名id

        :return: The id of this EdgeDDoSDomainVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdgeDDoSDomainVo.

        域名id

        :param id: The id of this EdgeDDoSDomainVo.
        :type id: str
        """
        self._id = id

    @property
    def domain_name(self):
        """Gets the domain_name of this EdgeDDoSDomainVo.

        域名

        :return: The domain_name of this EdgeDDoSDomainVo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this EdgeDDoSDomainVo.

        域名

        :param domain_name: The domain_name of this EdgeDDoSDomainVo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this EdgeDDoSDomainVo.

        租户ID

        :return: The tenant_id of this EdgeDDoSDomainVo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this EdgeDDoSDomainVo.

        租户ID

        :param tenant_id: The tenant_id of this EdgeDDoSDomainVo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def area_type(self):
        """Gets the area_type of this EdgeDDoSDomainVo.

        域名在CDN所属区域

        :return: The area_type of this EdgeDDoSDomainVo.
        :rtype: str
        """
        return self._area_type

    @area_type.setter
    def area_type(self, area_type):
        """Sets the area_type of this EdgeDDoSDomainVo.

        域名在CDN所属区域

        :param area_type: The area_type of this EdgeDDoSDomainVo.
        :type area_type: str
        """
        self._area_type = area_type

    @property
    def dispatch_status(self):
        """Gets the dispatch_status of this EdgeDDoSDomainVo.

        cdn域名调度情况（0：未防护，1：配置中，2：已防护，3：删除中）

        :return: The dispatch_status of this EdgeDDoSDomainVo.
        :rtype: int
        """
        return self._dispatch_status

    @dispatch_status.setter
    def dispatch_status(self, dispatch_status):
        """Sets the dispatch_status of this EdgeDDoSDomainVo.

        cdn域名调度情况（0：未防护，1：配置中，2：已防护，3：删除中）

        :param dispatch_status: The dispatch_status of this EdgeDDoSDomainVo.
        :type dispatch_status: int
        """
        self._dispatch_status = dispatch_status

    @property
    def protected_switch(self):
        """Gets the protected_switch of this EdgeDDoSDomainVo.

        防护开关（0:关，1:开）

        :return: The protected_switch of this EdgeDDoSDomainVo.
        :rtype: int
        """
        return self._protected_switch

    @protected_switch.setter
    def protected_switch(self, protected_switch):
        """Sets the protected_switch of this EdgeDDoSDomainVo.

        防护开关（0:关，1:开）

        :param protected_switch: The protected_switch of this EdgeDDoSDomainVo.
        :type protected_switch: int
        """
        self._protected_switch = protected_switch

    @property
    def open_date(self):
        """Gets the open_date of this EdgeDDoSDomainVo.

        开启时间

        :return: The open_date of this EdgeDDoSDomainVo.
        :rtype: int
        """
        return self._open_date

    @open_date.setter
    def open_date(self, open_date):
        """Sets the open_date of this EdgeDDoSDomainVo.

        开启时间

        :param open_date: The open_date of this EdgeDDoSDomainVo.
        :type open_date: int
        """
        self._open_date = open_date

    @property
    def close_date(self):
        """Gets the close_date of this EdgeDDoSDomainVo.

        关闭时间

        :return: The close_date of this EdgeDDoSDomainVo.
        :rtype: int
        """
        return self._close_date

    @close_date.setter
    def close_date(self, close_date):
        """Sets the close_date of this EdgeDDoSDomainVo.

        关闭时间

        :param close_date: The close_date of this EdgeDDoSDomainVo.
        :type close_date: int
        """
        self._close_date = close_date

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this EdgeDDoSDomainVo.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this EdgeDDoSDomainVo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this EdgeDDoSDomainVo.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this EdgeDDoSDomainVo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, EdgeDDoSDomainVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
