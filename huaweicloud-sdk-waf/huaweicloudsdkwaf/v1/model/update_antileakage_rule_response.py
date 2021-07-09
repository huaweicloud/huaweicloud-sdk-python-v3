# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateAntileakageRuleResponse(SdkResponse):


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
        'description': 'str'
    }

    attribute_map = {
        'url': 'url',
        'category': 'category',
        'contents': 'contents',
        'description': 'description'
    }

    def __init__(self, url=None, category=None, contents=None, description=None):
        """UpdateAntileakageRuleResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateAntileakageRuleResponse, self).__init__()

        self._url = None
        self._category = None
        self._contents = None
        self._description = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if category is not None:
            self.category = category
        if contents is not None:
            self.contents = contents
        if description is not None:
            self.description = description

    @property
    def url(self):
        """Gets the url of this UpdateAntileakageRuleResponse.

        规则应用的url

        :return: The url of this UpdateAntileakageRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdateAntileakageRuleResponse.

        规则应用的url

        :param url: The url of this UpdateAntileakageRuleResponse.
        :type: str
        """
        self._url = url

    @property
    def category(self):
        """Gets the category of this UpdateAntileakageRuleResponse.

        类别（响应码：code，敏感信息：sensitive）

        :return: The category of this UpdateAntileakageRuleResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this UpdateAntileakageRuleResponse.

        类别（响应码：code，敏感信息：sensitive）

        :param category: The category of this UpdateAntileakageRuleResponse.
        :type: str
        """
        self._category = category

    @property
    def contents(self):
        """Gets the contents of this UpdateAntileakageRuleResponse.

        规则内容（http状态码、手机：phone、身份证号：id_card、邮箱：email）

        :return: The contents of this UpdateAntileakageRuleResponse.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this UpdateAntileakageRuleResponse.

        规则内容（http状态码、手机：phone、身份证号：id_card、邮箱：email）

        :param contents: The contents of this UpdateAntileakageRuleResponse.
        :type: list[str]
        """
        self._contents = contents

    @property
    def description(self):
        """Gets the description of this UpdateAntileakageRuleResponse.

        规则描述

        :return: The description of this UpdateAntileakageRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAntileakageRuleResponse.

        规则描述

        :param description: The description of this UpdateAntileakageRuleResponse.
        :type: str
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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateAntileakageRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
