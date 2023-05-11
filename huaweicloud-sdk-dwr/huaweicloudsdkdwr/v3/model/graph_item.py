# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GraphItem:

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
        'created_at': 'str',
        'graph_urn': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'created_at': 'created_at',
        'graph_urn': 'graph_urn',
        'id': 'id'
    }

    def __init__(self, name=None, created_at=None, graph_urn=None, id=None):
        """GraphItem

        The model defined in huaweicloud sdk

        :param name: 工作流的名称。
        :type name: str
        :param created_at: 系统记录的创建工作流模板的时间。
        :type created_at: str
        :param graph_urn: 工作流的URN。
        :type graph_urn: str
        :param id: 工作流ID
        :type id: str
        """
        
        

        self._name = None
        self._created_at = None
        self._graph_urn = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if graph_urn is not None:
            self.graph_urn = graph_urn
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this GraphItem.

        工作流的名称。

        :return: The name of this GraphItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GraphItem.

        工作流的名称。

        :param name: The name of this GraphItem.
        :type name: str
        """
        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this GraphItem.

        系统记录的创建工作流模板的时间。

        :return: The created_at of this GraphItem.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GraphItem.

        系统记录的创建工作流模板的时间。

        :param created_at: The created_at of this GraphItem.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def graph_urn(self):
        """Gets the graph_urn of this GraphItem.

        工作流的URN。

        :return: The graph_urn of this GraphItem.
        :rtype: str
        """
        return self._graph_urn

    @graph_urn.setter
    def graph_urn(self, graph_urn):
        """Sets the graph_urn of this GraphItem.

        工作流的URN。

        :param graph_urn: The graph_urn of this GraphItem.
        :type graph_urn: str
        """
        self._graph_urn = graph_urn

    @property
    def id(self):
        """Gets the id of this GraphItem.

        工作流ID

        :return: The id of this GraphItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GraphItem.

        工作流ID

        :param id: The id of this GraphItem.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, GraphItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
