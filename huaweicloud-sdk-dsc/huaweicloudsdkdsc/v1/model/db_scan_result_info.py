# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbScanResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'db_name': 'str',
        'table_id': 'str',
        'table_name': 'str',
        'risk_level': 'int',
        'sensitive_data_type': 'list[str]',
        'match_info': 'list[DbMatchInfo]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'db_name': 'db_name',
        'table_id': 'table_id',
        'table_name': 'table_name',
        'risk_level': 'risk_level',
        'sensitive_data_type': 'sensitive_data_type',
        'match_info': 'match_info'
    }

    def __init__(self, task_id=None, db_name=None, table_id=None, table_name=None, risk_level=None, sensitive_data_type=None, match_info=None):
        """DbScanResultInfo

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param db_name: 数据库名称
        :type db_name: str
        :param table_id: 表ID
        :type table_id: str
        :param table_name: 表名称
        :type table_name: str
        :param risk_level: 风险等级
        :type risk_level: int
        :param sensitive_data_type: 匹配到的规则
        :type sensitive_data_type: list[str]
        :param match_info: 表中各列匹配到的规则
        :type match_info: list[:class:`huaweicloudsdkdsc.v1.DbMatchInfo`]
        """
        
        

        self._task_id = None
        self._db_name = None
        self._table_id = None
        self._table_name = None
        self._risk_level = None
        self._sensitive_data_type = None
        self._match_info = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if db_name is not None:
            self.db_name = db_name
        if table_id is not None:
            self.table_id = table_id
        if table_name is not None:
            self.table_name = table_name
        if risk_level is not None:
            self.risk_level = risk_level
        if sensitive_data_type is not None:
            self.sensitive_data_type = sensitive_data_type
        if match_info is not None:
            self.match_info = match_info

    @property
    def task_id(self):
        """Gets the task_id of this DbScanResultInfo.

        任务ID

        :return: The task_id of this DbScanResultInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this DbScanResultInfo.

        任务ID

        :param task_id: The task_id of this DbScanResultInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def db_name(self):
        """Gets the db_name of this DbScanResultInfo.

        数据库名称

        :return: The db_name of this DbScanResultInfo.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this DbScanResultInfo.

        数据库名称

        :param db_name: The db_name of this DbScanResultInfo.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_id(self):
        """Gets the table_id of this DbScanResultInfo.

        表ID

        :return: The table_id of this DbScanResultInfo.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this DbScanResultInfo.

        表ID

        :param table_id: The table_id of this DbScanResultInfo.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def table_name(self):
        """Gets the table_name of this DbScanResultInfo.

        表名称

        :return: The table_name of this DbScanResultInfo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this DbScanResultInfo.

        表名称

        :param table_name: The table_name of this DbScanResultInfo.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def risk_level(self):
        """Gets the risk_level of this DbScanResultInfo.

        风险等级

        :return: The risk_level of this DbScanResultInfo.
        :rtype: int
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """Sets the risk_level of this DbScanResultInfo.

        风险等级

        :param risk_level: The risk_level of this DbScanResultInfo.
        :type risk_level: int
        """
        self._risk_level = risk_level

    @property
    def sensitive_data_type(self):
        """Gets the sensitive_data_type of this DbScanResultInfo.

        匹配到的规则

        :return: The sensitive_data_type of this DbScanResultInfo.
        :rtype: list[str]
        """
        return self._sensitive_data_type

    @sensitive_data_type.setter
    def sensitive_data_type(self, sensitive_data_type):
        """Sets the sensitive_data_type of this DbScanResultInfo.

        匹配到的规则

        :param sensitive_data_type: The sensitive_data_type of this DbScanResultInfo.
        :type sensitive_data_type: list[str]
        """
        self._sensitive_data_type = sensitive_data_type

    @property
    def match_info(self):
        """Gets the match_info of this DbScanResultInfo.

        表中各列匹配到的规则

        :return: The match_info of this DbScanResultInfo.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.DbMatchInfo`]
        """
        return self._match_info

    @match_info.setter
    def match_info(self, match_info):
        """Sets the match_info of this DbScanResultInfo.

        表中各列匹配到的规则

        :param match_info: The match_info of this DbScanResultInfo.
        :type match_info: list[:class:`huaweicloudsdkdsc.v1.DbMatchInfo`]
        """
        self._match_info = match_info

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
        if not isinstance(other, DbScanResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
