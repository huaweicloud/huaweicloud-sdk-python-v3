# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DBSInstanceHostInfoResult:

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
        'host': 'str',
        'host_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'host': 'host',
        'host_name': 'host_name'
    }

    def __init__(self, id=None, host=None, host_name=None):
        """DBSInstanceHostInfoResult

        The model defined in huaweicloud sdk

        :param id: host  id
        :type id: str
        :param host: host地址
        :type host: str
        :param host_name: host 名称
        :type host_name: str
        """
        
        

        self._id = None
        self._host = None
        self._host_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if host is not None:
            self.host = host
        if host_name is not None:
            self.host_name = host_name

    @property
    def id(self):
        """Gets the id of this DBSInstanceHostInfoResult.

        host  id

        :return: The id of this DBSInstanceHostInfoResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DBSInstanceHostInfoResult.

        host  id

        :param id: The id of this DBSInstanceHostInfoResult.
        :type id: str
        """
        self._id = id

    @property
    def host(self):
        """Gets the host of this DBSInstanceHostInfoResult.

        host地址

        :return: The host of this DBSInstanceHostInfoResult.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DBSInstanceHostInfoResult.

        host地址

        :param host: The host of this DBSInstanceHostInfoResult.
        :type host: str
        """
        self._host = host

    @property
    def host_name(self):
        """Gets the host_name of this DBSInstanceHostInfoResult.

        host 名称

        :return: The host_name of this DBSInstanceHostInfoResult.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this DBSInstanceHostInfoResult.

        host 名称

        :param host_name: The host_name of this DBSInstanceHostInfoResult.
        :type host_name: str
        """
        self._host_name = host_name

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
        if not isinstance(other, DBSInstanceHostInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
