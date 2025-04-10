# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpRiverConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'site_name': 'str',
        'connect_timeout': 'int',
        'read_timeout': 'int',
        'send_timeout': 'int'
    }

    attribute_map = {
        'site_id': 'site_id',
        'site_name': 'site_name',
        'connect_timeout': 'connect_timeout',
        'read_timeout': 'read_timeout',
        'send_timeout': 'send_timeout'
    }

    def __init__(self, site_id=None, site_name=None, connect_timeout=None, read_timeout=None, send_timeout=None):
        r"""HttpRiverConfig

        The model defined in huaweicloud sdk

        :param site_id: 瑞数站点ID
        :type site_id: str
        :param site_name: 瑞数站点名称
        :type site_name: str
        :param connect_timeout: 连接超时（毫秒）
        :type connect_timeout: int
        :param read_timeout: 读超时（毫秒）
        :type read_timeout: int
        :param send_timeout: 写超时（毫秒）
        :type send_timeout: int
        """
        
        

        self._site_id = None
        self._site_name = None
        self._connect_timeout = None
        self._read_timeout = None
        self._send_timeout = None
        self.discriminator = None

        if site_id is not None:
            self.site_id = site_id
        if site_name is not None:
            self.site_name = site_name
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if read_timeout is not None:
            self.read_timeout = read_timeout
        if send_timeout is not None:
            self.send_timeout = send_timeout

    @property
    def site_id(self):
        r"""Gets the site_id of this HttpRiverConfig.

        瑞数站点ID

        :return: The site_id of this HttpRiverConfig.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this HttpRiverConfig.

        瑞数站点ID

        :param site_id: The site_id of this HttpRiverConfig.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def site_name(self):
        r"""Gets the site_name of this HttpRiverConfig.

        瑞数站点名称

        :return: The site_name of this HttpRiverConfig.
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        r"""Sets the site_name of this HttpRiverConfig.

        瑞数站点名称

        :param site_name: The site_name of this HttpRiverConfig.
        :type site_name: str
        """
        self._site_name = site_name

    @property
    def connect_timeout(self):
        r"""Gets the connect_timeout of this HttpRiverConfig.

        连接超时（毫秒）

        :return: The connect_timeout of this HttpRiverConfig.
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        r"""Sets the connect_timeout of this HttpRiverConfig.

        连接超时（毫秒）

        :param connect_timeout: The connect_timeout of this HttpRiverConfig.
        :type connect_timeout: int
        """
        self._connect_timeout = connect_timeout

    @property
    def read_timeout(self):
        r"""Gets the read_timeout of this HttpRiverConfig.

        读超时（毫秒）

        :return: The read_timeout of this HttpRiverConfig.
        :rtype: int
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        r"""Sets the read_timeout of this HttpRiverConfig.

        读超时（毫秒）

        :param read_timeout: The read_timeout of this HttpRiverConfig.
        :type read_timeout: int
        """
        self._read_timeout = read_timeout

    @property
    def send_timeout(self):
        r"""Gets the send_timeout of this HttpRiverConfig.

        写超时（毫秒）

        :return: The send_timeout of this HttpRiverConfig.
        :rtype: int
        """
        return self._send_timeout

    @send_timeout.setter
    def send_timeout(self, send_timeout):
        r"""Sets the send_timeout of this HttpRiverConfig.

        写超时（毫秒）

        :param send_timeout: The send_timeout of this HttpRiverConfig.
        :type send_timeout: int
        """
        self._send_timeout = send_timeout

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
        if not isinstance(other, HttpRiverConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
