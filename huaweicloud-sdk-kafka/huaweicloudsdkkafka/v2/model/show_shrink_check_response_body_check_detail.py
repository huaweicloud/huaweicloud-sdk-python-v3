# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShrinkCheckResponseBodyCheckDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'broker_id': 'int',
        'can_delete': 'bool',
        'is_zk_node': 'bool',
        'is_controller': 'bool',
        'has_topics': 'bool',
        'topics': 'list[str]'
    }

    attribute_map = {
        'broker_id': 'broker_id',
        'can_delete': 'can_delete',
        'is_zk_node': 'is_zk_node',
        'is_controller': 'is_controller',
        'has_topics': 'has_topics',
        'topics': 'topics'
    }

    def __init__(self, broker_id=None, can_delete=None, is_zk_node=None, is_controller=None, has_topics=None, topics=None):
        """ShowShrinkCheckResponseBodyCheckDetail

        The model defined in huaweicloud sdk

        :param broker_id: broker序号
        :type broker_id: int
        :param can_delete: 节点是否可删除。
        :type can_delete: bool
        :param is_zk_node: 节点是否为zk部署节点。
        :type is_zk_node: bool
        :param is_controller: broker是否为controller。
        :type is_controller: bool
        :param has_topics: broker上是否存在topic数据。
        :type has_topics: bool
        :param topics: broker上存在的topic列表。
        :type topics: list[str]
        """
        
        

        self._broker_id = None
        self._can_delete = None
        self._is_zk_node = None
        self._is_controller = None
        self._has_topics = None
        self._topics = None
        self.discriminator = None

        if broker_id is not None:
            self.broker_id = broker_id
        if can_delete is not None:
            self.can_delete = can_delete
        if is_zk_node is not None:
            self.is_zk_node = is_zk_node
        if is_controller is not None:
            self.is_controller = is_controller
        if has_topics is not None:
            self.has_topics = has_topics
        if topics is not None:
            self.topics = topics

    @property
    def broker_id(self):
        """Gets the broker_id of this ShowShrinkCheckResponseBodyCheckDetail.

        broker序号

        :return: The broker_id of this ShowShrinkCheckResponseBodyCheckDetail.
        :rtype: int
        """
        return self._broker_id

    @broker_id.setter
    def broker_id(self, broker_id):
        """Sets the broker_id of this ShowShrinkCheckResponseBodyCheckDetail.

        broker序号

        :param broker_id: The broker_id of this ShowShrinkCheckResponseBodyCheckDetail.
        :type broker_id: int
        """
        self._broker_id = broker_id

    @property
    def can_delete(self):
        """Gets the can_delete of this ShowShrinkCheckResponseBodyCheckDetail.

        节点是否可删除。

        :return: The can_delete of this ShowShrinkCheckResponseBodyCheckDetail.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        """Sets the can_delete of this ShowShrinkCheckResponseBodyCheckDetail.

        节点是否可删除。

        :param can_delete: The can_delete of this ShowShrinkCheckResponseBodyCheckDetail.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def is_zk_node(self):
        """Gets the is_zk_node of this ShowShrinkCheckResponseBodyCheckDetail.

        节点是否为zk部署节点。

        :return: The is_zk_node of this ShowShrinkCheckResponseBodyCheckDetail.
        :rtype: bool
        """
        return self._is_zk_node

    @is_zk_node.setter
    def is_zk_node(self, is_zk_node):
        """Sets the is_zk_node of this ShowShrinkCheckResponseBodyCheckDetail.

        节点是否为zk部署节点。

        :param is_zk_node: The is_zk_node of this ShowShrinkCheckResponseBodyCheckDetail.
        :type is_zk_node: bool
        """
        self._is_zk_node = is_zk_node

    @property
    def is_controller(self):
        """Gets the is_controller of this ShowShrinkCheckResponseBodyCheckDetail.

        broker是否为controller。

        :return: The is_controller of this ShowShrinkCheckResponseBodyCheckDetail.
        :rtype: bool
        """
        return self._is_controller

    @is_controller.setter
    def is_controller(self, is_controller):
        """Sets the is_controller of this ShowShrinkCheckResponseBodyCheckDetail.

        broker是否为controller。

        :param is_controller: The is_controller of this ShowShrinkCheckResponseBodyCheckDetail.
        :type is_controller: bool
        """
        self._is_controller = is_controller

    @property
    def has_topics(self):
        """Gets the has_topics of this ShowShrinkCheckResponseBodyCheckDetail.

        broker上是否存在topic数据。

        :return: The has_topics of this ShowShrinkCheckResponseBodyCheckDetail.
        :rtype: bool
        """
        return self._has_topics

    @has_topics.setter
    def has_topics(self, has_topics):
        """Sets the has_topics of this ShowShrinkCheckResponseBodyCheckDetail.

        broker上是否存在topic数据。

        :param has_topics: The has_topics of this ShowShrinkCheckResponseBodyCheckDetail.
        :type has_topics: bool
        """
        self._has_topics = has_topics

    @property
    def topics(self):
        """Gets the topics of this ShowShrinkCheckResponseBodyCheckDetail.

        broker上存在的topic列表。

        :return: The topics of this ShowShrinkCheckResponseBodyCheckDetail.
        :rtype: list[str]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ShowShrinkCheckResponseBodyCheckDetail.

        broker上存在的topic列表。

        :param topics: The topics of this ShowShrinkCheckResponseBodyCheckDetail.
        :type topics: list[str]
        """
        self._topics = topics

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
        if not isinstance(other, ShowShrinkCheckResponseBodyCheckDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
