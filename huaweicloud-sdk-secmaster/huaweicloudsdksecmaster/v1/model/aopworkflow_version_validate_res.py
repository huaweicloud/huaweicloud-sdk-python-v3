# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AopworkflowVersionValidateRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'taskconfig': 'str',
        'taskflow': 'str',
        'aopworkflow_id': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'taskconfig': 'taskconfig',
        'taskflow': 'taskflow',
        'aopworkflow_id': 'aopworkflow_id'
    }

    def __init__(self, mode=None, taskconfig=None, taskflow=None, aopworkflow_id=None):
        r"""AopworkflowVersionValidateRes

        The model defined in huaweicloud sdk

        :param mode: **参数解释**: 流程的校验类型 - BASIC 基础校验 - CIRCLE 环路校验 - APP_PARAMS 参数校验  **约束限制**: 不涉及         **取值范围**: - BASIC - CIRCLE - APP_PARAMS  **默认值**:  不涉及
        :type mode: str
        :param taskconfig: **参数解释**: 流程拓扑图的参数配置 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type taskconfig: str
        :param taskflow: **参数解释**: 流程的拓扑图的BASE64编码 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type taskflow: str
        :param aopworkflow_id: **参数解释**: 流程的ID **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type aopworkflow_id: str
        """
        
        

        self._mode = None
        self._taskconfig = None
        self._taskflow = None
        self._aopworkflow_id = None
        self.discriminator = None

        self.mode = mode
        self.taskconfig = taskconfig
        self.taskflow = taskflow
        self.aopworkflow_id = aopworkflow_id

    @property
    def mode(self):
        r"""Gets the mode of this AopworkflowVersionValidateRes.

        **参数解释**: 流程的校验类型 - BASIC 基础校验 - CIRCLE 环路校验 - APP_PARAMS 参数校验  **约束限制**: 不涉及         **取值范围**: - BASIC - CIRCLE - APP_PARAMS  **默认值**:  不涉及

        :return: The mode of this AopworkflowVersionValidateRes.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this AopworkflowVersionValidateRes.

        **参数解释**: 流程的校验类型 - BASIC 基础校验 - CIRCLE 环路校验 - APP_PARAMS 参数校验  **约束限制**: 不涉及         **取值范围**: - BASIC - CIRCLE - APP_PARAMS  **默认值**:  不涉及

        :param mode: The mode of this AopworkflowVersionValidateRes.
        :type mode: str
        """
        self._mode = mode

    @property
    def taskconfig(self):
        r"""Gets the taskconfig of this AopworkflowVersionValidateRes.

        **参数解释**: 流程拓扑图的参数配置 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The taskconfig of this AopworkflowVersionValidateRes.
        :rtype: str
        """
        return self._taskconfig

    @taskconfig.setter
    def taskconfig(self, taskconfig):
        r"""Sets the taskconfig of this AopworkflowVersionValidateRes.

        **参数解释**: 流程拓扑图的参数配置 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param taskconfig: The taskconfig of this AopworkflowVersionValidateRes.
        :type taskconfig: str
        """
        self._taskconfig = taskconfig

    @property
    def taskflow(self):
        r"""Gets the taskflow of this AopworkflowVersionValidateRes.

        **参数解释**: 流程的拓扑图的BASE64编码 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The taskflow of this AopworkflowVersionValidateRes.
        :rtype: str
        """
        return self._taskflow

    @taskflow.setter
    def taskflow(self, taskflow):
        r"""Sets the taskflow of this AopworkflowVersionValidateRes.

        **参数解释**: 流程的拓扑图的BASE64编码 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param taskflow: The taskflow of this AopworkflowVersionValidateRes.
        :type taskflow: str
        """
        self._taskflow = taskflow

    @property
    def aopworkflow_id(self):
        r"""Gets the aopworkflow_id of this AopworkflowVersionValidateRes.

        **参数解释**: 流程的ID **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The aopworkflow_id of this AopworkflowVersionValidateRes.
        :rtype: str
        """
        return self._aopworkflow_id

    @aopworkflow_id.setter
    def aopworkflow_id(self, aopworkflow_id):
        r"""Sets the aopworkflow_id of this AopworkflowVersionValidateRes.

        **参数解释**: 流程的ID **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param aopworkflow_id: The aopworkflow_id of this AopworkflowVersionValidateRes.
        :type aopworkflow_id: str
        """
        self._aopworkflow_id = aopworkflow_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AopworkflowVersionValidateRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
