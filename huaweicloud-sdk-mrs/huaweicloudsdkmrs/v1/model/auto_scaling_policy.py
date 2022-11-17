# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoScalingPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_scaling_enable': 'bool',
        'min_capacity': 'int',
        'max_capacity': 'int',
        'resources_plans': 'list[ResourcesPlan]',
        'rules': 'list[Rule]',
        'exec_scripts': 'list[ScaleScript]'
    }

    attribute_map = {
        'auto_scaling_enable': 'auto_scaling_enable',
        'min_capacity': 'min_capacity',
        'max_capacity': 'max_capacity',
        'resources_plans': 'resources_plans',
        'rules': 'rules',
        'exec_scripts': 'exec_scripts'
    }

    def __init__(self, auto_scaling_enable=None, min_capacity=None, max_capacity=None, resources_plans=None, rules=None, exec_scripts=None):
        """AutoScalingPolicy

        The model defined in huaweicloud sdk

        :param auto_scaling_enable: 当前自动伸缩规则是否开启。
        :type auto_scaling_enable: bool
        :param min_capacity: 指定该节点组的最小保留节点数。  取值范围：[0～500]
        :type min_capacity: int
        :param max_capacity: 指定该节点组的最大节点数。  取值范围：[0～500]
        :type max_capacity: int
        :param resources_plans: 资源计划列表。若该参数为空表示不启用资源计划。  当启用弹性伸缩时，资源计划与自动伸缩规则需至少配置其中一种。
        :type resources_plans: list[:class:`huaweicloudsdkmrs.v1.ResourcesPlan`]
        :param rules: 自动伸缩的规则列表。  当启用弹性伸缩时，资源计划与自动伸缩规则需至少配置其中一种。
        :type rules: list[:class:`huaweicloudsdkmrs.v1.Rule`]
        :param exec_scripts: 弹性伸缩自定义自动化脚本列表。若该参数为空表示不启用自动化脚本。
        :type exec_scripts: list[:class:`huaweicloudsdkmrs.v1.ScaleScript`]
        """
        
        

        self._auto_scaling_enable = None
        self._min_capacity = None
        self._max_capacity = None
        self._resources_plans = None
        self._rules = None
        self._exec_scripts = None
        self.discriminator = None

        self.auto_scaling_enable = auto_scaling_enable
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity
        if resources_plans is not None:
            self.resources_plans = resources_plans
        if rules is not None:
            self.rules = rules
        if exec_scripts is not None:
            self.exec_scripts = exec_scripts

    @property
    def auto_scaling_enable(self):
        """Gets the auto_scaling_enable of this AutoScalingPolicy.

        当前自动伸缩规则是否开启。

        :return: The auto_scaling_enable of this AutoScalingPolicy.
        :rtype: bool
        """
        return self._auto_scaling_enable

    @auto_scaling_enable.setter
    def auto_scaling_enable(self, auto_scaling_enable):
        """Sets the auto_scaling_enable of this AutoScalingPolicy.

        当前自动伸缩规则是否开启。

        :param auto_scaling_enable: The auto_scaling_enable of this AutoScalingPolicy.
        :type auto_scaling_enable: bool
        """
        self._auto_scaling_enable = auto_scaling_enable

    @property
    def min_capacity(self):
        """Gets the min_capacity of this AutoScalingPolicy.

        指定该节点组的最小保留节点数。  取值范围：[0～500]

        :return: The min_capacity of this AutoScalingPolicy.
        :rtype: int
        """
        return self._min_capacity

    @min_capacity.setter
    def min_capacity(self, min_capacity):
        """Sets the min_capacity of this AutoScalingPolicy.

        指定该节点组的最小保留节点数。  取值范围：[0～500]

        :param min_capacity: The min_capacity of this AutoScalingPolicy.
        :type min_capacity: int
        """
        self._min_capacity = min_capacity

    @property
    def max_capacity(self):
        """Gets the max_capacity of this AutoScalingPolicy.

        指定该节点组的最大节点数。  取值范围：[0～500]

        :return: The max_capacity of this AutoScalingPolicy.
        :rtype: int
        """
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        """Sets the max_capacity of this AutoScalingPolicy.

        指定该节点组的最大节点数。  取值范围：[0～500]

        :param max_capacity: The max_capacity of this AutoScalingPolicy.
        :type max_capacity: int
        """
        self._max_capacity = max_capacity

    @property
    def resources_plans(self):
        """Gets the resources_plans of this AutoScalingPolicy.

        资源计划列表。若该参数为空表示不启用资源计划。  当启用弹性伸缩时，资源计划与自动伸缩规则需至少配置其中一种。

        :return: The resources_plans of this AutoScalingPolicy.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.ResourcesPlan`]
        """
        return self._resources_plans

    @resources_plans.setter
    def resources_plans(self, resources_plans):
        """Sets the resources_plans of this AutoScalingPolicy.

        资源计划列表。若该参数为空表示不启用资源计划。  当启用弹性伸缩时，资源计划与自动伸缩规则需至少配置其中一种。

        :param resources_plans: The resources_plans of this AutoScalingPolicy.
        :type resources_plans: list[:class:`huaweicloudsdkmrs.v1.ResourcesPlan`]
        """
        self._resources_plans = resources_plans

    @property
    def rules(self):
        """Gets the rules of this AutoScalingPolicy.

        自动伸缩的规则列表。  当启用弹性伸缩时，资源计划与自动伸缩规则需至少配置其中一种。

        :return: The rules of this AutoScalingPolicy.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.Rule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this AutoScalingPolicy.

        自动伸缩的规则列表。  当启用弹性伸缩时，资源计划与自动伸缩规则需至少配置其中一种。

        :param rules: The rules of this AutoScalingPolicy.
        :type rules: list[:class:`huaweicloudsdkmrs.v1.Rule`]
        """
        self._rules = rules

    @property
    def exec_scripts(self):
        """Gets the exec_scripts of this AutoScalingPolicy.

        弹性伸缩自定义自动化脚本列表。若该参数为空表示不启用自动化脚本。

        :return: The exec_scripts of this AutoScalingPolicy.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.ScaleScript`]
        """
        return self._exec_scripts

    @exec_scripts.setter
    def exec_scripts(self, exec_scripts):
        """Sets the exec_scripts of this AutoScalingPolicy.

        弹性伸缩自定义自动化脚本列表。若该参数为空表示不启用自动化脚本。

        :param exec_scripts: The exec_scripts of this AutoScalingPolicy.
        :type exec_scripts: list[:class:`huaweicloudsdkmrs.v1.ScaleScript`]
        """
        self._exec_scripts = exec_scripts

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
        if not isinstance(other, AutoScalingPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
