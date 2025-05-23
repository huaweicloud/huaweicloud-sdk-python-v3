# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAntileakageRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'category': 'str',
        'contents': 'list[str]',
        'action': 'CreateAntileakageRuleRequestBodyAction',
        'description': 'str'
    }

    attribute_map = {
        'url': 'url',
        'category': 'category',
        'contents': 'contents',
        'action': 'action',
        'description': 'description'
    }

    def __init__(self, url=None, category=None, contents=None, action=None, description=None):
        r"""CreateAntileakageRuleRequestBody

        The model defined in huaweicloud sdk

        :param url: 规则应用的url
        :type url: str
        :param category: 类别（响应码：code，敏感信息：sensitive）
        :type category: str
        :param contents: 规则内容（http状态码：400 、401、402 、 403 、404 、 405 、500 、501 、502 、503、 504 、507；手机：phone、身份证号：id_card、邮箱：email）
        :type contents: list[str]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.CreateAntileakageRuleRequestBodyAction`
        :param description: 规则描述
        :type description: str
        """
        
        

        self._url = None
        self._category = None
        self._contents = None
        self._action = None
        self._description = None
        self.discriminator = None

        self.url = url
        self.category = category
        self.contents = contents
        if action is not None:
            self.action = action
        if description is not None:
            self.description = description

    @property
    def url(self):
        r"""Gets the url of this CreateAntileakageRuleRequestBody.

        规则应用的url

        :return: The url of this CreateAntileakageRuleRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateAntileakageRuleRequestBody.

        规则应用的url

        :param url: The url of this CreateAntileakageRuleRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def category(self):
        r"""Gets the category of this CreateAntileakageRuleRequestBody.

        类别（响应码：code，敏感信息：sensitive）

        :return: The category of this CreateAntileakageRuleRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateAntileakageRuleRequestBody.

        类别（响应码：code，敏感信息：sensitive）

        :param category: The category of this CreateAntileakageRuleRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def contents(self):
        r"""Gets the contents of this CreateAntileakageRuleRequestBody.

        规则内容（http状态码：400 、401、402 、 403 、404 、 405 、500 、501 、502 、503、 504 、507；手机：phone、身份证号：id_card、邮箱：email）

        :return: The contents of this CreateAntileakageRuleRequestBody.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this CreateAntileakageRuleRequestBody.

        规则内容（http状态码：400 、401、402 、 403 、404 、 405 、500 、501 、502 、503、 504 、507；手机：phone、身份证号：id_card、邮箱：email）

        :param contents: The contents of this CreateAntileakageRuleRequestBody.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def action(self):
        r"""Gets the action of this CreateAntileakageRuleRequestBody.

        :return: The action of this CreateAntileakageRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateAntileakageRuleRequestBodyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateAntileakageRuleRequestBody.

        :param action: The action of this CreateAntileakageRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.CreateAntileakageRuleRequestBodyAction`
        """
        self._action = action

    @property
    def description(self):
        r"""Gets the description of this CreateAntileakageRuleRequestBody.

        规则描述

        :return: The description of this CreateAntileakageRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAntileakageRuleRequestBody.

        规则描述

        :param description: The description of this CreateAntileakageRuleRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateAntileakageRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
