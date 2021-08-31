# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Rules:


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
        'adjustment_type': 'str',
        'cool_down_minutes': 'int',
        'scaling_adjustment': 'int',
        'trigger': 'Trigger'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'adjustment_type': 'adjustment_type',
        'cool_down_minutes': 'cool_down_minutes',
        'scaling_adjustment': 'scaling_adjustment',
        'trigger': 'trigger'
    }

    def __init__(self, name=None, description=None, adjustment_type=None, cool_down_minutes=None, scaling_adjustment=None, trigger=None):
        """Rules - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._adjustment_type = None
        self._cool_down_minutes = None
        self._scaling_adjustment = None
        self._trigger = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.adjustment_type = adjustment_type
        self.cool_down_minutes = cool_down_minutes
        self.scaling_adjustment = scaling_adjustment
        self.trigger = trigger

    @property
    def name(self):
        """Gets the name of this Rules.

        弹性伸缩规则的名称。  只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。  在一个节点组范围内，不允许重名。

        :return: The name of this Rules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Rules.

        弹性伸缩规则的名称。  只能由字母、数字、中划线和下划线组成，并且长度为1～64个字符。  在一个节点组范围内，不允许重名。

        :param name: The name of this Rules.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Rules.

        弹性伸缩规则的说明。  最大长度为1024字符。

        :return: The description of this Rules.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rules.

        弹性伸缩规则的说明。  最大长度为1024字符。

        :param description: The description of this Rules.
        :type: str
        """
        self._description = description

    @property
    def adjustment_type(self):
        """Gets the adjustment_type of this Rules.

        弹性伸缩规则的调整类型，只允许以下类型：  枚举值： - scale_out：扩容 - scale_in：缩容

        :return: The adjustment_type of this Rules.
        :rtype: str
        """
        return self._adjustment_type

    @adjustment_type.setter
    def adjustment_type(self, adjustment_type):
        """Sets the adjustment_type of this Rules.

        弹性伸缩规则的调整类型，只允许以下类型：  枚举值： - scale_out：扩容 - scale_in：缩容

        :param adjustment_type: The adjustment_type of this Rules.
        :type: str
        """
        self._adjustment_type = adjustment_type

    @property
    def cool_down_minutes(self):
        """Gets the cool_down_minutes of this Rules.

        触发弹性伸缩规则后，该集群处于冷却状态（不再执行弹性伸缩操作）的时长，单位为分钟。  取值范围[0～10080]，10080为一周的分钟数。

        :return: The cool_down_minutes of this Rules.
        :rtype: int
        """
        return self._cool_down_minutes

    @cool_down_minutes.setter
    def cool_down_minutes(self, cool_down_minutes):
        """Sets the cool_down_minutes of this Rules.

        触发弹性伸缩规则后，该集群处于冷却状态（不再执行弹性伸缩操作）的时长，单位为分钟。  取值范围[0～10080]，10080为一周的分钟数。

        :param cool_down_minutes: The cool_down_minutes of this Rules.
        :type: int
        """
        self._cool_down_minutes = cool_down_minutes

    @property
    def scaling_adjustment(self):
        """Gets the scaling_adjustment of this Rules.

        单次调整集群节点的个数。  取值范围[1～100]

        :return: The scaling_adjustment of this Rules.
        :rtype: int
        """
        return self._scaling_adjustment

    @scaling_adjustment.setter
    def scaling_adjustment(self, scaling_adjustment):
        """Sets the scaling_adjustment of this Rules.

        单次调整集群节点的个数。  取值范围[1～100]

        :param scaling_adjustment: The scaling_adjustment of this Rules.
        :type: int
        """
        self._scaling_adjustment = scaling_adjustment

    @property
    def trigger(self):
        """Gets the trigger of this Rules.


        :return: The trigger of this Rules.
        :rtype: Trigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this Rules.


        :param trigger: The trigger of this Rules.
        :type: Trigger
        """
        self._trigger = trigger

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
        if not isinstance(other, Rules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
