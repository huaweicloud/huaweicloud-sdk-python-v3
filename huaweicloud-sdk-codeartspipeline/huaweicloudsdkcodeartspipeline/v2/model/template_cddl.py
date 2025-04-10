# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateCddl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flow': 'dict(str, dict(str, str))',
        'states': 'dict(str, TemplateState)',
        'workflow': 'Workflow'
    }

    attribute_map = {
        'flow': 'flow',
        'states': 'states',
        'workflow': 'workflow'
    }

    def __init__(self, flow=None, states=None, workflow=None):
        r"""TemplateCddl

        The model defined in huaweicloud sdk

        :param flow: 编排flow详情，描述流水线内各阶段任务的串并行关系。map类型数据，key为阶段名字，默认第一阶段initial，最后阶段为final，其余名字以&#39;state_数字&#39;标识。value为该阶段内任务(以&#39;Task_数字&#39;标识)以及后续阶段的标识。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取
        :type flow: dict(str, dict(str, str))
        :param states: 编排State详情，map类型数据。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取
        :type states: dict(str, TemplateState)
        :param workflow: 
        :type workflow: :class:`huaweicloudsdkcodeartspipeline.v2.Workflow`
        """
        
        

        self._flow = None
        self._states = None
        self._workflow = None
        self.discriminator = None

        self.flow = flow
        self.states = states
        self.workflow = workflow

    @property
    def flow(self):
        r"""Gets the flow of this TemplateCddl.

        编排flow详情，描述流水线内各阶段任务的串并行关系。map类型数据，key为阶段名字，默认第一阶段initial，最后阶段为final，其余名字以'state_数字'标识。value为该阶段内任务(以'Task_数字'标识)以及后续阶段的标识。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :return: The flow of this TemplateCddl.
        :rtype: dict(str, dict(str, str))
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        r"""Sets the flow of this TemplateCddl.

        编排flow详情，描述流水线内各阶段任务的串并行关系。map类型数据，key为阶段名字，默认第一阶段initial，最后阶段为final，其余名字以'state_数字'标识。value为该阶段内任务(以'Task_数字'标识)以及后续阶段的标识。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :param flow: The flow of this TemplateCddl.
        :type flow: dict(str, dict(str, str))
        """
        self._flow = flow

    @property
    def states(self):
        r"""Gets the states of this TemplateCddl.

        编排State详情，map类型数据。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :return: The states of this TemplateCddl.
        :rtype: dict(str, TemplateState)
        """
        return self._states

    @states.setter
    def states(self, states):
        r"""Sets the states of this TemplateCddl.

        编排State详情，map类型数据。本字段为描述流水线基础编排数据之一，建议可通过流水线真实界面基于模板创建接口中获取

        :param states: The states of this TemplateCddl.
        :type states: dict(str, TemplateState)
        """
        self._states = states

    @property
    def workflow(self):
        r"""Gets the workflow of this TemplateCddl.

        :return: The workflow of this TemplateCddl.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.Workflow`
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        r"""Sets the workflow of this TemplateCddl.

        :param workflow: The workflow of this TemplateCddl.
        :type workflow: :class:`huaweicloudsdkcodeartspipeline.v2.Workflow`
        """
        self._workflow = workflow

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
        if not isinstance(other, TemplateCddl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
