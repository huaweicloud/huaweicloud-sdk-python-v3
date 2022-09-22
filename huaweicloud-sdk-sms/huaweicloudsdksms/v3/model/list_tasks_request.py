# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'name': 'str',
        'id': 'str',
        'source_server_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'state': 'state',
        'name': 'name',
        'id': 'id',
        'source_server_id': 'source_server_id',
        'limit': 'limit',
        'offset': 'offset',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, state=None, name=None, id=None, source_server_id=None, limit=None, offset=None, enterprise_project_id=None):
        """ListTasksRequest

        The model defined in huaweicloud sdk

        :param state: 迁移任务状态 READY:准备就绪 RUNNING:迁移中 SYNCING:同步中 MIGRATE_SUCCESS:迁移成功 MIGRATE_FAIL:迁移失败 ABORTING:中止中 ABORT:中止 DELETING::删除中 SYNC_F_ROLLBACKING:同步失败回滚中 SYNC_F_ROLLBACK_SUCCESS:同步失败回滚成功
        :type state: str
        :param name: 任务的名称
        :type name: str
        :param id: 任务的ID
        :type id: str
        :param source_server_id: 源端服务器的ID
        :type source_server_id: str
        :param limit: 每一页记录的任务数量
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param enterprise_project_id: 需要查询的企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._state = None
        self._name = None
        self._id = None
        self._source_server_id = None
        self._limit = None
        self._offset = None
        self._enterprise_project_id = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if source_server_id is not None:
            self.source_server_id = source_server_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def state(self):
        """Gets the state of this ListTasksRequest.

        迁移任务状态 READY:准备就绪 RUNNING:迁移中 SYNCING:同步中 MIGRATE_SUCCESS:迁移成功 MIGRATE_FAIL:迁移失败 ABORTING:中止中 ABORT:中止 DELETING::删除中 SYNC_F_ROLLBACKING:同步失败回滚中 SYNC_F_ROLLBACK_SUCCESS:同步失败回滚成功

        :return: The state of this ListTasksRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListTasksRequest.

        迁移任务状态 READY:准备就绪 RUNNING:迁移中 SYNCING:同步中 MIGRATE_SUCCESS:迁移成功 MIGRATE_FAIL:迁移失败 ABORTING:中止中 ABORT:中止 DELETING::删除中 SYNC_F_ROLLBACKING:同步失败回滚中 SYNC_F_ROLLBACK_SUCCESS:同步失败回滚成功

        :param state: The state of this ListTasksRequest.
        :type state: str
        """
        self._state = state

    @property
    def name(self):
        """Gets the name of this ListTasksRequest.

        任务的名称

        :return: The name of this ListTasksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTasksRequest.

        任务的名称

        :param name: The name of this ListTasksRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ListTasksRequest.

        任务的ID

        :return: The id of this ListTasksRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListTasksRequest.

        任务的ID

        :param id: The id of this ListTasksRequest.
        :type id: str
        """
        self._id = id

    @property
    def source_server_id(self):
        """Gets the source_server_id of this ListTasksRequest.

        源端服务器的ID

        :return: The source_server_id of this ListTasksRequest.
        :rtype: str
        """
        return self._source_server_id

    @source_server_id.setter
    def source_server_id(self, source_server_id):
        """Sets the source_server_id of this ListTasksRequest.

        源端服务器的ID

        :param source_server_id: The source_server_id of this ListTasksRequest.
        :type source_server_id: str
        """
        self._source_server_id = source_server_id

    @property
    def limit(self):
        """Gets the limit of this ListTasksRequest.

        每一页记录的任务数量

        :return: The limit of this ListTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTasksRequest.

        每一页记录的任务数量

        :param limit: The limit of this ListTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListTasksRequest.

        偏移量

        :return: The offset of this ListTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTasksRequest.

        偏移量

        :param offset: The offset of this ListTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListTasksRequest.

        需要查询的企业项目ID

        :return: The enterprise_project_id of this ListTasksRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListTasksRequest.

        需要查询的企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListTasksRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
