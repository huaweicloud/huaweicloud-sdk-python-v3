# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShrinkParam:

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
        'resource_ids': 'list[str]'
    }

    attribute_map = {
        'node_group_name': 'node_group_name',
        'count': 'count',
        'resource_ids': 'resource_ids'
    }

    def __init__(self, node_group_name=None, count=None, resource_ids=None):
        r"""ShrinkParam

        The model defined in huaweicloud sdk

        :param node_group_name: 节点组名称
        :type node_group_name: str
        :param count: 缩容节点数量，如果是指定节点缩容，则该参数可以不填。
        :type count: int
        :param resource_ids: 缩容节点时指定待删除节点的资源ID列表。 resource_ids为空时，按照系统规则自动选择删除节点。 仅支持删除状态异常的ecs节点。 会针对指定节点进行强制删除。 可通过查询主机接口获取resource_id。
        :type resource_ids: list[str]
        """
        
        

        self._node_group_name = None
        self._count = None
        self._resource_ids = None
        self.discriminator = None

        self.node_group_name = node_group_name
        if count is not None:
            self.count = count
        if resource_ids is not None:
            self.resource_ids = resource_ids

    @property
    def node_group_name(self):
        r"""Gets the node_group_name of this ShrinkParam.

        节点组名称

        :return: The node_group_name of this ShrinkParam.
        :rtype: str
        """
        return self._node_group_name

    @node_group_name.setter
    def node_group_name(self, node_group_name):
        r"""Sets the node_group_name of this ShrinkParam.

        节点组名称

        :param node_group_name: The node_group_name of this ShrinkParam.
        :type node_group_name: str
        """
        self._node_group_name = node_group_name

    @property
    def count(self):
        r"""Gets the count of this ShrinkParam.

        缩容节点数量，如果是指定节点缩容，则该参数可以不填。

        :return: The count of this ShrinkParam.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShrinkParam.

        缩容节点数量，如果是指定节点缩容，则该参数可以不填。

        :param count: The count of this ShrinkParam.
        :type count: int
        """
        self._count = count

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this ShrinkParam.

        缩容节点时指定待删除节点的资源ID列表。 resource_ids为空时，按照系统规则自动选择删除节点。 仅支持删除状态异常的ecs节点。 会针对指定节点进行强制删除。 可通过查询主机接口获取resource_id。

        :return: The resource_ids of this ShrinkParam.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this ShrinkParam.

        缩容节点时指定待删除节点的资源ID列表。 resource_ids为空时，按照系统规则自动选择删除节点。 仅支持删除状态异常的ecs节点。 会针对指定节点进行强制删除。 可通过查询主机接口获取resource_id。

        :param resource_ids: The resource_ids of this ShrinkParam.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

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
        if not isinstance(other, ShrinkParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
