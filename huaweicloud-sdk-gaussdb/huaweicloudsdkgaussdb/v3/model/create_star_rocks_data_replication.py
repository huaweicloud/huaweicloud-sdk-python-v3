# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStarRocksDataReplication:

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
        'source_database': 'str',
        'target_database': 'str',
        'task_name': 'str'
    }

    attribute_map = {
        'source_instance_id': 'source_instance_id',
        'source_node_id': 'source_node_id',
        'source_database': 'source_database',
        'target_database': 'target_database',
        'task_name': 'task_name'
    }

    def __init__(self, source_instance_id=None, source_node_id=None, source_database=None, target_database=None, task_name=None):
        r"""CreateStarRocksDataReplication

        The model defined in huaweicloud sdk

        :param source_instance_id: TaurusDB实例ID。
        :type source_instance_id: str
        :param source_node_id: TaurusDB只读节点ID。如为空，则取TaurusDB主节点ID
        :type source_node_id: str
        :param source_database: 源数据库。
        :type source_database: str
        :param target_database: 目标数据库。 字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线_。
        :type target_database: str
        :param task_name: 同步任务名。 字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线_。
        :type task_name: str
        """
        
        

        self._source_instance_id = None
        self._source_node_id = None
        self._source_database = None
        self._target_database = None
        self._task_name = None
        self.discriminator = None

        self.source_instance_id = source_instance_id
        if source_node_id is not None:
            self.source_node_id = source_node_id
        self.source_database = source_database
        self.target_database = target_database
        self.task_name = task_name

    @property
    def source_instance_id(self):
        r"""Gets the source_instance_id of this CreateStarRocksDataReplication.

        TaurusDB实例ID。

        :return: The source_instance_id of this CreateStarRocksDataReplication.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        r"""Sets the source_instance_id of this CreateStarRocksDataReplication.

        TaurusDB实例ID。

        :param source_instance_id: The source_instance_id of this CreateStarRocksDataReplication.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def source_node_id(self):
        r"""Gets the source_node_id of this CreateStarRocksDataReplication.

        TaurusDB只读节点ID。如为空，则取TaurusDB主节点ID

        :return: The source_node_id of this CreateStarRocksDataReplication.
        :rtype: str
        """
        return self._source_node_id

    @source_node_id.setter
    def source_node_id(self, source_node_id):
        r"""Sets the source_node_id of this CreateStarRocksDataReplication.

        TaurusDB只读节点ID。如为空，则取TaurusDB主节点ID

        :param source_node_id: The source_node_id of this CreateStarRocksDataReplication.
        :type source_node_id: str
        """
        self._source_node_id = source_node_id

    @property
    def source_database(self):
        r"""Gets the source_database of this CreateStarRocksDataReplication.

        源数据库。

        :return: The source_database of this CreateStarRocksDataReplication.
        :rtype: str
        """
        return self._source_database

    @source_database.setter
    def source_database(self, source_database):
        r"""Sets the source_database of this CreateStarRocksDataReplication.

        源数据库。

        :param source_database: The source_database of this CreateStarRocksDataReplication.
        :type source_database: str
        """
        self._source_database = source_database

    @property
    def target_database(self):
        r"""Gets the target_database of this CreateStarRocksDataReplication.

        目标数据库。 字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线_。

        :return: The target_database of this CreateStarRocksDataReplication.
        :rtype: str
        """
        return self._target_database

    @target_database.setter
    def target_database(self, target_database):
        r"""Sets the target_database of this CreateStarRocksDataReplication.

        目标数据库。 字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线_。

        :param target_database: The target_database of this CreateStarRocksDataReplication.
        :type target_database: str
        """
        self._target_database = target_database

    @property
    def task_name(self):
        r"""Gets the task_name of this CreateStarRocksDataReplication.

        同步任务名。 字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线_。

        :return: The task_name of this CreateStarRocksDataReplication.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this CreateStarRocksDataReplication.

        同步任务名。 字符长度限制3~128位，仅支持英文大小写字母、数字以及下划线_。

        :param task_name: The task_name of this CreateStarRocksDataReplication.
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
        if not isinstance(other, CreateStarRocksDataReplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
