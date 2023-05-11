# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'base_info': 'JobBaseInfo',
        'source_endpoint': 'list[JobEndpointInfo]',
        'target_endpoint': 'list[JobEndpointInfo]',
        'alarm_notify': 'AlarmNotifyConfig',
        'speed_limit': 'list[SpeedLimitInfo]',
        'user_migration': 'UserMigrationInfo',
        'policy_config': 'PolicyConfig',
        'db_object': 'DbObject',
        'db_param': 'DbParamInfo',
        'tuning_params': 'ModifyTuningParams',
        'period_order': 'PeriodOrderInfo',
        'node_info': 'JobNodeInfo'
    }

    attribute_map = {
        'job_id': 'job_id',
        'base_info': 'base_info',
        'source_endpoint': 'source_endpoint',
        'target_endpoint': 'target_endpoint',
        'alarm_notify': 'alarm_notify',
        'speed_limit': 'speed_limit',
        'user_migration': 'user_migration',
        'policy_config': 'policy_config',
        'db_object': 'db_object',
        'db_param': 'db_param',
        'tuning_params': 'tuning_params',
        'period_order': 'period_order',
        'node_info': 'node_info'
    }

    def __init__(self, job_id=None, base_info=None, source_endpoint=None, target_endpoint=None, alarm_notify=None, speed_limit=None, user_migration=None, policy_config=None, db_object=None, db_param=None, tuning_params=None, period_order=None, node_info=None):
        """UpdateJob

        The model defined in huaweicloud sdk

        :param job_id: 待更新的任务ID。
        :type job_id: str
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        :param source_endpoint: 任务源数据库信息体。
        :type source_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        :param target_endpoint: 任务目标数据库信息体。
        :type target_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        :param alarm_notify: 
        :type alarm_notify: :class:`huaweicloudsdkdrs.v5.AlarmNotifyConfig`
        :param speed_limit: 限速信息体。 - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。 - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。
        :type speed_limit: list[:class:`huaweicloudsdkdrs.v5.SpeedLimitInfo`]
        :param user_migration: 
        :type user_migration: :class:`huaweicloudsdkdrs.v5.UserMigrationInfo`
        :param policy_config: 
        :type policy_config: :class:`huaweicloudsdkdrs.v5.PolicyConfig`
        :param db_object: 
        :type db_object: :class:`huaweicloudsdkdrs.v5.DbObject`
        :param db_param: 
        :type db_param: :class:`huaweicloudsdkdrs.v5.DbParamInfo`
        :param tuning_params: 
        :type tuning_params: :class:`huaweicloudsdkdrs.v5.ModifyTuningParams`
        :param period_order: 
        :type period_order: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        :param node_info: 
        :type node_info: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        """
        
        

        self._job_id = None
        self._base_info = None
        self._source_endpoint = None
        self._target_endpoint = None
        self._alarm_notify = None
        self._speed_limit = None
        self._user_migration = None
        self._policy_config = None
        self._db_object = None
        self._db_param = None
        self._tuning_params = None
        self._period_order = None
        self._node_info = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if base_info is not None:
            self.base_info = base_info
        if source_endpoint is not None:
            self.source_endpoint = source_endpoint
        if target_endpoint is not None:
            self.target_endpoint = target_endpoint
        if alarm_notify is not None:
            self.alarm_notify = alarm_notify
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if user_migration is not None:
            self.user_migration = user_migration
        if policy_config is not None:
            self.policy_config = policy_config
        if db_object is not None:
            self.db_object = db_object
        if db_param is not None:
            self.db_param = db_param
        if tuning_params is not None:
            self.tuning_params = tuning_params
        if period_order is not None:
            self.period_order = period_order
        if node_info is not None:
            self.node_info = node_info

    @property
    def job_id(self):
        """Gets the job_id of this UpdateJob.

        待更新的任务ID。

        :return: The job_id of this UpdateJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateJob.

        待更新的任务ID。

        :param job_id: The job_id of this UpdateJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def base_info(self):
        """Gets the base_info of this UpdateJob.

        :return: The base_info of this UpdateJob.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        """Sets the base_info of this UpdateJob.

        :param base_info: The base_info of this UpdateJob.
        :type base_info: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        """
        self._base_info = base_info

    @property
    def source_endpoint(self):
        """Gets the source_endpoint of this UpdateJob.

        任务源数据库信息体。

        :return: The source_endpoint of this UpdateJob.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        """Sets the source_endpoint of this UpdateJob.

        任务源数据库信息体。

        :param source_endpoint: The source_endpoint of this UpdateJob.
        :type source_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        self._source_endpoint = source_endpoint

    @property
    def target_endpoint(self):
        """Gets the target_endpoint of this UpdateJob.

        任务目标数据库信息体。

        :return: The target_endpoint of this UpdateJob.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        return self._target_endpoint

    @target_endpoint.setter
    def target_endpoint(self, target_endpoint):
        """Sets the target_endpoint of this UpdateJob.

        任务目标数据库信息体。

        :param target_endpoint: The target_endpoint of this UpdateJob.
        :type target_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        self._target_endpoint = target_endpoint

    @property
    def alarm_notify(self):
        """Gets the alarm_notify of this UpdateJob.

        :return: The alarm_notify of this UpdateJob.
        :rtype: :class:`huaweicloudsdkdrs.v5.AlarmNotifyConfig`
        """
        return self._alarm_notify

    @alarm_notify.setter
    def alarm_notify(self, alarm_notify):
        """Sets the alarm_notify of this UpdateJob.

        :param alarm_notify: The alarm_notify of this UpdateJob.
        :type alarm_notify: :class:`huaweicloudsdkdrs.v5.AlarmNotifyConfig`
        """
        self._alarm_notify = alarm_notify

    @property
    def speed_limit(self):
        """Gets the speed_limit of this UpdateJob.

        限速信息体。 - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。 - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。

        :return: The speed_limit of this UpdateJob.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.SpeedLimitInfo`]
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        """Sets the speed_limit of this UpdateJob.

        限速信息体。 - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。 - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。

        :param speed_limit: The speed_limit of this UpdateJob.
        :type speed_limit: list[:class:`huaweicloudsdkdrs.v5.SpeedLimitInfo`]
        """
        self._speed_limit = speed_limit

    @property
    def user_migration(self):
        """Gets the user_migration of this UpdateJob.

        :return: The user_migration of this UpdateJob.
        :rtype: :class:`huaweicloudsdkdrs.v5.UserMigrationInfo`
        """
        return self._user_migration

    @user_migration.setter
    def user_migration(self, user_migration):
        """Sets the user_migration of this UpdateJob.

        :param user_migration: The user_migration of this UpdateJob.
        :type user_migration: :class:`huaweicloudsdkdrs.v5.UserMigrationInfo`
        """
        self._user_migration = user_migration

    @property
    def policy_config(self):
        """Gets the policy_config of this UpdateJob.

        :return: The policy_config of this UpdateJob.
        :rtype: :class:`huaweicloudsdkdrs.v5.PolicyConfig`
        """
        return self._policy_config

    @policy_config.setter
    def policy_config(self, policy_config):
        """Sets the policy_config of this UpdateJob.

        :param policy_config: The policy_config of this UpdateJob.
        :type policy_config: :class:`huaweicloudsdkdrs.v5.PolicyConfig`
        """
        self._policy_config = policy_config

    @property
    def db_object(self):
        """Gets the db_object of this UpdateJob.

        :return: The db_object of this UpdateJob.
        :rtype: :class:`huaweicloudsdkdrs.v5.DbObject`
        """
        return self._db_object

    @db_object.setter
    def db_object(self, db_object):
        """Sets the db_object of this UpdateJob.

        :param db_object: The db_object of this UpdateJob.
        :type db_object: :class:`huaweicloudsdkdrs.v5.DbObject`
        """
        self._db_object = db_object

    @property
    def db_param(self):
        """Gets the db_param of this UpdateJob.

        :return: The db_param of this UpdateJob.
        :rtype: :class:`huaweicloudsdkdrs.v5.DbParamInfo`
        """
        return self._db_param

    @db_param.setter
    def db_param(self, db_param):
        """Sets the db_param of this UpdateJob.

        :param db_param: The db_param of this UpdateJob.
        :type db_param: :class:`huaweicloudsdkdrs.v5.DbParamInfo`
        """
        self._db_param = db_param

    @property
    def tuning_params(self):
        """Gets the tuning_params of this UpdateJob.

        :return: The tuning_params of this UpdateJob.
        :rtype: :class:`huaweicloudsdkdrs.v5.ModifyTuningParams`
        """
        return self._tuning_params

    @tuning_params.setter
    def tuning_params(self, tuning_params):
        """Sets the tuning_params of this UpdateJob.

        :param tuning_params: The tuning_params of this UpdateJob.
        :type tuning_params: :class:`huaweicloudsdkdrs.v5.ModifyTuningParams`
        """
        self._tuning_params = tuning_params

    @property
    def period_order(self):
        """Gets the period_order of this UpdateJob.

        :return: The period_order of this UpdateJob.
        :rtype: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        """
        return self._period_order

    @period_order.setter
    def period_order(self, period_order):
        """Sets the period_order of this UpdateJob.

        :param period_order: The period_order of this UpdateJob.
        :type period_order: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        """
        self._period_order = period_order

    @property
    def node_info(self):
        """Gets the node_info of this UpdateJob.

        :return: The node_info of this UpdateJob.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        """Sets the node_info of this UpdateJob.

        :param node_info: The node_info of this UpdateJob.
        :type node_info: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        """
        self._node_info = node_info

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
        if not isinstance(other, UpdateJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
