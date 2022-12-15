# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvitorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'invitor_id': 'str',
        'invitor_name': 'str',
        'invitor_bcs_id': 'str',
        'invitor_bcs_name': 'str',
        'invitor_consensus': 'str',
        'invitor_project_id': 'str',
        'invitor_cluster_type': 'str',
        'invitor_database_type': 'str',
        'invitor_signature_algorithm': 'str',
        'invitor_fabric_version': 'str',
        'order_fade_enabled': 'bool',
        'order_fade_cache': 'int'
    }

    attribute_map = {
        'invitor_id': 'invitor_id',
        'invitor_name': 'invitor_name',
        'invitor_bcs_id': 'invitor_bcs_id',
        'invitor_bcs_name': 'invitor_bcs_name',
        'invitor_consensus': 'invitor_consensus',
        'invitor_project_id': 'invitor_project_id',
        'invitor_cluster_type': 'invitor_cluster_type',
        'invitor_database_type': 'invitor_database_type',
        'invitor_signature_algorithm': 'invitor_signature_algorithm',
        'invitor_fabric_version': 'invitor_fabric_version',
        'order_fade_enabled': 'order_fade_enabled',
        'order_fade_cache': 'order_fade_cache'
    }

    def __init__(self, invitor_id=None, invitor_name=None, invitor_bcs_id=None, invitor_bcs_name=None, invitor_consensus=None, invitor_project_id=None, invitor_cluster_type=None, invitor_database_type=None, invitor_signature_algorithm=None, invitor_fabric_version=None, order_fade_enabled=None, order_fade_cache=None):
        """InvitorInfo

        The model defined in huaweicloud sdk

        :param invitor_id: 邀请方用户id
        :type invitor_id: str
        :param invitor_name: 邀请方用户名
        :type invitor_name: str
        :param invitor_bcs_id: 邀请方的服务实例id
        :type invitor_bcs_id: str
        :param invitor_bcs_name: 邀请方的服务实例名
        :type invitor_bcs_name: str
        :param invitor_consensus: 邀请方的共识
        :type invitor_consensus: str
        :param invitor_project_id: 邀请方的projectID
        :type invitor_project_id: str
        :param invitor_cluster_type: 邀请方的集群类型
        :type invitor_cluster_type: str
        :param invitor_database_type: 邀请方数据库类型
        :type invitor_database_type: str
        :param invitor_signature_algorithm: 邀请方的签名算法
        :type invitor_signature_algorithm: str
        :param invitor_fabric_version: 邀请方的fabric版本
        :type invitor_fabric_version: str
        :param order_fade_enabled: 是否允许共识节点老化
        :type order_fade_enabled: bool
        :param order_fade_cache: 共识节点的老化阈值
        :type order_fade_cache: int
        """
        
        

        self._invitor_id = None
        self._invitor_name = None
        self._invitor_bcs_id = None
        self._invitor_bcs_name = None
        self._invitor_consensus = None
        self._invitor_project_id = None
        self._invitor_cluster_type = None
        self._invitor_database_type = None
        self._invitor_signature_algorithm = None
        self._invitor_fabric_version = None
        self._order_fade_enabled = None
        self._order_fade_cache = None
        self.discriminator = None

        if invitor_id is not None:
            self.invitor_id = invitor_id
        if invitor_name is not None:
            self.invitor_name = invitor_name
        if invitor_bcs_id is not None:
            self.invitor_bcs_id = invitor_bcs_id
        if invitor_bcs_name is not None:
            self.invitor_bcs_name = invitor_bcs_name
        if invitor_consensus is not None:
            self.invitor_consensus = invitor_consensus
        if invitor_project_id is not None:
            self.invitor_project_id = invitor_project_id
        if invitor_cluster_type is not None:
            self.invitor_cluster_type = invitor_cluster_type
        if invitor_database_type is not None:
            self.invitor_database_type = invitor_database_type
        if invitor_signature_algorithm is not None:
            self.invitor_signature_algorithm = invitor_signature_algorithm
        if invitor_fabric_version is not None:
            self.invitor_fabric_version = invitor_fabric_version
        if order_fade_enabled is not None:
            self.order_fade_enabled = order_fade_enabled
        if order_fade_cache is not None:
            self.order_fade_cache = order_fade_cache

    @property
    def invitor_id(self):
        """Gets the invitor_id of this InvitorInfo.

        邀请方用户id

        :return: The invitor_id of this InvitorInfo.
        :rtype: str
        """
        return self._invitor_id

    @invitor_id.setter
    def invitor_id(self, invitor_id):
        """Sets the invitor_id of this InvitorInfo.

        邀请方用户id

        :param invitor_id: The invitor_id of this InvitorInfo.
        :type invitor_id: str
        """
        self._invitor_id = invitor_id

    @property
    def invitor_name(self):
        """Gets the invitor_name of this InvitorInfo.

        邀请方用户名

        :return: The invitor_name of this InvitorInfo.
        :rtype: str
        """
        return self._invitor_name

    @invitor_name.setter
    def invitor_name(self, invitor_name):
        """Sets the invitor_name of this InvitorInfo.

        邀请方用户名

        :param invitor_name: The invitor_name of this InvitorInfo.
        :type invitor_name: str
        """
        self._invitor_name = invitor_name

    @property
    def invitor_bcs_id(self):
        """Gets the invitor_bcs_id of this InvitorInfo.

        邀请方的服务实例id

        :return: The invitor_bcs_id of this InvitorInfo.
        :rtype: str
        """
        return self._invitor_bcs_id

    @invitor_bcs_id.setter
    def invitor_bcs_id(self, invitor_bcs_id):
        """Sets the invitor_bcs_id of this InvitorInfo.

        邀请方的服务实例id

        :param invitor_bcs_id: The invitor_bcs_id of this InvitorInfo.
        :type invitor_bcs_id: str
        """
        self._invitor_bcs_id = invitor_bcs_id

    @property
    def invitor_bcs_name(self):
        """Gets the invitor_bcs_name of this InvitorInfo.

        邀请方的服务实例名

        :return: The invitor_bcs_name of this InvitorInfo.
        :rtype: str
        """
        return self._invitor_bcs_name

    @invitor_bcs_name.setter
    def invitor_bcs_name(self, invitor_bcs_name):
        """Sets the invitor_bcs_name of this InvitorInfo.

        邀请方的服务实例名

        :param invitor_bcs_name: The invitor_bcs_name of this InvitorInfo.
        :type invitor_bcs_name: str
        """
        self._invitor_bcs_name = invitor_bcs_name

    @property
    def invitor_consensus(self):
        """Gets the invitor_consensus of this InvitorInfo.

        邀请方的共识

        :return: The invitor_consensus of this InvitorInfo.
        :rtype: str
        """
        return self._invitor_consensus

    @invitor_consensus.setter
    def invitor_consensus(self, invitor_consensus):
        """Sets the invitor_consensus of this InvitorInfo.

        邀请方的共识

        :param invitor_consensus: The invitor_consensus of this InvitorInfo.
        :type invitor_consensus: str
        """
        self._invitor_consensus = invitor_consensus

    @property
    def invitor_project_id(self):
        """Gets the invitor_project_id of this InvitorInfo.

        邀请方的projectID

        :return: The invitor_project_id of this InvitorInfo.
        :rtype: str
        """
        return self._invitor_project_id

    @invitor_project_id.setter
    def invitor_project_id(self, invitor_project_id):
        """Sets the invitor_project_id of this InvitorInfo.

        邀请方的projectID

        :param invitor_project_id: The invitor_project_id of this InvitorInfo.
        :type invitor_project_id: str
        """
        self._invitor_project_id = invitor_project_id

    @property
    def invitor_cluster_type(self):
        """Gets the invitor_cluster_type of this InvitorInfo.

        邀请方的集群类型

        :return: The invitor_cluster_type of this InvitorInfo.
        :rtype: str
        """
        return self._invitor_cluster_type

    @invitor_cluster_type.setter
    def invitor_cluster_type(self, invitor_cluster_type):
        """Sets the invitor_cluster_type of this InvitorInfo.

        邀请方的集群类型

        :param invitor_cluster_type: The invitor_cluster_type of this InvitorInfo.
        :type invitor_cluster_type: str
        """
        self._invitor_cluster_type = invitor_cluster_type

    @property
    def invitor_database_type(self):
        """Gets the invitor_database_type of this InvitorInfo.

        邀请方数据库类型

        :return: The invitor_database_type of this InvitorInfo.
        :rtype: str
        """
        return self._invitor_database_type

    @invitor_database_type.setter
    def invitor_database_type(self, invitor_database_type):
        """Sets the invitor_database_type of this InvitorInfo.

        邀请方数据库类型

        :param invitor_database_type: The invitor_database_type of this InvitorInfo.
        :type invitor_database_type: str
        """
        self._invitor_database_type = invitor_database_type

    @property
    def invitor_signature_algorithm(self):
        """Gets the invitor_signature_algorithm of this InvitorInfo.

        邀请方的签名算法

        :return: The invitor_signature_algorithm of this InvitorInfo.
        :rtype: str
        """
        return self._invitor_signature_algorithm

    @invitor_signature_algorithm.setter
    def invitor_signature_algorithm(self, invitor_signature_algorithm):
        """Sets the invitor_signature_algorithm of this InvitorInfo.

        邀请方的签名算法

        :param invitor_signature_algorithm: The invitor_signature_algorithm of this InvitorInfo.
        :type invitor_signature_algorithm: str
        """
        self._invitor_signature_algorithm = invitor_signature_algorithm

    @property
    def invitor_fabric_version(self):
        """Gets the invitor_fabric_version of this InvitorInfo.

        邀请方的fabric版本

        :return: The invitor_fabric_version of this InvitorInfo.
        :rtype: str
        """
        return self._invitor_fabric_version

    @invitor_fabric_version.setter
    def invitor_fabric_version(self, invitor_fabric_version):
        """Sets the invitor_fabric_version of this InvitorInfo.

        邀请方的fabric版本

        :param invitor_fabric_version: The invitor_fabric_version of this InvitorInfo.
        :type invitor_fabric_version: str
        """
        self._invitor_fabric_version = invitor_fabric_version

    @property
    def order_fade_enabled(self):
        """Gets the order_fade_enabled of this InvitorInfo.

        是否允许共识节点老化

        :return: The order_fade_enabled of this InvitorInfo.
        :rtype: bool
        """
        return self._order_fade_enabled

    @order_fade_enabled.setter
    def order_fade_enabled(self, order_fade_enabled):
        """Sets the order_fade_enabled of this InvitorInfo.

        是否允许共识节点老化

        :param order_fade_enabled: The order_fade_enabled of this InvitorInfo.
        :type order_fade_enabled: bool
        """
        self._order_fade_enabled = order_fade_enabled

    @property
    def order_fade_cache(self):
        """Gets the order_fade_cache of this InvitorInfo.

        共识节点的老化阈值

        :return: The order_fade_cache of this InvitorInfo.
        :rtype: int
        """
        return self._order_fade_cache

    @order_fade_cache.setter
    def order_fade_cache(self, order_fade_cache):
        """Sets the order_fade_cache of this InvitorInfo.

        共识节点的老化阈值

        :param order_fade_cache: The order_fade_cache of this InvitorInfo.
        :type order_fade_cache: int
        """
        self._order_fade_cache = order_fade_cache

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
        if not isinstance(other, InvitorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
