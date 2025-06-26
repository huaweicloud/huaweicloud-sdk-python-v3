# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainNameInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'instance_id': 'str',
        'type': 'str',
        'domain_name': 'str',
        'certificate_id': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'type': 'type',
        'domain_name': 'domain_name',
        'certificate_id': 'certificate_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, uid=None, domain_id=None, project_id=None, instance_id=None, type=None, domain_name=None, certificate_id=None, created_at=None, updated_at=None):
        r"""DomainNameInfo

        The model defined in huaweicloud sdk

        :param uid: 域名ID
        :type uid: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param type: 域名类型(default/custom)
        :type type: str
        :param domain_name: 域名，只能由字母、数字、中划线、星号组成， 星号只能在开头，中划线不能在开头或末 尾，至少包含两个字符串，单个字符串不 超过63个字符，字符串间以点分割，且总 长度不超过100个字符。例如： example.com 或 *example.com。
        :type domain_name: str
        :param certificate_id: SCM服务的证书ID
        :type certificate_id: str
        :param created_at: 增加域名的时间
        :type created_at: str
        :param updated_at: 更新域名的时间
        :type updated_at: str
        """
        
        

        self._uid = None
        self._domain_id = None
        self._project_id = None
        self._instance_id = None
        self._type = None
        self._domain_name = None
        self._certificate_id = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if type is not None:
            self.type = type
        if domain_name is not None:
            self.domain_name = domain_name
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def uid(self):
        r"""Gets the uid of this DomainNameInfo.

        域名ID

        :return: The uid of this DomainNameInfo.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this DomainNameInfo.

        域名ID

        :param uid: The uid of this DomainNameInfo.
        :type uid: str
        """
        self._uid = uid

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DomainNameInfo.

        租户ID

        :return: The domain_id of this DomainNameInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DomainNameInfo.

        租户ID

        :param domain_id: The domain_id of this DomainNameInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this DomainNameInfo.

        项目ID

        :return: The project_id of this DomainNameInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DomainNameInfo.

        项目ID

        :param project_id: The project_id of this DomainNameInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DomainNameInfo.

        实例ID

        :return: The instance_id of this DomainNameInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DomainNameInfo.

        实例ID

        :param instance_id: The instance_id of this DomainNameInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        r"""Gets the type of this DomainNameInfo.

        域名类型(default/custom)

        :return: The type of this DomainNameInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DomainNameInfo.

        域名类型(default/custom)

        :param type: The type of this DomainNameInfo.
        :type type: str
        """
        self._type = type

    @property
    def domain_name(self):
        r"""Gets the domain_name of this DomainNameInfo.

        域名，只能由字母、数字、中划线、星号组成， 星号只能在开头，中划线不能在开头或末 尾，至少包含两个字符串，单个字符串不 超过63个字符，字符串间以点分割，且总 长度不超过100个字符。例如： example.com 或 *example.com。

        :return: The domain_name of this DomainNameInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this DomainNameInfo.

        域名，只能由字母、数字、中划线、星号组成， 星号只能在开头，中划线不能在开头或末 尾，至少包含两个字符串，单个字符串不 超过63个字符，字符串间以点分割，且总 长度不超过100个字符。例如： example.com 或 *example.com。

        :param domain_name: The domain_name of this DomainNameInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this DomainNameInfo.

        SCM服务的证书ID

        :return: The certificate_id of this DomainNameInfo.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this DomainNameInfo.

        SCM服务的证书ID

        :param certificate_id: The certificate_id of this DomainNameInfo.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def created_at(self):
        r"""Gets the created_at of this DomainNameInfo.

        增加域名的时间

        :return: The created_at of this DomainNameInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DomainNameInfo.

        增加域名的时间

        :param created_at: The created_at of this DomainNameInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this DomainNameInfo.

        更新域名的时间

        :return: The updated_at of this DomainNameInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this DomainNameInfo.

        更新域名的时间

        :param updated_at: The updated_at of this DomainNameInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, DomainNameInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
