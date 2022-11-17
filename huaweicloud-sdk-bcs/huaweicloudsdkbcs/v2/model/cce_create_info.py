# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CCECreateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_num': 'int',
        'node_flavor': 'str',
        'cce_flavor': 'str',
        'init_node_pwd': 'str',
        'az': 'str',
        'cluster_platform_type': 'str'
    }

    attribute_map = {
        'node_num': 'node_num',
        'node_flavor': 'node_flavor',
        'cce_flavor': 'cce_flavor',
        'init_node_pwd': 'init_node_pwd',
        'az': 'az',
        'cluster_platform_type': 'cluster_platform_type'
    }

    def __init__(self, node_num=None, node_flavor=None, cce_flavor=None, init_node_pwd=None, az=None, cluster_platform_type=None):
        """CCECreateInfo

        The model defined in huaweicloud sdk

        :param node_num: 集群节点数
        :type node_num: int
        :param node_flavor: 集群节点规格ID（支持的规格配置最小为4u8g）
        :type node_flavor: str
        :param cce_flavor: CCE集群规格
        :type cce_flavor: str
        :param init_node_pwd: 节点初始密码
        :type init_node_pwd: str
        :param az: 可用区
        :type az: str
        :param cluster_platform_type: 集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）
        :type cluster_platform_type: str
        """
        
        

        self._node_num = None
        self._node_flavor = None
        self._cce_flavor = None
        self._init_node_pwd = None
        self._az = None
        self._cluster_platform_type = None
        self.discriminator = None

        self.node_num = node_num
        self.node_flavor = node_flavor
        self.cce_flavor = cce_flavor
        self.init_node_pwd = init_node_pwd
        self.az = az
        self.cluster_platform_type = cluster_platform_type

    @property
    def node_num(self):
        """Gets the node_num of this CCECreateInfo.

        集群节点数

        :return: The node_num of this CCECreateInfo.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this CCECreateInfo.

        集群节点数

        :param node_num: The node_num of this CCECreateInfo.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def node_flavor(self):
        """Gets the node_flavor of this CCECreateInfo.

        集群节点规格ID（支持的规格配置最小为4u8g）

        :return: The node_flavor of this CCECreateInfo.
        :rtype: str
        """
        return self._node_flavor

    @node_flavor.setter
    def node_flavor(self, node_flavor):
        """Sets the node_flavor of this CCECreateInfo.

        集群节点规格ID（支持的规格配置最小为4u8g）

        :param node_flavor: The node_flavor of this CCECreateInfo.
        :type node_flavor: str
        """
        self._node_flavor = node_flavor

    @property
    def cce_flavor(self):
        """Gets the cce_flavor of this CCECreateInfo.

        CCE集群规格

        :return: The cce_flavor of this CCECreateInfo.
        :rtype: str
        """
        return self._cce_flavor

    @cce_flavor.setter
    def cce_flavor(self, cce_flavor):
        """Sets the cce_flavor of this CCECreateInfo.

        CCE集群规格

        :param cce_flavor: The cce_flavor of this CCECreateInfo.
        :type cce_flavor: str
        """
        self._cce_flavor = cce_flavor

    @property
    def init_node_pwd(self):
        """Gets the init_node_pwd of this CCECreateInfo.

        节点初始密码

        :return: The init_node_pwd of this CCECreateInfo.
        :rtype: str
        """
        return self._init_node_pwd

    @init_node_pwd.setter
    def init_node_pwd(self, init_node_pwd):
        """Sets the init_node_pwd of this CCECreateInfo.

        节点初始密码

        :param init_node_pwd: The init_node_pwd of this CCECreateInfo.
        :type init_node_pwd: str
        """
        self._init_node_pwd = init_node_pwd

    @property
    def az(self):
        """Gets the az of this CCECreateInfo.

        可用区

        :return: The az of this CCECreateInfo.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this CCECreateInfo.

        可用区

        :param az: The az of this CCECreateInfo.
        :type az: str
        """
        self._az = az

    @property
    def cluster_platform_type(self):
        """Gets the cluster_platform_type of this CCECreateInfo.

        集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）

        :return: The cluster_platform_type of this CCECreateInfo.
        :rtype: str
        """
        return self._cluster_platform_type

    @cluster_platform_type.setter
    def cluster_platform_type(self, cluster_platform_type):
        """Sets the cluster_platform_type of this CCECreateInfo.

        集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）

        :param cluster_platform_type: The cluster_platform_type of this CCECreateInfo.
        :type cluster_platform_type: str
        """
        self._cluster_platform_type = cluster_platform_type

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
        if not isinstance(other, CCECreateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
