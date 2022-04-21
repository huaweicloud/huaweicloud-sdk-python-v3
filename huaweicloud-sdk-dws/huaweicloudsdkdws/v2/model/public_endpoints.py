# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicEndpoints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'public_connect_info': 'str',
        'jdbc_url': 'str'
    }

    attribute_map = {
        'public_connect_info': 'public_connect_info',
        'jdbc_url': 'jdbc_url'
    }

    def __init__(self, public_connect_info=None, jdbc_url=None):
        """PublicEndpoints

        The model defined in huaweicloud sdk

        :param public_connect_info: 公网连接信息
        :type public_connect_info: str
        :param jdbc_url: 公网JDBC URL，默认格式如下： jdbc:postgresql://&lt;public_connect_info&gt;/&lt;YOUR_DATABASE_name&gt;
        :type jdbc_url: str
        """
        
        

        self._public_connect_info = None
        self._jdbc_url = None
        self.discriminator = None

        if public_connect_info is not None:
            self.public_connect_info = public_connect_info
        if jdbc_url is not None:
            self.jdbc_url = jdbc_url

    @property
    def public_connect_info(self):
        """Gets the public_connect_info of this PublicEndpoints.

        公网连接信息

        :return: The public_connect_info of this PublicEndpoints.
        :rtype: str
        """
        return self._public_connect_info

    @public_connect_info.setter
    def public_connect_info(self, public_connect_info):
        """Sets the public_connect_info of this PublicEndpoints.

        公网连接信息

        :param public_connect_info: The public_connect_info of this PublicEndpoints.
        :type public_connect_info: str
        """
        self._public_connect_info = public_connect_info

    @property
    def jdbc_url(self):
        """Gets the jdbc_url of this PublicEndpoints.

        公网JDBC URL，默认格式如下： jdbc:postgresql://<public_connect_info>/<YOUR_DATABASE_name>

        :return: The jdbc_url of this PublicEndpoints.
        :rtype: str
        """
        return self._jdbc_url

    @jdbc_url.setter
    def jdbc_url(self, jdbc_url):
        """Sets the jdbc_url of this PublicEndpoints.

        公网JDBC URL，默认格式如下： jdbc:postgresql://<public_connect_info>/<YOUR_DATABASE_name>

        :param jdbc_url: The jdbc_url of this PublicEndpoints.
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
        if not isinstance(other, PublicEndpoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
