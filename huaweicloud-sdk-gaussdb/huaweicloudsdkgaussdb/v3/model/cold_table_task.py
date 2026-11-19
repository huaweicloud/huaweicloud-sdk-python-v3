# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColdTableTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'table_name': 'str',
        'partition_name': 'str',
        'status': 'str',
        'target_storage': 'str',
        'percent': 'float',
        'total_cnt': 'float',
        'space_id': 'str',
        'version': 'str'
    }

    attribute_map = {
        'db_name': 'db_name',
        'table_name': 'table_name',
        'partition_name': 'partition_name',
        'status': 'status',
        'target_storage': 'target_storage',
        'percent': 'percent',
        'total_cnt': 'total_cnt',
        'space_id': 'space_id',
        'version': 'version'
    }

    def __init__(self, db_name=None, table_name=None, partition_name=None, status=None, target_storage=None, percent=None, total_cnt=None, space_id=None, version=None):
        r"""ColdTableTask

        The model defined in huaweicloud sdk

        :param db_name: **参数解释**：  数据库名。  **取值范围**：  不涉及。
        :type db_name: str
        :param table_name: **参数解释**：  表名。  **取值范围**：  不涉及。
        :type table_name: str
        :param partition_name: **参数解释**：  分区名，为空表示无分区表。  **取值范围**：  不涉及。
        :type partition_name: str
        :param status: **参数解释**：  任务状态。  **取值范围**：  - BEGIN：开始。 - RUNNING：进行中。 - FINISH：已完成。 - FAIL：失败。 - REVOKE：回滚。
        :type status: str
        :param target_storage: **参数解释**：  操作类型。  **取值范围**：  - OBS：创建冷表。 - SLICE：回迁冷表。
        :type target_storage: str
        :param percent: **参数解释**：  任务进度百分比。  **取值范围**：  0-1。
        :type percent: float
        :param total_cnt: **参数解释**：  对象数。  **取值范围**：  非负数。
        :type total_cnt: float
        :param space_id: **参数解释**：  表空间ID。  **取值范围**：  不涉及。
        :type space_id: str
        :param version: **参数解释**：  冷表版本。  **取值范围**：  不涉及。
        :type version: str
        """
        
        

        self._db_name = None
        self._table_name = None
        self._partition_name = None
        self._status = None
        self._target_storage = None
        self._percent = None
        self._total_cnt = None
        self._space_id = None
        self._version = None
        self.discriminator = None

        self.db_name = db_name
        self.table_name = table_name
        if partition_name is not None:
            self.partition_name = partition_name
        self.status = status
        if target_storage is not None:
            self.target_storage = target_storage
        if percent is not None:
            self.percent = percent
        if total_cnt is not None:
            self.total_cnt = total_cnt
        if space_id is not None:
            self.space_id = space_id
        if version is not None:
            self.version = version

    @property
    def db_name(self):
        r"""Gets the db_name of this ColdTableTask.

        **参数解释**：  数据库名。  **取值范围**：  不涉及。

        :return: The db_name of this ColdTableTask.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ColdTableTask.

        **参数解释**：  数据库名。  **取值范围**：  不涉及。

        :param db_name: The db_name of this ColdTableTask.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ColdTableTask.

        **参数解释**：  表名。  **取值范围**：  不涉及。

        :return: The table_name of this ColdTableTask.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ColdTableTask.

        **参数解释**：  表名。  **取值范围**：  不涉及。

        :param table_name: The table_name of this ColdTableTask.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def partition_name(self):
        r"""Gets the partition_name of this ColdTableTask.

        **参数解释**：  分区名，为空表示无分区表。  **取值范围**：  不涉及。

        :return: The partition_name of this ColdTableTask.
        :rtype: str
        """
        return self._partition_name

    @partition_name.setter
    def partition_name(self, partition_name):
        r"""Sets the partition_name of this ColdTableTask.

        **参数解释**：  分区名，为空表示无分区表。  **取值范围**：  不涉及。

        :param partition_name: The partition_name of this ColdTableTask.
        :type partition_name: str
        """
        self._partition_name = partition_name

    @property
    def status(self):
        r"""Gets the status of this ColdTableTask.

        **参数解释**：  任务状态。  **取值范围**：  - BEGIN：开始。 - RUNNING：进行中。 - FINISH：已完成。 - FAIL：失败。 - REVOKE：回滚。

        :return: The status of this ColdTableTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ColdTableTask.

        **参数解释**：  任务状态。  **取值范围**：  - BEGIN：开始。 - RUNNING：进行中。 - FINISH：已完成。 - FAIL：失败。 - REVOKE：回滚。

        :param status: The status of this ColdTableTask.
        :type status: str
        """
        self._status = status

    @property
    def target_storage(self):
        r"""Gets the target_storage of this ColdTableTask.

        **参数解释**：  操作类型。  **取值范围**：  - OBS：创建冷表。 - SLICE：回迁冷表。

        :return: The target_storage of this ColdTableTask.
        :rtype: str
        """
        return self._target_storage

    @target_storage.setter
    def target_storage(self, target_storage):
        r"""Sets the target_storage of this ColdTableTask.

        **参数解释**：  操作类型。  **取值范围**：  - OBS：创建冷表。 - SLICE：回迁冷表。

        :param target_storage: The target_storage of this ColdTableTask.
        :type target_storage: str
        """
        self._target_storage = target_storage

    @property
    def percent(self):
        r"""Gets the percent of this ColdTableTask.

        **参数解释**：  任务进度百分比。  **取值范围**：  0-1。

        :return: The percent of this ColdTableTask.
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        r"""Sets the percent of this ColdTableTask.

        **参数解释**：  任务进度百分比。  **取值范围**：  0-1。

        :param percent: The percent of this ColdTableTask.
        :type percent: float
        """
        self._percent = percent

    @property
    def total_cnt(self):
        r"""Gets the total_cnt of this ColdTableTask.

        **参数解释**：  对象数。  **取值范围**：  非负数。

        :return: The total_cnt of this ColdTableTask.
        :rtype: float
        """
        return self._total_cnt

    @total_cnt.setter
    def total_cnt(self, total_cnt):
        r"""Sets the total_cnt of this ColdTableTask.

        **参数解释**：  对象数。  **取值范围**：  非负数。

        :param total_cnt: The total_cnt of this ColdTableTask.
        :type total_cnt: float
        """
        self._total_cnt = total_cnt

    @property
    def space_id(self):
        r"""Gets the space_id of this ColdTableTask.

        **参数解释**：  表空间ID。  **取值范围**：  不涉及。

        :return: The space_id of this ColdTableTask.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        r"""Sets the space_id of this ColdTableTask.

        **参数解释**：  表空间ID。  **取值范围**：  不涉及。

        :param space_id: The space_id of this ColdTableTask.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def version(self):
        r"""Gets the version of this ColdTableTask.

        **参数解释**：  冷表版本。  **取值范围**：  不涉及。

        :return: The version of this ColdTableTask.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ColdTableTask.

        **参数解释**：  冷表版本。  **取值范围**：  不涉及。

        :param version: The version of this ColdTableTask.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ColdTableTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
