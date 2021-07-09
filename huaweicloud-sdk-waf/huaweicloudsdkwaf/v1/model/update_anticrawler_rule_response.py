# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateAnticrawlerRuleResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'url': 'str',
        'logic': 'int',
        'name': 'str',
        'type': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'logic': 'logic',
        'name': 'name',
        'type': 'type',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, url=None, logic=None, name=None, type=None, timestamp=None):
        """UpdateAnticrawlerRuleResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateAnticrawlerRuleResponse, self).__init__()

        self._id = None
        self._url = None
        self._logic = None
        self._name = None
        self._type = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if logic is not None:
            self.logic = logic
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this UpdateAnticrawlerRuleResponse.

        规则id

        :return: The id of this UpdateAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateAnticrawlerRuleResponse.

        规则id

        :param id: The id of this UpdateAnticrawlerRuleResponse.
        :type: str
        """
        self._id = id

    @property
    def url(self):
        """Gets the url of this UpdateAnticrawlerRuleResponse.

        规则应用的url

        :return: The url of this UpdateAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UpdateAnticrawlerRuleResponse.

        规则应用的url

        :param url: The url of this UpdateAnticrawlerRuleResponse.
        :type: str
        """
        self._url = url

    @property
    def logic(self):
        """Gets the logic of this UpdateAnticrawlerRuleResponse.

        规则匹配逻辑

        :return: The logic of this UpdateAnticrawlerRuleResponse.
        :rtype: int
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        """Sets the logic of this UpdateAnticrawlerRuleResponse.

        规则匹配逻辑

        :param logic: The logic of this UpdateAnticrawlerRuleResponse.
        :type: int
        """
        self._logic = logic

    @property
    def name(self):
        """Gets the name of this UpdateAnticrawlerRuleResponse.

        规则名称

        :return: The name of this UpdateAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAnticrawlerRuleResponse.

        规则名称

        :param name: The name of this UpdateAnticrawlerRuleResponse.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this UpdateAnticrawlerRuleResponse.

        反爬虫类型，指定防护：anticrawler_specific_url 例外防护：anticrawler_except_url

        :return: The type of this UpdateAnticrawlerRuleResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateAnticrawlerRuleResponse.

        反爬虫类型，指定防护：anticrawler_specific_url 例外防护：anticrawler_except_url

        :param type: The type of this UpdateAnticrawlerRuleResponse.
        :type: str
        """
        self._type = type

    @property
    def timestamp(self):
        """Gets the timestamp of this UpdateAnticrawlerRuleResponse.

        创建规则时间戳

        :return: The timestamp of this UpdateAnticrawlerRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpdateAnticrawlerRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this UpdateAnticrawlerRuleResponse.
        :type: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, UpdateAnticrawlerRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
