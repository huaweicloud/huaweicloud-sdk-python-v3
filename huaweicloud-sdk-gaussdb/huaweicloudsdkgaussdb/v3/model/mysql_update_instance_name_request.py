# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlUpdateInstanceNameRequest:

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
        'is_modify_node_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'is_modify_node_name': 'is_modify_node_name'
    }

    def __init__(self, name=None, is_modify_node_name=None):
        """MysqlUpdateInstanceNameRequest

        The model defined in huaweicloud sdk

        :param name: 实例名称。  用于表示实例的名称，同一租户下，同类型的实例名可重名。取值范围：最小为4个字符，最大为64个字符且不超过64个字节（注意：一个中文字符占用3个字节），必须以字母或中文开头，区分大小写，可以包含字母、数字、中划线、下划线或中文，不能包含其他特殊字符。
        :type name: str
        :param is_modify_node_name: 是否同步修改节点名称，取值：true或false, 默认值为true。
        :type is_modify_node_name: str
        """
        
        

        self._name = None
        self._is_modify_node_name = None
        self.discriminator = None

        self.name = name
        if is_modify_node_name is not None:
            self.is_modify_node_name = is_modify_node_name

    @property
    def name(self):
        """Gets the name of this MysqlUpdateInstanceNameRequest.

        实例名称。  用于表示实例的名称，同一租户下，同类型的实例名可重名。取值范围：最小为4个字符，最大为64个字符且不超过64个字节（注意：一个中文字符占用3个字节），必须以字母或中文开头，区分大小写，可以包含字母、数字、中划线、下划线或中文，不能包含其他特殊字符。

        :return: The name of this MysqlUpdateInstanceNameRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MysqlUpdateInstanceNameRequest.

        实例名称。  用于表示实例的名称，同一租户下，同类型的实例名可重名。取值范围：最小为4个字符，最大为64个字符且不超过64个字节（注意：一个中文字符占用3个字节），必须以字母或中文开头，区分大小写，可以包含字母、数字、中划线、下划线或中文，不能包含其他特殊字符。

        :param name: The name of this MysqlUpdateInstanceNameRequest.
        :type name: str
        """
        self._name = name

    @property
    def is_modify_node_name(self):
        """Gets the is_modify_node_name of this MysqlUpdateInstanceNameRequest.

        是否同步修改节点名称，取值：true或false, 默认值为true。

        :return: The is_modify_node_name of this MysqlUpdateInstanceNameRequest.
        :rtype: str
        """
        return self._is_modify_node_name

    @is_modify_node_name.setter
    def is_modify_node_name(self, is_modify_node_name):
        """Sets the is_modify_node_name of this MysqlUpdateInstanceNameRequest.

        是否同步修改节点名称，取值：true或false, 默认值为true。

        :param is_modify_node_name: The is_modify_node_name of this MysqlUpdateInstanceNameRequest.
        :type is_modify_node_name: str
        """
        self._is_modify_node_name = is_modify_node_name

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
        if not isinstance(other, MysqlUpdateInstanceNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
