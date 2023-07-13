# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeGroupCertResponse(SdkResponse):

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
        'description': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'group_id': 'str',
        'is_deleted': 'bool',
        'project_id': 'str',
        'type': 'str',
        'serial_num': 'str',
        'ca': 'str',
        'certificate': 'str',
        'private_key': 'str',
        'package': 'str',
        'cert_remaining_valid_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'group_id': 'group_id',
        'is_deleted': 'is_deleted',
        'project_id': 'project_id',
        'type': 'type',
        'serial_num': 'serial_num',
        'ca': 'ca',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'package': 'package',
        'cert_remaining_valid_time': 'cert_remaining_valid_time'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, group_id=None, is_deleted=None, project_id=None, type=None, serial_num=None, ca=None, certificate=None, private_key=None, package=None, cert_remaining_valid_time=None):
        """CreateEdgeGroupCertResponse

        The model defined in huaweicloud sdk

        :param id: 证书ID
        :type id: str
        :param name: 证书名称
        :type name: str
        :param description: 证书描述
        :type description: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param group_id: 证书绑定的边缘节点组ID
        :type group_id: str
        :param is_deleted: 证书是否处于删除中
        :type is_deleted: bool
        :param project_id: 证书所属账号的项目ID
        :type project_id: str
        :param type: 证书类型，包含： - system：创建节点时会默认创建一套系统证书 - application：应用证书 - device：设备证书
        :type type: str
        :param serial_num: 证书序列号
        :type serial_num: str
        :param ca: 根证书
        :type ca: str
        :param certificate: 证书
        :type certificate: str
        :param private_key: 私钥
        :type private_key: str
        :param package: 将证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。
        :type package: str
        :param cert_remaining_valid_time: 证书有效期持续时间
        :type cert_remaining_valid_time: int
        """
        
        super(CreateEdgeGroupCertResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._group_id = None
        self._is_deleted = None
        self._project_id = None
        self._type = None
        self._serial_num = None
        self._ca = None
        self._certificate = None
        self._private_key = None
        self._package = None
        self._cert_remaining_valid_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if group_id is not None:
            self.group_id = group_id
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if project_id is not None:
            self.project_id = project_id
        if type is not None:
            self.type = type
        if serial_num is not None:
            self.serial_num = serial_num
        if ca is not None:
            self.ca = ca
        if certificate is not None:
            self.certificate = certificate
        if private_key is not None:
            self.private_key = private_key
        if package is not None:
            self.package = package
        if cert_remaining_valid_time is not None:
            self.cert_remaining_valid_time = cert_remaining_valid_time

    @property
    def id(self):
        """Gets the id of this CreateEdgeGroupCertResponse.

        证书ID

        :return: The id of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateEdgeGroupCertResponse.

        证书ID

        :param id: The id of this CreateEdgeGroupCertResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateEdgeGroupCertResponse.

        证书名称

        :return: The name of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEdgeGroupCertResponse.

        证书名称

        :param name: The name of this CreateEdgeGroupCertResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateEdgeGroupCertResponse.

        证书描述

        :return: The description of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEdgeGroupCertResponse.

        证书描述

        :param description: The description of this CreateEdgeGroupCertResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this CreateEdgeGroupCertResponse.

        创建时间

        :return: The created_at of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateEdgeGroupCertResponse.

        创建时间

        :param created_at: The created_at of this CreateEdgeGroupCertResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CreateEdgeGroupCertResponse.

        更新时间

        :return: The updated_at of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CreateEdgeGroupCertResponse.

        更新时间

        :param updated_at: The updated_at of this CreateEdgeGroupCertResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def group_id(self):
        """Gets the group_id of this CreateEdgeGroupCertResponse.

        证书绑定的边缘节点组ID

        :return: The group_id of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateEdgeGroupCertResponse.

        证书绑定的边缘节点组ID

        :param group_id: The group_id of this CreateEdgeGroupCertResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def is_deleted(self):
        """Gets the is_deleted of this CreateEdgeGroupCertResponse.

        证书是否处于删除中

        :return: The is_deleted of this CreateEdgeGroupCertResponse.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this CreateEdgeGroupCertResponse.

        证书是否处于删除中

        :param is_deleted: The is_deleted of this CreateEdgeGroupCertResponse.
        :type is_deleted: bool
        """
        self._is_deleted = is_deleted

    @property
    def project_id(self):
        """Gets the project_id of this CreateEdgeGroupCertResponse.

        证书所属账号的项目ID

        :return: The project_id of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateEdgeGroupCertResponse.

        证书所属账号的项目ID

        :param project_id: The project_id of this CreateEdgeGroupCertResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        """Gets the type of this CreateEdgeGroupCertResponse.

        证书类型，包含： - system：创建节点时会默认创建一套系统证书 - application：应用证书 - device：设备证书

        :return: The type of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateEdgeGroupCertResponse.

        证书类型，包含： - system：创建节点时会默认创建一套系统证书 - application：应用证书 - device：设备证书

        :param type: The type of this CreateEdgeGroupCertResponse.
        :type type: str
        """
        self._type = type

    @property
    def serial_num(self):
        """Gets the serial_num of this CreateEdgeGroupCertResponse.

        证书序列号

        :return: The serial_num of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._serial_num

    @serial_num.setter
    def serial_num(self, serial_num):
        """Sets the serial_num of this CreateEdgeGroupCertResponse.

        证书序列号

        :param serial_num: The serial_num of this CreateEdgeGroupCertResponse.
        :type serial_num: str
        """
        self._serial_num = serial_num

    @property
    def ca(self):
        """Gets the ca of this CreateEdgeGroupCertResponse.

        根证书

        :return: The ca of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this CreateEdgeGroupCertResponse.

        根证书

        :param ca: The ca of this CreateEdgeGroupCertResponse.
        :type ca: str
        """
        self._ca = ca

    @property
    def certificate(self):
        """Gets the certificate of this CreateEdgeGroupCertResponse.

        证书

        :return: The certificate of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CreateEdgeGroupCertResponse.

        证书

        :param certificate: The certificate of this CreateEdgeGroupCertResponse.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        """Gets the private_key of this CreateEdgeGroupCertResponse.

        私钥

        :return: The private_key of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CreateEdgeGroupCertResponse.

        私钥

        :param private_key: The private_key of this CreateEdgeGroupCertResponse.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def package(self):
        """Gets the package of this CreateEdgeGroupCertResponse.

        将证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。

        :return: The package of this CreateEdgeGroupCertResponse.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this CreateEdgeGroupCertResponse.

        将证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。

        :param package: The package of this CreateEdgeGroupCertResponse.
        :type package: str
        """
        self._package = package

    @property
    def cert_remaining_valid_time(self):
        """Gets the cert_remaining_valid_time of this CreateEdgeGroupCertResponse.

        证书有效期持续时间

        :return: The cert_remaining_valid_time of this CreateEdgeGroupCertResponse.
        :rtype: int
        """
        return self._cert_remaining_valid_time

    @cert_remaining_valid_time.setter
    def cert_remaining_valid_time(self, cert_remaining_valid_time):
        """Sets the cert_remaining_valid_time of this CreateEdgeGroupCertResponse.

        证书有效期持续时间

        :param cert_remaining_valid_time: The cert_remaining_valid_time of this CreateEdgeGroupCertResponse.
        :type cert_remaining_valid_time: int
        """
        self._cert_remaining_valid_time = cert_remaining_valid_time

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
        if not isinstance(other, CreateEdgeGroupCertResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
