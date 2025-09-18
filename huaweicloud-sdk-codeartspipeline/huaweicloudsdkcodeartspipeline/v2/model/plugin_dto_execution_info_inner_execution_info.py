# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginDTOExecutionInfoInnerExecutionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_type': 'str',
        'steps': 'list[PluginDTOExecutionInfoInnerExecutionInfoSteps]'
    }

    attribute_map = {
        'execution_type': 'execution_type',
        'steps': 'steps'
    }

    def __init__(self, execution_type=None, steps=None):
        r"""PluginDTOExecutionInfoInnerExecutionInfo

        The model defined in huaweicloud sdk

        :param execution_type: **参数解释**： 插件类型。 **约束限制**： 不涉及。 **取值范围**： CONTAINER, ZIP, SHELL, COMPOSITE。 **默认取值**： 不涉及。 
        :type execution_type: str
        :param steps: 
        :type steps: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginDTOExecutionInfoInnerExecutionInfoSteps`]
        """
        
        

        self._execution_type = None
        self._steps = None
        self.discriminator = None

        if execution_type is not None:
            self.execution_type = execution_type
        if steps is not None:
            self.steps = steps

    @property
    def execution_type(self):
        r"""Gets the execution_type of this PluginDTOExecutionInfoInnerExecutionInfo.

        **参数解释**： 插件类型。 **约束限制**： 不涉及。 **取值范围**： CONTAINER, ZIP, SHELL, COMPOSITE。 **默认取值**： 不涉及。 

        :return: The execution_type of this PluginDTOExecutionInfoInnerExecutionInfo.
        :rtype: str
        """
        return self._execution_type

    @execution_type.setter
    def execution_type(self, execution_type):
        r"""Sets the execution_type of this PluginDTOExecutionInfoInnerExecutionInfo.

        **参数解释**： 插件类型。 **约束限制**： 不涉及。 **取值范围**： CONTAINER, ZIP, SHELL, COMPOSITE。 **默认取值**： 不涉及。 

        :param execution_type: The execution_type of this PluginDTOExecutionInfoInnerExecutionInfo.
        :type execution_type: str
        """
        self._execution_type = execution_type

    @property
    def steps(self):
        r"""Gets the steps of this PluginDTOExecutionInfoInnerExecutionInfo.

        :return: The steps of this PluginDTOExecutionInfoInnerExecutionInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginDTOExecutionInfoInnerExecutionInfoSteps`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this PluginDTOExecutionInfoInnerExecutionInfo.

        :param steps: The steps of this PluginDTOExecutionInfoInnerExecutionInfo.
        :type steps: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginDTOExecutionInfoInnerExecutionInfoSteps`]
        """
        self._steps = steps

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
        if not isinstance(other, PluginDTOExecutionInfoInnerExecutionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
