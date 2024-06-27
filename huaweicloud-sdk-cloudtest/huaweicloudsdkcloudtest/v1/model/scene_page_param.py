# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScenePageParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deleted': 'str',
        'limit': 'int',
        'mindmap_id': 'str',
        'node_id': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'deleted': 'deleted',
        'limit': 'limit',
        'mindmap_id': 'mindmap_id',
        'node_id': 'node_id',
        'offset': 'offset'
    }

    def __init__(self, deleted=None, limit=None, mindmap_id=None, node_id=None, offset=None):
        """ScenePageParam

        The model defined in huaweicloud sdk

        :param deleted: 
        :type deleted: str
        :param limit: 
        :type limit: int
        :param mindmap_id: 
        :type mindmap_id: str
        :param node_id: 
        :type node_id: str
        :param offset: 
        :type offset: int
        """
        
        

        self._deleted = None
        self._limit = None
        self._mindmap_id = None
        self._node_id = None
        self._offset = None
        self.discriminator = None

        if deleted is not None:
            self.deleted = deleted
        if limit is not None:
            self.limit = limit
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id
        if node_id is not None:
            self.node_id = node_id
        if offset is not None:
            self.offset = offset

    @property
    def deleted(self):
        """Gets the deleted of this ScenePageParam.

        :return: The deleted of this ScenePageParam.
        :rtype: str
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ScenePageParam.

        :param deleted: The deleted of this ScenePageParam.
        :type deleted: str
        """
        self._deleted = deleted

    @property
    def limit(self):
        """Gets the limit of this ScenePageParam.

        :return: The limit of this ScenePageParam.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ScenePageParam.

        :param limit: The limit of this ScenePageParam.
        :type limit: int
        """
        self._limit = limit

    @property
    def mindmap_id(self):
        """Gets the mindmap_id of this ScenePageParam.

        :return: The mindmap_id of this ScenePageParam.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        """Sets the mindmap_id of this ScenePageParam.

        :param mindmap_id: The mindmap_id of this ScenePageParam.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

    @property
    def node_id(self):
        """Gets the node_id of this ScenePageParam.

        :return: The node_id of this ScenePageParam.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ScenePageParam.

        :param node_id: The node_id of this ScenePageParam.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def offset(self):
        """Gets the offset of this ScenePageParam.

        :return: The offset of this ScenePageParam.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ScenePageParam.

        :param offset: The offset of this ScenePageParam.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ScenePageParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
