# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Creator:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'domain_id': 'str',
        'user_name': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'domain_id': 'domain_id',
        'user_name': 'user_name',
        'user_id': 'user_id'
    }

    def __init__(self, domain_name=None, domain_id=None, user_name=None, user_id=None):
        r"""Creator

        The model defined in huaweicloud sdk

        :param domain_name: **参数解释**：租户名称。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度为1~64个字符。 
        :type domain_name: str
        :param domain_id: **参数解释**：租户ID。 **取值范围**：支持英文字母、数字及中划线，长度为1~64个字符。 
        :type domain_id: str
        :param user_name: **参数解释**：用户名称。 **取值范围**：支持英文字母、数字、下划线的组合，长度为1~64个字符。 
        :type user_name: str
        :param user_id: **参数解释**：用户ID。 **取值范围**：支持英文字母、数字及中划线，长度为1~64个字符。 
        :type user_id: str
        """
        
        

        self._domain_name = None
        self._domain_id = None
        self._user_name = None
        self._user_id = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if domain_id is not None:
            self.domain_id = domain_id
        if user_name is not None:
            self.user_name = user_name
        if user_id is not None:
            self.user_id = user_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this Creator.

        **参数解释**：租户名称。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度为1~64个字符。 

        :return: The domain_name of this Creator.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this Creator.

        **参数解释**：租户名称。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度为1~64个字符。 

        :param domain_name: The domain_name of this Creator.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this Creator.

        **参数解释**：租户ID。 **取值范围**：支持英文字母、数字及中划线，长度为1~64个字符。 

        :return: The domain_id of this Creator.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this Creator.

        **参数解释**：租户ID。 **取值范围**：支持英文字母、数字及中划线，长度为1~64个字符。 

        :param domain_id: The domain_id of this Creator.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def user_name(self):
        r"""Gets the user_name of this Creator.

        **参数解释**：用户名称。 **取值范围**：支持英文字母、数字、下划线的组合，长度为1~64个字符。 

        :return: The user_name of this Creator.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this Creator.

        **参数解释**：用户名称。 **取值范围**：支持英文字母、数字、下划线的组合，长度为1~64个字符。 

        :param user_name: The user_name of this Creator.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_id(self):
        r"""Gets the user_id of this Creator.

        **参数解释**：用户ID。 **取值范围**：支持英文字母、数字及中划线，长度为1~64个字符。 

        :return: The user_id of this Creator.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this Creator.

        **参数解释**：用户ID。 **取值范围**：支持英文字母、数字及中划线，长度为1~64个字符。 

        :param user_id: The user_id of this Creator.
        :type user_id: str
        """
        self._user_id = user_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Creator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
