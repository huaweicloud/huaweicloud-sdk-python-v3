# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateAntileakageRulesResponse(SdkResponse):


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
        'category': 'str',
        'status': 'int',
        'contents': 'list[str]',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'category': 'category',
        'status': 'status',
        'contents': 'contents',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, url=None, category=None, status=None, contents=None, timestamp=None):
        """CreateAntileakageRulesResponse - a model defined in huaweicloud sdk"""
        
        super(CreateAntileakageRulesResponse, self).__init__()

        self._id = None
        self._url = None
        self._category = None
        self._status = None
        self._contents = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if category is not None:
            self.category = category
        if status is not None:
            self.status = status
        if contents is not None:
            self.contents = contents
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this CreateAntileakageRulesResponse.

        规则id

        :return: The id of this CreateAntileakageRulesResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateAntileakageRulesResponse.

        规则id

        :param id: The id of this CreateAntileakageRulesResponse.
        :type: str
        """
        self._id = id

    @property
    def url(self):
        """Gets the url of this CreateAntileakageRulesResponse.

        规则应用的url

        :return: The url of this CreateAntileakageRulesResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateAntileakageRulesResponse.

        规则应用的url

        :param url: The url of this CreateAntileakageRulesResponse.
        :type: str
        """
        self._url = url

    @property
    def category(self):
        """Gets the category of this CreateAntileakageRulesResponse.

        类别

        :return: The category of this CreateAntileakageRulesResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CreateAntileakageRulesResponse.

        类别

        :param category: The category of this CreateAntileakageRulesResponse.
        :type: str
        """
        self._category = category

    @property
    def status(self):
        """Gets the status of this CreateAntileakageRulesResponse.

        状态

        :return: The status of this CreateAntileakageRulesResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateAntileakageRulesResponse.

        状态

        :param status: The status of this CreateAntileakageRulesResponse.
        :type: int
        """
        self._status = status

    @property
    def contents(self):
        """Gets the contents of this CreateAntileakageRulesResponse.

        规则内容

        :return: The contents of this CreateAntileakageRulesResponse.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this CreateAntileakageRulesResponse.

        规则内容

        :param contents: The contents of this CreateAntileakageRulesResponse.
        :type: list[str]
        """
        self._contents = contents

    @property
    def timestamp(self):
        """Gets the timestamp of this CreateAntileakageRulesResponse.

        创建规则时间戳

        :return: The timestamp of this CreateAntileakageRulesResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this CreateAntileakageRulesResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this CreateAntileakageRulesResponse.
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
        if not isinstance(other, CreateAntileakageRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
