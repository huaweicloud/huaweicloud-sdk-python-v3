# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepairPriorityListInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repair_priority': 'str',
        'host_num': 'int'
    }

    attribute_map = {
        'repair_priority': 'repair_priority',
        'host_num': 'host_num'
    }

    def __init__(self, repair_priority=None, host_num=None):
        r"""RepairPriorityListInfo

        The model defined in huaweicloud sdk

        :param repair_priority: **参数解释**: 修复优先级 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低 
        :type repair_priority: str
        :param host_num: **参数解释**: 当前修复优先级对应的主机数量 **取值范围**: 取值0-2147483647 
        :type host_num: int
        """
        
        

        self._repair_priority = None
        self._host_num = None
        self.discriminator = None

        if repair_priority is not None:
            self.repair_priority = repair_priority
        if host_num is not None:
            self.host_num = host_num

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this RepairPriorityListInfo.

        **参数解释**: 修复优先级 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低 

        :return: The repair_priority of this RepairPriorityListInfo.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this RepairPriorityListInfo.

        **参数解释**: 修复优先级 **取值范围**: - Critical：紧急 - High：高 - Medium：中 - Low：低 

        :param repair_priority: The repair_priority of this RepairPriorityListInfo.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

    @property
    def host_num(self):
        r"""Gets the host_num of this RepairPriorityListInfo.

        **参数解释**: 当前修复优先级对应的主机数量 **取值范围**: 取值0-2147483647 

        :return: The host_num of this RepairPriorityListInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this RepairPriorityListInfo.

        **参数解释**: 当前修复优先级对应的主机数量 **取值范围**: 取值0-2147483647 

        :param host_num: The host_num of this RepairPriorityListInfo.
        :type host_num: int
        """
        self._host_num = host_num

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
        if not isinstance(other, RepairPriorityListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
