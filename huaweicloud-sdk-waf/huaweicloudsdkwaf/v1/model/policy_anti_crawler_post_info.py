# coding: utf-8

import re
import six





class PolicyAntiCrawlerPostInfo:


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
        'logic': 'int',
        'name': 'str',
        'type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'url': 'url',
        'logic': 'logic',
        'name': 'name',
        'type': 'type',
        'description': 'description'
    }

    def __init__(self, url=None, logic=None, name=None, type=None, description=None):
        """PolicyAntiCrawlerPostInfo - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._logic = None
        self._name = None
        self._type = None
        self._description = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if logic is not None:
            self.logic = logic
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description

    @property
    def url(self):
        """Gets the url of this PolicyAntiCrawlerPostInfo.

        规则应用的url

        :return: The url of this PolicyAntiCrawlerPostInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PolicyAntiCrawlerPostInfo.

        规则应用的url

        :param url: The url of this PolicyAntiCrawlerPostInfo.
        :type: str
        """
        self._url = url

    @property
    def logic(self):
        """Gets the logic of this PolicyAntiCrawlerPostInfo.

        规则匹配逻辑（说明：1：包含，2：不包含，3：等于，4：不等于，5：前缀为，6：前缀不为，7：后缀为，8：后缀不为）

        :return: The logic of this PolicyAntiCrawlerPostInfo.
        :rtype: int
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        """Sets the logic of this PolicyAntiCrawlerPostInfo.

        规则匹配逻辑（说明：1：包含，2：不包含，3：等于，4：不等于，5：前缀为，6：前缀不为，7：后缀为，8：后缀不为）

        :param logic: The logic of this PolicyAntiCrawlerPostInfo.
        :type: int
        """
        self._logic = logic

    @property
    def name(self):
        """Gets the name of this PolicyAntiCrawlerPostInfo.

        规则名称

        :return: The name of this PolicyAntiCrawlerPostInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyAntiCrawlerPostInfo.

        规则名称

        :param name: The name of this PolicyAntiCrawlerPostInfo.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this PolicyAntiCrawlerPostInfo.

        规则url，默认为anticrawler_specific_url

        :return: The type of this PolicyAntiCrawlerPostInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyAntiCrawlerPostInfo.

        规则url，默认为anticrawler_specific_url

        :param type: The type of this PolicyAntiCrawlerPostInfo.
        :type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this PolicyAntiCrawlerPostInfo.

        规则描述

        :return: The description of this PolicyAntiCrawlerPostInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyAntiCrawlerPostInfo.

        规则描述

        :param description: The description of this PolicyAntiCrawlerPostInfo.
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
        if not isinstance(other, PolicyAntiCrawlerPostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
