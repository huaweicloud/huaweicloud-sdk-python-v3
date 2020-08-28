# coding: utf-8

import pprint
import re

import six





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
        'flow': 'FlowItem',
        'states': 'dict(str, TemplateState)',
        'workflow': 'Workflow'
    }

    attribute_map = {
        'flow': 'flow',
        'states': 'states',
        'workflow': 'workflow'
    }

    def __init__(self, flow=None, states=None, workflow=None):
        """TemplateCddl - a model defined in huaweicloud sdk"""
        
        

        self._flow = None
        self._states = None
        self._workflow = None
        self.discriminator = None

        self.flow = flow
        self.states = states
        self.workflow = workflow

    @property
    def flow(self):
        """Gets the flow of this TemplateCddl.


        :return: The flow of this TemplateCddl.
        :rtype: FlowItem
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this TemplateCddl.


        :param flow: The flow of this TemplateCddl.
        :type: FlowItem
        """
        self._flow = flow

    @property
    def states(self):
        """Gets the states of this TemplateCddl.

        子任务states，map类型数据

        :return: The states of this TemplateCddl.
        :rtype: dict(str, TemplateState)
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this TemplateCddl.

        子任务states，map类型数据

        :param states: The states of this TemplateCddl.
        :type: dict(str, TemplateState)
        """
        self._states = states

    @property
    def workflow(self):
        """Gets the workflow of this TemplateCddl.


        :return: The workflow of this TemplateCddl.
        :rtype: Workflow
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this TemplateCddl.


        :param workflow: The workflow of this TemplateCddl.
        :type: Workflow
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TemplateCddl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
