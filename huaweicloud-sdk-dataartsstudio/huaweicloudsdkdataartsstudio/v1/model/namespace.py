# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Namespace:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace_name': 'str',
        'namespace_guid': 'str',
        'namespace_qualified_name': 'str',
        'table_count': 'int'
    }

    attribute_map = {
        'namespace_name': 'namespace_name',
        'namespace_guid': 'namespace_guid',
        'namespace_qualified_name': 'namespace_qualified_name',
        'table_count': 'table_count'
    }

    def __init__(self, namespace_name=None, namespace_guid=None, namespace_qualified_name=None, table_count=None):
        r"""Namespace

        The model defined in huaweicloud sdk

        :param namespace_name: 命名空间的名称
        :type namespace_name: str
        :param namespace_guid: 命名空间的guid
        :type namespace_guid: str
        :param namespace_qualified_name: 命名空间的唯一标识名称
        :type namespace_qualified_name: str
        :param table_count: 命名空间下的表总数
        :type table_count: int
        """
        
        

        self._namespace_name = None
        self._namespace_guid = None
        self._namespace_qualified_name = None
        self._table_count = None
        self.discriminator = None

        if namespace_name is not None:
            self.namespace_name = namespace_name
        if namespace_guid is not None:
            self.namespace_guid = namespace_guid
        if namespace_qualified_name is not None:
            self.namespace_qualified_name = namespace_qualified_name
        if table_count is not None:
            self.table_count = table_count

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this Namespace.

        命名空间的名称

        :return: The namespace_name of this Namespace.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this Namespace.

        命名空间的名称

        :param namespace_name: The namespace_name of this Namespace.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def namespace_guid(self):
        r"""Gets the namespace_guid of this Namespace.

        命名空间的guid

        :return: The namespace_guid of this Namespace.
        :rtype: str
        """
        return self._namespace_guid

    @namespace_guid.setter
    def namespace_guid(self, namespace_guid):
        r"""Sets the namespace_guid of this Namespace.

        命名空间的guid

        :param namespace_guid: The namespace_guid of this Namespace.
        :type namespace_guid: str
        """
        self._namespace_guid = namespace_guid

    @property
    def namespace_qualified_name(self):
        r"""Gets the namespace_qualified_name of this Namespace.

        命名空间的唯一标识名称

        :return: The namespace_qualified_name of this Namespace.
        :rtype: str
        """
        return self._namespace_qualified_name

    @namespace_qualified_name.setter
    def namespace_qualified_name(self, namespace_qualified_name):
        r"""Sets the namespace_qualified_name of this Namespace.

        命名空间的唯一标识名称

        :param namespace_qualified_name: The namespace_qualified_name of this Namespace.
        :type namespace_qualified_name: str
        """
        self._namespace_qualified_name = namespace_qualified_name

    @property
    def table_count(self):
        r"""Gets the table_count of this Namespace.

        命名空间下的表总数

        :return: The table_count of this Namespace.
        :rtype: int
        """
        return self._table_count

    @table_count.setter
    def table_count(self, table_count):
        r"""Sets the table_count of this Namespace.

        命名空间下的表总数

        :param table_count: The table_count of this Namespace.
        :type table_count: int
        """
        self._table_count = table_count

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
        if not isinstance(other, Namespace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
