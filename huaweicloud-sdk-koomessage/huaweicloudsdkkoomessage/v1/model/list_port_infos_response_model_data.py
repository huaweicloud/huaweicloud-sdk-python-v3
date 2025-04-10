# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortInfosResponseModelData:

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
        'create_time': 'datetime',
        'pub_id': 'str',
        'port': 'str',
        'sign': 'list[str]',
        'authorization_files': 'dict(str, str)',
        'pub_name': 'str',
        'port_type': 'int',
        'sign_check': 'int',
        'province': 'str',
        'is_bind': 'int',
        'pub_list': 'list[PortSearchPubDetail]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'pub_id': 'pub_id',
        'port': 'port',
        'sign': 'sign',
        'authorization_files': 'authorization_files',
        'pub_name': 'pub_name',
        'port_type': 'port_type',
        'sign_check': 'sign_check',
        'province': 'province',
        'is_bind': 'is_bind',
        'pub_list': 'pub_list'
    }

    def __init__(self, id=None, create_time=None, pub_id=None, port=None, sign=None, authorization_files=None, pub_name=None, port_type=None, sign_check=None, province=None, is_bind=None, pub_list=None):
        r"""ListPortInfosResponseModelData

        The model defined in huaweicloud sdk

        :param id: 主键ID。
        :type id: str
        :param create_time: 创建时间，格式：yyyy-MM-ddTHH:mm:ssZ。
        :type create_time: datetime
        :param pub_id: 服务号ID，在通道号列表显示为null。
        :type pub_id: str
        :param port: 通道号。 
        :type port: str
        :param sign: 签名数组。  - 查询通道号列表时，该项为通道号签名列表  - 查询绑定关系时，该项为通道号绑定签名列表 
        :type sign: list[str]
        :param authorization_files: 授权证明图片，key是上传的图片ID，value是图片对应的URL。
        :type authorization_files: dict(str, str)
        :param pub_name: 服务号名称，查询通道号列表时该项为null。
        :type pub_name: str
        :param port_type: 通道号类型。 - 1：普通 - 3：前缀号段 - 5：后缀号段  
        :type port_type: int
        :param sign_check: 是否需要校验。  - 0：不校验 - 1：校验签名 
        :type sign_check: int
        :param province: 未绑定服务号时该项为null。
        :type province: str
        :param is_bind: 是否绑定。  - 0: 未绑定 - 1: 绑定 
        :type is_bind: int
        :param pub_list: 绑定的服务号列表。  &gt; 以JSON列表返回，格式： &gt; [{\&quot;pub_name\&quot;:\&quot;服务号名称\&quot;,\&quot;pub_reference\&quot;:\&quot;服务号备注\&quot;}]。 
        :type pub_list: list[:class:`huaweicloudsdkkoomessage.v1.PortSearchPubDetail`]
        """
        
        

        self._id = None
        self._create_time = None
        self._pub_id = None
        self._port = None
        self._sign = None
        self._authorization_files = None
        self._pub_name = None
        self._port_type = None
        self._sign_check = None
        self._province = None
        self._is_bind = None
        self._pub_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if pub_id is not None:
            self.pub_id = pub_id
        if port is not None:
            self.port = port
        if sign is not None:
            self.sign = sign
        if authorization_files is not None:
            self.authorization_files = authorization_files
        if pub_name is not None:
            self.pub_name = pub_name
        if port_type is not None:
            self.port_type = port_type
        if sign_check is not None:
            self.sign_check = sign_check
        if province is not None:
            self.province = province
        if is_bind is not None:
            self.is_bind = is_bind
        if pub_list is not None:
            self.pub_list = pub_list

    @property
    def id(self):
        r"""Gets the id of this ListPortInfosResponseModelData.

        主键ID。

        :return: The id of this ListPortInfosResponseModelData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListPortInfosResponseModelData.

        主键ID。

        :param id: The id of this ListPortInfosResponseModelData.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        r"""Gets the create_time of this ListPortInfosResponseModelData.

        创建时间，格式：yyyy-MM-ddTHH:mm:ssZ。

        :return: The create_time of this ListPortInfosResponseModelData.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListPortInfosResponseModelData.

        创建时间，格式：yyyy-MM-ddTHH:mm:ssZ。

        :param create_time: The create_time of this ListPortInfosResponseModelData.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def pub_id(self):
        r"""Gets the pub_id of this ListPortInfosResponseModelData.

        服务号ID，在通道号列表显示为null。

        :return: The pub_id of this ListPortInfosResponseModelData.
        :rtype: str
        """
        return self._pub_id

    @pub_id.setter
    def pub_id(self, pub_id):
        r"""Sets the pub_id of this ListPortInfosResponseModelData.

        服务号ID，在通道号列表显示为null。

        :param pub_id: The pub_id of this ListPortInfosResponseModelData.
        :type pub_id: str
        """
        self._pub_id = pub_id

    @property
    def port(self):
        r"""Gets the port of this ListPortInfosResponseModelData.

        通道号。 

        :return: The port of this ListPortInfosResponseModelData.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ListPortInfosResponseModelData.

        通道号。 

        :param port: The port of this ListPortInfosResponseModelData.
        :type port: str
        """
        self._port = port

    @property
    def sign(self):
        r"""Gets the sign of this ListPortInfosResponseModelData.

        签名数组。  - 查询通道号列表时，该项为通道号签名列表  - 查询绑定关系时，该项为通道号绑定签名列表 

        :return: The sign of this ListPortInfosResponseModelData.
        :rtype: list[str]
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        r"""Sets the sign of this ListPortInfosResponseModelData.

        签名数组。  - 查询通道号列表时，该项为通道号签名列表  - 查询绑定关系时，该项为通道号绑定签名列表 

        :param sign: The sign of this ListPortInfosResponseModelData.
        :type sign: list[str]
        """
        self._sign = sign

    @property
    def authorization_files(self):
        r"""Gets the authorization_files of this ListPortInfosResponseModelData.

        授权证明图片，key是上传的图片ID，value是图片对应的URL。

        :return: The authorization_files of this ListPortInfosResponseModelData.
        :rtype: dict(str, str)
        """
        return self._authorization_files

    @authorization_files.setter
    def authorization_files(self, authorization_files):
        r"""Sets the authorization_files of this ListPortInfosResponseModelData.

        授权证明图片，key是上传的图片ID，value是图片对应的URL。

        :param authorization_files: The authorization_files of this ListPortInfosResponseModelData.
        :type authorization_files: dict(str, str)
        """
        self._authorization_files = authorization_files

    @property
    def pub_name(self):
        r"""Gets the pub_name of this ListPortInfosResponseModelData.

        服务号名称，查询通道号列表时该项为null。

        :return: The pub_name of this ListPortInfosResponseModelData.
        :rtype: str
        """
        return self._pub_name

    @pub_name.setter
    def pub_name(self, pub_name):
        r"""Sets the pub_name of this ListPortInfosResponseModelData.

        服务号名称，查询通道号列表时该项为null。

        :param pub_name: The pub_name of this ListPortInfosResponseModelData.
        :type pub_name: str
        """
        self._pub_name = pub_name

    @property
    def port_type(self):
        r"""Gets the port_type of this ListPortInfosResponseModelData.

        通道号类型。 - 1：普通 - 3：前缀号段 - 5：后缀号段  

        :return: The port_type of this ListPortInfosResponseModelData.
        :rtype: int
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        r"""Sets the port_type of this ListPortInfosResponseModelData.

        通道号类型。 - 1：普通 - 3：前缀号段 - 5：后缀号段  

        :param port_type: The port_type of this ListPortInfosResponseModelData.
        :type port_type: int
        """
        self._port_type = port_type

    @property
    def sign_check(self):
        r"""Gets the sign_check of this ListPortInfosResponseModelData.

        是否需要校验。  - 0：不校验 - 1：校验签名 

        :return: The sign_check of this ListPortInfosResponseModelData.
        :rtype: int
        """
        return self._sign_check

    @sign_check.setter
    def sign_check(self, sign_check):
        r"""Sets the sign_check of this ListPortInfosResponseModelData.

        是否需要校验。  - 0：不校验 - 1：校验签名 

        :param sign_check: The sign_check of this ListPortInfosResponseModelData.
        :type sign_check: int
        """
        self._sign_check = sign_check

    @property
    def province(self):
        r"""Gets the province of this ListPortInfosResponseModelData.

        未绑定服务号时该项为null。

        :return: The province of this ListPortInfosResponseModelData.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this ListPortInfosResponseModelData.

        未绑定服务号时该项为null。

        :param province: The province of this ListPortInfosResponseModelData.
        :type province: str
        """
        self._province = province

    @property
    def is_bind(self):
        r"""Gets the is_bind of this ListPortInfosResponseModelData.

        是否绑定。  - 0: 未绑定 - 1: 绑定 

        :return: The is_bind of this ListPortInfosResponseModelData.
        :rtype: int
        """
        return self._is_bind

    @is_bind.setter
    def is_bind(self, is_bind):
        r"""Sets the is_bind of this ListPortInfosResponseModelData.

        是否绑定。  - 0: 未绑定 - 1: 绑定 

        :param is_bind: The is_bind of this ListPortInfosResponseModelData.
        :type is_bind: int
        """
        self._is_bind = is_bind

    @property
    def pub_list(self):
        r"""Gets the pub_list of this ListPortInfosResponseModelData.

        绑定的服务号列表。  > 以JSON列表返回，格式： > [{\"pub_name\":\"服务号名称\",\"pub_reference\":\"服务号备注\"}]。 

        :return: The pub_list of this ListPortInfosResponseModelData.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.PortSearchPubDetail`]
        """
        return self._pub_list

    @pub_list.setter
    def pub_list(self, pub_list):
        r"""Sets the pub_list of this ListPortInfosResponseModelData.

        绑定的服务号列表。  > 以JSON列表返回，格式： > [{\"pub_name\":\"服务号名称\",\"pub_reference\":\"服务号备注\"}]。 

        :param pub_list: The pub_list of this ListPortInfosResponseModelData.
        :type pub_list: list[:class:`huaweicloudsdkkoomessage.v1.PortSearchPubDetail`]
        """
        self._pub_list = pub_list

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
        if not isinstance(other, ListPortInfosResponseModelData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
