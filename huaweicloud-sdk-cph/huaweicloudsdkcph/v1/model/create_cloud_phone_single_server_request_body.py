# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCloudPhoneSingleServerRequestBody:

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
        'count': 'int',
        'order_param': 'CreateCloudPhoneSingleServerRequestBodyOrderParam',
        'nics': 'list[NicForSingleServer]',
        'public_ip': 'CreateCloudPhoneSingleServerRequestBodyPublicIp',
        'availability_zone': 'str',
        'data_volume': 'CreateCloudPhoneSingleServerRequestBodyDataVolume',
        'keypair_name': 'str',
        'enterprise_project_id': 'str',
        'image_id': 'str'
    }

    attribute_map = {
        'server_name': 'server_name',
        'server_model_name': 'server_model_name',
        'count': 'count',
        'order_param': 'order_param',
        'nics': 'nics',
        'public_ip': 'public_ip',
        'availability_zone': 'availability_zone',
        'data_volume': 'data_volume',
        'keypair_name': 'keypair_name',
        'enterprise_project_id': 'enterprise_project_id',
        'image_id': 'image_id'
    }

    def __init__(self, server_name=None, server_model_name=None, count=None, order_param=None, nics=None, public_ip=None, availability_zone=None, data_volume=None, keypair_name=None, enterprise_project_id=None, image_id=None):
        r"""CreateCloudPhoneSingleServerRequestBody

        The model defined in huaweicloud sdk

        :param server_name: 云手机裸服务器名称，不超过60个字符，只支持英文字母、数字、汉字、下划线和中划线。批量购买会在云手机裸服务器名称后自动添加序号，比如设置此参数为server-1，那么创建的云手机裸服务器名称会自动按序增加数字后缀，比如为server-1-0001。
        :type server_name: str
        :param server_model_name: 云手机裸服务器规格名称。
        :type server_model_name: str
        :param count: 购买的云手机裸服务器个数，最多可购买10台。
        :type count: int
        :param order_param: 
        :type order_param: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyOrderParam`
        :param nics: 租户自定义的网卡的结构体，为待创建的云手机裸服务器的网卡信息。
        :type nics: list[:class:`huaweicloudsdkcph.v1.NicForSingleServer`]
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyPublicIp`
        :param availability_zone: 待创建云手机裸服务器所在的可用区（AZ）的名称。如上海一可用区1为cn-east-3a。
        :type availability_zone: str
        :param data_volume: 
        :type data_volume: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyDataVolume`
        :param keypair_name: 指定登录云手机裸服务器已有密钥的名称。
        :type keypair_name: str
        :param enterprise_project_id: 企业项目ID。 该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。
        :type enterprise_project_id: str
        :param image_id: 云手机裸服务器镜像ID，不超过36个字节。未指定时使用默认云手机裸服务器镜像。
        :type image_id: str
        """
        
        

        self._server_name = None
        self._server_model_name = None
        self._count = None
        self._order_param = None
        self._nics = None
        self._public_ip = None
        self._availability_zone = None
        self._data_volume = None
        self._keypair_name = None
        self._enterprise_project_id = None
        self._image_id = None
        self.discriminator = None

        self.server_name = server_name
        self.server_model_name = server_model_name
        self.count = count
        self.order_param = order_param
        self.nics = nics
        self.public_ip = public_ip
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if data_volume is not None:
            self.data_volume = data_volume
        self.keypair_name = keypair_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_id is not None:
            self.image_id = image_id

    @property
    def server_name(self):
        r"""Gets the server_name of this CreateCloudPhoneSingleServerRequestBody.

        云手机裸服务器名称，不超过60个字符，只支持英文字母、数字、汉字、下划线和中划线。批量购买会在云手机裸服务器名称后自动添加序号，比如设置此参数为server-1，那么创建的云手机裸服务器名称会自动按序增加数字后缀，比如为server-1-0001。

        :return: The server_name of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        r"""Sets the server_name of this CreateCloudPhoneSingleServerRequestBody.

        云手机裸服务器名称，不超过60个字符，只支持英文字母、数字、汉字、下划线和中划线。批量购买会在云手机裸服务器名称后自动添加序号，比如设置此参数为server-1，那么创建的云手机裸服务器名称会自动按序增加数字后缀，比如为server-1-0001。

        :param server_name: The server_name of this CreateCloudPhoneSingleServerRequestBody.
        :type server_name: str
        """
        self._server_name = server_name

    @property
    def server_model_name(self):
        r"""Gets the server_model_name of this CreateCloudPhoneSingleServerRequestBody.

        云手机裸服务器规格名称。

        :return: The server_model_name of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: str
        """
        return self._server_model_name

    @server_model_name.setter
    def server_model_name(self, server_model_name):
        r"""Sets the server_model_name of this CreateCloudPhoneSingleServerRequestBody.

        云手机裸服务器规格名称。

        :param server_model_name: The server_model_name of this CreateCloudPhoneSingleServerRequestBody.
        :type server_model_name: str
        """
        self._server_model_name = server_model_name

    @property
    def count(self):
        r"""Gets the count of this CreateCloudPhoneSingleServerRequestBody.

        购买的云手机裸服务器个数，最多可购买10台。

        :return: The count of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this CreateCloudPhoneSingleServerRequestBody.

        购买的云手机裸服务器个数，最多可购买10台。

        :param count: The count of this CreateCloudPhoneSingleServerRequestBody.
        :type count: int
        """
        self._count = count

    @property
    def order_param(self):
        r"""Gets the order_param of this CreateCloudPhoneSingleServerRequestBody.

        :return: The order_param of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyOrderParam`
        """
        return self._order_param

    @order_param.setter
    def order_param(self, order_param):
        r"""Sets the order_param of this CreateCloudPhoneSingleServerRequestBody.

        :param order_param: The order_param of this CreateCloudPhoneSingleServerRequestBody.
        :type order_param: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyOrderParam`
        """
        self._order_param = order_param

    @property
    def nics(self):
        r"""Gets the nics of this CreateCloudPhoneSingleServerRequestBody.

        租户自定义的网卡的结构体，为待创建的云手机裸服务器的网卡信息。

        :return: The nics of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: list[:class:`huaweicloudsdkcph.v1.NicForSingleServer`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        r"""Sets the nics of this CreateCloudPhoneSingleServerRequestBody.

        租户自定义的网卡的结构体，为待创建的云手机裸服务器的网卡信息。

        :param nics: The nics of this CreateCloudPhoneSingleServerRequestBody.
        :type nics: list[:class:`huaweicloudsdkcph.v1.NicForSingleServer`]
        """
        self._nics = nics

    @property
    def public_ip(self):
        r"""Gets the public_ip of this CreateCloudPhoneSingleServerRequestBody.

        :return: The public_ip of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyPublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this CreateCloudPhoneSingleServerRequestBody.

        :param public_ip: The public_ip of this CreateCloudPhoneSingleServerRequestBody.
        :type public_ip: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyPublicIp`
        """
        self._public_ip = public_ip

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateCloudPhoneSingleServerRequestBody.

        待创建云手机裸服务器所在的可用区（AZ）的名称。如上海一可用区1为cn-east-3a。

        :return: The availability_zone of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateCloudPhoneSingleServerRequestBody.

        待创建云手机裸服务器所在的可用区（AZ）的名称。如上海一可用区1为cn-east-3a。

        :param availability_zone: The availability_zone of this CreateCloudPhoneSingleServerRequestBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def data_volume(self):
        r"""Gets the data_volume of this CreateCloudPhoneSingleServerRequestBody.

        :return: The data_volume of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyDataVolume`
        """
        return self._data_volume

    @data_volume.setter
    def data_volume(self, data_volume):
        r"""Sets the data_volume of this CreateCloudPhoneSingleServerRequestBody.

        :param data_volume: The data_volume of this CreateCloudPhoneSingleServerRequestBody.
        :type data_volume: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyDataVolume`
        """
        self._data_volume = data_volume

    @property
    def keypair_name(self):
        r"""Gets the keypair_name of this CreateCloudPhoneSingleServerRequestBody.

        指定登录云手机裸服务器已有密钥的名称。

        :return: The keypair_name of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: str
        """
        return self._keypair_name

    @keypair_name.setter
    def keypair_name(self, keypair_name):
        r"""Sets the keypair_name of this CreateCloudPhoneSingleServerRequestBody.

        指定登录云手机裸服务器已有密钥的名称。

        :param keypair_name: The keypair_name of this CreateCloudPhoneSingleServerRequestBody.
        :type keypair_name: str
        """
        self._keypair_name = keypair_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateCloudPhoneSingleServerRequestBody.

        企业项目ID。 该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。

        :return: The enterprise_project_id of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateCloudPhoneSingleServerRequestBody.

        企业项目ID。 该字段不传（或传为字符串“0”），则将资源绑定给默认企业项目。

        :param enterprise_project_id: The enterprise_project_id of this CreateCloudPhoneSingleServerRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_id(self):
        r"""Gets the image_id of this CreateCloudPhoneSingleServerRequestBody.

        云手机裸服务器镜像ID，不超过36个字节。未指定时使用默认云手机裸服务器镜像。

        :return: The image_id of this CreateCloudPhoneSingleServerRequestBody.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this CreateCloudPhoneSingleServerRequestBody.

        云手机裸服务器镜像ID，不超过36个字节。未指定时使用默认云手机裸服务器镜像。

        :param image_id: The image_id of this CreateCloudPhoneSingleServerRequestBody.
        :type image_id: str
        """
        self._image_id = image_id

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
        if not isinstance(other, CreateCloudPhoneSingleServerRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
