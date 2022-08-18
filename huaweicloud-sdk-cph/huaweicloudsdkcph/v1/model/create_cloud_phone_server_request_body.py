# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCloudPhoneServerRequestBody:

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
        'ports': 'list[CreateCloudPhoneServerRequestBodyPorts]',
        'band_width': 'CreateCloudPhoneServerRequestBodyBandWidth',
        'extend_param': 'CreateCloudPhoneServerRequestBodyExtendParam',
        'vnc_enable': 'str',
        'subnet_cidr': 'str'
    }

    attribute_map = {
        'server_name': 'server_name',
        'server_model_name': 'server_model_name',
        'phone_model_name': 'phone_model_name',
        'image_id': 'image_id',
        'count': 'count',
        'keypair_name': 'keypair_name',
        'ports': 'ports',
        'band_width': 'band_width',
        'extend_param': 'extend_param',
        'vnc_enable': 'vnc_enable',
        'subnet_cidr': 'subnet_cidr'
    }

    def __init__(self, server_name=None, server_model_name=None, phone_model_name=None, image_id=None, count=None, keypair_name=None, ports=None, band_width=None, extend_param=None, vnc_enable=None, subnet_cidr=None):
        """CreateCloudPhoneServerRequestBody

        The model defined in huaweicloud sdk

        :param server_name: 云手机服务器名称 不超过60个字符，只支持英文字母、数字、汉字、下划线和中划线。 批量购买会在服务器名称后自动添加序号，比如设置此参数为server-1，那么创建的云手机服务器名称会自动按序增加数字后缀，比如为server-1-0001
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
        :type ports: list[:class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerRequestBodyPorts`]
        :param band_width: 
        :type band_width: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerRequestBodyBandWidth`
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerRequestBodyExtendParam`
        :param vnc_enable: (已废弃)是否开启VNC方式登录云手机。 - 为\&quot;true\&quot;时开启（忽略大小写）。 - 为其他，则不开启
        :type vnc_enable: str
        :param subnet_cidr: 服务器的子网信息，第一次购买系统会自动创建172.31.0.0/16的子网。需要自定义子网的客户，需要全部通过API购买，设置的子网，必须是子网的格式且和已有子网不能重叠
        :type subnet_cidr: str
        """
        
        

        self._server_name = None
        self._server_model_name = None
        self._phone_model_name = None
        self._image_id = None
        self._count = None
        self._keypair_name = None
        self._ports = None
        self._band_width = None
        self._extend_param = None
        self._vnc_enable = None
        self._subnet_cidr = None
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
        self.band_width = band_width
        self.extend_param = extend_param
        if vnc_enable is not None:
            self.vnc_enable = vnc_enable
        if subnet_cidr is not None:
            self.subnet_cidr = subnet_cidr

    @property
    def server_name(self):
        """Gets the server_name of this CreateCloudPhoneServerRequestBody.

        云手机服务器名称 不超过60个字符，只支持英文字母、数字、汉字、下划线和中划线。 批量购买会在服务器名称后自动添加序号，比如设置此参数为server-1，那么创建的云手机服务器名称会自动按序增加数字后缀，比如为server-1-0001

        :return: The server_name of this CreateCloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this CreateCloudPhoneServerRequestBody.

        云手机服务器名称 不超过60个字符，只支持英文字母、数字、汉字、下划线和中划线。 批量购买会在服务器名称后自动添加序号，比如设置此参数为server-1，那么创建的云手机服务器名称会自动按序增加数字后缀，比如为server-1-0001

        :param server_name: The server_name of this CreateCloudPhoneServerRequestBody.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_model_name(self):
        """Gets the server_model_name of this CreateCloudPhoneServerRequestBody.

        云手机服务器规格，不超过64个字节

        :return: The server_model_name of this CreateCloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._server_model_name

    @server_model_name.setter
    def server_model_name(self, server_model_name):
        """Sets the server_model_name of this CreateCloudPhoneServerRequestBody.

        云手机服务器规格，不超过64个字节

        :param server_model_name: The server_model_name of this CreateCloudPhoneServerRequestBody.
        :type server_model_name: str
        """
        self._server_model_name = server_model_name

    @property
    def phone_model_name(self):
        """Gets the phone_model_name of this CreateCloudPhoneServerRequestBody.

        云手机规格，不超过64个字节

        :return: The phone_model_name of this CreateCloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._phone_model_name

    @phone_model_name.setter
    def phone_model_name(self, phone_model_name):
        """Sets the phone_model_name of this CreateCloudPhoneServerRequestBody.

        云手机规格，不超过64个字节

        :param phone_model_name: The phone_model_name of this CreateCloudPhoneServerRequestBody.
        :type phone_model_name: str
        """
        self._phone_model_name = phone_model_name

    @property
    def image_id(self):
        """Gets the image_id of this CreateCloudPhoneServerRequestBody.

        云手机镜像ID，不超过32个字节

        :return: The image_id of this CreateCloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this CreateCloudPhoneServerRequestBody.

        云手机镜像ID，不超过32个字节

        :param image_id: The image_id of this CreateCloudPhoneServerRequestBody.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def count(self):
        """Gets the count of this CreateCloudPhoneServerRequestBody.

        购买的云手机服务器个数，最多可购买10台

        :return: The count of this CreateCloudPhoneServerRequestBody.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CreateCloudPhoneServerRequestBody.

        购买的云手机服务器个数，最多可购买10台

        :param count: The count of this CreateCloudPhoneServerRequestBody.
        :type count: int
        """
        self._count = count

    @property
    def keypair_name(self):
        """Gets the keypair_name of this CreateCloudPhoneServerRequestBody.

        密钥对名称，不超过64个字节，用于云手机ADB登录

        :return: The keypair_name of this CreateCloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._keypair_name

    @keypair_name.setter
    def keypair_name(self, keypair_name):
        """Sets the keypair_name of this CreateCloudPhoneServerRequestBody.

        密钥对名称，不超过64个字节，用于云手机ADB登录

        :param keypair_name: The keypair_name of this CreateCloudPhoneServerRequestBody.
        :type keypair_name: str
        """
        self._keypair_name = keypair_name

    @property
    def ports(self):
        """Gets the ports of this CreateCloudPhoneServerRequestBody.

        云手机启用的应用端口，云手机服务会做端口转发

        :return: The ports of this CreateCloudPhoneServerRequestBody.
        :rtype: list[:class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerRequestBodyPorts`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this CreateCloudPhoneServerRequestBody.

        云手机启用的应用端口，云手机服务会做端口转发

        :param ports: The ports of this CreateCloudPhoneServerRequestBody.
        :type ports: list[:class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerRequestBodyPorts`]
        """
        self._ports = ports

    @property
    def band_width(self):
        """Gets the band_width of this CreateCloudPhoneServerRequestBody.


        :return: The band_width of this CreateCloudPhoneServerRequestBody.
        :rtype: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerRequestBodyBandWidth`
        """
        return self._band_width

    @band_width.setter
    def band_width(self, band_width):
        """Sets the band_width of this CreateCloudPhoneServerRequestBody.


        :param band_width: The band_width of this CreateCloudPhoneServerRequestBody.
        :type band_width: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerRequestBodyBandWidth`
        """
        self._band_width = band_width

    @property
    def extend_param(self):
        """Gets the extend_param of this CreateCloudPhoneServerRequestBody.


        :return: The extend_param of this CreateCloudPhoneServerRequestBody.
        :rtype: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerRequestBodyExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this CreateCloudPhoneServerRequestBody.


        :param extend_param: The extend_param of this CreateCloudPhoneServerRequestBody.
        :type extend_param: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneServerRequestBodyExtendParam`
        """
        self._extend_param = extend_param

    @property
    def vnc_enable(self):
        """Gets the vnc_enable of this CreateCloudPhoneServerRequestBody.

        (已废弃)是否开启VNC方式登录云手机。 - 为\"true\"时开启（忽略大小写）。 - 为其他，则不开启

        :return: The vnc_enable of this CreateCloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._vnc_enable

    @vnc_enable.setter
    def vnc_enable(self, vnc_enable):
        """Sets the vnc_enable of this CreateCloudPhoneServerRequestBody.

        (已废弃)是否开启VNC方式登录云手机。 - 为\"true\"时开启（忽略大小写）。 - 为其他，则不开启

        :param vnc_enable: The vnc_enable of this CreateCloudPhoneServerRequestBody.
        :type vnc_enable: str
        """
        self._vnc_enable = vnc_enable

    @property
    def subnet_cidr(self):
        """Gets the subnet_cidr of this CreateCloudPhoneServerRequestBody.

        服务器的子网信息，第一次购买系统会自动创建172.31.0.0/16的子网。需要自定义子网的客户，需要全部通过API购买，设置的子网，必须是子网的格式且和已有子网不能重叠

        :return: The subnet_cidr of this CreateCloudPhoneServerRequestBody.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        """Sets the subnet_cidr of this CreateCloudPhoneServerRequestBody.

        服务器的子网信息，第一次购买系统会自动创建172.31.0.0/16的子网。需要自定义子网的客户，需要全部通过API购买，设置的子网，必须是子网的格式且和已有子网不能重叠

        :param subnet_cidr: The subnet_cidr of this CreateCloudPhoneServerRequestBody.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

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
        if not isinstance(other, CreateCloudPhoneServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
