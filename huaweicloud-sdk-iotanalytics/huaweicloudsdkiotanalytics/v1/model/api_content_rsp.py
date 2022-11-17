# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiContentRsp:

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
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url'
    }

    def __init__(self, name=None, url=None):
        """ApiContentRsp

        The model defined in huaweicloud sdk

        :param name: 数据源名称
        :type name: str
        :param url: 数据上报url
        :type url: str
        """
        
        

        self._name = None
        self._url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if url is not None:
            self.url = url

    @property
    def name(self):
        """Gets the name of this ApiContentRsp.

        数据源名称

        :return: The name of this ApiContentRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiContentRsp.

        数据源名称

        :param name: The name of this ApiContentRsp.
        :type name: str
        """
        self._name = name

    @property
    def url(self):
        """Gets the url of this ApiContentRsp.

        数据上报url

        :return: The url of this ApiContentRsp.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ApiContentRsp.

        数据上报url

        :param url: The url of this ApiContentRsp.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, ApiContentRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
