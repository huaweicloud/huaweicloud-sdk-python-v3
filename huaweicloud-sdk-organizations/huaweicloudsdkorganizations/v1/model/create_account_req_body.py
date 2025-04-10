# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccountReqBody:

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
        'email': 'str',
        'phone': 'str',
        'agency_name': 'str',
        'description': 'str',
        'tags': 'list[TagDto]'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'phone': 'phone',
        'agency_name': 'agency_name',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, name=None, email=None, phone=None, agency_name=None, description=None, tags=None):
        r"""CreateAccountReqBody

        The model defined in huaweicloud sdk

        :param name: 账号名称
        :type name: str
        :param email: 邮箱
        :type email: str
        :param phone: 手机号码
        :type phone: str
        :param agency_name: 委托名称
        :type agency_name: str
        :param description: 描述信息。
        :type description: str
        :param tags: 要绑定到新创建的账号的标签列表。
        :type tags: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        
        

        self._name = None
        self._email = None
        self._phone = None
        self._agency_name = None
        self._description = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if agency_name is not None:
            self.agency_name = agency_name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateAccountReqBody.

        账号名称

        :return: The name of this CreateAccountReqBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAccountReqBody.

        账号名称

        :param name: The name of this CreateAccountReqBody.
        :type name: str
        """
        self._name = name

    @property
    def email(self):
        r"""Gets the email of this CreateAccountReqBody.

        邮箱

        :return: The email of this CreateAccountReqBody.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this CreateAccountReqBody.

        邮箱

        :param email: The email of this CreateAccountReqBody.
        :type email: str
        """
        self._email = email

    @property
    def phone(self):
        r"""Gets the phone of this CreateAccountReqBody.

        手机号码

        :return: The phone of this CreateAccountReqBody.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this CreateAccountReqBody.

        手机号码

        :param phone: The phone of this CreateAccountReqBody.
        :type phone: str
        """
        self._phone = phone

    @property
    def agency_name(self):
        r"""Gets the agency_name of this CreateAccountReqBody.

        委托名称

        :return: The agency_name of this CreateAccountReqBody.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this CreateAccountReqBody.

        委托名称

        :param agency_name: The agency_name of this CreateAccountReqBody.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def description(self):
        r"""Gets the description of this CreateAccountReqBody.

        描述信息。

        :return: The description of this CreateAccountReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAccountReqBody.

        描述信息。

        :param description: The description of this CreateAccountReqBody.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this CreateAccountReqBody.

        要绑定到新创建的账号的标签列表。

        :return: The tags of this CreateAccountReqBody.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateAccountReqBody.

        要绑定到新创建的账号的标签列表。

        :param tags: The tags of this CreateAccountReqBody.
        :type tags: list[:class:`huaweicloudsdkorganizations.v1.TagDto`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateAccountReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
