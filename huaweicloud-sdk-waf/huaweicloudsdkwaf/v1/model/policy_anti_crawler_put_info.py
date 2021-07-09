# coding: utf-8

import re
import six





class PolicyAntiCrawlerPutInfo:


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
        'name': 'str'
    }

    attribute_map = {
        'url': 'url',
        'logic': 'logic',
        'name': 'name'
    }

    def __init__(self, url=None, logic=None, name=None):
        """PolicyAntiCrawlerPutInfo - a model defined in huaweicloud sdk"""
        
        

        self._url = None
        self._logic = None
        self._name = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if logic is not None:
            self.logic = logic
        if name is not None:
            self.name = name

    @property
    def url(self):
        """Gets the url of this PolicyAntiCrawlerPutInfo.

        规则应用的url

        :return: The url of this PolicyAntiCrawlerPutInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PolicyAntiCrawlerPutInfo.

        规则应用的url

        :param url: The url of this PolicyAntiCrawlerPutInfo.
        :type: str
        """
        self._url = url

    @property
    def logic(self):
        """Gets the logic of this PolicyAntiCrawlerPutInfo.

        规则匹配逻辑

        :return: The logic of this PolicyAntiCrawlerPutInfo.
        :rtype: int
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        """Sets the logic of this PolicyAntiCrawlerPutInfo.

        规则匹配逻辑

        :param logic: The logic of this PolicyAntiCrawlerPutInfo.
        :type: int
        """
        self._logic = logic

    @property
    def name(self):
        """Gets the name of this PolicyAntiCrawlerPutInfo.

        规则名称

        :return: The name of this PolicyAntiCrawlerPutInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyAntiCrawlerPutInfo.

        规则名称

        :param name: The name of this PolicyAntiCrawlerPutInfo.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, PolicyAntiCrawlerPutInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
