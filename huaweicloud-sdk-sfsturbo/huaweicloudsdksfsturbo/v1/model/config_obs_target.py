# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigObsTarget:

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
        'type': 'str',
        'url': 'str',
        'bucket': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'url': 'url',
        'bucket': 'bucket'
    }

    def __init__(self, name=None, type=None, url=None, bucket=None):
        """ConfigObsTarget

        The model defined in huaweicloud sdk

        :param name: obs 配置名
        :type name: str
        :param type: obs 配置协议类型
        :type type: str
        :param url: obs 桶 endpoint
        :type url: str
        :param bucket: obs 桶名
        :type bucket: str
        """
        
        

        self._name = None
        self._type = None
        self._url = None
        self._bucket = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.url = url
        self.bucket = bucket

    @property
    def name(self):
        """Gets the name of this ConfigObsTarget.

        obs 配置名

        :return: The name of this ConfigObsTarget.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigObsTarget.

        obs 配置名

        :param name: The name of this ConfigObsTarget.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ConfigObsTarget.

        obs 配置协议类型

        :return: The type of this ConfigObsTarget.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConfigObsTarget.

        obs 配置协议类型

        :param type: The type of this ConfigObsTarget.
        :type type: str
        """
        self._type = type

    @property
    def url(self):
        """Gets the url of this ConfigObsTarget.

        obs 桶 endpoint

        :return: The url of this ConfigObsTarget.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ConfigObsTarget.

        obs 桶 endpoint

        :param url: The url of this ConfigObsTarget.
        :type url: str
        """
        self._url = url

    @property
    def bucket(self):
        """Gets the bucket of this ConfigObsTarget.

        obs 桶名

        :return: The bucket of this ConfigObsTarget.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ConfigObsTarget.

        obs 桶名

        :param bucket: The bucket of this ConfigObsTarget.
        :type bucket: str
        """
        self._bucket = bucket

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
        if not isinstance(other, ConfigObsTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
