# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppReq:

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
        'remark': 'str',
        'key': 'str',
        'secret': 'str',
        'favorite': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'remark': 'remark',
        'key': 'key',
        'secret': 'secret',
        'favorite': 'favorite'
    }

    def __init__(self, name=None, remark=None, key=None, secret=None, favorite=None):
        """CreateAppReq

        The model defined in huaweicloud sdk

        :param name: 应用名称 - 字符集：支持中文、英文字母、数字、中划线、下划线、点、空格和中英文圆括号 - 约束：实例下唯一
        :type name: str
        :param remark: 应用描述
        :type remark: str
        :param key: 应用认证访问KEY,未提供时随机生成 - 字符集：支持中文、英文字母、数字、中划线、下划线、@号和点，以字母或中文或数字开头 - 约束：实例下唯一
        :type key: str
        :param secret: 应用认证访问SECRET,未提供（字段不存在或值为null）时随机生成 - 字符集：英文字母、数字、！、@、#、$、%、+、&#x3D;、点、中划线、斜线/ - 复杂度：满足大小写字母、数字、特殊字符的复杂度组合，考虑兼容性暂时可不做
        :type secret: str
        :param favorite: 是否收藏应用，收藏的应用会在列表里优先显示
        :type favorite: bool
        """
        
        

        self._name = None
        self._remark = None
        self._key = None
        self._secret = None
        self._favorite = None
        self.discriminator = None

        self.name = name
        if remark is not None:
            self.remark = remark
        if key is not None:
            self.key = key
        if secret is not None:
            self.secret = secret
        if favorite is not None:
            self.favorite = favorite

    @property
    def name(self):
        """Gets the name of this CreateAppReq.

        应用名称 - 字符集：支持中文、英文字母、数字、中划线、下划线、点、空格和中英文圆括号 - 约束：实例下唯一

        :return: The name of this CreateAppReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAppReq.

        应用名称 - 字符集：支持中文、英文字母、数字、中划线、下划线、点、空格和中英文圆括号 - 约束：实例下唯一

        :param name: The name of this CreateAppReq.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this CreateAppReq.

        应用描述

        :return: The remark of this CreateAppReq.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this CreateAppReq.

        应用描述

        :param remark: The remark of this CreateAppReq.
        :type remark: str
        """
        self._remark = remark

    @property
    def key(self):
        """Gets the key of this CreateAppReq.

        应用认证访问KEY,未提供时随机生成 - 字符集：支持中文、英文字母、数字、中划线、下划线、@号和点，以字母或中文或数字开头 - 约束：实例下唯一

        :return: The key of this CreateAppReq.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateAppReq.

        应用认证访问KEY,未提供时随机生成 - 字符集：支持中文、英文字母、数字、中划线、下划线、@号和点，以字母或中文或数字开头 - 约束：实例下唯一

        :param key: The key of this CreateAppReq.
        :type key: str
        """
        self._key = key

    @property
    def secret(self):
        """Gets the secret of this CreateAppReq.

        应用认证访问SECRET,未提供（字段不存在或值为null）时随机生成 - 字符集：英文字母、数字、！、@、#、$、%、+、=、点、中划线、斜线/ - 复杂度：满足大小写字母、数字、特殊字符的复杂度组合，考虑兼容性暂时可不做

        :return: The secret of this CreateAppReq.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this CreateAppReq.

        应用认证访问SECRET,未提供（字段不存在或值为null）时随机生成 - 字符集：英文字母、数字、！、@、#、$、%、+、=、点、中划线、斜线/ - 复杂度：满足大小写字母、数字、特殊字符的复杂度组合，考虑兼容性暂时可不做

        :param secret: The secret of this CreateAppReq.
        :type secret: str
        """
        self._secret = secret

    @property
    def favorite(self):
        """Gets the favorite of this CreateAppReq.

        是否收藏应用，收藏的应用会在列表里优先显示

        :return: The favorite of this CreateAppReq.
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this CreateAppReq.

        是否收藏应用，收藏的应用会在列表里优先显示

        :param favorite: The favorite of this CreateAppReq.
        :type favorite: bool
        """
        self._favorite = favorite

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
        if not isinstance(other, CreateAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
