# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'nic_num': 'int'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'nic_num': 'nic_num'
    }

    def __init__(self, vpc_id=None, nic_num=None):
        """NetConfig

        The model defined in huaweicloud sdk

        :param vpc_id: 边缘网络ID。  约束： - 创建边缘业务仅支持使用系统规划的虚拟私有云。
        :type vpc_id: str
        :param nic_num: 边缘实例绑定的网卡数量。  约束：一台边缘实例最少绑定一张网卡，最多绑定8张网卡。
        :type nic_num: int
        """
        
        

        self._vpc_id = None
        self._nic_num = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.nic_num = nic_num

    @property
    def vpc_id(self):
        """Gets the vpc_id of this NetConfig.

        边缘网络ID。  约束： - 创建边缘业务仅支持使用系统规划的虚拟私有云。

        :return: The vpc_id of this NetConfig.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this NetConfig.

        边缘网络ID。  约束： - 创建边缘业务仅支持使用系统规划的虚拟私有云。

        :param vpc_id: The vpc_id of this NetConfig.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def nic_num(self):
        """Gets the nic_num of this NetConfig.

        边缘实例绑定的网卡数量。  约束：一台边缘实例最少绑定一张网卡，最多绑定8张网卡。

        :return: The nic_num of this NetConfig.
        :rtype: int
        """
        return self._nic_num

    @nic_num.setter
    def nic_num(self, nic_num):
        """Sets the nic_num of this NetConfig.

        边缘实例绑定的网卡数量。  约束：一台边缘实例最少绑定一张网卡，最多绑定8张网卡。

        :param nic_num: The nic_num of this NetConfig.
        :type nic_num: int
        """
        self._nic_num = nic_num

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
        if not isinstance(other, NetConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
