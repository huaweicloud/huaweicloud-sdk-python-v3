# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsyncCreateJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_info': 'JobBaseInfo',
        'source_endpoint': 'list[JobEndpointInfo]',
        'target_endpoint': 'list[JobEndpointInfo]',
        'alarm_notify': 'AlarmNotifyConfig',
        'speed_limit': 'list[SpeedLimitInfo]',
        'user_migration': 'UserMigrationInfo',
        'policy_config': 'PolicyConfig',
        'db_object': 'DbObject',
        'db_param': 'DbParamInfo',
        'tuning_params': 'TuningParamInfo',
        'period_order': 'PeriodOrderInfo',
        'node_info': 'JobNodeInfo',
        'public_ip_list': 'list[PublicIpConfig]'
    }

    attribute_map = {
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
        'node_info': 'node_info',
        'public_ip_list': 'public_ip_list'
    }

    def __init__(self, base_info=None, source_endpoint=None, target_endpoint=None, alarm_notify=None, speed_limit=None, user_migration=None, policy_config=None, db_object=None, db_param=None, tuning_params=None, period_order=None, node_info=None, public_ip_list=None):
        r"""AsyncCreateJobReq

        The model defined in huaweicloud sdk

        :param base_info: 
        :type base_info: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        :param source_endpoint: 创建任务数据库信息体。
        :type source_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        :param target_endpoint: 创建任务数据库信息体。
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
        :type tuning_params: :class:`huaweicloudsdkdrs.v5.TuningParamInfo`
        :param period_order: 
        :type period_order: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        :param node_info: 
        :type node_info: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        :param public_ip_list: 指定公网IP的信息
        :type public_ip_list: list[:class:`huaweicloudsdkdrs.v5.PublicIpConfig`]
        """
        
        

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
        self._public_ip_list = None
        self.discriminator = None

        self.base_info = base_info
        self.source_endpoint = source_endpoint
        self.target_endpoint = target_endpoint
        if alarm_notify is not None:
            self.alarm_notify = alarm_notify
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if user_migration is not None:
            self.user_migration = user_migration
        self.policy_config = policy_config
        self.db_object = db_object
        if db_param is not None:
            self.db_param = db_param
        if tuning_params is not None:
            self.tuning_params = tuning_params
        if period_order is not None:
            self.period_order = period_order
        self.node_info = node_info
        if public_ip_list is not None:
            self.public_ip_list = public_ip_list

    @property
    def base_info(self):
        r"""Gets the base_info of this AsyncCreateJobReq.

        :return: The base_info of this AsyncCreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this AsyncCreateJobReq.

        :param base_info: The base_info of this AsyncCreateJobReq.
        :type base_info: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        """
        self._base_info = base_info

    @property
    def source_endpoint(self):
        r"""Gets the source_endpoint of this AsyncCreateJobReq.

        创建任务数据库信息体。

        :return: The source_endpoint of this AsyncCreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        r"""Sets the source_endpoint of this AsyncCreateJobReq.

        创建任务数据库信息体。

        :param source_endpoint: The source_endpoint of this AsyncCreateJobReq.
        :type source_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        self._source_endpoint = source_endpoint

    @property
    def target_endpoint(self):
        r"""Gets the target_endpoint of this AsyncCreateJobReq.

        创建任务数据库信息体。

        :return: The target_endpoint of this AsyncCreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        return self._target_endpoint

    @target_endpoint.setter
    def target_endpoint(self, target_endpoint):
        r"""Sets the target_endpoint of this AsyncCreateJobReq.

        创建任务数据库信息体。

        :param target_endpoint: The target_endpoint of this AsyncCreateJobReq.
        :type target_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        self._target_endpoint = target_endpoint

    @property
    def alarm_notify(self):
        r"""Gets the alarm_notify of this AsyncCreateJobReq.

        :return: The alarm_notify of this AsyncCreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.AlarmNotifyConfig`
        """
        return self._alarm_notify

    @alarm_notify.setter
    def alarm_notify(self, alarm_notify):
        r"""Sets the alarm_notify of this AsyncCreateJobReq.

        :param alarm_notify: The alarm_notify of this AsyncCreateJobReq.
        :type alarm_notify: :class:`huaweicloudsdkdrs.v5.AlarmNotifyConfig`
        """
        self._alarm_notify = alarm_notify

    @property
    def speed_limit(self):
        r"""Gets the speed_limit of this AsyncCreateJobReq.

        限速信息体。 - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。 - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。

        :return: The speed_limit of this AsyncCreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.SpeedLimitInfo`]
        """
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, speed_limit):
        r"""Sets the speed_limit of this AsyncCreateJobReq.

        限速信息体。 - 限速：自定义的最大迁移速度，迁移过程中的迁移速度将不会超过该速度。 - 不限速：对迁移速度不进行限制，通常会最大化使用源数据库的出口带宽。该流速模式同时会对源数据库造成读消耗，消耗取决于源数据库的出口带宽。比如：源数据库的出口带宽为100MB/s，假设高速模式使用了80%带宽，则迁移对源数据库将造成80MB/s的读操作IO消耗。

        :param speed_limit: The speed_limit of this AsyncCreateJobReq.
        :type speed_limit: list[:class:`huaweicloudsdkdrs.v5.SpeedLimitInfo`]
        """
        self._speed_limit = speed_limit

    @property
    def user_migration(self):
        r"""Gets the user_migration of this AsyncCreateJobReq.

        :return: The user_migration of this AsyncCreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.UserMigrationInfo`
        """
        return self._user_migration

    @user_migration.setter
    def user_migration(self, user_migration):
        r"""Sets the user_migration of this AsyncCreateJobReq.

        :param user_migration: The user_migration of this AsyncCreateJobReq.
        :type user_migration: :class:`huaweicloudsdkdrs.v5.UserMigrationInfo`
        """
        self._user_migration = user_migration

    @property
    def policy_config(self):
        r"""Gets the policy_config of this AsyncCreateJobReq.

        :return: The policy_config of this AsyncCreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.PolicyConfig`
        """
        return self._policy_config

    @policy_config.setter
    def policy_config(self, policy_config):
        r"""Sets the policy_config of this AsyncCreateJobReq.

        :param policy_config: The policy_config of this AsyncCreateJobReq.
        :type policy_config: :class:`huaweicloudsdkdrs.v5.PolicyConfig`
        """
        self._policy_config = policy_config

    @property
    def db_object(self):
        r"""Gets the db_object of this AsyncCreateJobReq.

        :return: The db_object of this AsyncCreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.DbObject`
        """
        return self._db_object

    @db_object.setter
    def db_object(self, db_object):
        r"""Sets the db_object of this AsyncCreateJobReq.

        :param db_object: The db_object of this AsyncCreateJobReq.
        :type db_object: :class:`huaweicloudsdkdrs.v5.DbObject`
        """
        self._db_object = db_object

    @property
    def db_param(self):
        r"""Gets the db_param of this AsyncCreateJobReq.

        :return: The db_param of this AsyncCreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.DbParamInfo`
        """
        return self._db_param

    @db_param.setter
    def db_param(self, db_param):
        r"""Sets the db_param of this AsyncCreateJobReq.

        :param db_param: The db_param of this AsyncCreateJobReq.
        :type db_param: :class:`huaweicloudsdkdrs.v5.DbParamInfo`
        """
        self._db_param = db_param

    @property
    def tuning_params(self):
        r"""Gets the tuning_params of this AsyncCreateJobReq.

        :return: The tuning_params of this AsyncCreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.TuningParamInfo`
        """
        return self._tuning_params

    @tuning_params.setter
    def tuning_params(self, tuning_params):
        r"""Sets the tuning_params of this AsyncCreateJobReq.

        :param tuning_params: The tuning_params of this AsyncCreateJobReq.
        :type tuning_params: :class:`huaweicloudsdkdrs.v5.TuningParamInfo`
        """
        self._tuning_params = tuning_params

    @property
    def period_order(self):
        r"""Gets the period_order of this AsyncCreateJobReq.

        :return: The period_order of this AsyncCreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        """
        return self._period_order

    @period_order.setter
    def period_order(self, period_order):
        r"""Sets the period_order of this AsyncCreateJobReq.

        :param period_order: The period_order of this AsyncCreateJobReq.
        :type period_order: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        """
        self._period_order = period_order

    @property
    def node_info(self):
        r"""Gets the node_info of this AsyncCreateJobReq.

        :return: The node_info of this AsyncCreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        r"""Sets the node_info of this AsyncCreateJobReq.

        :param node_info: The node_info of this AsyncCreateJobReq.
        :type node_info: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        """
        self._node_info = node_info

    @property
    def public_ip_list(self):
        r"""Gets the public_ip_list of this AsyncCreateJobReq.

        指定公网IP的信息

        :return: The public_ip_list of this AsyncCreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.PublicIpConfig`]
        """
        return self._public_ip_list

    @public_ip_list.setter
    def public_ip_list(self, public_ip_list):
        r"""Sets the public_ip_list of this AsyncCreateJobReq.

        指定公网IP的信息

        :param public_ip_list: The public_ip_list of this AsyncCreateJobReq.
        :type public_ip_list: list[:class:`huaweicloudsdkdrs.v5.PublicIpConfig`]
        """
        self._public_ip_list = public_ip_list

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
        if not isinstance(other, AsyncCreateJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
