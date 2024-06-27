# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateChDatabaseReplicationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_instance_id': 'str',
        'source_node_id': 'str',
        'source_database': 'str'
    }

    attribute_map = {
        'source_instance_id': 'source_instance_id',
        'source_node_id': 'source_node_id',
        'source_database': 'source_database'
    }

    def __init__(self, source_instance_id=None, source_node_id=None, source_database=None):
        """CreateChDatabaseReplicationRequestBody

        The model defined in huaweicloud sdk

        :param source_instance_id: 源实例ID。
        :type source_instance_id: str
        :param source_node_id: 源节点ID。GaussDB(for MySQL)只读节点ID。如为空，则取GaussDB(for MySQL)主节点ID。
        :type source_node_id: str
        :param source_database: 源数据库。
        :type source_database: str
        """
        
        

        self._source_instance_id = None
        self._source_node_id = None
        self._source_database = None
        self.discriminator = None

        self.source_instance_id = source_instance_id
        if source_node_id is not None:
            self.source_node_id = source_node_id
        self.source_database = source_database

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this CreateChDatabaseReplicationRequestBody.

        源实例ID。

        :return: The source_instance_id of this CreateChDatabaseReplicationRequestBody.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this CreateChDatabaseReplicationRequestBody.

        源实例ID。

        :param source_instance_id: The source_instance_id of this CreateChDatabaseReplicationRequestBody.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def source_node_id(self):
        """Gets the source_node_id of this CreateChDatabaseReplicationRequestBody.

        源节点ID。GaussDB(for MySQL)只读节点ID。如为空，则取GaussDB(for MySQL)主节点ID。

        :return: The source_node_id of this CreateChDatabaseReplicationRequestBody.
        :rtype: str
        """
        return self._source_node_id

    @source_node_id.setter
    def source_node_id(self, source_node_id):
        """Sets the source_node_id of this CreateChDatabaseReplicationRequestBody.

        源节点ID。GaussDB(for MySQL)只读节点ID。如为空，则取GaussDB(for MySQL)主节点ID。

        :param source_node_id: The source_node_id of this CreateChDatabaseReplicationRequestBody.
        :type source_node_id: str
        """
        self._source_node_id = source_node_id

    @property
    def source_database(self):
        """Gets the source_database of this CreateChDatabaseReplicationRequestBody.

        源数据库。

        :return: The source_database of this CreateChDatabaseReplicationRequestBody.
        :rtype: str
        """
        return self._source_database

    @source_database.setter
    def source_database(self, source_database):
        """Sets the source_database of this CreateChDatabaseReplicationRequestBody.

        源数据库。

        :param source_database: The source_database of this CreateChDatabaseReplicationRequestBody.
        :type source_database: str
        """
        self._source_database = source_database

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
        if not isinstance(other, CreateChDatabaseReplicationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
