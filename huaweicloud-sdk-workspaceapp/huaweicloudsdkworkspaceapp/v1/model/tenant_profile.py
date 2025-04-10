# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantProfile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'project_name': 'str',
        'tenant_domain_id': 'str',
        'service_status': 'str',
        'open_with_ad': 'bool',
        'tenant_domain_name': 'str',
        'create_time': 'datetime'
    }

    attribute_map = {
        'project_id': 'project_id',
        'project_name': 'project_name',
        'tenant_domain_id': 'tenant_domain_id',
        'service_status': 'service_status',
        'open_with_ad': 'open_with_ad',
        'tenant_domain_name': 'tenant_domain_name',
        'create_time': 'create_time'
    }

    def __init__(self, project_id=None, project_name=None, tenant_domain_id=None, service_status=None, open_with_ad=None, tenant_domain_name=None, create_time=None):
        r"""TenantProfile

        The model defined in huaweicloud sdk

        :param project_id: 租户ID 同tenant_id。
        :type project_id: str
        :param project_name: 租户名称。
        :type project_name: str
        :param tenant_domain_id: 租户的域ID。
        :type tenant_domain_id: str
        :param service_status: 服务状态 * &#x60;active&#x60; - 激活 * &#x60;inactive&#x60; - 未激活
        :type service_status: str
        :param open_with_ad: 是否对接AD。 有AD的情况下，提示租户单会话模式和多会话模式都支持; 在没有AD的情况下，提示租户仅支持VDI单会话模式。
        :type open_with_ad: bool
        :param tenant_domain_name: 租户的域名称。
        :type tenant_domain_name: str
        :param create_time: 租户信息创建时间。
        :type create_time: datetime
        """
        
        

        self._project_id = None
        self._project_name = None
        self._tenant_domain_id = None
        self._service_status = None
        self._open_with_ad = None
        self._tenant_domain_name = None
        self._create_time = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if tenant_domain_id is not None:
            self.tenant_domain_id = tenant_domain_id
        if service_status is not None:
            self.service_status = service_status
        if open_with_ad is not None:
            self.open_with_ad = open_with_ad
        if tenant_domain_name is not None:
            self.tenant_domain_name = tenant_domain_name
        if create_time is not None:
            self.create_time = create_time

    @property
    def project_id(self):
        r"""Gets the project_id of this TenantProfile.

        租户ID 同tenant_id。

        :return: The project_id of this TenantProfile.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TenantProfile.

        租户ID 同tenant_id。

        :param project_id: The project_id of this TenantProfile.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this TenantProfile.

        租户名称。

        :return: The project_name of this TenantProfile.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this TenantProfile.

        租户名称。

        :param project_name: The project_name of this TenantProfile.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def tenant_domain_id(self):
        r"""Gets the tenant_domain_id of this TenantProfile.

        租户的域ID。

        :return: The tenant_domain_id of this TenantProfile.
        :rtype: str
        """
        return self._tenant_domain_id

    @tenant_domain_id.setter
    def tenant_domain_id(self, tenant_domain_id):
        r"""Sets the tenant_domain_id of this TenantProfile.

        租户的域ID。

        :param tenant_domain_id: The tenant_domain_id of this TenantProfile.
        :type tenant_domain_id: str
        """
        self._tenant_domain_id = tenant_domain_id

    @property
    def service_status(self):
        r"""Gets the service_status of this TenantProfile.

        服务状态 * `active` - 激活 * `inactive` - 未激活

        :return: The service_status of this TenantProfile.
        :rtype: str
        """
        return self._service_status

    @service_status.setter
    def service_status(self, service_status):
        r"""Sets the service_status of this TenantProfile.

        服务状态 * `active` - 激活 * `inactive` - 未激活

        :param service_status: The service_status of this TenantProfile.
        :type service_status: str
        """
        self._service_status = service_status

    @property
    def open_with_ad(self):
        r"""Gets the open_with_ad of this TenantProfile.

        是否对接AD。 有AD的情况下，提示租户单会话模式和多会话模式都支持; 在没有AD的情况下，提示租户仅支持VDI单会话模式。

        :return: The open_with_ad of this TenantProfile.
        :rtype: bool
        """
        return self._open_with_ad

    @open_with_ad.setter
    def open_with_ad(self, open_with_ad):
        r"""Sets the open_with_ad of this TenantProfile.

        是否对接AD。 有AD的情况下，提示租户单会话模式和多会话模式都支持; 在没有AD的情况下，提示租户仅支持VDI单会话模式。

        :param open_with_ad: The open_with_ad of this TenantProfile.
        :type open_with_ad: bool
        """
        self._open_with_ad = open_with_ad

    @property
    def tenant_domain_name(self):
        r"""Gets the tenant_domain_name of this TenantProfile.

        租户的域名称。

        :return: The tenant_domain_name of this TenantProfile.
        :rtype: str
        """
        return self._tenant_domain_name

    @tenant_domain_name.setter
    def tenant_domain_name(self, tenant_domain_name):
        r"""Sets the tenant_domain_name of this TenantProfile.

        租户的域名称。

        :param tenant_domain_name: The tenant_domain_name of this TenantProfile.
        :type tenant_domain_name: str
        """
        self._tenant_domain_name = tenant_domain_name

    @property
    def create_time(self):
        r"""Gets the create_time of this TenantProfile.

        租户信息创建时间。

        :return: The create_time of this TenantProfile.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TenantProfile.

        租户信息创建时间。

        :param create_time: The create_time of this TenantProfile.
        :type create_time: datetime
        """
        self._create_time = create_time

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
        if not isinstance(other, TenantProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
