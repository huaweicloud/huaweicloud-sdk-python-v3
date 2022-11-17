# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentGroupUpdateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'slave_cluster_id': 'str',
        'auto_connection_test_switch': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'slave_cluster_id': 'slave_cluster_id',
        'auto_connection_test_switch': 'auto_connection_test_switch'
    }

    def __init__(self, name=None, description=None, slave_cluster_id=None, auto_connection_test_switch=None):
        """DeploymentGroupUpdateRequest

        The model defined in huaweicloud sdk

        :param name: 主机组名
        :type name: str
        :param description: 描述
        :type description: str
        :param slave_cluster_id: 自定义slave资源池id
        :type slave_cluster_id: str
        :param auto_connection_test_switch: 自动连通性验证 0不执行 1每日 2每周
        :type auto_connection_test_switch: int
        """
        
        

        self._name = None
        self._description = None
        self._slave_cluster_id = None
        self._auto_connection_test_switch = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if slave_cluster_id is not None:
            self.slave_cluster_id = slave_cluster_id
        if auto_connection_test_switch is not None:
            self.auto_connection_test_switch = auto_connection_test_switch

    @property
    def name(self):
        """Gets the name of this DeploymentGroupUpdateRequest.

        主机组名

        :return: The name of this DeploymentGroupUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentGroupUpdateRequest.

        主机组名

        :param name: The name of this DeploymentGroupUpdateRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this DeploymentGroupUpdateRequest.

        描述

        :return: The description of this DeploymentGroupUpdateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeploymentGroupUpdateRequest.

        描述

        :param description: The description of this DeploymentGroupUpdateRequest.
        :type description: str
        """
        self._description = description

    @property
    def slave_cluster_id(self):
        """Gets the slave_cluster_id of this DeploymentGroupUpdateRequest.

        自定义slave资源池id

        :return: The slave_cluster_id of this DeploymentGroupUpdateRequest.
        :rtype: str
        """
        return self._slave_cluster_id

    @slave_cluster_id.setter
    def slave_cluster_id(self, slave_cluster_id):
        """Sets the slave_cluster_id of this DeploymentGroupUpdateRequest.

        自定义slave资源池id

        :param slave_cluster_id: The slave_cluster_id of this DeploymentGroupUpdateRequest.
        :type slave_cluster_id: str
        """
        self._slave_cluster_id = slave_cluster_id

    @property
    def auto_connection_test_switch(self):
        """Gets the auto_connection_test_switch of this DeploymentGroupUpdateRequest.

        自动连通性验证 0不执行 1每日 2每周

        :return: The auto_connection_test_switch of this DeploymentGroupUpdateRequest.
        :rtype: int
        """
        return self._auto_connection_test_switch

    @auto_connection_test_switch.setter
    def auto_connection_test_switch(self, auto_connection_test_switch):
        """Sets the auto_connection_test_switch of this DeploymentGroupUpdateRequest.

        自动连通性验证 0不执行 1每日 2每周

        :param auto_connection_test_switch: The auto_connection_test_switch of this DeploymentGroupUpdateRequest.
        :type auto_connection_test_switch: int
        """
        self._auto_connection_test_switch = auto_connection_test_switch

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
        if not isinstance(other, DeploymentGroupUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
