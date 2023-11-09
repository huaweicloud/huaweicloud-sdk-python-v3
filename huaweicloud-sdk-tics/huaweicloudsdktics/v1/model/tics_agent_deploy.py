# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsAgentDeploy:

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
        'aom_flag': 'str',
        'bcs_flag': 'str',
        'cce_version': 'str',
        'create_time': 'datetime',
        'creator_domain_id': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'creator_project_id': 'str',
        'deploy_status': 'str',
        'deploy_type': 'str',
        'deployment_event_information': 'str',
        'high_avail': 'str',
        'image_id': 'str',
        'image_version': 'str',
        'league_id': 'str',
        'league_name': 'str',
        'league_region_name': 'str',
        'league_version': 'str',
        'nat_id': 'str',
        'storage_mount_type': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'agent_name': 'agent_name',
        'aom_flag': 'aom_flag',
        'bcs_flag': 'bcs_flag',
        'cce_version': 'cce_version',
        'create_time': 'create_time',
        'creator_domain_id': 'creator_domain_id',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'creator_project_id': 'creator_project_id',
        'deploy_status': 'deploy_status',
        'deploy_type': 'deploy_type',
        'deployment_event_information': 'deployment_event_information',
        'high_avail': 'high_avail',
        'image_id': 'image_id',
        'image_version': 'image_version',
        'league_id': 'league_id',
        'league_name': 'league_name',
        'league_region_name': 'league_region_name',
        'league_version': 'league_version',
        'nat_id': 'nat_id',
        'storage_mount_type': 'storage_mount_type'
    }

    def __init__(self, agent_id=None, agent_name=None, aom_flag=None, bcs_flag=None, cce_version=None, create_time=None, creator_domain_id=None, creator_id=None, creator_name=None, creator_project_id=None, deploy_status=None, deploy_type=None, deployment_event_information=None, high_avail=None, image_id=None, image_version=None, league_id=None, league_name=None, league_region_name=None, league_version=None, nat_id=None, storage_mount_type=None):
        """TicsAgentDeploy

        The model defined in huaweicloud sdk

        :param agent_id: 可信节点Id
        :type agent_id: str
        :param agent_name: 可信节点名称
        :type agent_name: str
        :param aom_flag: 是否开启aom监控
        :type aom_flag: str
        :param bcs_flag: 是否使用区块链存证
        :type bcs_flag: str
        :param cce_version: 可信节点使用cce集群的版本
        :type cce_version: str
        :param create_time: 可信节点创建时间
        :type create_time: datetime
        :param creator_domain_id: 可信节点创建者的租户Id
        :type creator_domain_id: str
        :param creator_id: 可信节点创建者的Id
        :type creator_id: str
        :param creator_name: 可信节点创建者的名称
        :type creator_name: str
        :param creator_project_id: 创建可信节点所在项目Id
        :type creator_project_id: str
        :param deploy_status: 可信节点部署状态，ABNORMAL.正常,RESTARTING.重启中,RESTART_FAILED.重启失败，ROLLBACKING.回滚中，STARTING.启动中，DEPLOYING.创建中,DEPLOY_FAILED.创建失败,DEPLOY_SUCCESS.创建成功,RUNNING.运行中,DELETING.删除中,DELETE_FAILED.删除失败,DELETE_SUCCESS.删除成功,UPGRADING.升级中,UPGRADE_FAILED.升级失败,ROLLBACK.回退中,ROLLBACK_FAILED.回退失败,SUCCESS.成功,FAILED.失败,TO_START.待开始,IN_PROGRESS.进行中
        :type deploy_status: str
        :param deploy_type: 可信节点部署类型，CCE.云容器集群，IEF.边缘容器
        :type deploy_type: str
        :param deployment_event_information: 可信节点部署类型
        :type deployment_event_information: str
        :param high_avail: 可信节点是否高可用部署
        :type high_avail: str
        :param image_id: 可信节点部署使用的镜像Id
        :type image_id: str
        :param image_version: 可信节点部署使用的镜像版本
        :type image_version: str
        :param league_id: 可信节点所在联盟的Id
        :type league_id: str
        :param league_name: 可信节点所在联盟的名称
        :type league_name: str
        :param league_region_name: 可信节点所在联盟的区域
        :type league_region_name: str
        :param league_version: 可信节点所在联盟的版本
        :type league_version: str
        :param nat_id: 可信节点使用的网关的Id
        :type nat_id: str
        :param storage_mount_type: 可信节点使用的存储方式，HOST_PATH.本地存储，OBS.对象云存储，SFS_TURBO.极速文件存储
        :type storage_mount_type: str
        """
        
        

        self._agent_id = None
        self._agent_name = None
        self._aom_flag = None
        self._bcs_flag = None
        self._cce_version = None
        self._create_time = None
        self._creator_domain_id = None
        self._creator_id = None
        self._creator_name = None
        self._creator_project_id = None
        self._deploy_status = None
        self._deploy_type = None
        self._deployment_event_information = None
        self._high_avail = None
        self._image_id = None
        self._image_version = None
        self._league_id = None
        self._league_name = None
        self._league_region_name = None
        self._league_version = None
        self._nat_id = None
        self._storage_mount_type = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if agent_name is not None:
            self.agent_name = agent_name
        if aom_flag is not None:
            self.aom_flag = aom_flag
        if bcs_flag is not None:
            self.bcs_flag = bcs_flag
        if cce_version is not None:
            self.cce_version = cce_version
        if create_time is not None:
            self.create_time = create_time
        if creator_domain_id is not None:
            self.creator_domain_id = creator_domain_id
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if creator_project_id is not None:
            self.creator_project_id = creator_project_id
        if deploy_status is not None:
            self.deploy_status = deploy_status
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if deployment_event_information is not None:
            self.deployment_event_information = deployment_event_information
        if high_avail is not None:
            self.high_avail = high_avail
        if image_id is not None:
            self.image_id = image_id
        if image_version is not None:
            self.image_version = image_version
        if league_id is not None:
            self.league_id = league_id
        if league_name is not None:
            self.league_name = league_name
        if league_region_name is not None:
            self.league_region_name = league_region_name
        if league_version is not None:
            self.league_version = league_version
        if nat_id is not None:
            self.nat_id = nat_id
        if storage_mount_type is not None:
            self.storage_mount_type = storage_mount_type

    @property
    def agent_id(self):
        """Gets the agent_id of this TicsAgentDeploy.

        可信节点Id

        :return: The agent_id of this TicsAgentDeploy.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this TicsAgentDeploy.

        可信节点Id

        :param agent_id: The agent_id of this TicsAgentDeploy.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_name(self):
        """Gets the agent_name of this TicsAgentDeploy.

        可信节点名称

        :return: The agent_name of this TicsAgentDeploy.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this TicsAgentDeploy.

        可信节点名称

        :param agent_name: The agent_name of this TicsAgentDeploy.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def aom_flag(self):
        """Gets the aom_flag of this TicsAgentDeploy.

        是否开启aom监控

        :return: The aom_flag of this TicsAgentDeploy.
        :rtype: str
        """
        return self._aom_flag

    @aom_flag.setter
    def aom_flag(self, aom_flag):
        """Sets the aom_flag of this TicsAgentDeploy.

        是否开启aom监控

        :param aom_flag: The aom_flag of this TicsAgentDeploy.
        :type aom_flag: str
        """
        self._aom_flag = aom_flag

    @property
    def bcs_flag(self):
        """Gets the bcs_flag of this TicsAgentDeploy.

        是否使用区块链存证

        :return: The bcs_flag of this TicsAgentDeploy.
        :rtype: str
        """
        return self._bcs_flag

    @bcs_flag.setter
    def bcs_flag(self, bcs_flag):
        """Sets the bcs_flag of this TicsAgentDeploy.

        是否使用区块链存证

        :param bcs_flag: The bcs_flag of this TicsAgentDeploy.
        :type bcs_flag: str
        """
        self._bcs_flag = bcs_flag

    @property
    def cce_version(self):
        """Gets the cce_version of this TicsAgentDeploy.

        可信节点使用cce集群的版本

        :return: The cce_version of this TicsAgentDeploy.
        :rtype: str
        """
        return self._cce_version

    @cce_version.setter
    def cce_version(self, cce_version):
        """Sets the cce_version of this TicsAgentDeploy.

        可信节点使用cce集群的版本

        :param cce_version: The cce_version of this TicsAgentDeploy.
        :type cce_version: str
        """
        self._cce_version = cce_version

    @property
    def create_time(self):
        """Gets the create_time of this TicsAgentDeploy.

        可信节点创建时间

        :return: The create_time of this TicsAgentDeploy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TicsAgentDeploy.

        可信节点创建时间

        :param create_time: The create_time of this TicsAgentDeploy.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def creator_domain_id(self):
        """Gets the creator_domain_id of this TicsAgentDeploy.

        可信节点创建者的租户Id

        :return: The creator_domain_id of this TicsAgentDeploy.
        :rtype: str
        """
        return self._creator_domain_id

    @creator_domain_id.setter
    def creator_domain_id(self, creator_domain_id):
        """Sets the creator_domain_id of this TicsAgentDeploy.

        可信节点创建者的租户Id

        :param creator_domain_id: The creator_domain_id of this TicsAgentDeploy.
        :type creator_domain_id: str
        """
        self._creator_domain_id = creator_domain_id

    @property
    def creator_id(self):
        """Gets the creator_id of this TicsAgentDeploy.

        可信节点创建者的Id

        :return: The creator_id of this TicsAgentDeploy.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this TicsAgentDeploy.

        可信节点创建者的Id

        :param creator_id: The creator_id of this TicsAgentDeploy.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        """Gets the creator_name of this TicsAgentDeploy.

        可信节点创建者的名称

        :return: The creator_name of this TicsAgentDeploy.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this TicsAgentDeploy.

        可信节点创建者的名称

        :param creator_name: The creator_name of this TicsAgentDeploy.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def creator_project_id(self):
        """Gets the creator_project_id of this TicsAgentDeploy.

        创建可信节点所在项目Id

        :return: The creator_project_id of this TicsAgentDeploy.
        :rtype: str
        """
        return self._creator_project_id

    @creator_project_id.setter
    def creator_project_id(self, creator_project_id):
        """Sets the creator_project_id of this TicsAgentDeploy.

        创建可信节点所在项目Id

        :param creator_project_id: The creator_project_id of this TicsAgentDeploy.
        :type creator_project_id: str
        """
        self._creator_project_id = creator_project_id

    @property
    def deploy_status(self):
        """Gets the deploy_status of this TicsAgentDeploy.

        可信节点部署状态，ABNORMAL.正常,RESTARTING.重启中,RESTART_FAILED.重启失败，ROLLBACKING.回滚中，STARTING.启动中，DEPLOYING.创建中,DEPLOY_FAILED.创建失败,DEPLOY_SUCCESS.创建成功,RUNNING.运行中,DELETING.删除中,DELETE_FAILED.删除失败,DELETE_SUCCESS.删除成功,UPGRADING.升级中,UPGRADE_FAILED.升级失败,ROLLBACK.回退中,ROLLBACK_FAILED.回退失败,SUCCESS.成功,FAILED.失败,TO_START.待开始,IN_PROGRESS.进行中

        :return: The deploy_status of this TicsAgentDeploy.
        :rtype: str
        """
        return self._deploy_status

    @deploy_status.setter
    def deploy_status(self, deploy_status):
        """Sets the deploy_status of this TicsAgentDeploy.

        可信节点部署状态，ABNORMAL.正常,RESTARTING.重启中,RESTART_FAILED.重启失败，ROLLBACKING.回滚中，STARTING.启动中，DEPLOYING.创建中,DEPLOY_FAILED.创建失败,DEPLOY_SUCCESS.创建成功,RUNNING.运行中,DELETING.删除中,DELETE_FAILED.删除失败,DELETE_SUCCESS.删除成功,UPGRADING.升级中,UPGRADE_FAILED.升级失败,ROLLBACK.回退中,ROLLBACK_FAILED.回退失败,SUCCESS.成功,FAILED.失败,TO_START.待开始,IN_PROGRESS.进行中

        :param deploy_status: The deploy_status of this TicsAgentDeploy.
        :type deploy_status: str
        """
        self._deploy_status = deploy_status

    @property
    def deploy_type(self):
        """Gets the deploy_type of this TicsAgentDeploy.

        可信节点部署类型，CCE.云容器集群，IEF.边缘容器

        :return: The deploy_type of this TicsAgentDeploy.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this TicsAgentDeploy.

        可信节点部署类型，CCE.云容器集群，IEF.边缘容器

        :param deploy_type: The deploy_type of this TicsAgentDeploy.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def deployment_event_information(self):
        """Gets the deployment_event_information of this TicsAgentDeploy.

        可信节点部署类型

        :return: The deployment_event_information of this TicsAgentDeploy.
        :rtype: str
        """
        return self._deployment_event_information

    @deployment_event_information.setter
    def deployment_event_information(self, deployment_event_information):
        """Sets the deployment_event_information of this TicsAgentDeploy.

        可信节点部署类型

        :param deployment_event_information: The deployment_event_information of this TicsAgentDeploy.
        :type deployment_event_information: str
        """
        self._deployment_event_information = deployment_event_information

    @property
    def high_avail(self):
        """Gets the high_avail of this TicsAgentDeploy.

        可信节点是否高可用部署

        :return: The high_avail of this TicsAgentDeploy.
        :rtype: str
        """
        return self._high_avail

    @high_avail.setter
    def high_avail(self, high_avail):
        """Sets the high_avail of this TicsAgentDeploy.

        可信节点是否高可用部署

        :param high_avail: The high_avail of this TicsAgentDeploy.
        :type high_avail: str
        """
        self._high_avail = high_avail

    @property
    def image_id(self):
        """Gets the image_id of this TicsAgentDeploy.

        可信节点部署使用的镜像Id

        :return: The image_id of this TicsAgentDeploy.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this TicsAgentDeploy.

        可信节点部署使用的镜像Id

        :param image_id: The image_id of this TicsAgentDeploy.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_version(self):
        """Gets the image_version of this TicsAgentDeploy.

        可信节点部署使用的镜像版本

        :return: The image_version of this TicsAgentDeploy.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this TicsAgentDeploy.

        可信节点部署使用的镜像版本

        :param image_version: The image_version of this TicsAgentDeploy.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def league_id(self):
        """Gets the league_id of this TicsAgentDeploy.

        可信节点所在联盟的Id

        :return: The league_id of this TicsAgentDeploy.
        :rtype: str
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this TicsAgentDeploy.

        可信节点所在联盟的Id

        :param league_id: The league_id of this TicsAgentDeploy.
        :type league_id: str
        """
        self._league_id = league_id

    @property
    def league_name(self):
        """Gets the league_name of this TicsAgentDeploy.

        可信节点所在联盟的名称

        :return: The league_name of this TicsAgentDeploy.
        :rtype: str
        """
        return self._league_name

    @league_name.setter
    def league_name(self, league_name):
        """Sets the league_name of this TicsAgentDeploy.

        可信节点所在联盟的名称

        :param league_name: The league_name of this TicsAgentDeploy.
        :type league_name: str
        """
        self._league_name = league_name

    @property
    def league_region_name(self):
        """Gets the league_region_name of this TicsAgentDeploy.

        可信节点所在联盟的区域

        :return: The league_region_name of this TicsAgentDeploy.
        :rtype: str
        """
        return self._league_region_name

    @league_region_name.setter
    def league_region_name(self, league_region_name):
        """Sets the league_region_name of this TicsAgentDeploy.

        可信节点所在联盟的区域

        :param league_region_name: The league_region_name of this TicsAgentDeploy.
        :type league_region_name: str
        """
        self._league_region_name = league_region_name

    @property
    def league_version(self):
        """Gets the league_version of this TicsAgentDeploy.

        可信节点所在联盟的版本

        :return: The league_version of this TicsAgentDeploy.
        :rtype: str
        """
        return self._league_version

    @league_version.setter
    def league_version(self, league_version):
        """Sets the league_version of this TicsAgentDeploy.

        可信节点所在联盟的版本

        :param league_version: The league_version of this TicsAgentDeploy.
        :type league_version: str
        """
        self._league_version = league_version

    @property
    def nat_id(self):
        """Gets the nat_id of this TicsAgentDeploy.

        可信节点使用的网关的Id

        :return: The nat_id of this TicsAgentDeploy.
        :rtype: str
        """
        return self._nat_id

    @nat_id.setter
    def nat_id(self, nat_id):
        """Sets the nat_id of this TicsAgentDeploy.

        可信节点使用的网关的Id

        :param nat_id: The nat_id of this TicsAgentDeploy.
        :type nat_id: str
        """
        self._nat_id = nat_id

    @property
    def storage_mount_type(self):
        """Gets the storage_mount_type of this TicsAgentDeploy.

        可信节点使用的存储方式，HOST_PATH.本地存储，OBS.对象云存储，SFS_TURBO.极速文件存储

        :return: The storage_mount_type of this TicsAgentDeploy.
        :rtype: str
        """
        return self._storage_mount_type

    @storage_mount_type.setter
    def storage_mount_type(self, storage_mount_type):
        """Sets the storage_mount_type of this TicsAgentDeploy.

        可信节点使用的存储方式，HOST_PATH.本地存储，OBS.对象云存储，SFS_TURBO.极速文件存储

        :param storage_mount_type: The storage_mount_type of this TicsAgentDeploy.
        :type storage_mount_type: str
        """
        self._storage_mount_type = storage_mount_type

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
        if not isinstance(other, TicsAgentDeploy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
