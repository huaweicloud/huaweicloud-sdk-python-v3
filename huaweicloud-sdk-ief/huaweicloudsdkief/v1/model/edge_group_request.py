# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeGroupRequest:

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
        'description': 'str',
        'node_ids': 'list[str]',
        'tags': 'list[Attributes]',
        'device_ids': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'node_ids': 'node_ids',
        'tags': 'tags',
        'device_ids': 'device_ids'
    }

    def __init__(self, name=None, description=None, node_ids=None, tags=None, device_ids=None):
        """EdgeGroupRequest

        The model defined in huaweicloud sdk

        :param name: 节点组名称。只允许中文字符、英文字母、数字、下划线、中划线，最大长度64
        :type name: str
        :param description: 节点组描述。最大长度255个字符
        :type description: str
        :param node_ids: 节点组绑定的节点ID列表
        :type node_ids: list[str]
        :param tags: 节点组标签
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        :param device_ids: 节点组绑定的终端设备ID列表
        :type device_ids: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._node_ids = None
        self._tags = None
        self._device_ids = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if node_ids is not None:
            self.node_ids = node_ids
        if tags is not None:
            self.tags = tags
        if device_ids is not None:
            self.device_ids = device_ids

    @property
    def name(self):
        """Gets the name of this EdgeGroupRequest.

        节点组名称。只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :return: The name of this EdgeGroupRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EdgeGroupRequest.

        节点组名称。只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :param name: The name of this EdgeGroupRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EdgeGroupRequest.

        节点组描述。最大长度255个字符

        :return: The description of this EdgeGroupRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdgeGroupRequest.

        节点组描述。最大长度255个字符

        :param description: The description of this EdgeGroupRequest.
        :type description: str
        """
        self._description = description

    @property
    def node_ids(self):
        """Gets the node_ids of this EdgeGroupRequest.

        节点组绑定的节点ID列表

        :return: The node_ids of this EdgeGroupRequest.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this EdgeGroupRequest.

        节点组绑定的节点ID列表

        :param node_ids: The node_ids of this EdgeGroupRequest.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def tags(self):
        """Gets the tags of this EdgeGroupRequest.

        节点组标签

        :return: The tags of this EdgeGroupRequest.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this EdgeGroupRequest.

        节点组标签

        :param tags: The tags of this EdgeGroupRequest.
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._tags = tags

    @property
    def device_ids(self):
        """Gets the device_ids of this EdgeGroupRequest.

        节点组绑定的终端设备ID列表

        :return: The device_ids of this EdgeGroupRequest.
        :rtype: list[str]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this EdgeGroupRequest.

        节点组绑定的终端设备ID列表

        :param device_ids: The device_ids of this EdgeGroupRequest.
        :type device_ids: list[str]
        """
        self._device_ids = device_ids

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
        if not isinstance(other, EdgeGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
