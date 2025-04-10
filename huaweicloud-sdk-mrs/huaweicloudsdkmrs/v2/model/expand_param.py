# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_group_name': 'str',
        'count': 'int',
        'skip_bootstrap_scripts': 'bool',
        'scale_without_start': 'bool'
    }

    attribute_map = {
        'node_group_name': 'node_group_name',
        'count': 'count',
        'skip_bootstrap_scripts': 'skip_bootstrap_scripts',
        'scale_without_start': 'scale_without_start'
    }

    def __init__(self, node_group_name=None, count=None, skip_bootstrap_scripts=None, scale_without_start=None):
        r"""ExpandParam

        The model defined in huaweicloud sdk

        :param node_group_name: 节点组名称
        :type node_group_name: str
        :param count: 扩容节点数量
        :type count: int
        :param skip_bootstrap_scripts: 扩容时是否在新增节点上跳过执行创建集群时指定的引导操作。未填写时，默认不执行引导操作。
        :type skip_bootstrap_scripts: bool
        :param scale_without_start: 扩容后是否选择不启动扩容节点上的组件。未填写时，默认启动组件。  - true：扩容后不启动组件。 - false：扩容后启动组件。
        :type scale_without_start: bool
        """
        
        

        self._node_group_name = None
        self._count = None
        self._skip_bootstrap_scripts = None
        self._scale_without_start = None
        self.discriminator = None

        self.node_group_name = node_group_name
        self.count = count
        if skip_bootstrap_scripts is not None:
            self.skip_bootstrap_scripts = skip_bootstrap_scripts
        if scale_without_start is not None:
            self.scale_without_start = scale_without_start

    @property
    def node_group_name(self):
        r"""Gets the node_group_name of this ExpandParam.

        节点组名称

        :return: The node_group_name of this ExpandParam.
        :rtype: str
        """
        return self._node_group_name

    @node_group_name.setter
    def node_group_name(self, node_group_name):
        r"""Sets the node_group_name of this ExpandParam.

        节点组名称

        :param node_group_name: The node_group_name of this ExpandParam.
        :type node_group_name: str
        """
        self._node_group_name = node_group_name

    @property
    def count(self):
        r"""Gets the count of this ExpandParam.

        扩容节点数量

        :return: The count of this ExpandParam.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ExpandParam.

        扩容节点数量

        :param count: The count of this ExpandParam.
        :type count: int
        """
        self._count = count

    @property
    def skip_bootstrap_scripts(self):
        r"""Gets the skip_bootstrap_scripts of this ExpandParam.

        扩容时是否在新增节点上跳过执行创建集群时指定的引导操作。未填写时，默认不执行引导操作。

        :return: The skip_bootstrap_scripts of this ExpandParam.
        :rtype: bool
        """
        return self._skip_bootstrap_scripts

    @skip_bootstrap_scripts.setter
    def skip_bootstrap_scripts(self, skip_bootstrap_scripts):
        r"""Sets the skip_bootstrap_scripts of this ExpandParam.

        扩容时是否在新增节点上跳过执行创建集群时指定的引导操作。未填写时，默认不执行引导操作。

        :param skip_bootstrap_scripts: The skip_bootstrap_scripts of this ExpandParam.
        :type skip_bootstrap_scripts: bool
        """
        self._skip_bootstrap_scripts = skip_bootstrap_scripts

    @property
    def scale_without_start(self):
        r"""Gets the scale_without_start of this ExpandParam.

        扩容后是否选择不启动扩容节点上的组件。未填写时，默认启动组件。  - true：扩容后不启动组件。 - false：扩容后启动组件。

        :return: The scale_without_start of this ExpandParam.
        :rtype: bool
        """
        return self._scale_without_start

    @scale_without_start.setter
    def scale_without_start(self, scale_without_start):
        r"""Sets the scale_without_start of this ExpandParam.

        扩容后是否选择不启动扩容节点上的组件。未填写时，默认启动组件。  - true：扩容后不启动组件。 - false：扩容后启动组件。

        :param scale_without_start: The scale_without_start of this ExpandParam.
        :type scale_without_start: bool
        """
        self._scale_without_start = scale_without_start

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
        if not isinstance(other, ExpandParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
