# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeMessage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'content': 'str',
        'origin': 'str',
        'node_id': 'str',
        'node_type': 'str',
        'node_name': 'str',
        'created_time': 'int'
    }

    attribute_map = {
        'role': 'role',
        'content': 'content',
        'origin': 'origin',
        'node_id': 'nodeId',
        'node_type': 'nodeType',
        'node_name': 'nodeName',
        'created_time': 'createdTime'
    }

    def __init__(self, role=None, content=None, origin=None, node_id=None, node_type=None, node_name=None, created_time=None):
        r"""NodeMessage

        The model defined in huaweicloud sdk

        :param role: 角色
        :type role: str
        :param content: 内容
        :type content: str
        :param origin: 原始内容
        :type origin: str
        :param node_id: 节点id
        :type node_id: str
        :param node_type: 节点类型
        :type node_type: str
        :param node_name: 节点名
        :type node_name: str
        :param created_time: 事件发生时间
        :type created_time: int
        """
        
        

        self._role = None
        self._content = None
        self._origin = None
        self._node_id = None
        self._node_type = None
        self._node_name = None
        self._created_time = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if content is not None:
            self.content = content
        if origin is not None:
            self.origin = origin
        if node_id is not None:
            self.node_id = node_id
        if node_type is not None:
            self.node_type = node_type
        if node_name is not None:
            self.node_name = node_name
        if created_time is not None:
            self.created_time = created_time

    @property
    def role(self):
        r"""Gets the role of this NodeMessage.

        角色

        :return: The role of this NodeMessage.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this NodeMessage.

        角色

        :param role: The role of this NodeMessage.
        :type role: str
        """
        self._role = role

    @property
    def content(self):
        r"""Gets the content of this NodeMessage.

        内容

        :return: The content of this NodeMessage.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this NodeMessage.

        内容

        :param content: The content of this NodeMessage.
        :type content: str
        """
        self._content = content

    @property
    def origin(self):
        r"""Gets the origin of this NodeMessage.

        原始内容

        :return: The origin of this NodeMessage.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        r"""Sets the origin of this NodeMessage.

        原始内容

        :param origin: The origin of this NodeMessage.
        :type origin: str
        """
        self._origin = origin

    @property
    def node_id(self):
        r"""Gets the node_id of this NodeMessage.

        节点id

        :return: The node_id of this NodeMessage.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this NodeMessage.

        节点id

        :param node_id: The node_id of this NodeMessage.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_type(self):
        r"""Gets the node_type of this NodeMessage.

        节点类型

        :return: The node_type of this NodeMessage.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this NodeMessage.

        节点类型

        :param node_type: The node_type of this NodeMessage.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def node_name(self):
        r"""Gets the node_name of this NodeMessage.

        节点名

        :return: The node_name of this NodeMessage.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this NodeMessage.

        节点名

        :param node_name: The node_name of this NodeMessage.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def created_time(self):
        r"""Gets the created_time of this NodeMessage.

        事件发生时间

        :return: The created_time of this NodeMessage.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this NodeMessage.

        事件发生时间

        :param created_time: The created_time of this NodeMessage.
        :type created_time: int
        """
        self._created_time = created_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
