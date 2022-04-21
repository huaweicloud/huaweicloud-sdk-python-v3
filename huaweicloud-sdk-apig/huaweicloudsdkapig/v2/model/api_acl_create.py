# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiAclCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'acl_name': 'str',
        'acl_type': 'str',
        'acl_value': 'str',
        'entity_type': 'str'
    }

    attribute_map = {
        'acl_name': 'acl_name',
        'acl_type': 'acl_type',
        'acl_value': 'acl_value',
        'entity_type': 'entity_type'
    }

    def __init__(self, acl_name=None, acl_type=None, acl_value=None, entity_type=None):
        """ApiAclCreate

        The model defined in huaweicloud sdk

        :param acl_name: ACL策略名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 &gt; 中文字符必须为UTF-8或者unicode编码。
        :type acl_name: str
        :param acl_type: 类型 -  PERMIT (白名单类型) -  DENY (黑名单类型)
        :type acl_type: str
        :param acl_value: ACL策略值，支持一个或多个值，使用英文半角逗号分隔
        :type acl_value: str
        :param entity_type: 对象类型： - IP - DOMAIN
        :type entity_type: str
        """
        
        

        self._acl_name = None
        self._acl_type = None
        self._acl_value = None
        self._entity_type = None
        self.discriminator = None

        self.acl_name = acl_name
        self.acl_type = acl_type
        self.acl_value = acl_value
        self.entity_type = entity_type

    @property
    def acl_name(self):
        """Gets the acl_name of this ApiAclCreate.

        ACL策略名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The acl_name of this ApiAclCreate.
        :rtype: str
        """
        return self._acl_name

    @acl_name.setter
    def acl_name(self, acl_name):
        """Sets the acl_name of this ApiAclCreate.

        ACL策略名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param acl_name: The acl_name of this ApiAclCreate.
        :type acl_name: str
        """
        self._acl_name = acl_name

    @property
    def acl_type(self):
        """Gets the acl_type of this ApiAclCreate.

        类型 -  PERMIT (白名单类型) -  DENY (黑名单类型)

        :return: The acl_type of this ApiAclCreate.
        :rtype: str
        """
        return self._acl_type

    @acl_type.setter
    def acl_type(self, acl_type):
        """Sets the acl_type of this ApiAclCreate.

        类型 -  PERMIT (白名单类型) -  DENY (黑名单类型)

        :param acl_type: The acl_type of this ApiAclCreate.
        :type acl_type: str
        """
        self._acl_type = acl_type

    @property
    def acl_value(self):
        """Gets the acl_value of this ApiAclCreate.

        ACL策略值，支持一个或多个值，使用英文半角逗号分隔

        :return: The acl_value of this ApiAclCreate.
        :rtype: str
        """
        return self._acl_value

    @acl_value.setter
    def acl_value(self, acl_value):
        """Sets the acl_value of this ApiAclCreate.

        ACL策略值，支持一个或多个值，使用英文半角逗号分隔

        :param acl_value: The acl_value of this ApiAclCreate.
        :type acl_value: str
        """
        self._acl_value = acl_value

    @property
    def entity_type(self):
        """Gets the entity_type of this ApiAclCreate.

        对象类型： - IP - DOMAIN

        :return: The entity_type of this ApiAclCreate.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ApiAclCreate.

        对象类型： - IP - DOMAIN

        :param entity_type: The entity_type of this ApiAclCreate.
        :type entity_type: str
        """
        self._entity_type = entity_type

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
        if not isinstance(other, ApiAclCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
