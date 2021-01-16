# coding: utf-8

import pprint
import re

import six





class CreateRequestBodyCceCreateInfo:


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
        """CreateRequestBodyCceCreateInfo - a model defined in huaweicloud sdk"""
        
        

        self._node_num = None
        self._node_flavor = None
        self._cce_flavor = None
        self._init_node_pwd = None
        self._az = None
        self._cluster_platform_type = None
        self.discriminator = None

        if node_num is not None:
            self.node_num = node_num
        if node_flavor is not None:
            self.node_flavor = node_flavor
        if cce_flavor is not None:
            self.cce_flavor = cce_flavor
        if init_node_pwd is not None:
            self.init_node_pwd = init_node_pwd
        if az is not None:
            self.az = az
        if cluster_platform_type is not None:
            self.cluster_platform_type = cluster_platform_type

    @property
    def node_num(self):
        """Gets the node_num of this CreateRequestBodyCceCreateInfo.

        集群节点数

        :return: The node_num of this CreateRequestBodyCceCreateInfo.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this CreateRequestBodyCceCreateInfo.

        集群节点数

        :param node_num: The node_num of this CreateRequestBodyCceCreateInfo.
        :type: int
        """
        self._node_num = node_num

    @property
    def node_flavor(self):
        """Gets the node_flavor of this CreateRequestBodyCceCreateInfo.

        集群节点规格

        :return: The node_flavor of this CreateRequestBodyCceCreateInfo.
        :rtype: str
        """
        return self._node_flavor

    @node_flavor.setter
    def node_flavor(self, node_flavor):
        """Sets the node_flavor of this CreateRequestBodyCceCreateInfo.

        集群节点规格

        :param node_flavor: The node_flavor of this CreateRequestBodyCceCreateInfo.
        :type: str
        """
        self._node_flavor = node_flavor

    @property
    def cce_flavor(self):
        """Gets the cce_flavor of this CreateRequestBodyCceCreateInfo.

        CCE集群规格

        :return: The cce_flavor of this CreateRequestBodyCceCreateInfo.
        :rtype: str
        """
        return self._cce_flavor

    @cce_flavor.setter
    def cce_flavor(self, cce_flavor):
        """Sets the cce_flavor of this CreateRequestBodyCceCreateInfo.

        CCE集群规格

        :param cce_flavor: The cce_flavor of this CreateRequestBodyCceCreateInfo.
        :type: str
        """
        self._cce_flavor = cce_flavor

    @property
    def init_node_pwd(self):
        """Gets the init_node_pwd of this CreateRequestBodyCceCreateInfo.

        节点初始密码

        :return: The init_node_pwd of this CreateRequestBodyCceCreateInfo.
        :rtype: str
        """
        return self._init_node_pwd

    @init_node_pwd.setter
    def init_node_pwd(self, init_node_pwd):
        """Sets the init_node_pwd of this CreateRequestBodyCceCreateInfo.

        节点初始密码

        :param init_node_pwd: The init_node_pwd of this CreateRequestBodyCceCreateInfo.
        :type: str
        """
        self._init_node_pwd = init_node_pwd

    @property
    def az(self):
        """Gets the az of this CreateRequestBodyCceCreateInfo.

        可用区

        :return: The az of this CreateRequestBodyCceCreateInfo.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this CreateRequestBodyCceCreateInfo.

        可用区

        :param az: The az of this CreateRequestBodyCceCreateInfo.
        :type: str
        """
        self._az = az

    @property
    def cluster_platform_type(self):
        """Gets the cluster_platform_type of this CreateRequestBodyCceCreateInfo.

        集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）

        :return: The cluster_platform_type of this CreateRequestBodyCceCreateInfo.
        :rtype: str
        """
        return self._cluster_platform_type

    @cluster_platform_type.setter
    def cluster_platform_type(self, cluster_platform_type):
        """Sets the cluster_platform_type of this CreateRequestBodyCceCreateInfo.

        集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）

        :param cluster_platform_type: The cluster_platform_type of this CreateRequestBodyCceCreateInfo.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRequestBodyCceCreateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
