# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentListVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'agent_name': 'str',
        'create_time': 'datetime',
        'creator_domain_id': 'str',
        'creator_user_name': 'str',
        'deploy_status': 'str',
        'deploy_type': 'str',
        'deployment_event_information': 'str',
        'enable_delete': 'bool',
        'enable_upgrade': 'bool',
        'image_version': 'str',
        'is_high_avail': 'bool',
        'league_id': 'str',
        'league_name': 'str',
        'league_version': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'agent_name': 'agent_name',
        'create_time': 'create_time',
        'creator_domain_id': 'creator_domain_id',
        'creator_user_name': 'creator_user_name',
        'deploy_status': 'deploy_status',
        'deploy_type': 'deploy_type',
        'deployment_event_information': 'deployment_event_information',
        'enable_delete': 'enable_delete',
        'enable_upgrade': 'enable_upgrade',
        'image_version': 'image_version',
        'is_high_avail': 'is_high_avail',
        'league_id': 'league_id',
        'league_name': 'league_name',
        'league_version': 'league_version'
    }

    def __init__(self, agent_id=None, agent_name=None, create_time=None, creator_domain_id=None, creator_user_name=None, deploy_status=None, deploy_type=None, deployment_event_information=None, enable_delete=None, enable_upgrade=None, image_version=None, is_high_avail=None, league_id=None, league_name=None, league_version=None):
        """AgentListVo

        The model defined in huaweicloud sdk

        :param agent_id: 可信节点id
        :type agent_id: str
        :param agent_name: 可信节点名称
        :type agent_name: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param creator_domain_id: 创建者租户id
        :type creator_domain_id: str
        :param creator_user_name: 创建者名称
        :type creator_user_name: str
        :param deploy_status: 部署状态 ABNORMAL.正常,RESTARTING.重启中,RESTART_FAILED.重启失败，ROLLBACKING.回滚中，STARTING.启动中，DEPLOYING.创建中,DEPLOY_FAILED.创建失败,DEPLOY_SUCCESS.创建成功,RUNNING.运行中,DELETING.删除中,DELETE_FAILED.删除失败,DELETE_SUCCESS.删除成功,UPGRADING.升级中,UPGRADE_FAILED.升级失败,ROLLBACK.回退中,ROLLBACK_FAILED.回退失败,SUCCESS.成功,FAILED.失败,TO_START.待开始,IN_PROGRESS.进行中
        :type deploy_status: str
        :param deploy_type: 部署类型 CCE,IEF,EXTERNAL
        :type deploy_type: str
        :param deployment_event_information: 部署事件状态
        :type deployment_event_information: str
        :param enable_delete: 是否可删除
        :type enable_delete: bool
        :param enable_upgrade: 是否可升级
        :type enable_upgrade: bool
        :param image_version: 节点镜像版本
        :type image_version: str
        :param is_high_avail: 节点是否高可用
        :type is_high_avail: bool
        :param league_id: 联盟ID
        :type league_id: str
        :param league_name: 联盟名称
        :type league_name: str
        :param league_version: 联盟版本
        :type league_version: str
        """
        
        

        self._agent_id = None
        self._agent_name = None
        self._create_time = None
        self._creator_domain_id = None
        self._creator_user_name = None
        self._deploy_status = None
        self._deploy_type = None
        self._deployment_event_information = None
        self._enable_delete = None
        self._enable_upgrade = None
        self._image_version = None
        self._is_high_avail = None
        self._league_id = None
        self._league_name = None
        self._league_version = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if agent_name is not None:
            self.agent_name = agent_name
        if create_time is not None:
            self.create_time = create_time
        if creator_domain_id is not None:
            self.creator_domain_id = creator_domain_id
        if creator_user_name is not None:
            self.creator_user_name = creator_user_name
        if deploy_status is not None:
            self.deploy_status = deploy_status
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if deployment_event_information is not None:
            self.deployment_event_information = deployment_event_information
        if enable_delete is not None:
            self.enable_delete = enable_delete
        if enable_upgrade is not None:
            self.enable_upgrade = enable_upgrade
        if image_version is not None:
            self.image_version = image_version
        if is_high_avail is not None:
            self.is_high_avail = is_high_avail
        if league_id is not None:
            self.league_id = league_id
        if league_name is not None:
            self.league_name = league_name
        if league_version is not None:
            self.league_version = league_version

    @property
    def agent_id(self):
        """Gets the agent_id of this AgentListVo.

        可信节点id

        :return: The agent_id of this AgentListVo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AgentListVo.

        可信节点id

        :param agent_id: The agent_id of this AgentListVo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_name(self):
        """Gets the agent_name of this AgentListVo.

        可信节点名称

        :return: The agent_name of this AgentListVo.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this AgentListVo.

        可信节点名称

        :param agent_name: The agent_name of this AgentListVo.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def create_time(self):
        """Gets the create_time of this AgentListVo.

        创建时间

        :return: The create_time of this AgentListVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AgentListVo.

        创建时间

        :param create_time: The create_time of this AgentListVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def creator_domain_id(self):
        """Gets the creator_domain_id of this AgentListVo.

        创建者租户id

        :return: The creator_domain_id of this AgentListVo.
        :rtype: str
        """
        return self._creator_domain_id

    @creator_domain_id.setter
    def creator_domain_id(self, creator_domain_id):
        """Sets the creator_domain_id of this AgentListVo.

        创建者租户id

        :param creator_domain_id: The creator_domain_id of this AgentListVo.
        :type creator_domain_id: str
        """
        self._creator_domain_id = creator_domain_id

    @property
    def creator_user_name(self):
        """Gets the creator_user_name of this AgentListVo.

        创建者名称

        :return: The creator_user_name of this AgentListVo.
        :rtype: str
        """
        return self._creator_user_name

    @creator_user_name.setter
    def creator_user_name(self, creator_user_name):
        """Sets the creator_user_name of this AgentListVo.

        创建者名称

        :param creator_user_name: The creator_user_name of this AgentListVo.
        :type creator_user_name: str
        """
        self._creator_user_name = creator_user_name

    @property
    def deploy_status(self):
        """Gets the deploy_status of this AgentListVo.

        部署状态 ABNORMAL.正常,RESTARTING.重启中,RESTART_FAILED.重启失败，ROLLBACKING.回滚中，STARTING.启动中，DEPLOYING.创建中,DEPLOY_FAILED.创建失败,DEPLOY_SUCCESS.创建成功,RUNNING.运行中,DELETING.删除中,DELETE_FAILED.删除失败,DELETE_SUCCESS.删除成功,UPGRADING.升级中,UPGRADE_FAILED.升级失败,ROLLBACK.回退中,ROLLBACK_FAILED.回退失败,SUCCESS.成功,FAILED.失败,TO_START.待开始,IN_PROGRESS.进行中

        :return: The deploy_status of this AgentListVo.
        :rtype: str
        """
        return self._deploy_status

    @deploy_status.setter
    def deploy_status(self, deploy_status):
        """Sets the deploy_status of this AgentListVo.

        部署状态 ABNORMAL.正常,RESTARTING.重启中,RESTART_FAILED.重启失败，ROLLBACKING.回滚中，STARTING.启动中，DEPLOYING.创建中,DEPLOY_FAILED.创建失败,DEPLOY_SUCCESS.创建成功,RUNNING.运行中,DELETING.删除中,DELETE_FAILED.删除失败,DELETE_SUCCESS.删除成功,UPGRADING.升级中,UPGRADE_FAILED.升级失败,ROLLBACK.回退中,ROLLBACK_FAILED.回退失败,SUCCESS.成功,FAILED.失败,TO_START.待开始,IN_PROGRESS.进行中

        :param deploy_status: The deploy_status of this AgentListVo.
        :type deploy_status: str
        """
        self._deploy_status = deploy_status

    @property
    def deploy_type(self):
        """Gets the deploy_type of this AgentListVo.

        部署类型 CCE,IEF,EXTERNAL

        :return: The deploy_type of this AgentListVo.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this AgentListVo.

        部署类型 CCE,IEF,EXTERNAL

        :param deploy_type: The deploy_type of this AgentListVo.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def deployment_event_information(self):
        """Gets the deployment_event_information of this AgentListVo.

        部署事件状态

        :return: The deployment_event_information of this AgentListVo.
        :rtype: str
        """
        return self._deployment_event_information

    @deployment_event_information.setter
    def deployment_event_information(self, deployment_event_information):
        """Sets the deployment_event_information of this AgentListVo.

        部署事件状态

        :param deployment_event_information: The deployment_event_information of this AgentListVo.
        :type deployment_event_information: str
        """
        self._deployment_event_information = deployment_event_information

    @property
    def enable_delete(self):
        """Gets the enable_delete of this AgentListVo.

        是否可删除

        :return: The enable_delete of this AgentListVo.
        :rtype: bool
        """
        return self._enable_delete

    @enable_delete.setter
    def enable_delete(self, enable_delete):
        """Sets the enable_delete of this AgentListVo.

        是否可删除

        :param enable_delete: The enable_delete of this AgentListVo.
        :type enable_delete: bool
        """
        self._enable_delete = enable_delete

    @property
    def enable_upgrade(self):
        """Gets the enable_upgrade of this AgentListVo.

        是否可升级

        :return: The enable_upgrade of this AgentListVo.
        :rtype: bool
        """
        return self._enable_upgrade

    @enable_upgrade.setter
    def enable_upgrade(self, enable_upgrade):
        """Sets the enable_upgrade of this AgentListVo.

        是否可升级

        :param enable_upgrade: The enable_upgrade of this AgentListVo.
        :type enable_upgrade: bool
        """
        self._enable_upgrade = enable_upgrade

    @property
    def image_version(self):
        """Gets the image_version of this AgentListVo.

        节点镜像版本

        :return: The image_version of this AgentListVo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this AgentListVo.

        节点镜像版本

        :param image_version: The image_version of this AgentListVo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def is_high_avail(self):
        """Gets the is_high_avail of this AgentListVo.

        节点是否高可用

        :return: The is_high_avail of this AgentListVo.
        :rtype: bool
        """
        return self._is_high_avail

    @is_high_avail.setter
    def is_high_avail(self, is_high_avail):
        """Sets the is_high_avail of this AgentListVo.

        节点是否高可用

        :param is_high_avail: The is_high_avail of this AgentListVo.
        :type is_high_avail: bool
        """
        self._is_high_avail = is_high_avail

    @property
    def league_id(self):
        """Gets the league_id of this AgentListVo.

        联盟ID

        :return: The league_id of this AgentListVo.
        :rtype: str
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this AgentListVo.

        联盟ID

        :param league_id: The league_id of this AgentListVo.
        :type league_id: str
        """
        self._league_id = league_id

    @property
    def league_name(self):
        """Gets the league_name of this AgentListVo.

        联盟名称

        :return: The league_name of this AgentListVo.
        :rtype: str
        """
        return self._league_name

    @league_name.setter
    def league_name(self, league_name):
        """Sets the league_name of this AgentListVo.

        联盟名称

        :param league_name: The league_name of this AgentListVo.
        :type league_name: str
        """
        self._league_name = league_name

    @property
    def league_version(self):
        """Gets the league_version of this AgentListVo.

        联盟版本

        :return: The league_version of this AgentListVo.
        :rtype: str
        """
        return self._league_version

    @league_version.setter
    def league_version(self, league_version):
        """Sets the league_version of this AgentListVo.

        联盟版本

        :param league_version: The league_version of this AgentListVo.
        :type league_version: str
        """
        self._league_version = league_version

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
        if not isinstance(other, AgentListVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
