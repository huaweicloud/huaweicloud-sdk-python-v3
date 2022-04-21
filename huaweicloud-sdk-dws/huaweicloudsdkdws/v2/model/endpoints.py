# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Endpoints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'connect_info': 'str',
        'jdbc_url': 'str'
    }

    attribute_map = {
        'connect_info': 'connect_info',
        'jdbc_url': 'jdbc_url'
    }

    def __init__(self, connect_info=None, jdbc_url=None):
        """Endpoints

        The model defined in huaweicloud sdk

        :param connect_info: 内网连接信息。
        :type connect_info: str
        :param jdbc_url: 内网JDBC URL，默认格式如下： jdbc:postgresql://&lt;connect_info&gt;/&lt;YOUR_DATABASE_NAME&gt;
        :type jdbc_url: str
        """
        
        

        self._connect_info = None
        self._jdbc_url = None
        self.discriminator = None

        if connect_info is not None:
            self.connect_info = connect_info
        if jdbc_url is not None:
            self.jdbc_url = jdbc_url

    @property
    def connect_info(self):
        """Gets the connect_info of this Endpoints.

        内网连接信息。

        :return: The connect_info of this Endpoints.
        :rtype: str
        """
        return self._connect_info

    @connect_info.setter
    def connect_info(self, connect_info):
        """Sets the connect_info of this Endpoints.

        内网连接信息。

        :param connect_info: The connect_info of this Endpoints.
        :type connect_info: str
        """
        self._connect_info = connect_info

    @property
    def jdbc_url(self):
        """Gets the jdbc_url of this Endpoints.

        内网JDBC URL，默认格式如下： jdbc:postgresql://<connect_info>/<YOUR_DATABASE_NAME>

        :return: The jdbc_url of this Endpoints.
        :rtype: str
        """
        return self._jdbc_url

    @jdbc_url.setter
    def jdbc_url(self, jdbc_url):
        """Sets the jdbc_url of this Endpoints.

        内网JDBC URL，默认格式如下： jdbc:postgresql://<connect_info>/<YOUR_DATABASE_NAME>

        :param jdbc_url: The jdbc_url of this Endpoints.
        :type jdbc_url: str
        """
        self._jdbc_url = jdbc_url

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
        if not isinstance(other, Endpoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
