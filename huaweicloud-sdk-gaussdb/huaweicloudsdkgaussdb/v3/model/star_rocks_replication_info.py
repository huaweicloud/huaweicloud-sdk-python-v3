# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StarRocksReplicationInfo:

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
        'task_name': 'str',
        'status': 'str',
        'stage': 'str',
        'percentage': 'str',
        'catchup_stage': 'str',
        'catchup_percentage': 'str'
    }

    attribute_map = {
        'source_database': 'source_database',
        'target_database': 'target_database',
        'task_name': 'task_name',
        'status': 'status',
        'stage': 'stage',
        'percentage': 'percentage',
        'catchup_stage': 'catchup_stage',
        'catchup_percentage': 'catchup_percentage'
    }

    def __init__(self, source_database=None, target_database=None, task_name=None, status=None, stage=None, percentage=None, catchup_stage=None, catchup_percentage=None):
        r"""StarRocksReplicationInfo

        The model defined in huaweicloud sdk

        :param source_database: TaurusDB数据库。
        :type source_database: str
        :param target_database: 目标数据库。
        :type target_database: str
        :param task_name: 同步任务名。
        :type task_name: str
        :param status: 当前状态。Yes:正常;No:异常。
        :type status: str
        :param stage: 同步阶段。wait:等待同步;incremental:增量同步;full:全量同步;cancelled:删除;paused:暂停同步。
        :type stage: str
        :param percentage: 进度百分比。
        :type percentage: str
        :param catchup_stage: 追赶阶段。wait:等待同步;incremental:增量同步;full:全量同步;cancelled:删除;paused:暂停同步。
        :type catchup_stage: str
        :param catchup_percentage: 追赶进度百分比。
        :type catchup_percentage: str
        """
        
        

        self._source_database = None
        self._target_database = None
        self._task_name = None
        self._status = None
        self._stage = None
        self._percentage = None
        self._catchup_stage = None
        self._catchup_percentage = None
        self.discriminator = None

        if source_database is not None:
            self.source_database = source_database
        if target_database is not None:
            self.target_database = target_database
        if task_name is not None:
            self.task_name = task_name
        if status is not None:
            self.status = status
        if stage is not None:
            self.stage = stage
        if percentage is not None:
            self.percentage = percentage
        if catchup_stage is not None:
            self.catchup_stage = catchup_stage
        if catchup_percentage is not None:
            self.catchup_percentage = catchup_percentage

    @property
    def source_database(self):
        r"""Gets the source_database of this StarRocksReplicationInfo.

        TaurusDB数据库。

        :return: The source_database of this StarRocksReplicationInfo.
        :rtype: str
        """
        return self._source_database

    @source_database.setter
    def source_database(self, source_database):
        r"""Sets the source_database of this StarRocksReplicationInfo.

        TaurusDB数据库。

        :param source_database: The source_database of this StarRocksReplicationInfo.
        :type source_database: str
        """
        self._source_database = source_database

    @property
    def target_database(self):
        r"""Gets the target_database of this StarRocksReplicationInfo.

        目标数据库。

        :return: The target_database of this StarRocksReplicationInfo.
        :rtype: str
        """
        return self._target_database

    @target_database.setter
    def target_database(self, target_database):
        r"""Sets the target_database of this StarRocksReplicationInfo.

        目标数据库。

        :param target_database: The target_database of this StarRocksReplicationInfo.
        :type target_database: str
        """
        self._target_database = target_database

    @property
    def task_name(self):
        r"""Gets the task_name of this StarRocksReplicationInfo.

        同步任务名。

        :return: The task_name of this StarRocksReplicationInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this StarRocksReplicationInfo.

        同步任务名。

        :param task_name: The task_name of this StarRocksReplicationInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def status(self):
        r"""Gets the status of this StarRocksReplicationInfo.

        当前状态。Yes:正常;No:异常。

        :return: The status of this StarRocksReplicationInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StarRocksReplicationInfo.

        当前状态。Yes:正常;No:异常。

        :param status: The status of this StarRocksReplicationInfo.
        :type status: str
        """
        self._status = status

    @property
    def stage(self):
        r"""Gets the stage of this StarRocksReplicationInfo.

        同步阶段。wait:等待同步;incremental:增量同步;full:全量同步;cancelled:删除;paused:暂停同步。

        :return: The stage of this StarRocksReplicationInfo.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this StarRocksReplicationInfo.

        同步阶段。wait:等待同步;incremental:增量同步;full:全量同步;cancelled:删除;paused:暂停同步。

        :param stage: The stage of this StarRocksReplicationInfo.
        :type stage: str
        """
        self._stage = stage

    @property
    def percentage(self):
        r"""Gets the percentage of this StarRocksReplicationInfo.

        进度百分比。

        :return: The percentage of this StarRocksReplicationInfo.
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        r"""Sets the percentage of this StarRocksReplicationInfo.

        进度百分比。

        :param percentage: The percentage of this StarRocksReplicationInfo.
        :type percentage: str
        """
        self._percentage = percentage

    @property
    def catchup_stage(self):
        r"""Gets the catchup_stage of this StarRocksReplicationInfo.

        追赶阶段。wait:等待同步;incremental:增量同步;full:全量同步;cancelled:删除;paused:暂停同步。

        :return: The catchup_stage of this StarRocksReplicationInfo.
        :rtype: str
        """
        return self._catchup_stage

    @catchup_stage.setter
    def catchup_stage(self, catchup_stage):
        r"""Sets the catchup_stage of this StarRocksReplicationInfo.

        追赶阶段。wait:等待同步;incremental:增量同步;full:全量同步;cancelled:删除;paused:暂停同步。

        :param catchup_stage: The catchup_stage of this StarRocksReplicationInfo.
        :type catchup_stage: str
        """
        self._catchup_stage = catchup_stage

    @property
    def catchup_percentage(self):
        r"""Gets the catchup_percentage of this StarRocksReplicationInfo.

        追赶进度百分比。

        :return: The catchup_percentage of this StarRocksReplicationInfo.
        :rtype: str
        """
        return self._catchup_percentage

    @catchup_percentage.setter
    def catchup_percentage(self, catchup_percentage):
        r"""Sets the catchup_percentage of this StarRocksReplicationInfo.

        追赶进度百分比。

        :param catchup_percentage: The catchup_percentage of this StarRocksReplicationInfo.
        :type catchup_percentage: str
        """
        self._catchup_percentage = catchup_percentage

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
        if not isinstance(other, StarRocksReplicationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
