# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAvailableNodeTypeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'db_use_type': 'str',
        'job_direction': 'str',
        'node_type': 'str',
        'multi_write': 'str'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'db_use_type': 'db_use_type',
        'job_direction': 'job_direction',
        'node_type': 'node_type',
        'multi_write': 'multi_write'
    }

    def __init__(self, engine_type=None, db_use_type=None, job_direction=None, node_type=None, multi_write=None):
        """QueryAvailableNodeTypeReq

        The model defined in huaweicloud sdk

        :param engine_type: 引擎类型
        :type engine_type: str
        :param db_use_type: 迁移场景，migration-实时迁移,sync-实时同步,cloudDataGuard-实时灾备
        :type db_use_type: str
        :param job_direction: 迁移方向，up ：入云 ，灾备场景时对应本云为备，down：出云，灾备场景时对应本云为主，non-dbs：自建
        :type job_direction: str
        :param node_type: 规格类型。
        :type node_type: str
        :param multi_write: 是否是双主灾备，不填默认为false
        :type multi_write: str
        """
        
        

        self._engine_type = None
        self._db_use_type = None
        self._job_direction = None
        self._node_type = None
        self._multi_write = None
        self.discriminator = None

        self.engine_type = engine_type
        self.db_use_type = db_use_type
        self.job_direction = job_direction
        self.node_type = node_type
        if multi_write is not None:
            self.multi_write = multi_write

    @property
    def engine_type(self):
        """Gets the engine_type of this QueryAvailableNodeTypeReq.

        引擎类型

        :return: The engine_type of this QueryAvailableNodeTypeReq.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this QueryAvailableNodeTypeReq.

        引擎类型

        :param engine_type: The engine_type of this QueryAvailableNodeTypeReq.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def db_use_type(self):
        """Gets the db_use_type of this QueryAvailableNodeTypeReq.

        迁移场景，migration-实时迁移,sync-实时同步,cloudDataGuard-实时灾备

        :return: The db_use_type of this QueryAvailableNodeTypeReq.
        :rtype: str
        """
        return self._db_use_type

    @db_use_type.setter
    def db_use_type(self, db_use_type):
        """Sets the db_use_type of this QueryAvailableNodeTypeReq.

        迁移场景，migration-实时迁移,sync-实时同步,cloudDataGuard-实时灾备

        :param db_use_type: The db_use_type of this QueryAvailableNodeTypeReq.
        :type db_use_type: str
        """
        self._db_use_type = db_use_type

    @property
    def job_direction(self):
        """Gets the job_direction of this QueryAvailableNodeTypeReq.

        迁移方向，up ：入云 ，灾备场景时对应本云为备，down：出云，灾备场景时对应本云为主，non-dbs：自建

        :return: The job_direction of this QueryAvailableNodeTypeReq.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        """Sets the job_direction of this QueryAvailableNodeTypeReq.

        迁移方向，up ：入云 ，灾备场景时对应本云为备，down：出云，灾备场景时对应本云为主，non-dbs：自建

        :param job_direction: The job_direction of this QueryAvailableNodeTypeReq.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def node_type(self):
        """Gets the node_type of this QueryAvailableNodeTypeReq.

        规格类型。

        :return: The node_type of this QueryAvailableNodeTypeReq.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this QueryAvailableNodeTypeReq.

        规格类型。

        :param node_type: The node_type of this QueryAvailableNodeTypeReq.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def multi_write(self):
        """Gets the multi_write of this QueryAvailableNodeTypeReq.

        是否是双主灾备，不填默认为false

        :return: The multi_write of this QueryAvailableNodeTypeReq.
        :rtype: str
        """
        return self._multi_write

    @multi_write.setter
    def multi_write(self, multi_write):
        """Sets the multi_write of this QueryAvailableNodeTypeReq.

        是否是双主灾备，不填默认为false

        :param multi_write: The multi_write of this QueryAvailableNodeTypeReq.
        :type multi_write: str
        """
        self._multi_write = multi_write

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
        if not isinstance(other, QueryAvailableNodeTypeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
