# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginDTOExecutionInfoInnerExecutionInfoSteps:

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
        'task': 'str',
        'variables': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'task': 'task',
        'variables': 'variables'
    }

    def __init__(self, name=None, task=None, variables=None):
        r"""PluginDTOExecutionInfoInnerExecutionInfoSteps

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 任务名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type name: str
        :param task: **参数解释**： 任务类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type task: str
        :param variables: **参数解释**： 参数信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type variables: dict(str, object)
        """
        
        

        self._name = None
        self._task = None
        self._variables = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if task is not None:
            self.task = task
        if variables is not None:
            self.variables = variables

    @property
    def name(self):
        r"""Gets the name of this PluginDTOExecutionInfoInnerExecutionInfoSteps.

        **参数解释**： 任务名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The name of this PluginDTOExecutionInfoInnerExecutionInfoSteps.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PluginDTOExecutionInfoInnerExecutionInfoSteps.

        **参数解释**： 任务名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param name: The name of this PluginDTOExecutionInfoInnerExecutionInfoSteps.
        :type name: str
        """
        self._name = name

    @property
    def task(self):
        r"""Gets the task of this PluginDTOExecutionInfoInnerExecutionInfoSteps.

        **参数解释**： 任务类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The task of this PluginDTOExecutionInfoInnerExecutionInfoSteps.
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        r"""Sets the task of this PluginDTOExecutionInfoInnerExecutionInfoSteps.

        **参数解释**： 任务类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param task: The task of this PluginDTOExecutionInfoInnerExecutionInfoSteps.
        :type task: str
        """
        self._task = task

    @property
    def variables(self):
        r"""Gets the variables of this PluginDTOExecutionInfoInnerExecutionInfoSteps.

        **参数解释**： 参数信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The variables of this PluginDTOExecutionInfoInnerExecutionInfoSteps.
        :rtype: dict(str, object)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this PluginDTOExecutionInfoInnerExecutionInfoSteps.

        **参数解释**： 参数信息。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param variables: The variables of this PluginDTOExecutionInfoInnerExecutionInfoSteps.
        :type variables: dict(str, object)
        """
        self._variables = variables

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
        if not isinstance(other, PluginDTOExecutionInfoInnerExecutionInfoSteps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
