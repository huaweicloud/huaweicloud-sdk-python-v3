# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HaResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replication_mode': 'str'
    }

    attribute_map = {
        'replication_mode': 'replication_mode'
    }

    def __init__(self, replication_mode=None):
        """HaResponse

        The model defined in huaweicloud sdk

        :param replication_mode: 备机同步参数。实例主备模式为Ha时有效。 取值： - MySQL为“async”或“semisync”。 - PostgreSQL为“async”或“sync”。 - Microsoft SQL Server为“sync”。
        :type replication_mode: str
        """
        
        

        self._replication_mode = None
        self.discriminator = None

        self.replication_mode = replication_mode

    @property
    def replication_mode(self):
        """Gets the replication_mode of this HaResponse.

        备机同步参数。实例主备模式为Ha时有效。 取值： - MySQL为“async”或“semisync”。 - PostgreSQL为“async”或“sync”。 - Microsoft SQL Server为“sync”。

        :return: The replication_mode of this HaResponse.
        :rtype: str
        """
        return self._replication_mode

    @replication_mode.setter
    def replication_mode(self, replication_mode):
        """Sets the replication_mode of this HaResponse.

        备机同步参数。实例主备模式为Ha时有效。 取值： - MySQL为“async”或“semisync”。 - PostgreSQL为“async”或“sync”。 - Microsoft SQL Server为“sync”。

        :param replication_mode: The replication_mode of this HaResponse.
        :type replication_mode: str
        """
        self._replication_mode = replication_mode

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
        if not isinstance(other, HaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
