# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLimitTaskNodeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'sql_id': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'sql_id': 'sql_id'
    }

    def __init__(self, node_id=None, sql_id=None):
        r"""CreateLimitTaskNodeOption

        The model defined in huaweicloud sdk

        :param node_id: 节点id。
        :type node_id: str
        :param sql_id: 该节点执行的sql语句id。如果类型为SQL_ID，必须与limit_type_value值一致。
        :type sql_id: str
        """
        
        

        self._node_id = None
        self._sql_id = None
        self.discriminator = None

        self.node_id = node_id
        self.sql_id = sql_id

    @property
    def node_id(self):
        r"""Gets the node_id of this CreateLimitTaskNodeOption.

        节点id。

        :return: The node_id of this CreateLimitTaskNodeOption.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CreateLimitTaskNodeOption.

        节点id。

        :param node_id: The node_id of this CreateLimitTaskNodeOption.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def sql_id(self):
        r"""Gets the sql_id of this CreateLimitTaskNodeOption.

        该节点执行的sql语句id。如果类型为SQL_ID，必须与limit_type_value值一致。

        :return: The sql_id of this CreateLimitTaskNodeOption.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this CreateLimitTaskNodeOption.

        该节点执行的sql语句id。如果类型为SQL_ID，必须与limit_type_value值一致。

        :param sql_id: The sql_id of this CreateLimitTaskNodeOption.
        :type sql_id: str
        """
        self._sql_id = sql_id

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
        if not isinstance(other, CreateLimitTaskNodeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
