# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkElementChange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_id': 'str'
    }

    attribute_map = {
        'operation_id': 'operation_id'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, operation_id=None):
        """CentralNetworkElementChange

        The model defined in huaweicloud sdk

        :param operation_id: 实例状态。 - CreateCentralNetworkPlane: 新增中心网络平面 - DeleteCentralNetworkPlane: 移除中心网络平面 - UpdateCentralNetworkPlane: 更新中心网络平面 - CreateCentralNetworkErInstance: 新增中心网络ER实例 - DeleteCentralNetworkErInstance: 移除中心网络ER实例 - CreateCentralNetworkErConnection: 新增中心网络ER连接 - DeleteCentralNetworkErConnection: 移除中心网络ER连接 - CreateCentralNetworkErTable: 新增中心网络ER路由表 - DeleteCentralNetworkErTable: 移除中心网络ER路由表
        :type operation_id: str
        """
        
        

        self._operation_id = None
        self.discriminator = 'operation_id'

        self.operation_id = operation_id

    @property
    def operation_id(self):
        """Gets the operation_id of this CentralNetworkElementChange.

        实例状态。 - CreateCentralNetworkPlane: 新增中心网络平面 - DeleteCentralNetworkPlane: 移除中心网络平面 - UpdateCentralNetworkPlane: 更新中心网络平面 - CreateCentralNetworkErInstance: 新增中心网络ER实例 - DeleteCentralNetworkErInstance: 移除中心网络ER实例 - CreateCentralNetworkErConnection: 新增中心网络ER连接 - DeleteCentralNetworkErConnection: 移除中心网络ER连接 - CreateCentralNetworkErTable: 新增中心网络ER路由表 - DeleteCentralNetworkErTable: 移除中心网络ER路由表

        :return: The operation_id of this CentralNetworkElementChange.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this CentralNetworkElementChange.

        实例状态。 - CreateCentralNetworkPlane: 新增中心网络平面 - DeleteCentralNetworkPlane: 移除中心网络平面 - UpdateCentralNetworkPlane: 更新中心网络平面 - CreateCentralNetworkErInstance: 新增中心网络ER实例 - DeleteCentralNetworkErInstance: 移除中心网络ER实例 - CreateCentralNetworkErConnection: 新增中心网络ER连接 - DeleteCentralNetworkErConnection: 移除中心网络ER连接 - CreateCentralNetworkErTable: 新增中心网络ER路由表 - DeleteCentralNetworkErTable: 移除中心网络ER路由表

        :param operation_id: The operation_id of this CentralNetworkElementChange.
        :type operation_id: str
        """
        self._operation_id = operation_id

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)
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
        if not isinstance(other, CentralNetworkElementChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
