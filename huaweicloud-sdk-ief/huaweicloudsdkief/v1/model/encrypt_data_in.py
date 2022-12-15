# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptDataIn:

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
        'description': 'str',
        'config': 'list[EncryptDataItem]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'config': 'config'
    }

    def __init__(self, name=None, description=None, config=None):
        """EncryptDataIn

        The model defined in huaweicloud sdk

        :param name: 加密数据名称，小写英文字母、数字、中划线，以小写字母或数字开头，最大长度为64个字符，不能为空
        :type name: str
        :param description: 加密数据描述
        :type description: str
        :param config: 加密数据项配置
        :type config: list[:class:`huaweicloudsdkief.v1.EncryptDataItem`]
        """
        
        

        self._name = None
        self._description = None
        self._config = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.config = config

    @property
    def name(self):
        """Gets the name of this EncryptDataIn.

        加密数据名称，小写英文字母、数字、中划线，以小写字母或数字开头，最大长度为64个字符，不能为空

        :return: The name of this EncryptDataIn.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EncryptDataIn.

        加密数据名称，小写英文字母、数字、中划线，以小写字母或数字开头，最大长度为64个字符，不能为空

        :param name: The name of this EncryptDataIn.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EncryptDataIn.

        加密数据描述

        :return: The description of this EncryptDataIn.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EncryptDataIn.

        加密数据描述

        :param description: The description of this EncryptDataIn.
        :type description: str
        """
        self._description = description

    @property
    def config(self):
        """Gets the config of this EncryptDataIn.

        加密数据项配置

        :return: The config of this EncryptDataIn.
        :rtype: list[:class:`huaweicloudsdkief.v1.EncryptDataItem`]
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this EncryptDataIn.

        加密数据项配置

        :param config: The config of this EncryptDataIn.
        :type config: list[:class:`huaweicloudsdkief.v1.EncryptDataItem`]
        """
        self._config = config

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
        if not isinstance(other, EncryptDataIn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
