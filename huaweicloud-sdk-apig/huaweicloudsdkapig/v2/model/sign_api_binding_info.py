# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignApiBindingInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publish_id': 'str',
        'api_id': 'str',
        'group_name': 'str',
        'binding_time': 'datetime',
        'env_id': 'str',
        'env_name': 'str',
        'api_type': 'int',
        'api_name': 'str',
        'id': 'str',
        'api_remark': 'str',
        'sign_id': 'str',
        'sign_name': 'str',
        'sign_key': 'str',
        'sign_secret': 'str',
        'sign_type': 'str'
    }

    attribute_map = {
        'publish_id': 'publish_id',
        'api_id': 'api_id',
        'group_name': 'group_name',
        'binding_time': 'binding_time',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'api_type': 'api_type',
        'api_name': 'api_name',
        'id': 'id',
        'api_remark': 'api_remark',
        'sign_id': 'sign_id',
        'sign_name': 'sign_name',
        'sign_key': 'sign_key',
        'sign_secret': 'sign_secret',
        'sign_type': 'sign_type'
    }

    def __init__(self, publish_id=None, api_id=None, group_name=None, binding_time=None, env_id=None, env_name=None, api_type=None, api_name=None, id=None, api_remark=None, sign_id=None, sign_name=None, sign_key=None, sign_secret=None, sign_type=None):
        """SignApiBindingInfo

        The model defined in huaweicloud sdk

        :param publish_id: API的发布编号
        :type publish_id: str
        :param api_id: API编号
        :type api_id: str
        :param group_name: API所属分组的名称
        :type group_name: str
        :param binding_time: 绑定时间
        :type binding_time: datetime
        :param env_id: API所属环境的编号
        :type env_id: str
        :param env_name: API所属环境的名称
        :type env_name: str
        :param api_type: API类型
        :type api_type: int
        :param api_name: API名称
        :type api_name: str
        :param id: 绑定关系的ID
        :type id: str
        :param api_remark: API描述
        :type api_remark: str
        :param sign_id: 签名密钥的编号
        :type sign_id: str
        :param sign_name: 签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type sign_name: str
        :param sign_key: 签名密钥的key。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母或数字开头，8 ~ 32字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母开头，4 ~ 32字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，+，/，&#x3D;，可以英文字母，数字，+，/开头，8 ~ 512字符。未填写时后台自动生成。 - aes类型的签名秘钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，&#x3D;，可以英文字母，数字，+，/开头，签名算法为aes-128-cfb时为16个字符，签名算法为aes-256-cfb时为32个字符。未填写时后台自动生成。
        :type sign_key: str
        :param sign_secret: 签名密钥的密钥。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，16 ~ 64字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，8 ~ 64字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，&#x3D;，可以英文字母，数字，+，/开头，15 ~ 2048字符。未填写时后台自动生成。 - aes类型签名秘钥使用的向量：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，&#x3D;，可以英文字母，数字，+，/开头，16个字符。未填写时后台自动生成。
        :type sign_secret: str
        :param sign_type: 签名密钥类型： - hmac - basic - public_key - aes  basic类型需要实例升级到对应版本，若不存在可联系技术工程师升级。  public_key类型开启实例配置public_key才可使用，实例特性配置详情请参考“附录 &gt; 实例支持的APIG特性”，如确认实例不存在public_key配置可联系技术工程师开启。  aes类型需要实例升级到对应版本，若不存在可联系技术工程师升级。
        :type sign_type: str
        """
        
        

        self._publish_id = None
        self._api_id = None
        self._group_name = None
        self._binding_time = None
        self._env_id = None
        self._env_name = None
        self._api_type = None
        self._api_name = None
        self._id = None
        self._api_remark = None
        self._sign_id = None
        self._sign_name = None
        self._sign_key = None
        self._sign_secret = None
        self._sign_type = None
        self.discriminator = None

        if publish_id is not None:
            self.publish_id = publish_id
        if api_id is not None:
            self.api_id = api_id
        if group_name is not None:
            self.group_name = group_name
        if binding_time is not None:
            self.binding_time = binding_time
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if api_type is not None:
            self.api_type = api_type
        if api_name is not None:
            self.api_name = api_name
        if id is not None:
            self.id = id
        if api_remark is not None:
            self.api_remark = api_remark
        if sign_id is not None:
            self.sign_id = sign_id
        if sign_name is not None:
            self.sign_name = sign_name
        if sign_key is not None:
            self.sign_key = sign_key
        if sign_secret is not None:
            self.sign_secret = sign_secret
        if sign_type is not None:
            self.sign_type = sign_type

    @property
    def publish_id(self):
        """Gets the publish_id of this SignApiBindingInfo.

        API的发布编号

        :return: The publish_id of this SignApiBindingInfo.
        :rtype: str
        """
        return self._publish_id

    @publish_id.setter
    def publish_id(self, publish_id):
        """Sets the publish_id of this SignApiBindingInfo.

        API的发布编号

        :param publish_id: The publish_id of this SignApiBindingInfo.
        :type publish_id: str
        """
        self._publish_id = publish_id

    @property
    def api_id(self):
        """Gets the api_id of this SignApiBindingInfo.

        API编号

        :return: The api_id of this SignApiBindingInfo.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this SignApiBindingInfo.

        API编号

        :param api_id: The api_id of this SignApiBindingInfo.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def group_name(self):
        """Gets the group_name of this SignApiBindingInfo.

        API所属分组的名称

        :return: The group_name of this SignApiBindingInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this SignApiBindingInfo.

        API所属分组的名称

        :param group_name: The group_name of this SignApiBindingInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def binding_time(self):
        """Gets the binding_time of this SignApiBindingInfo.

        绑定时间

        :return: The binding_time of this SignApiBindingInfo.
        :rtype: datetime
        """
        return self._binding_time

    @binding_time.setter
    def binding_time(self, binding_time):
        """Sets the binding_time of this SignApiBindingInfo.

        绑定时间

        :param binding_time: The binding_time of this SignApiBindingInfo.
        :type binding_time: datetime
        """
        self._binding_time = binding_time

    @property
    def env_id(self):
        """Gets the env_id of this SignApiBindingInfo.

        API所属环境的编号

        :return: The env_id of this SignApiBindingInfo.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this SignApiBindingInfo.

        API所属环境的编号

        :param env_id: The env_id of this SignApiBindingInfo.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        """Gets the env_name of this SignApiBindingInfo.

        API所属环境的名称

        :return: The env_name of this SignApiBindingInfo.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this SignApiBindingInfo.

        API所属环境的名称

        :param env_name: The env_name of this SignApiBindingInfo.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def api_type(self):
        """Gets the api_type of this SignApiBindingInfo.

        API类型

        :return: The api_type of this SignApiBindingInfo.
        :rtype: int
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        """Sets the api_type of this SignApiBindingInfo.

        API类型

        :param api_type: The api_type of this SignApiBindingInfo.
        :type api_type: int
        """
        self._api_type = api_type

    @property
    def api_name(self):
        """Gets the api_name of this SignApiBindingInfo.

        API名称

        :return: The api_name of this SignApiBindingInfo.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this SignApiBindingInfo.

        API名称

        :param api_name: The api_name of this SignApiBindingInfo.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def id(self):
        """Gets the id of this SignApiBindingInfo.

        绑定关系的ID

        :return: The id of this SignApiBindingInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SignApiBindingInfo.

        绑定关系的ID

        :param id: The id of this SignApiBindingInfo.
        :type id: str
        """
        self._id = id

    @property
    def api_remark(self):
        """Gets the api_remark of this SignApiBindingInfo.

        API描述

        :return: The api_remark of this SignApiBindingInfo.
        :rtype: str
        """
        return self._api_remark

    @api_remark.setter
    def api_remark(self, api_remark):
        """Sets the api_remark of this SignApiBindingInfo.

        API描述

        :param api_remark: The api_remark of this SignApiBindingInfo.
        :type api_remark: str
        """
        self._api_remark = api_remark

    @property
    def sign_id(self):
        """Gets the sign_id of this SignApiBindingInfo.

        签名密钥的编号

        :return: The sign_id of this SignApiBindingInfo.
        :rtype: str
        """
        return self._sign_id

    @sign_id.setter
    def sign_id(self, sign_id):
        """Sets the sign_id of this SignApiBindingInfo.

        签名密钥的编号

        :param sign_id: The sign_id of this SignApiBindingInfo.
        :type sign_id: str
        """
        self._sign_id = sign_id

    @property
    def sign_name(self):
        """Gets the sign_name of this SignApiBindingInfo.

        签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The sign_name of this SignApiBindingInfo.
        :rtype: str
        """
        return self._sign_name

    @sign_name.setter
    def sign_name(self, sign_name):
        """Sets the sign_name of this SignApiBindingInfo.

        签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param sign_name: The sign_name of this SignApiBindingInfo.
        :type sign_name: str
        """
        self._sign_name = sign_name

    @property
    def sign_key(self):
        """Gets the sign_key of this SignApiBindingInfo.

        签名密钥的key。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母或数字开头，8 ~ 32字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母开头，4 ~ 32字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，+，/，=，可以英文字母，数字，+，/开头，8 ~ 512字符。未填写时后台自动生成。 - aes类型的签名秘钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，签名算法为aes-128-cfb时为16个字符，签名算法为aes-256-cfb时为32个字符。未填写时后台自动生成。

        :return: The sign_key of this SignApiBindingInfo.
        :rtype: str
        """
        return self._sign_key

    @sign_key.setter
    def sign_key(self, sign_key):
        """Sets the sign_key of this SignApiBindingInfo.

        签名密钥的key。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母或数字开头，8 ~ 32字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，且只能以英文字母开头，4 ~ 32字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，+，/，=，可以英文字母，数字，+，/开头，8 ~ 512字符。未填写时后台自动生成。 - aes类型的签名秘钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，签名算法为aes-128-cfb时为16个字符，签名算法为aes-256-cfb时为32个字符。未填写时后台自动生成。

        :param sign_key: The sign_key of this SignApiBindingInfo.
        :type sign_key: str
        """
        self._sign_key = sign_key

    @property
    def sign_secret(self):
        """Gets the sign_secret of this SignApiBindingInfo.

        签名密钥的密钥。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，16 ~ 64字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，8 ~ 64字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，15 ~ 2048字符。未填写时后台自动生成。 - aes类型签名秘钥使用的向量：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，16个字符。未填写时后台自动生成。

        :return: The sign_secret of this SignApiBindingInfo.
        :rtype: str
        """
        return self._sign_secret

    @sign_secret.setter
    def sign_secret(self, sign_secret):
        """Sets the sign_secret of this SignApiBindingInfo.

        签名密钥的密钥。 - hmac类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，16 ~ 64字符。未填写时后台自动生成。 - basic类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母或数字开头，8 ~ 64字符。未填写时后台自动生成。 - public_key类型的签名密钥key：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，15 ~ 2048字符。未填写时后台自动生成。 - aes类型签名秘钥使用的向量：支持英文，数字，下划线，中划线，!，@，#，$，%，+，/，=，可以英文字母，数字，+，/开头，16个字符。未填写时后台自动生成。

        :param sign_secret: The sign_secret of this SignApiBindingInfo.
        :type sign_secret: str
        """
        self._sign_secret = sign_secret

    @property
    def sign_type(self):
        """Gets the sign_type of this SignApiBindingInfo.

        签名密钥类型： - hmac - basic - public_key - aes  basic类型需要实例升级到对应版本，若不存在可联系技术工程师升级。  public_key类型开启实例配置public_key才可使用，实例特性配置详情请参考“附录 > 实例支持的APIG特性”，如确认实例不存在public_key配置可联系技术工程师开启。  aes类型需要实例升级到对应版本，若不存在可联系技术工程师升级。

        :return: The sign_type of this SignApiBindingInfo.
        :rtype: str
        """
        return self._sign_type

    @sign_type.setter
    def sign_type(self, sign_type):
        """Sets the sign_type of this SignApiBindingInfo.

        签名密钥类型： - hmac - basic - public_key - aes  basic类型需要实例升级到对应版本，若不存在可联系技术工程师升级。  public_key类型开启实例配置public_key才可使用，实例特性配置详情请参考“附录 > 实例支持的APIG特性”，如确认实例不存在public_key配置可联系技术工程师开启。  aes类型需要实例升级到对应版本，若不存在可联系技术工程师升级。

        :param sign_type: The sign_type of this SignApiBindingInfo.
        :type sign_type: str
        """
        self._sign_type = sign_type

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
        if not isinstance(other, SignApiBindingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
