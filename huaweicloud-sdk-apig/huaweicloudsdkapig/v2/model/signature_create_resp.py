# coding: utf-8

import pprint
import re

import six





class SignatureCreateResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sign_secret': 'str',
        'update_time': 'datetime',
        'create_time': 'datetime',
        'name': 'str',
        'id': 'str',
        'sign_key': 'str',
        'sign_type': 'str',
        'bind_num': 'int',
        'ldapi_bind_num': 'int'
    }

    attribute_map = {
        'sign_secret': 'sign_secret',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'name': 'name',
        'id': 'id',
        'sign_key': 'sign_key',
        'sign_type': 'sign_type',
        'bind_num': 'bind_num',
        'ldapi_bind_num': 'ldapi_bind_num'
    }

    def __init__(self, sign_secret=None, update_time=None, create_time=None, name=None, id=None, sign_key=None, sign_type=None, bind_num=None, ldapi_bind_num=None):
        """SignatureCreateResp - a model defined in huaweicloud sdk"""
        
        

        self._sign_secret = None
        self._update_time = None
        self._create_time = None
        self._name = None
        self._id = None
        self._sign_key = None
        self._sign_type = None
        self._bind_num = None
        self._ldapi_bind_num = None
        self.discriminator = None

        if sign_secret is not None:
            self.sign_secret = sign_secret
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if sign_key is not None:
            self.sign_key = sign_key
        if sign_type is not None:
            self.sign_type = sign_type
        if bind_num is not None:
            self.bind_num = bind_num
        if ldapi_bind_num is not None:
            self.ldapi_bind_num = ldapi_bind_num

    @property
    def sign_secret(self):
        """Gets the sign_secret of this SignatureCreateResp.

        签名密钥的密钥

        :return: The sign_secret of this SignatureCreateResp.
        :rtype: str
        """
        return self._sign_secret

    @sign_secret.setter
    def sign_secret(self, sign_secret):
        """Sets the sign_secret of this SignatureCreateResp.

        签名密钥的密钥

        :param sign_secret: The sign_secret of this SignatureCreateResp.
        :type: str
        """
        self._sign_secret = sign_secret

    @property
    def update_time(self):
        """Gets the update_time of this SignatureCreateResp.

        更新时间

        :return: The update_time of this SignatureCreateResp.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this SignatureCreateResp.

        更新时间

        :param update_time: The update_time of this SignatureCreateResp.
        :type: datetime
        """
        self._update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this SignatureCreateResp.

        创建时间

        :return: The create_time of this SignatureCreateResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SignatureCreateResp.

        创建时间

        :param create_time: The create_time of this SignatureCreateResp.
        :type: datetime
        """
        self._create_time = create_time

    @property
    def name(self):
        """Gets the name of this SignatureCreateResp.

        签名密钥的名称

        :return: The name of this SignatureCreateResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SignatureCreateResp.

        签名密钥的名称

        :param name: The name of this SignatureCreateResp.
        :type: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this SignatureCreateResp.

        签名密钥的编号

        :return: The id of this SignatureCreateResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SignatureCreateResp.

        签名密钥的编号

        :param id: The id of this SignatureCreateResp.
        :type: str
        """
        self._id = id

    @property
    def sign_key(self):
        """Gets the sign_key of this SignatureCreateResp.

        签名密钥的key

        :return: The sign_key of this SignatureCreateResp.
        :rtype: str
        """
        return self._sign_key

    @sign_key.setter
    def sign_key(self, sign_key):
        """Sets the sign_key of this SignatureCreateResp.

        签名密钥的key

        :param sign_key: The sign_key of this SignatureCreateResp.
        :type: str
        """
        self._sign_key = sign_key

    @property
    def sign_type(self):
        """Gets the sign_type of this SignatureCreateResp.

        签名密钥的类型

        :return: The sign_type of this SignatureCreateResp.
        :rtype: str
        """
        return self._sign_type

    @sign_type.setter
    def sign_type(self, sign_type):
        """Sets the sign_type of this SignatureCreateResp.

        签名密钥的类型

        :param sign_type: The sign_type of this SignatureCreateResp.
        :type: str
        """
        self._sign_type = sign_type

    @property
    def bind_num(self):
        """Gets the bind_num of this SignatureCreateResp.

        绑定的API数量

        :return: The bind_num of this SignatureCreateResp.
        :rtype: int
        """
        return self._bind_num

    @bind_num.setter
    def bind_num(self, bind_num):
        """Sets the bind_num of this SignatureCreateResp.

        绑定的API数量

        :param bind_num: The bind_num of this SignatureCreateResp.
        :type: int
        """
        self._bind_num = bind_num

    @property
    def ldapi_bind_num(self):
        """Gets the ldapi_bind_num of this SignatureCreateResp.

        绑定的自定义后端数量  暂不支持

        :return: The ldapi_bind_num of this SignatureCreateResp.
        :rtype: int
        """
        return self._ldapi_bind_num

    @ldapi_bind_num.setter
    def ldapi_bind_num(self, ldapi_bind_num):
        """Sets the ldapi_bind_num of this SignatureCreateResp.

        绑定的自定义后端数量  暂不支持

        :param ldapi_bind_num: The ldapi_bind_num of this SignatureCreateResp.
        :type: int
        """
        self._ldapi_bind_num = ldapi_bind_num

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SignatureCreateResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
