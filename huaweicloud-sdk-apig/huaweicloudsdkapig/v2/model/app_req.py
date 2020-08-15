# coding: utf-8

import pprint
import re

import six





class AppReq:


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
        'app_key': 'str',
        'app_secret': 'str'
    }

    attribute_map = {
        'name': 'name',
        'remark': 'remark',
        'app_key': 'app_key',
        'app_secret': 'app_secret'
    }

    def __init__(self, name=None, remark=None, app_key=None, app_secret=None):
        """AppReq - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._remark = None
        self._app_key = None
        self._app_secret = None
        self.discriminator = None

        self.name = name
        if remark is not None:
            self.remark = remark
        if app_key is not None:
            self.app_key = app_key
        if app_secret is not None:
            self.app_secret = app_secret

    @property
    def name(self):
        """Gets the name of this AppReq.

        APP的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64个字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this AppReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppReq.

        APP的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64个字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this AppReq.
        :type: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this AppReq.

        APP描述。字符长度不能大于255。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this AppReq.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this AppReq.

        APP描述。字符长度不能大于255。 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this AppReq.
        :type: str
        """
        self._remark = remark

    @property
    def app_key(self):
        """Gets the app_key of this AppReq.

        APP的key。支持英文，数字，“_”,“-”,且只能以英文或数字开头，8 ~ 64个字符。 > 只支持部分region。

        :return: The app_key of this AppReq.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this AppReq.

        APP的key。支持英文，数字，“_”,“-”,且只能以英文或数字开头，8 ~ 64个字符。 > 只支持部分region。

        :param app_key: The app_key of this AppReq.
        :type: str
        """
        self._app_key = app_key

    @property
    def app_secret(self):
        """Gets the app_secret of this AppReq.

        密钥。支持英文，数字，“_”,“-”,“_”,“!”,“@”,“#”,“$”,“%”且只能以英文或数字开头，8 ~ 64个字符。 > 只支持部分region。

        :return: The app_secret of this AppReq.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this AppReq.

        密钥。支持英文，数字，“_”,“-”,“_”,“!”,“@”,“#”,“$”,“%”且只能以英文或数字开头，8 ~ 64个字符。 > 只支持部分region。

        :param app_secret: The app_secret of this AppReq.
        :type: str
        """
        self._app_secret = app_secret

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
        if not isinstance(other, AppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
