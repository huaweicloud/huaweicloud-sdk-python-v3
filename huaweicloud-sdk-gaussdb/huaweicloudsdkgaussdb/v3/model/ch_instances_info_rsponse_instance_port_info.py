# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChInstancesInfoRsponseInstancePortInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tep_port': 'int',
        'http_port': 'int',
        'mysql_port': 'int',
        'https_port': 'int',
        'tep_secure_port': 'int'
    }

    attribute_map = {
        'tep_port': 'tep_port',
        'http_port': 'http_port',
        'mysql_port': 'mysql_port',
        'https_port': 'https_port',
        'tep_secure_port': 'tep_secure_port'
    }

    def __init__(self, tep_port=None, http_port=None, mysql_port=None, https_port=None, tep_secure_port=None):
        """ChInstancesInfoRsponseInstancePortInfo

        The model defined in huaweicloud sdk

        :param tep_port: tep端口。取值范围：0~65535。
        :type tep_port: int
        :param http_port: http端口。取值范围：0~65535。
        :type http_port: int
        :param mysql_port: MySql端口号。取值范围：0~65535。
        :type mysql_port: int
        :param https_port: https端口号。取值范围：0~65535。
        :type https_port: int
        :param tep_secure_port: tep安全端口。取值范围：0~65535。
        :type tep_secure_port: int
        """
        
        

        self._tep_port = None
        self._http_port = None
        self._mysql_port = None
        self._https_port = None
        self._tep_secure_port = None
        self.discriminator = None

        self.tep_port = tep_port
        self.http_port = http_port
        self.mysql_port = mysql_port
        self.https_port = https_port
        self.tep_secure_port = tep_secure_port

    @property
    def tep_port(self):
        """Gets the tep_port of this ChInstancesInfoRsponseInstancePortInfo.

        tep端口。取值范围：0~65535。

        :return: The tep_port of this ChInstancesInfoRsponseInstancePortInfo.
        :rtype: int
        """
        return self._tep_port

    @tep_port.setter
    def tep_port(self, tep_port):
        """Sets the tep_port of this ChInstancesInfoRsponseInstancePortInfo.

        tep端口。取值范围：0~65535。

        :param tep_port: The tep_port of this ChInstancesInfoRsponseInstancePortInfo.
        :type tep_port: int
        """
        self._tep_port = tep_port

    @property
    def http_port(self):
        """Gets the http_port of this ChInstancesInfoRsponseInstancePortInfo.

        http端口。取值范围：0~65535。

        :return: The http_port of this ChInstancesInfoRsponseInstancePortInfo.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this ChInstancesInfoRsponseInstancePortInfo.

        http端口。取值范围：0~65535。

        :param http_port: The http_port of this ChInstancesInfoRsponseInstancePortInfo.
        :type http_port: int
        """
        self._http_port = http_port

    @property
    def mysql_port(self):
        """Gets the mysql_port of this ChInstancesInfoRsponseInstancePortInfo.

        MySql端口号。取值范围：0~65535。

        :return: The mysql_port of this ChInstancesInfoRsponseInstancePortInfo.
        :rtype: int
        """
        return self._mysql_port

    @mysql_port.setter
    def mysql_port(self, mysql_port):
        """Sets the mysql_port of this ChInstancesInfoRsponseInstancePortInfo.

        MySql端口号。取值范围：0~65535。

        :param mysql_port: The mysql_port of this ChInstancesInfoRsponseInstancePortInfo.
        :type mysql_port: int
        """
        self._mysql_port = mysql_port

    @property
    def https_port(self):
        """Gets the https_port of this ChInstancesInfoRsponseInstancePortInfo.

        https端口号。取值范围：0~65535。

        :return: The https_port of this ChInstancesInfoRsponseInstancePortInfo.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this ChInstancesInfoRsponseInstancePortInfo.

        https端口号。取值范围：0~65535。

        :param https_port: The https_port of this ChInstancesInfoRsponseInstancePortInfo.
        :type https_port: int
        """
        self._https_port = https_port

    @property
    def tep_secure_port(self):
        """Gets the tep_secure_port of this ChInstancesInfoRsponseInstancePortInfo.

        tep安全端口。取值范围：0~65535。

        :return: The tep_secure_port of this ChInstancesInfoRsponseInstancePortInfo.
        :rtype: int
        """
        return self._tep_secure_port

    @tep_secure_port.setter
    def tep_secure_port(self, tep_secure_port):
        """Sets the tep_secure_port of this ChInstancesInfoRsponseInstancePortInfo.

        tep安全端口。取值范围：0~65535。

        :param tep_secure_port: The tep_secure_port of this ChInstancesInfoRsponseInstancePortInfo.
        :type tep_secure_port: int
        """
        self._tep_secure_port = tep_secure_port

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
        if not isinstance(other, ChInstancesInfoRsponseInstancePortInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
