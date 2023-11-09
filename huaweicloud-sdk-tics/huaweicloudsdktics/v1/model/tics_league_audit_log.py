# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsLeagueAuditLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_user_domain_id': 'str',
        'create_user_project_id': 'str',
        'creator_alias_name': 'str',
        'event_end_time': 'datetime',
        'event_info': 'str',
        'event_start_time': 'datetime',
        'event_status': 'str',
        'id': 'int',
        'league_id': 'str',
        'sponsor_agent_name': 'str'
    }

    attribute_map = {
        'create_user_domain_id': 'create_user_domain_id',
        'create_user_project_id': 'create_user_project_id',
        'creator_alias_name': 'creator_alias_name',
        'event_end_time': 'event_end_time',
        'event_info': 'event_info',
        'event_start_time': 'event_start_time',
        'event_status': 'event_status',
        'id': 'id',
        'league_id': 'league_id',
        'sponsor_agent_name': 'sponsor_agent_name'
    }

    def __init__(self, create_user_domain_id=None, create_user_project_id=None, creator_alias_name=None, event_end_time=None, event_info=None, event_start_time=None, event_status=None, id=None, league_id=None, sponsor_agent_name=None):
        """TicsLeagueAuditLog

        The model defined in huaweicloud sdk

        :param create_user_domain_id: 创建者账户id
        :type create_user_domain_id: str
        :param create_user_project_id: 创建者项目id
        :type create_user_project_id: str
        :param creator_alias_name: 创建者别名
        :type creator_alias_name: str
        :param event_end_time: 事件结束时间
        :type event_end_time: datetime
        :param event_info: 事件信息
        :type event_info: str
        :param event_start_time: 事件开始时间
        :type event_start_time: datetime
        :param event_status: 事件状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中
        :type event_status: str
        :param id: 日志记录id
        :type id: int
        :param league_id: 联盟id
        :type league_id: str
        :param sponsor_agent_name: 作业发起节点名称
        :type sponsor_agent_name: str
        """
        
        

        self._create_user_domain_id = None
        self._create_user_project_id = None
        self._creator_alias_name = None
        self._event_end_time = None
        self._event_info = None
        self._event_start_time = None
        self._event_status = None
        self._id = None
        self._league_id = None
        self._sponsor_agent_name = None
        self.discriminator = None

        if create_user_domain_id is not None:
            self.create_user_domain_id = create_user_domain_id
        if create_user_project_id is not None:
            self.create_user_project_id = create_user_project_id
        if creator_alias_name is not None:
            self.creator_alias_name = creator_alias_name
        if event_end_time is not None:
            self.event_end_time = event_end_time
        if event_info is not None:
            self.event_info = event_info
        if event_start_time is not None:
            self.event_start_time = event_start_time
        if event_status is not None:
            self.event_status = event_status
        if id is not None:
            self.id = id
        if league_id is not None:
            self.league_id = league_id
        if sponsor_agent_name is not None:
            self.sponsor_agent_name = sponsor_agent_name

    @property
    def create_user_domain_id(self):
        """Gets the create_user_domain_id of this TicsLeagueAuditLog.

        创建者账户id

        :return: The create_user_domain_id of this TicsLeagueAuditLog.
        :rtype: str
        """
        return self._create_user_domain_id

    @create_user_domain_id.setter
    def create_user_domain_id(self, create_user_domain_id):
        """Sets the create_user_domain_id of this TicsLeagueAuditLog.

        创建者账户id

        :param create_user_domain_id: The create_user_domain_id of this TicsLeagueAuditLog.
        :type create_user_domain_id: str
        """
        self._create_user_domain_id = create_user_domain_id

    @property
    def create_user_project_id(self):
        """Gets the create_user_project_id of this TicsLeagueAuditLog.

        创建者项目id

        :return: The create_user_project_id of this TicsLeagueAuditLog.
        :rtype: str
        """
        return self._create_user_project_id

    @create_user_project_id.setter
    def create_user_project_id(self, create_user_project_id):
        """Sets the create_user_project_id of this TicsLeagueAuditLog.

        创建者项目id

        :param create_user_project_id: The create_user_project_id of this TicsLeagueAuditLog.
        :type create_user_project_id: str
        """
        self._create_user_project_id = create_user_project_id

    @property
    def creator_alias_name(self):
        """Gets the creator_alias_name of this TicsLeagueAuditLog.

        创建者别名

        :return: The creator_alias_name of this TicsLeagueAuditLog.
        :rtype: str
        """
        return self._creator_alias_name

    @creator_alias_name.setter
    def creator_alias_name(self, creator_alias_name):
        """Sets the creator_alias_name of this TicsLeagueAuditLog.

        创建者别名

        :param creator_alias_name: The creator_alias_name of this TicsLeagueAuditLog.
        :type creator_alias_name: str
        """
        self._creator_alias_name = creator_alias_name

    @property
    def event_end_time(self):
        """Gets the event_end_time of this TicsLeagueAuditLog.

        事件结束时间

        :return: The event_end_time of this TicsLeagueAuditLog.
        :rtype: datetime
        """
        return self._event_end_time

    @event_end_time.setter
    def event_end_time(self, event_end_time):
        """Sets the event_end_time of this TicsLeagueAuditLog.

        事件结束时间

        :param event_end_time: The event_end_time of this TicsLeagueAuditLog.
        :type event_end_time: datetime
        """
        self._event_end_time = event_end_time

    @property
    def event_info(self):
        """Gets the event_info of this TicsLeagueAuditLog.

        事件信息

        :return: The event_info of this TicsLeagueAuditLog.
        :rtype: str
        """
        return self._event_info

    @event_info.setter
    def event_info(self, event_info):
        """Sets the event_info of this TicsLeagueAuditLog.

        事件信息

        :param event_info: The event_info of this TicsLeagueAuditLog.
        :type event_info: str
        """
        self._event_info = event_info

    @property
    def event_start_time(self):
        """Gets the event_start_time of this TicsLeagueAuditLog.

        事件开始时间

        :return: The event_start_time of this TicsLeagueAuditLog.
        :rtype: datetime
        """
        return self._event_start_time

    @event_start_time.setter
    def event_start_time(self, event_start_time):
        """Sets the event_start_time of this TicsLeagueAuditLog.

        事件开始时间

        :param event_start_time: The event_start_time of this TicsLeagueAuditLog.
        :type event_start_time: datetime
        """
        self._event_start_time = event_start_time

    @property
    def event_status(self):
        """Gets the event_status of this TicsLeagueAuditLog.

        事件状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中

        :return: The event_status of this TicsLeagueAuditLog.
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """Sets the event_status of this TicsLeagueAuditLog.

        事件状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中

        :param event_status: The event_status of this TicsLeagueAuditLog.
        :type event_status: str
        """
        self._event_status = event_status

    @property
    def id(self):
        """Gets the id of this TicsLeagueAuditLog.

        日志记录id

        :return: The id of this TicsLeagueAuditLog.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TicsLeagueAuditLog.

        日志记录id

        :param id: The id of this TicsLeagueAuditLog.
        :type id: int
        """
        self._id = id

    @property
    def league_id(self):
        """Gets the league_id of this TicsLeagueAuditLog.

        联盟id

        :return: The league_id of this TicsLeagueAuditLog.
        :rtype: str
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this TicsLeagueAuditLog.

        联盟id

        :param league_id: The league_id of this TicsLeagueAuditLog.
        :type league_id: str
        """
        self._league_id = league_id

    @property
    def sponsor_agent_name(self):
        """Gets the sponsor_agent_name of this TicsLeagueAuditLog.

        作业发起节点名称

        :return: The sponsor_agent_name of this TicsLeagueAuditLog.
        :rtype: str
        """
        return self._sponsor_agent_name

    @sponsor_agent_name.setter
    def sponsor_agent_name(self, sponsor_agent_name):
        """Sets the sponsor_agent_name of this TicsLeagueAuditLog.

        作业发起节点名称

        :param sponsor_agent_name: The sponsor_agent_name of this TicsLeagueAuditLog.
        :type sponsor_agent_name: str
        """
        self._sponsor_agent_name = sponsor_agent_name

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
        if not isinstance(other, TicsLeagueAuditLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
