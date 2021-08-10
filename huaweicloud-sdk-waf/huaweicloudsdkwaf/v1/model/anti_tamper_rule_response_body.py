# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiTamperRuleResponseBody:


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
        'hostname': 'str',
        'url': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hostname': 'hostname',
        'url': 'url',
        'description': 'description'
    }

    def __init__(self, id=None, hostname=None, url=None, description=None):
        """AntiTamperRuleResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._hostname = None
        self._url = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if hostname is not None:
            self.hostname = hostname
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this AntiTamperRuleResponseBody.

        规则id

        :return: The id of this AntiTamperRuleResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AntiTamperRuleResponseBody.

        规则id

        :param id: The id of this AntiTamperRuleResponseBody.
        :type: str
        """
        self._id = id

    @property
    def hostname(self):
        """Gets the hostname of this AntiTamperRuleResponseBody.

        防篡改的域名

        :return: The hostname of this AntiTamperRuleResponseBody.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this AntiTamperRuleResponseBody.

        防篡改的域名

        :param hostname: The hostname of this AntiTamperRuleResponseBody.
        :type: str
        """
        self._hostname = hostname

    @property
    def url(self):
        """Gets the url of this AntiTamperRuleResponseBody.

        防篡改的url

        :return: The url of this AntiTamperRuleResponseBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AntiTamperRuleResponseBody.

        防篡改的url

        :param url: The url of this AntiTamperRuleResponseBody.
        :type: str
        """
        self._url = url

    @property
    def description(self):
        """Gets the description of this AntiTamperRuleResponseBody.

        创建规则的时间戳

        :return: The description of this AntiTamperRuleResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AntiTamperRuleResponseBody.

        创建规则的时间戳

        :param description: The description of this AntiTamperRuleResponseBody.
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
        if not isinstance(other, AntiTamperRuleResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
