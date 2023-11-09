# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsTrustInfoVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'datetime',
        'ha_mode': 'str',
        'ne_deploy_type': 'str',
        'ne_node_type': 'str',
        'ne_status': 'str',
        'node_id': 'str',
        'node_name': 'str',
        'partner_alias': 'str',
        'update_time': 'datetime'
    }

    attribute_map = {
        'create_time': 'create_time',
        'ha_mode': 'ha_mode',
        'ne_deploy_type': 'ne_deploy_type',
        'ne_node_type': 'ne_node_type',
        'ne_status': 'ne_status',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'partner_alias': 'partner_alias',
        'update_time': 'update_time'
    }

    def __init__(self, create_time=None, ha_mode=None, ne_deploy_type=None, ne_node_type=None, ne_status=None, node_id=None, node_name=None, partner_alias=None, update_time=None):
        """TicsTrustInfoVo

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: datetime
        :param ha_mode: 主备模式，ACTIVE.主，STANDBY.备
        :type ha_mode: str
        :param ne_deploy_type: 网元部署类型，CCE.容器集群部署，IEF.边缘部署
        :type ne_deploy_type: str
        :param ne_node_type: 节点类型,AGENT.计算节点，AGG.聚合节点，AGG_MANAGER.聚合器管理节点,SERVER.控制节点
        :type ne_node_type: str
        :param ne_status: 网元状态，INIT.初始化,UNKNOWN.未知,OFFLINE.离线,ONLINE.在线,FAULT.故障,TRUSTING.互信中,TRUST.已互信
        :type ne_status: str
        :param node_id: 节点id
        :type node_id: str
        :param node_name: 节点名称
        :type node_name: str
        :param partner_alias: 合作方别名
        :type partner_alias: str
        :param update_time: 更新时间
        :type update_time: datetime
        """
        
        

        self._create_time = None
        self._ha_mode = None
        self._ne_deploy_type = None
        self._ne_node_type = None
        self._ne_status = None
        self._node_id = None
        self._node_name = None
        self._partner_alias = None
        self._update_time = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if ha_mode is not None:
            self.ha_mode = ha_mode
        if ne_deploy_type is not None:
            self.ne_deploy_type = ne_deploy_type
        if ne_node_type is not None:
            self.ne_node_type = ne_node_type
        if ne_status is not None:
            self.ne_status = ne_status
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if partner_alias is not None:
            self.partner_alias = partner_alias
        if update_time is not None:
            self.update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this TicsTrustInfoVo.

        创建时间

        :return: The create_time of this TicsTrustInfoVo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TicsTrustInfoVo.

        创建时间

        :param create_time: The create_time of this TicsTrustInfoVo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def ha_mode(self):
        """Gets the ha_mode of this TicsTrustInfoVo.

        主备模式，ACTIVE.主，STANDBY.备

        :return: The ha_mode of this TicsTrustInfoVo.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        """Sets the ha_mode of this TicsTrustInfoVo.

        主备模式，ACTIVE.主，STANDBY.备

        :param ha_mode: The ha_mode of this TicsTrustInfoVo.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def ne_deploy_type(self):
        """Gets the ne_deploy_type of this TicsTrustInfoVo.

        网元部署类型，CCE.容器集群部署，IEF.边缘部署

        :return: The ne_deploy_type of this TicsTrustInfoVo.
        :rtype: str
        """
        return self._ne_deploy_type

    @ne_deploy_type.setter
    def ne_deploy_type(self, ne_deploy_type):
        """Sets the ne_deploy_type of this TicsTrustInfoVo.

        网元部署类型，CCE.容器集群部署，IEF.边缘部署

        :param ne_deploy_type: The ne_deploy_type of this TicsTrustInfoVo.
        :type ne_deploy_type: str
        """
        self._ne_deploy_type = ne_deploy_type

    @property
    def ne_node_type(self):
        """Gets the ne_node_type of this TicsTrustInfoVo.

        节点类型,AGENT.计算节点，AGG.聚合节点，AGG_MANAGER.聚合器管理节点,SERVER.控制节点

        :return: The ne_node_type of this TicsTrustInfoVo.
        :rtype: str
        """
        return self._ne_node_type

    @ne_node_type.setter
    def ne_node_type(self, ne_node_type):
        """Sets the ne_node_type of this TicsTrustInfoVo.

        节点类型,AGENT.计算节点，AGG.聚合节点，AGG_MANAGER.聚合器管理节点,SERVER.控制节点

        :param ne_node_type: The ne_node_type of this TicsTrustInfoVo.
        :type ne_node_type: str
        """
        self._ne_node_type = ne_node_type

    @property
    def ne_status(self):
        """Gets the ne_status of this TicsTrustInfoVo.

        网元状态，INIT.初始化,UNKNOWN.未知,OFFLINE.离线,ONLINE.在线,FAULT.故障,TRUSTING.互信中,TRUST.已互信

        :return: The ne_status of this TicsTrustInfoVo.
        :rtype: str
        """
        return self._ne_status

    @ne_status.setter
    def ne_status(self, ne_status):
        """Sets the ne_status of this TicsTrustInfoVo.

        网元状态，INIT.初始化,UNKNOWN.未知,OFFLINE.离线,ONLINE.在线,FAULT.故障,TRUSTING.互信中,TRUST.已互信

        :param ne_status: The ne_status of this TicsTrustInfoVo.
        :type ne_status: str
        """
        self._ne_status = ne_status

    @property
    def node_id(self):
        """Gets the node_id of this TicsTrustInfoVo.

        节点id

        :return: The node_id of this TicsTrustInfoVo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this TicsTrustInfoVo.

        节点id

        :param node_id: The node_id of this TicsTrustInfoVo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        """Gets the node_name of this TicsTrustInfoVo.

        节点名称

        :return: The node_name of this TicsTrustInfoVo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this TicsTrustInfoVo.

        节点名称

        :param node_name: The node_name of this TicsTrustInfoVo.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def partner_alias(self):
        """Gets the partner_alias of this TicsTrustInfoVo.

        合作方别名

        :return: The partner_alias of this TicsTrustInfoVo.
        :rtype: str
        """
        return self._partner_alias

    @partner_alias.setter
    def partner_alias(self, partner_alias):
        """Sets the partner_alias of this TicsTrustInfoVo.

        合作方别名

        :param partner_alias: The partner_alias of this TicsTrustInfoVo.
        :type partner_alias: str
        """
        self._partner_alias = partner_alias

    @property
    def update_time(self):
        """Gets the update_time of this TicsTrustInfoVo.

        更新时间

        :return: The update_time of this TicsTrustInfoVo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TicsTrustInfoVo.

        更新时间

        :param update_time: The update_time of this TicsTrustInfoVo.
        :type update_time: datetime
        """
        self._update_time = update_time

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
        if not isinstance(other, TicsTrustInfoVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
