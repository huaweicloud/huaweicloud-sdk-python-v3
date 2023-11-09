# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'node_name': 'str',
        'node_partner_alias': 'str',
        'node_type': 'str',
        'stages': 'list[StageVo]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'node_name': 'node_name',
        'node_partner_alias': 'node_partner_alias',
        'node_type': 'node_type',
        'stages': 'stages'
    }

    def __init__(self, node_id=None, node_name=None, node_partner_alias=None, node_type=None, stages=None):
        """DeployVo

        The model defined in huaweicloud sdk

        :param node_id: 节点Id
        :type node_id: str
        :param node_name: 节点名称
        :type node_name: str
        :param node_partner_alias: 参与方别名
        :type node_partner_alias: str
        :param node_type: 节点类型,AGENT.计算节点，AGG.聚合节点，AGG_MANAGER.聚合器管理节点,SERVER.控制节点
        :type node_type: str
        :param stages: 执行阶段
        :type stages: list[:class:`huaweicloudsdktics.v1.StageVo`]
        """
        
        

        self._node_id = None
        self._node_name = None
        self._node_partner_alias = None
        self._node_type = None
        self._stages = None
        self.discriminator = None

        self.node_id = node_id
        self.node_name = node_name
        self.node_partner_alias = node_partner_alias
        if node_type is not None:
            self.node_type = node_type
        if stages is not None:
            self.stages = stages

    @property
    def node_id(self):
        """Gets the node_id of this DeployVo.

        节点Id

        :return: The node_id of this DeployVo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DeployVo.

        节点Id

        :param node_id: The node_id of this DeployVo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        """Gets the node_name of this DeployVo.

        节点名称

        :return: The node_name of this DeployVo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this DeployVo.

        节点名称

        :param node_name: The node_name of this DeployVo.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def node_partner_alias(self):
        """Gets the node_partner_alias of this DeployVo.

        参与方别名

        :return: The node_partner_alias of this DeployVo.
        :rtype: str
        """
        return self._node_partner_alias

    @node_partner_alias.setter
    def node_partner_alias(self, node_partner_alias):
        """Sets the node_partner_alias of this DeployVo.

        参与方别名

        :param node_partner_alias: The node_partner_alias of this DeployVo.
        :type node_partner_alias: str
        """
        self._node_partner_alias = node_partner_alias

    @property
    def node_type(self):
        """Gets the node_type of this DeployVo.

        节点类型,AGENT.计算节点，AGG.聚合节点，AGG_MANAGER.聚合器管理节点,SERVER.控制节点

        :return: The node_type of this DeployVo.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this DeployVo.

        节点类型,AGENT.计算节点，AGG.聚合节点，AGG_MANAGER.聚合器管理节点,SERVER.控制节点

        :param node_type: The node_type of this DeployVo.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def stages(self):
        """Gets the stages of this DeployVo.

        执行阶段

        :return: The stages of this DeployVo.
        :rtype: list[:class:`huaweicloudsdktics.v1.StageVo`]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this DeployVo.

        执行阶段

        :param stages: The stages of this DeployVo.
        :type stages: list[:class:`huaweicloudsdktics.v1.StageVo`]
        """
        self._stages = stages

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
        if not isinstance(other, DeployVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
