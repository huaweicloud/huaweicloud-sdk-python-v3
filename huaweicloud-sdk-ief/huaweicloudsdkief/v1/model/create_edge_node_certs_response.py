# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeNodeCertsResponse(SdkResponse):

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
        'node_id': 'str',
        'type': 'str',
        'serial_num': 'str',
        'ca': 'str',
        'certificate': 'str',
        'private_key': 'str',
        'package': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'node_id': 'node_id',
        'type': 'type',
        'serial_num': 'serial_num',
        'ca': 'ca',
        'certificate': 'certificate',
        'private_key': 'private_key',
        'package': 'package'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, node_id=None, type=None, serial_num=None, ca=None, certificate=None, private_key=None, package=None):
        """CreateEdgeNodeCertsResponse

        The model defined in huaweicloud sdk

        :param id: 证书id
        :type id: str
        :param name: 证书名称
        :type name: str
        :param description: 证书的描述
        :type description: str
        :param created_at: 证书的创建时间
        :type created_at: str
        :param node_id: 节点id
        :type node_id: str
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
        """
        
        super(CreateEdgeNodeCertsResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._node_id = None
        self._type = None
        self._serial_num = None
        self._ca = None
        self._certificate = None
        self._private_key = None
        self._package = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if node_id is not None:
            self.node_id = node_id
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

    @property
    def id(self):
        """Gets the id of this CreateEdgeNodeCertsResponse.

        证书id

        :return: The id of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateEdgeNodeCertsResponse.

        证书id

        :param id: The id of this CreateEdgeNodeCertsResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateEdgeNodeCertsResponse.

        证书名称

        :return: The name of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEdgeNodeCertsResponse.

        证书名称

        :param name: The name of this CreateEdgeNodeCertsResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateEdgeNodeCertsResponse.

        证书的描述

        :return: The description of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEdgeNodeCertsResponse.

        证书的描述

        :param description: The description of this CreateEdgeNodeCertsResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this CreateEdgeNodeCertsResponse.

        证书的创建时间

        :return: The created_at of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateEdgeNodeCertsResponse.

        证书的创建时间

        :param created_at: The created_at of this CreateEdgeNodeCertsResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def node_id(self):
        """Gets the node_id of this CreateEdgeNodeCertsResponse.

        节点id

        :return: The node_id of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this CreateEdgeNodeCertsResponse.

        节点id

        :param node_id: The node_id of this CreateEdgeNodeCertsResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def type(self):
        """Gets the type of this CreateEdgeNodeCertsResponse.

        证书类型，包含： - system：创建节点时会默认创建一套系统证书 - application：应用证书 - device：设备证书

        :return: The type of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateEdgeNodeCertsResponse.

        证书类型，包含： - system：创建节点时会默认创建一套系统证书 - application：应用证书 - device：设备证书

        :param type: The type of this CreateEdgeNodeCertsResponse.
        :type type: str
        """
        self._type = type

    @property
    def serial_num(self):
        """Gets the serial_num of this CreateEdgeNodeCertsResponse.

        证书序列号

        :return: The serial_num of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._serial_num

    @serial_num.setter
    def serial_num(self, serial_num):
        """Sets the serial_num of this CreateEdgeNodeCertsResponse.

        证书序列号

        :param serial_num: The serial_num of this CreateEdgeNodeCertsResponse.
        :type serial_num: str
        """
        self._serial_num = serial_num

    @property
    def ca(self):
        """Gets the ca of this CreateEdgeNodeCertsResponse.

        根证书

        :return: The ca of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this CreateEdgeNodeCertsResponse.

        根证书

        :param ca: The ca of this CreateEdgeNodeCertsResponse.
        :type ca: str
        """
        self._ca = ca

    @property
    def certificate(self):
        """Gets the certificate of this CreateEdgeNodeCertsResponse.

        证书

        :return: The certificate of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this CreateEdgeNodeCertsResponse.

        证书

        :param certificate: The certificate of this CreateEdgeNodeCertsResponse.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def private_key(self):
        """Gets the private_key of this CreateEdgeNodeCertsResponse.

        私钥

        :return: The private_key of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CreateEdgeNodeCertsResponse.

        私钥

        :param private_key: The private_key of this CreateEdgeNodeCertsResponse.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def package(self):
        """Gets the package of this CreateEdgeNodeCertsResponse.

        将证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。

        :return: The package of this CreateEdgeNodeCertsResponse.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this CreateEdgeNodeCertsResponse.

        将证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。

        :param package: The package of this CreateEdgeNodeCertsResponse.
        :type package: str
        """
        self._package = package

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
        if not isinstance(other, CreateEdgeNodeCertsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
