# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChDatabaseReplicationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_database': 'str',
        'target_database': 'str',
        'status': 'str',
        'stage': 'str',
        'percentage': 'str',
        'catchup_stage': 'str'
    }

    attribute_map = {
        'source_database': 'source_database',
        'target_database': 'target_database',
        'status': 'status',
        'stage': 'stage',
        'percentage': 'percentage',
        'catchup_stage': 'catchup_stage'
    }

    def __init__(self, source_database=None, target_database=None, status=None, stage=None, percentage=None, catchup_stage=None):
        """ChDatabaseReplicationInfo

        The model defined in huaweicloud sdk

        :param source_database: 源数据库。
        :type source_database: str
        :param target_database: 目标数据库。
        :type target_database: str
        :param status: 当前状态。 取值范围： - normal：正常 - abnormal：异常
        :type status: str
        :param stage: 同步阶段。 取值范围： - wait：等待同步 - failed：同步失败 - incremental：增量同步 - full：全量同步 - other：其他
        :type stage: str
        :param percentage: 进度百分比。
        :type percentage: str
        :param catchup_stage: 追赶阶段。 取值范围： - wait：等待同步 - failed：同步失败 - incremental：增量同步 - full：全量同步 - other：其他
        :type catchup_stage: str
        """
        
        

        self._source_database = None
        self._target_database = None
        self._status = None
        self._stage = None
        self._percentage = None
        self._catchup_stage = None
        self.discriminator = None

        self.source_database = source_database
        self.target_database = target_database
        self.status = status
        self.stage = stage
        self.percentage = percentage
        self.catchup_stage = catchup_stage

    @property
    def source_database(self):
        """Gets the source_database of this ChDatabaseReplicationInfo.

        源数据库。

        :return: The source_database of this ChDatabaseReplicationInfo.
        :rtype: str
        """
        return self._source_database

    @source_database.setter
    def source_database(self, source_database):
        """Sets the source_database of this ChDatabaseReplicationInfo.

        源数据库。

        :param source_database: The source_database of this ChDatabaseReplicationInfo.
        :type source_database: str
        """
        self._source_database = source_database

    @property
    def target_database(self):
        """Gets the target_database of this ChDatabaseReplicationInfo.

        目标数据库。

        :return: The target_database of this ChDatabaseReplicationInfo.
        :rtype: str
        """
        return self._target_database

    @target_database.setter
    def target_database(self, target_database):
        """Sets the target_database of this ChDatabaseReplicationInfo.

        目标数据库。

        :param target_database: The target_database of this ChDatabaseReplicationInfo.
        :type target_database: str
        """
        self._target_database = target_database

    @property
    def status(self):
        """Gets the status of this ChDatabaseReplicationInfo.

        当前状态。 取值范围： - normal：正常 - abnormal：异常

        :return: The status of this ChDatabaseReplicationInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChDatabaseReplicationInfo.

        当前状态。 取值范围： - normal：正常 - abnormal：异常

        :param status: The status of this ChDatabaseReplicationInfo.
        :type status: str
        """
        self._status = status

    @property
    def stage(self):
        """Gets the stage of this ChDatabaseReplicationInfo.

        同步阶段。 取值范围： - wait：等待同步 - failed：同步失败 - incremental：增量同步 - full：全量同步 - other：其他

        :return: The stage of this ChDatabaseReplicationInfo.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        """Sets the stage of this ChDatabaseReplicationInfo.

        同步阶段。 取值范围： - wait：等待同步 - failed：同步失败 - incremental：增量同步 - full：全量同步 - other：其他

        :param stage: The stage of this ChDatabaseReplicationInfo.
        :type stage: str
        """
        self._stage = stage

    @property
    def percentage(self):
        """Gets the percentage of this ChDatabaseReplicationInfo.

        进度百分比。

        :return: The percentage of this ChDatabaseReplicationInfo.
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this ChDatabaseReplicationInfo.

        进度百分比。

        :param percentage: The percentage of this ChDatabaseReplicationInfo.
        :type percentage: str
        """
        self._percentage = percentage

    @property
    def catchup_stage(self):
        """Gets the catchup_stage of this ChDatabaseReplicationInfo.

        追赶阶段。 取值范围： - wait：等待同步 - failed：同步失败 - incremental：增量同步 - full：全量同步 - other：其他

        :return: The catchup_stage of this ChDatabaseReplicationInfo.
        :rtype: str
        """
        return self._catchup_stage

    @catchup_stage.setter
    def catchup_stage(self, catchup_stage):
        """Sets the catchup_stage of this ChDatabaseReplicationInfo.

        追赶阶段。 取值范围： - wait：等待同步 - failed：同步失败 - incremental：增量同步 - full：全量同步 - other：其他

        :param catchup_stage: The catchup_stage of this ChDatabaseReplicationInfo.
        :type catchup_stage: str
        """
        self._catchup_stage = catchup_stage

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
        if not isinstance(other, ChDatabaseReplicationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
