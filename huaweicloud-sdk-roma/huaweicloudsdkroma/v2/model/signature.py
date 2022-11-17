# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Signature:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'sign_type': 'str',
        'sign_key': 'str',
        'sign_secret': 'str',
        'sign_algorithm': 'str',
        'update_time': 'datetime',
        'create_time': 'datetime',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'sign_type': 'sign_type',
        'sign_key': 'sign_key',
        'sign_secret': 'sign_secret',
        'sign_algorithm': 'sign_algorithm',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'id': 'id'
    }

    def __init__(self, name=None, sign_type=None, sign_key=None, sign_secret=None, sign_algorithm=None, update_time=None, create_time=None, id=None):
        """Signature

        The model defined in huaweicloud sdk

        :param name: 签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type name: str
        :param sign_type: 签名密钥类型： - hmac - basic - public_key - aes  basic类型需要实例升级到对应版本，若不存在可联系技术工程师升级。  public_key类型开启实例配置public_key才可使用，实例特性配置详情请参考“附录 &gt; 实例支持的APIC特性”，如确认实例不存在public_key配置可联系技术工程师开启。  aes类型需要实例升级到对应版本，若不存在可联系技术工程师升级。
        :type sign_type: str
        :param sign_key: 签名密钥的key。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母或数字开头，8 ~ 32字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母开头，4 ~ 32字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，+，/，&#x3D;，可以英文字母，数字，+，/开头，8 ~ 512字符。未填写时后台自动生成。 - aes类型的签名秘钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，&#x3D;，可以英文字母，数字，+，/开头，签名算法为aes-128-cfb时为16个字符，签名算法为aes-256-cfb时为32个字符。未填写时后台自动生成。
        :type sign_key: str
        :param sign_secret: 签名密钥的密钥。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，16 ~ 64字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，8 ~ 64字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，&#x3D;，可以英文字母，数字，+，/开头，15 ~ 2048字符。未填写时后台自动生成。 - aes类型签名秘钥使用的向量：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，&#x3D;，可以英文字母，数字，+，/开头，16个字符。未填写时后台自动生成。
        :type sign_secret: str
        :param sign_algorithm: 签名算法。默认值为空，仅aes类型签名秘钥支持选择签名算法，其他类型签名秘钥不支持签名算法。
        :type sign_algorithm: str
        :param update_time: 更新时间
        :type update_time: datetime
        :param create_time: 创建时间
        :type create_time: datetime
        :param id: 签名密钥的编号
        :type id: str
        """
        
        

        self._name = None
        self._sign_type = None
        self._sign_key = None
        self._sign_secret = None
        self._sign_algorithm = None
        self._update_time = None
        self._create_time = None
        self._id = None
        self.discriminator = None

        self.name = name
        if sign_type is not None:
            self.sign_type = sign_type
        if sign_key is not None:
            self.sign_key = sign_key
        if sign_secret is not None:
            self.sign_secret = sign_secret
        if sign_algorithm is not None:
            self.sign_algorithm = sign_algorithm
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this Signature.

        签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this Signature.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Signature.

        签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this Signature.
        :type name: str
        """
        self._name = name

    @property
    def sign_type(self):
        """Gets the sign_type of this Signature.

        签名密钥类型： - hmac - basic - public_key - aes  basic类型需要实例升级到对应版本，若不存在可联系技术工程师升级。  public_key类型开启实例配置public_key才可使用，实例特性配置详情请参考“附录 > 实例支持的APIC特性”，如确认实例不存在public_key配置可联系技术工程师开启。  aes类型需要实例升级到对应版本，若不存在可联系技术工程师升级。

        :return: The sign_type of this Signature.
        :rtype: str
        """
        return self._sign_type

    @sign_type.setter
    def sign_type(self, sign_type):
        """Sets the sign_type of this Signature.

        签名密钥类型： - hmac - basic - public_key - aes  basic类型需要实例升级到对应版本，若不存在可联系技术工程师升级。  public_key类型开启实例配置public_key才可使用，实例特性配置详情请参考“附录 > 实例支持的APIC特性”，如确认实例不存在public_key配置可联系技术工程师开启。  aes类型需要实例升级到对应版本，若不存在可联系技术工程师升级。

        :param sign_type: The sign_type of this Signature.
        :type sign_type: str
        """
        self._sign_type = sign_type

    @property
    def sign_key(self):
        """Gets the sign_key of this Signature.

        签名密钥的key。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母或数字开头，8 ~ 32字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母开头，4 ~ 32字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，+，/，=，可以英文字母，数字，+，/开头，8 ~ 512字符。未填写时后台自动生成。 - aes类型的签名秘钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，签名算法为aes-128-cfb时为16个字符，签名算法为aes-256-cfb时为32个字符。未填写时后台自动生成。

        :return: The sign_key of this Signature.
        :rtype: str
        """
        return self._sign_key

    @sign_key.setter
    def sign_key(self, sign_key):
        """Sets the sign_key of this Signature.

        签名密钥的key。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母或数字开头，8 ~ 32字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母开头，4 ~ 32字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，+，/，=，可以英文字母，数字，+，/开头，8 ~ 512字符。未填写时后台自动生成。 - aes类型的签名秘钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，签名算法为aes-128-cfb时为16个字符，签名算法为aes-256-cfb时为32个字符。未填写时后台自动生成。

        :param sign_key: The sign_key of this Signature.
        :type sign_key: str
        """
        self._sign_key = sign_key

    @property
    def sign_secret(self):
        """Gets the sign_secret of this Signature.

        签名密钥的密钥。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，16 ~ 64字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，8 ~ 64字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，15 ~ 2048字符。未填写时后台自动生成。 - aes类型签名秘钥使用的向量：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，16个字符。未填写时后台自动生成。

        :return: The sign_secret of this Signature.
        :rtype: str
        """
        return self._sign_secret

    @sign_secret.setter
    def sign_secret(self, sign_secret):
        """Sets the sign_secret of this Signature.

        签名密钥的密钥。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，16 ~ 64字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，8 ~ 64字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，15 ~ 2048字符。未填写时后台自动生成。 - aes类型签名秘钥使用的向量：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，16个字符。未填写时后台自动生成。

        :param sign_secret: The sign_secret of this Signature.
        :type sign_secret: str
        """
        self._sign_secret = sign_secret

    @property
    def sign_algorithm(self):
        """Gets the sign_algorithm of this Signature.

        签名算法。默认值为空，仅aes类型签名秘钥支持选择签名算法，其他类型签名秘钥不支持签名算法。

        :return: The sign_algorithm of this Signature.
        :rtype: str
        """
        return self._sign_algorithm

    @sign_algorithm.setter
    def sign_algorithm(self, sign_algorithm):
        """Sets the sign_algorithm of this Signature.

        签名算法。默认值为空，仅aes类型签名秘钥支持选择签名算法，其他类型签名秘钥不支持签名算法。

        :param sign_algorithm: The sign_algorithm of this Signature.
        :type sign_algorithm: str
        """
        self._sign_algorithm = sign_algorithm

    @property
    def update_time(self):
        """Gets the update_time of this Signature.

        更新时间

        :return: The update_time of this Signature.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Signature.

        更新时间

        :param update_time: The update_time of this Signature.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this Signature.

        创建时间

        :return: The create_time of this Signature.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Signature.

        创建时间

        :param create_time: The create_time of this Signature.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def id(self):
        """Gets the id of this Signature.

        签名密钥的编号

        :return: The id of this Signature.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Signature.

        签名密钥的编号

        :param id: The id of this Signature.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, Signature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
