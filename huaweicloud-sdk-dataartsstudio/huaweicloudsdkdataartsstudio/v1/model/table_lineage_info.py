# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableLineageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_guid': 'str',
        'source_qualified_name': 'str',
        'source_type': 'str',
        'source_db': 'str',
        'source_schema': 'str',
        'source_table': 'str',
        'target_guid': 'str',
        'target_qualified_name': 'str',
        'target_type': 'str',
        'target_db': 'str',
        'target_schema': 'str',
        'target_table': 'str',
        'node_guid': 'str',
        'node_name': 'str',
        'node_type': 'str',
        'node_qualified_name': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'source_guid': 'source_guid',
        'source_qualified_name': 'source_qualified_name',
        'source_type': 'source_type',
        'source_db': 'source_db',
        'source_schema': 'source_schema',
        'source_table': 'source_table',
        'target_guid': 'target_guid',
        'target_qualified_name': 'target_qualified_name',
        'target_type': 'target_type',
        'target_db': 'target_db',
        'target_schema': 'target_schema',
        'target_table': 'target_table',
        'node_guid': 'node_guid',
        'node_name': 'node_name',
        'node_type': 'node_type',
        'node_qualified_name': 'node_qualified_name',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, source_guid=None, source_qualified_name=None, source_type=None, source_db=None, source_schema=None, source_table=None, target_guid=None, target_qualified_name=None, target_type=None, target_db=None, target_schema=None, target_table=None, node_guid=None, node_name=None, node_type=None, node_qualified_name=None, workspace_id=None):
        """TableLineageInfo

        The model defined in huaweicloud sdk

        :param source_guid: 上游血缘资产guid
        :type source_guid: str
        :param source_qualified_name: 上游血缘资产Qname
        :type source_qualified_name: str
        :param source_type: 上游血缘资产类型
        :type source_type: str
        :param source_db: 上游血缘资产数据库
        :type source_db: str
        :param source_schema: 上游血缘资产逻辑库
        :type source_schema: str
        :param source_table: 上游血缘资产表
        :type source_table: str
        :param target_guid: 下游血缘资产guid
        :type target_guid: str
        :param target_qualified_name: 下游血缘资产Qname
        :type target_qualified_name: str
        :param target_type: 下游血缘资产类型
        :type target_type: str
        :param target_db: 下游血缘资产数据库
        :type target_db: str
        :param target_schema: 下游血缘资产逻辑库
        :type target_schema: str
        :param target_table: 下游血缘资产表
        :type target_table: str
        :param node_guid: 作业算子guid
        :type node_guid: str
        :param node_name: 作业算子名称
        :type node_name: str
        :param node_type: 作业算子类型
        :type node_type: str
        :param node_qualified_name: 作业算子Qname
        :type node_qualified_name: str
        :param workspace_id: 作业算子类型所属空间
        :type workspace_id: str
        """
        
        

        self._source_guid = None
        self._source_qualified_name = None
        self._source_type = None
        self._source_db = None
        self._source_schema = None
        self._source_table = None
        self._target_guid = None
        self._target_qualified_name = None
        self._target_type = None
        self._target_db = None
        self._target_schema = None
        self._target_table = None
        self._node_guid = None
        self._node_name = None
        self._node_type = None
        self._node_qualified_name = None
        self._workspace_id = None
        self.discriminator = None

        if source_guid is not None:
            self.source_guid = source_guid
        if source_qualified_name is not None:
            self.source_qualified_name = source_qualified_name
        if source_type is not None:
            self.source_type = source_type
        if source_db is not None:
            self.source_db = source_db
        if source_schema is not None:
            self.source_schema = source_schema
        if source_table is not None:
            self.source_table = source_table
        if target_guid is not None:
            self.target_guid = target_guid
        if target_qualified_name is not None:
            self.target_qualified_name = target_qualified_name
        if target_type is not None:
            self.target_type = target_type
        if target_db is not None:
            self.target_db = target_db
        if target_schema is not None:
            self.target_schema = target_schema
        if target_table is not None:
            self.target_table = target_table
        if node_guid is not None:
            self.node_guid = node_guid
        if node_name is not None:
            self.node_name = node_name
        if node_type is not None:
            self.node_type = node_type
        if node_qualified_name is not None:
            self.node_qualified_name = node_qualified_name
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def source_guid(self):
        """Gets the source_guid of this TableLineageInfo.

        上游血缘资产guid

        :return: The source_guid of this TableLineageInfo.
        :rtype: str
        """
        return self._source_guid

    @source_guid.setter
    def source_guid(self, source_guid):
        """Sets the source_guid of this TableLineageInfo.

        上游血缘资产guid

        :param source_guid: The source_guid of this TableLineageInfo.
        :type source_guid: str
        """
        self._source_guid = source_guid

    @property
    def source_qualified_name(self):
        """Gets the source_qualified_name of this TableLineageInfo.

        上游血缘资产Qname

        :return: The source_qualified_name of this TableLineageInfo.
        :rtype: str
        """
        return self._source_qualified_name

    @source_qualified_name.setter
    def source_qualified_name(self, source_qualified_name):
        """Sets the source_qualified_name of this TableLineageInfo.

        上游血缘资产Qname

        :param source_qualified_name: The source_qualified_name of this TableLineageInfo.
        :type source_qualified_name: str
        """
        self._source_qualified_name = source_qualified_name

    @property
    def source_type(self):
        """Gets the source_type of this TableLineageInfo.

        上游血缘资产类型

        :return: The source_type of this TableLineageInfo.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this TableLineageInfo.

        上游血缘资产类型

        :param source_type: The source_type of this TableLineageInfo.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_db(self):
        """Gets the source_db of this TableLineageInfo.

        上游血缘资产数据库

        :return: The source_db of this TableLineageInfo.
        :rtype: str
        """
        return self._source_db

    @source_db.setter
    def source_db(self, source_db):
        """Sets the source_db of this TableLineageInfo.

        上游血缘资产数据库

        :param source_db: The source_db of this TableLineageInfo.
        :type source_db: str
        """
        self._source_db = source_db

    @property
    def source_schema(self):
        """Gets the source_schema of this TableLineageInfo.

        上游血缘资产逻辑库

        :return: The source_schema of this TableLineageInfo.
        :rtype: str
        """
        return self._source_schema

    @source_schema.setter
    def source_schema(self, source_schema):
        """Sets the source_schema of this TableLineageInfo.

        上游血缘资产逻辑库

        :param source_schema: The source_schema of this TableLineageInfo.
        :type source_schema: str
        """
        self._source_schema = source_schema

    @property
    def source_table(self):
        """Gets the source_table of this TableLineageInfo.

        上游血缘资产表

        :return: The source_table of this TableLineageInfo.
        :rtype: str
        """
        return self._source_table

    @source_table.setter
    def source_table(self, source_table):
        """Sets the source_table of this TableLineageInfo.

        上游血缘资产表

        :param source_table: The source_table of this TableLineageInfo.
        :type source_table: str
        """
        self._source_table = source_table

    @property
    def target_guid(self):
        """Gets the target_guid of this TableLineageInfo.

        下游血缘资产guid

        :return: The target_guid of this TableLineageInfo.
        :rtype: str
        """
        return self._target_guid

    @target_guid.setter
    def target_guid(self, target_guid):
        """Sets the target_guid of this TableLineageInfo.

        下游血缘资产guid

        :param target_guid: The target_guid of this TableLineageInfo.
        :type target_guid: str
        """
        self._target_guid = target_guid

    @property
    def target_qualified_name(self):
        """Gets the target_qualified_name of this TableLineageInfo.

        下游血缘资产Qname

        :return: The target_qualified_name of this TableLineageInfo.
        :rtype: str
        """
        return self._target_qualified_name

    @target_qualified_name.setter
    def target_qualified_name(self, target_qualified_name):
        """Sets the target_qualified_name of this TableLineageInfo.

        下游血缘资产Qname

        :param target_qualified_name: The target_qualified_name of this TableLineageInfo.
        :type target_qualified_name: str
        """
        self._target_qualified_name = target_qualified_name

    @property
    def target_type(self):
        """Gets the target_type of this TableLineageInfo.

        下游血缘资产类型

        :return: The target_type of this TableLineageInfo.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this TableLineageInfo.

        下游血缘资产类型

        :param target_type: The target_type of this TableLineageInfo.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_db(self):
        """Gets the target_db of this TableLineageInfo.

        下游血缘资产数据库

        :return: The target_db of this TableLineageInfo.
        :rtype: str
        """
        return self._target_db

    @target_db.setter
    def target_db(self, target_db):
        """Sets the target_db of this TableLineageInfo.

        下游血缘资产数据库

        :param target_db: The target_db of this TableLineageInfo.
        :type target_db: str
        """
        self._target_db = target_db

    @property
    def target_schema(self):
        """Gets the target_schema of this TableLineageInfo.

        下游血缘资产逻辑库

        :return: The target_schema of this TableLineageInfo.
        :rtype: str
        """
        return self._target_schema

    @target_schema.setter
    def target_schema(self, target_schema):
        """Sets the target_schema of this TableLineageInfo.

        下游血缘资产逻辑库

        :param target_schema: The target_schema of this TableLineageInfo.
        :type target_schema: str
        """
        self._target_schema = target_schema

    @property
    def target_table(self):
        """Gets the target_table of this TableLineageInfo.

        下游血缘资产表

        :return: The target_table of this TableLineageInfo.
        :rtype: str
        """
        return self._target_table

    @target_table.setter
    def target_table(self, target_table):
        """Sets the target_table of this TableLineageInfo.

        下游血缘资产表

        :param target_table: The target_table of this TableLineageInfo.
        :type target_table: str
        """
        self._target_table = target_table

    @property
    def node_guid(self):
        """Gets the node_guid of this TableLineageInfo.

        作业算子guid

        :return: The node_guid of this TableLineageInfo.
        :rtype: str
        """
        return self._node_guid

    @node_guid.setter
    def node_guid(self, node_guid):
        """Sets the node_guid of this TableLineageInfo.

        作业算子guid

        :param node_guid: The node_guid of this TableLineageInfo.
        :type node_guid: str
        """
        self._node_guid = node_guid

    @property
    def node_name(self):
        """Gets the node_name of this TableLineageInfo.

        作业算子名称

        :return: The node_name of this TableLineageInfo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this TableLineageInfo.

        作业算子名称

        :param node_name: The node_name of this TableLineageInfo.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def node_type(self):
        """Gets the node_type of this TableLineageInfo.

        作业算子类型

        :return: The node_type of this TableLineageInfo.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this TableLineageInfo.

        作业算子类型

        :param node_type: The node_type of this TableLineageInfo.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def node_qualified_name(self):
        """Gets the node_qualified_name of this TableLineageInfo.

        作业算子Qname

        :return: The node_qualified_name of this TableLineageInfo.
        :rtype: str
        """
        return self._node_qualified_name

    @node_qualified_name.setter
    def node_qualified_name(self, node_qualified_name):
        """Sets the node_qualified_name of this TableLineageInfo.

        作业算子Qname

        :param node_qualified_name: The node_qualified_name of this TableLineageInfo.
        :type node_qualified_name: str
        """
        self._node_qualified_name = node_qualified_name

    @property
    def workspace_id(self):
        """Gets the workspace_id of this TableLineageInfo.

        作业算子类型所属空间

        :return: The workspace_id of this TableLineageInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this TableLineageInfo.

        作业算子类型所属空间

        :param workspace_id: The workspace_id of this TableLineageInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, TableLineageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
