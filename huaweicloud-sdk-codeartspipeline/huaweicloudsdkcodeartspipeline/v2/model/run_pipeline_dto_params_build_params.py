# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunPipelineDTOParamsBuildParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'build_type': 'str',
        'event_type': 'str',
        'target_branch': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'build_type': 'build_type',
        'event_type': 'event_type',
        'target_branch': 'target_branch',
        'tag': 'tag'
    }

    def __init__(self, build_type=None, event_type=None, target_branch=None, tag=None):
        r"""RunPipelineDTOParamsBuildParams

        The model defined in huaweicloud sdk

        :param build_type: **参数解释**： 代码仓触发类型，包含branch-分支触发，tag-标签触发等。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type build_type: str
        :param event_type: **参数解释**： 流水线的触发方式。 - Manual：手动触发。 - Scheduler：定时任务。 - MR：MR触发。 - Push：Push事件触发。 - CreateTag：Tag事件触发。 - Issue：Issue触发。 - Note：评论触发。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type event_type: str
        :param target_branch: **参数解释**： 流水线触发运行分支。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type target_branch: str
        :param tag: **参数解释**： 流水线触发运行的标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type tag: str
        """
        
        

        self._build_type = None
        self._event_type = None
        self._target_branch = None
        self._tag = None
        self.discriminator = None

        self.build_type = build_type
        if event_type is not None:
            self.event_type = event_type
        if target_branch is not None:
            self.target_branch = target_branch
        if tag is not None:
            self.tag = tag

    @property
    def build_type(self):
        r"""Gets the build_type of this RunPipelineDTOParamsBuildParams.

        **参数解释**： 代码仓触发类型，包含branch-分支触发，tag-标签触发等。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The build_type of this RunPipelineDTOParamsBuildParams.
        :rtype: str
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        r"""Sets the build_type of this RunPipelineDTOParamsBuildParams.

        **参数解释**： 代码仓触发类型，包含branch-分支触发，tag-标签触发等。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param build_type: The build_type of this RunPipelineDTOParamsBuildParams.
        :type build_type: str
        """
        self._build_type = build_type

    @property
    def event_type(self):
        r"""Gets the event_type of this RunPipelineDTOParamsBuildParams.

        **参数解释**： 流水线的触发方式。 - Manual：手动触发。 - Scheduler：定时任务。 - MR：MR触发。 - Push：Push事件触发。 - CreateTag：Tag事件触发。 - Issue：Issue触发。 - Note：评论触发。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The event_type of this RunPipelineDTOParamsBuildParams.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this RunPipelineDTOParamsBuildParams.

        **参数解释**： 流水线的触发方式。 - Manual：手动触发。 - Scheduler：定时任务。 - MR：MR触发。 - Push：Push事件触发。 - CreateTag：Tag事件触发。 - Issue：Issue触发。 - Note：评论触发。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param event_type: The event_type of this RunPipelineDTOParamsBuildParams.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def target_branch(self):
        r"""Gets the target_branch of this RunPipelineDTOParamsBuildParams.

        **参数解释**： 流水线触发运行分支。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The target_branch of this RunPipelineDTOParamsBuildParams.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this RunPipelineDTOParamsBuildParams.

        **参数解释**： 流水线触发运行分支。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param target_branch: The target_branch of this RunPipelineDTOParamsBuildParams.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def tag(self):
        r"""Gets the tag of this RunPipelineDTOParamsBuildParams.

        **参数解释**： 流水线触发运行的标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The tag of this RunPipelineDTOParamsBuildParams.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this RunPipelineDTOParamsBuildParams.

        **参数解释**： 流水线触发运行的标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param tag: The tag of this RunPipelineDTOParamsBuildParams.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, RunPipelineDTOParamsBuildParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
