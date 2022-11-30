# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNet2CloudPhoneServerRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_name': 'str',
        'server_model_name': 'str',
        'phone_model_name': 'str',
        'image_id': 'str',
        'count': 'int',
        'keypair_name': 'str',
        'ports': 'list[Port]',
        'extend_param': 'CreateNet2CloudPhoneServerRequestBodyExtendParam',
        'tenant_vpc_id': 'str',
        'nics': 'list[Nic]',
        'public_ip': 'CreateNet2CloudPhoneServerRequestBodyPublicIp',
        'band_width': 'CreateNet2CloudPhoneServerRequestBodyBandWidth',
        'availability_zone': 'str'
    }

    attribute_map = {
        'server_name': 'server_name',
        'server_model_name': 'server_model_name',
        'phone_model_name': 'phone_model_name',
        'image_id': 'image_id',
        'count': 'count',
        'keypair_name': 'keypair_name',
        'ports': 'ports',
        'extend_param': 'extend_param',
        'tenant_vpc_id': 'tenant_vpc_id',
        'nics': 'nics',
        'public_ip': 'public_ip',
        'band_width': 'band_width',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, server_name=None, server_model_name=None, phone_model_name=None, image_id=None, count=None, keypair_name=None, ports=None, extend_param=None, tenant_vpc_id=None, nics=None, public_ip=None, band_width=None, availability_zone=None):
        """CreateNet2CloudPhoneServerRequestBody

        The model defined in huaweicloud sdk

        :param server_name: 云手机服务器名称  不超过60个字符，只支持英文字母、数字、汉字、下划线和中划线。  批量购买会在服务器名称后自动添加序号，比如设置此参数为server-1，那么创建的云手机服务器名称会自动按序增加数字后缀，比如为server-1-0001
        :type server_name: str
        :param server_model_name: 云手机服务器规格，不超过64个字节
        :type server_model_name: str
        :param phone_model_name: 云手机规格，不超过64个字节
        :type phone_model_name: str
        :param image_id: 云手机镜像ID，不超过32个字节
        :type image_id: str
        :param count: 购买的云手机服务器个数，最多可购买10台
        :type count: int
        :param keypair_name: 密钥对名称，不超过64个字节，用于云手机ADB登录
        :type keypair_name: str
        :param ports: 云手机启用的应用端口，云手机服务会做端口转发
        :type ports: list[:class:`huaweicloudsdkcph.v1.Port`]
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyExtendParam`
        :param tenant_vpc_id: 租户自定义的VPC ID，为待创建的云服务器所属的虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式
        :type tenant_vpc_id: str
        :param nics: 租户自定义的网卡的结构体，为待创建的云服务器的网卡信息
        :type nics: list[:class:`huaweicloudsdkcph.v1.Nic`]
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyPublicIp`
        :param band_width: 
        :type band_width: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyBandWidth`
        :param availability_zone: 待创建云服务器所在的可用区，需要指定可用区（AZ）的名称
        :type availability_zone: str
        """
        
        

        self._server_name = None
        self._server_model_name = None
        self._phone_model_name = None
        self._image_id = None
        self._count = None
        self._keypair_name = None
        self._ports = None
        self._extend_param = None
        self._tenant_vpc_id = None
        self._nics = None
        self._public_ip = None
        self._band_width = None
        self._availability_zone = None
        self.discriminator = None

        self.server_name = server_name
        self.server_model_name = server_model_name
        self.phone_model_name = phone_model_name
        self.image_id = image_id
        self.count = count
        if keypair_name is not None:
            self.keypair_name = keypair_name
        if ports is not None:
            self.ports = ports
        self.extend_param = extend_param
        self.tenant_vpc_id = tenant_vpc_id
        self.nics = nics
        self.public_ip = public_ip
        self.band_width = band_width
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def server_name(self):
        """Gets the server_name of this CreateNet2CloudPhoneServerRequestBody.

        云手机服务器名称  不超过60个字符，只支持英文字母、数字、汉字、下划线和中划线。  批量购买会在服务器名称后自动添加序号，比如设置此参数为server-1，那么创建的云手机服务器名称会自动按序增加数字后缀，比如为server-1-0001

        :return: The server_name of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this CreateNet2CloudPhoneServerRequestBody.

        云手机服务器名称  不超过60个字符，只支持英文字母、数字、汉字、下划线和中划线。  批量购买会在服务器名称后自动添加序号，比如设置此参数为server-1，那么创建的云手机服务器名称会自动按序增加数字后缀，比如为server-1-0001

        :param server_name: The server_name of this CreateNet2CloudPhoneServerRequestBody.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_model_name(self):
        """Gets the server_model_name of this CreateNet2CloudPhoneServerRequestBody.

        云手机服务器规格，不超过64个字节

        :return: The server_model_name of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._server_model_name

    @server_model_name.setter
    def server_model_name(self, server_model_name):
        """Sets the server_model_name of this CreateNet2CloudPhoneServerRequestBody.

        云手机服务器规格，不超过64个字节

        :param server_model_name: The server_model_name of this CreateNet2CloudPhoneServerRequestBody.
        :type server_model_name: str
        """
        self._server_model_name = server_model_name

    @property
    def phone_model_name(self):
        """Gets the phone_model_name of this CreateNet2CloudPhoneServerRequestBody.

        云手机规格，不超过64个字节

        :return: The phone_model_name of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._phone_model_name

    @phone_model_name.setter
    def phone_model_name(self, phone_model_name):
        """Sets the phone_model_name of this CreateNet2CloudPhoneServerRequestBody.

        云手机规格，不超过64个字节

        :param phone_model_name: The phone_model_name of this CreateNet2CloudPhoneServerRequestBody.
        :type phone_model_name: str
        """
        self._phone_model_name = phone_model_name

    @property
    def image_id(self):
        """Gets the image_id of this CreateNet2CloudPhoneServerRequestBody.

        云手机镜像ID，不超过32个字节

        :return: The image_id of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this CreateNet2CloudPhoneServerRequestBody.

        云手机镜像ID，不超过32个字节

        :param image_id: The image_id of this CreateNet2CloudPhoneServerRequestBody.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def count(self):
        """Gets the count of this CreateNet2CloudPhoneServerRequestBody.

        购买的云手机服务器个数，最多可购买10台

        :return: The count of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CreateNet2CloudPhoneServerRequestBody.

        购买的云手机服务器个数，最多可购买10台

        :param count: The count of this CreateNet2CloudPhoneServerRequestBody.
        :type count: int
        """
        self._count = count

    @property
    def keypair_name(self):
        """Gets the keypair_name of this CreateNet2CloudPhoneServerRequestBody.

        密钥对名称，不超过64个字节，用于云手机ADB登录

        :return: The keypair_name of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._keypair_name

    @keypair_name.setter
    def keypair_name(self, keypair_name):
        """Sets the keypair_name of this CreateNet2CloudPhoneServerRequestBody.

        密钥对名称，不超过64个字节，用于云手机ADB登录

        :param keypair_name: The keypair_name of this CreateNet2CloudPhoneServerRequestBody.
        :type keypair_name: str
        """
        self._keypair_name = keypair_name

    @property
    def ports(self):
        """Gets the ports of this CreateNet2CloudPhoneServerRequestBody.

        云手机启用的应用端口，云手机服务会做端口转发

        :return: The ports of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: list[:class:`huaweicloudsdkcph.v1.Port`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this CreateNet2CloudPhoneServerRequestBody.

        云手机启用的应用端口，云手机服务会做端口转发

        :param ports: The ports of this CreateNet2CloudPhoneServerRequestBody.
        :type ports: list[:class:`huaweicloudsdkcph.v1.Port`]
        """
        self._ports = ports

    @property
    def extend_param(self):
        """Gets the extend_param of this CreateNet2CloudPhoneServerRequestBody.

        :return: The extend_param of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this CreateNet2CloudPhoneServerRequestBody.

        :param extend_param: The extend_param of this CreateNet2CloudPhoneServerRequestBody.
        :type extend_param: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyExtendParam`
        """
        self._extend_param = extend_param

    @property
    def tenant_vpc_id(self):
        """Gets the tenant_vpc_id of this CreateNet2CloudPhoneServerRequestBody.

        租户自定义的VPC ID，为待创建的云服务器所属的虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式

        :return: The tenant_vpc_id of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._tenant_vpc_id

    @tenant_vpc_id.setter
    def tenant_vpc_id(self, tenant_vpc_id):
        """Sets the tenant_vpc_id of this CreateNet2CloudPhoneServerRequestBody.

        租户自定义的VPC ID，为待创建的云服务器所属的虚拟私有云（简称VPC），需要指定已创建VPC的ID，UUID格式

        :param tenant_vpc_id: The tenant_vpc_id of this CreateNet2CloudPhoneServerRequestBody.
        :type tenant_vpc_id: str
        """
        self._tenant_vpc_id = tenant_vpc_id

    @property
    def nics(self):
        """Gets the nics of this CreateNet2CloudPhoneServerRequestBody.

        租户自定义的网卡的结构体，为待创建的云服务器的网卡信息

        :return: The nics of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: list[:class:`huaweicloudsdkcph.v1.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this CreateNet2CloudPhoneServerRequestBody.

        租户自定义的网卡的结构体，为待创建的云服务器的网卡信息

        :param nics: The nics of this CreateNet2CloudPhoneServerRequestBody.
        :type nics: list[:class:`huaweicloudsdkcph.v1.Nic`]
        """
        self._nics = nics

    @property
    def public_ip(self):
        """Gets the public_ip of this CreateNet2CloudPhoneServerRequestBody.

        :return: The public_ip of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyPublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this CreateNet2CloudPhoneServerRequestBody.

        :param public_ip: The public_ip of this CreateNet2CloudPhoneServerRequestBody.
        :type public_ip: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyPublicIp`
        """
        self._public_ip = public_ip

    @property
    def band_width(self):
        """Gets the band_width of this CreateNet2CloudPhoneServerRequestBody.

        :return: The band_width of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyBandWidth`
        """
        return self._band_width

    @band_width.setter
    def band_width(self, band_width):
        """Sets the band_width of this CreateNet2CloudPhoneServerRequestBody.

        :param band_width: The band_width of this CreateNet2CloudPhoneServerRequestBody.
        :type band_width: :class:`huaweicloudsdkcph.v1.CreateNet2CloudPhoneServerRequestBodyBandWidth`
        """
        self._band_width = band_width

    @property
    def availability_zone(self):
        """Gets the availability_zone of this CreateNet2CloudPhoneServerRequestBody.

        待创建云服务器所在的可用区，需要指定可用区（AZ）的名称

        :return: The availability_zone of this CreateNet2CloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this CreateNet2CloudPhoneServerRequestBody.

        待创建云服务器所在的可用区，需要指定可用区（AZ）的名称

        :param availability_zone: The availability_zone of this CreateNet2CloudPhoneServerRequestBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, CreateNet2CloudPhoneServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
