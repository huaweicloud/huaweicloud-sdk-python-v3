# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCertificateResponse(SdkResponse):

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
        'tenant_id': 'str',
        'admin_state_up': 'bool',
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'domain': 'str',
        'private_key': 'str',
        'certificate': 'str',
        'expire_time': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'admin_state_up': 'admin_state_up',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'domain': 'domain',
        'private_key': 'private_key',
        'certificate': 'certificate',
        'expire_time': 'expire_time',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, tenant_id=None, admin_state_up=None, name=None, description=None, type=None, domain=None, private_key=None, certificate=None, expire_time=None, create_time=None, update_time=None):
        """UpdateCertificateResponse

        The model defined in huaweicloud sdk

        :param id: SSL证书id
        :type id: str
        :param tenant_id: SSL证书所在的项目ID
        :type tenant_id: str
        :param admin_state_up: SSL证书的管理状态；暂不支持
        :type admin_state_up: bool
        :param name: SSL证书的名称。
        :type name: str
        :param description: SSL证书的描述。
        :type description: str
        :param type: SSL证书的类型。分为服务器证书(server)和CA证书(client)。
        :type type: str
        :param domain: 服务器证书所签域名。该字段仅type为server时有效。
        :type domain: str
        :param private_key: 服务器证书的私钥。仅type为server时有效。type为server时必选。
        :type private_key: str
        :param certificate: 当type为server时，表示服务器证书的公钥；当type为client时，表示用于认证客户端证书的CA证书。
        :type certificate: str
        :param expire_time: SSL证书的过期时间。 UTC时间，格式为：yyyy-MM-dd HH:mm:ss ，如2020-05-28 08:30:09
        :type expire_time: str
        :param create_time: SSL证书的创建时间。 UTC时间，格式为：yyyy-MM-dd HH:mm:ss ，如2020-05-28 08:30:09
        :type create_time: str
        :param update_time: SSL证书的更新时间。 UTC时间，格式为：yyyy-MM-dd HH:mm:ss ，如2020-05-28 08:30:09
        :type update_time: str
        """
        
        super(UpdateCertificateResponse, self).__init__()

        self._id = None
        self._tenant_id = None
        self._admin_state_up = None
        self._name = None
        self._description = None
        self._type = None
        self._domain = None
        self._private_key = None
        self._certificate = None
        self._expire_time = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if domain is not None:
            self.domain = domain
        if private_key is not None:
            self.private_key = private_key
        if certificate is not None:
            self.certificate = certificate
        if expire_time is not None:
            self.expire_time = expire_time
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this UpdateCertificateResponse.

        SSL证书id

        :return: The id of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateCertificateResponse.

        SSL证书id

        :param id: The id of this UpdateCertificateResponse.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this UpdateCertificateResponse.

        SSL证书所在的项目ID

        :return: The tenant_id of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this UpdateCertificateResponse.

        SSL证书所在的项目ID

        :param tenant_id: The tenant_id of this UpdateCertificateResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateCertificateResponse.

        SSL证书的管理状态；暂不支持

        :return: The admin_state_up of this UpdateCertificateResponse.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateCertificateResponse.

        SSL证书的管理状态；暂不支持

        :param admin_state_up: The admin_state_up of this UpdateCertificateResponse.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def name(self):
        """Gets the name of this UpdateCertificateResponse.

        SSL证书的名称。

        :return: The name of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCertificateResponse.

        SSL证书的名称。

        :param name: The name of this UpdateCertificateResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateCertificateResponse.

        SSL证书的描述。

        :return: The description of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCertificateResponse.

        SSL证书的描述。

        :param description: The description of this UpdateCertificateResponse.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this UpdateCertificateResponse.

        SSL证书的类型。分为服务器证书(server)和CA证书(client)。

        :return: The type of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateCertificateResponse.

        SSL证书的类型。分为服务器证书(server)和CA证书(client)。

        :param type: The type of this UpdateCertificateResponse.
        :type type: str
        """
        self._type = type

    @property
    def domain(self):
        """Gets the domain of this UpdateCertificateResponse.

        服务器证书所签域名。该字段仅type为server时有效。

        :return: The domain of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this UpdateCertificateResponse.

        服务器证书所签域名。该字段仅type为server时有效。

        :param domain: The domain of this UpdateCertificateResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def private_key(self):
        """Gets the private_key of this UpdateCertificateResponse.

        服务器证书的私钥。仅type为server时有效。type为server时必选。

        :return: The private_key of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this UpdateCertificateResponse.

        服务器证书的私钥。仅type为server时有效。type为server时必选。

        :param private_key: The private_key of this UpdateCertificateResponse.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate(self):
        """Gets the certificate of this UpdateCertificateResponse.

        当type为server时，表示服务器证书的公钥；当type为client时，表示用于认证客户端证书的CA证书。

        :return: The certificate of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this UpdateCertificateResponse.

        当type为server时，表示服务器证书的公钥；当type为client时，表示用于认证客户端证书的CA证书。

        :param certificate: The certificate of this UpdateCertificateResponse.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def expire_time(self):
        """Gets the expire_time of this UpdateCertificateResponse.

        SSL证书的过期时间。 UTC时间，格式为：yyyy-MM-dd HH:mm:ss ，如2020-05-28 08:30:09

        :return: The expire_time of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this UpdateCertificateResponse.

        SSL证书的过期时间。 UTC时间，格式为：yyyy-MM-dd HH:mm:ss ，如2020-05-28 08:30:09

        :param expire_time: The expire_time of this UpdateCertificateResponse.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def create_time(self):
        """Gets the create_time of this UpdateCertificateResponse.

        SSL证书的创建时间。 UTC时间，格式为：yyyy-MM-dd HH:mm:ss ，如2020-05-28 08:30:09

        :return: The create_time of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateCertificateResponse.

        SSL证书的创建时间。 UTC时间，格式为：yyyy-MM-dd HH:mm:ss ，如2020-05-28 08:30:09

        :param create_time: The create_time of this UpdateCertificateResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this UpdateCertificateResponse.

        SSL证书的更新时间。 UTC时间，格式为：yyyy-MM-dd HH:mm:ss ，如2020-05-28 08:30:09

        :return: The update_time of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UpdateCertificateResponse.

        SSL证书的更新时间。 UTC时间，格式为：yyyy-MM-dd HH:mm:ss ，如2020-05-28 08:30:09

        :param update_time: The update_time of this UpdateCertificateResponse.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, UpdateCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
