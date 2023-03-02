# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Node:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_node': 'str',
        'category': 'str',
        'description': 'str',
        'id': 'str',
        'ignore_error': 'bool',
        'metadata': 'Metadata',
        'name': 'str',
        'task_name': 'str'
    }

    attribute_map = {
        'parent_node': 'parent_node',
        'category': 'category',
        'description': 'description',
        'id': 'id',
        'ignore_error': 'ignore_error',
        'metadata': 'metadata',
        'name': 'name',
        'task_name': 'task_name'
    }

    def __init__(self, parent_node=None, category=None, description=None, id=None, ignore_error=None, metadata=None, name=None, task_name=None):
        """Node

        The model defined in huaweicloud sdk

        :param parent_node: 父亲节点的名称。
        :type parent_node: str
        :param category: 节点类型。
        :type category: str
        :param description: 节点描述。
        :type description: str
        :param id: 节点id
        :type id: str
        :param ignore_error: 是否忽略错误
        :type ignore_error: bool
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkaom.v1.Metadata`
        :param name: 节点名称,比如是Node。
        :type name: str
        :param task_name: 任务名称，节点上任务的名称。
        :type task_name: str
        """
        
        

        self._parent_node = None
        self._category = None
        self._description = None
        self._id = None
        self._ignore_error = None
        self._metadata = None
        self._name = None
        self._task_name = None
        self.discriminator = None

        if parent_node is not None:
            self.parent_node = parent_node
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if ignore_error is not None:
            self.ignore_error = ignore_error
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if task_name is not None:
            self.task_name = task_name

    @property
    def parent_node(self):
        """Gets the parent_node of this Node.

        父亲节点的名称。

        :return: The parent_node of this Node.
        :rtype: str
        """
        return self._parent_node

    @parent_node.setter
    def parent_node(self, parent_node):
        """Sets the parent_node of this Node.

        父亲节点的名称。

        :param parent_node: The parent_node of this Node.
        :type parent_node: str
        """
        self._parent_node = parent_node

    @property
    def category(self):
        """Gets the category of this Node.

        节点类型。

        :return: The category of this Node.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Node.

        节点类型。

        :param category: The category of this Node.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        """Gets the description of this Node.

        节点描述。

        :return: The description of this Node.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Node.

        节点描述。

        :param description: The description of this Node.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this Node.

        节点id

        :return: The id of this Node.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Node.

        节点id

        :param id: The id of this Node.
        :type id: str
        """
        self._id = id

    @property
    def ignore_error(self):
        """Gets the ignore_error of this Node.

        是否忽略错误

        :return: The ignore_error of this Node.
        :rtype: bool
        """
        return self._ignore_error

    @ignore_error.setter
    def ignore_error(self, ignore_error):
        """Sets the ignore_error of this Node.

        是否忽略错误

        :param ignore_error: The ignore_error of this Node.
        :type ignore_error: bool
        """
        self._ignore_error = ignore_error

    @property
    def metadata(self):
        """Gets the metadata of this Node.

        :return: The metadata of this Node.
        :rtype: :class:`huaweicloudsdkaom.v1.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Node.

        :param metadata: The metadata of this Node.
        :type metadata: :class:`huaweicloudsdkaom.v1.Metadata`
        """
        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this Node.

        节点名称,比如是Node。

        :return: The name of this Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Node.

        节点名称,比如是Node。

        :param name: The name of this Node.
        :type name: str
        """
        self._name = name

    @property
    def task_name(self):
        """Gets the task_name of this Node.

        任务名称，节点上任务的名称。

        :return: The task_name of this Node.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this Node.

        任务名称，节点上任务的名称。

        :param task_name: The task_name of this Node.
        :type task_name: str
        """
        self._task_name = task_name

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
        if not isinstance(other, Node):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
