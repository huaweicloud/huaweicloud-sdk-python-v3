# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationRisks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package': 'str',
        'source_file': 'str',
        'node_msg': 'str',
        'field': 'str',
        'operation': 'str',
        'original_value': 'str',
        'value': 'str'
    }

    attribute_map = {
        'package': 'package',
        'source_file': 'sourceFile',
        'node_msg': 'nodeMsg',
        'field': 'field',
        'operation': 'operation',
        'original_value': 'originalValue',
        'value': 'value'
    }

    def __init__(self, package=None, source_file=None, node_msg=None, field=None, operation=None, original_value=None, value=None):
        r"""ConfigurationRisks

        The model defined in huaweicloud sdk

        :param package: 组件名称
        :type package: str
        :param source_file: 涉及文件路径
        :type source_file: str
        :param node_msg: 节点信息
        :type node_msg: str
        :param field: 参数值
        :type field: str
        :param operation: 修改操作类型
        :type operation: str
        :param original_value: 原始值
        :type original_value: str
        :param value: 当前值
        :type value: str
        """
        
        

        self._package = None
        self._source_file = None
        self._node_msg = None
        self._field = None
        self._operation = None
        self._original_value = None
        self._value = None
        self.discriminator = None

        if package is not None:
            self.package = package
        if source_file is not None:
            self.source_file = source_file
        if node_msg is not None:
            self.node_msg = node_msg
        if field is not None:
            self.field = field
        if operation is not None:
            self.operation = operation
        if original_value is not None:
            self.original_value = original_value
        if value is not None:
            self.value = value

    @property
    def package(self):
        r"""Gets the package of this ConfigurationRisks.

        组件名称

        :return: The package of this ConfigurationRisks.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        r"""Sets the package of this ConfigurationRisks.

        组件名称

        :param package: The package of this ConfigurationRisks.
        :type package: str
        """
        self._package = package

    @property
    def source_file(self):
        r"""Gets the source_file of this ConfigurationRisks.

        涉及文件路径

        :return: The source_file of this ConfigurationRisks.
        :rtype: str
        """
        return self._source_file

    @source_file.setter
    def source_file(self, source_file):
        r"""Sets the source_file of this ConfigurationRisks.

        涉及文件路径

        :param source_file: The source_file of this ConfigurationRisks.
        :type source_file: str
        """
        self._source_file = source_file

    @property
    def node_msg(self):
        r"""Gets the node_msg of this ConfigurationRisks.

        节点信息

        :return: The node_msg of this ConfigurationRisks.
        :rtype: str
        """
        return self._node_msg

    @node_msg.setter
    def node_msg(self, node_msg):
        r"""Sets the node_msg of this ConfigurationRisks.

        节点信息

        :param node_msg: The node_msg of this ConfigurationRisks.
        :type node_msg: str
        """
        self._node_msg = node_msg

    @property
    def field(self):
        r"""Gets the field of this ConfigurationRisks.

        参数值

        :return: The field of this ConfigurationRisks.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this ConfigurationRisks.

        参数值

        :param field: The field of this ConfigurationRisks.
        :type field: str
        """
        self._field = field

    @property
    def operation(self):
        r"""Gets the operation of this ConfigurationRisks.

        修改操作类型

        :return: The operation of this ConfigurationRisks.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ConfigurationRisks.

        修改操作类型

        :param operation: The operation of this ConfigurationRisks.
        :type operation: str
        """
        self._operation = operation

    @property
    def original_value(self):
        r"""Gets the original_value of this ConfigurationRisks.

        原始值

        :return: The original_value of this ConfigurationRisks.
        :rtype: str
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        r"""Sets the original_value of this ConfigurationRisks.

        原始值

        :param original_value: The original_value of this ConfigurationRisks.
        :type original_value: str
        """
        self._original_value = original_value

    @property
    def value(self):
        r"""Gets the value of this ConfigurationRisks.

        当前值

        :return: The value of this ConfigurationRisks.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ConfigurationRisks.

        当前值

        :param value: The value of this ConfigurationRisks.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, ConfigurationRisks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
