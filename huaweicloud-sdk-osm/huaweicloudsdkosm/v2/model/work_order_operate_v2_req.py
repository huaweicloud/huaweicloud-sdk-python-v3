# coding: utf-8

import pprint
import re

import six





class WorkOrderOperateV2Req:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'judgement': 'str',
        'operate_desc': 'str',
        'group_id': 'str',
        'incident_satisfaction_list': 'list[IncidentSatisfactionV2Do]'
    }

    attribute_map = {
        'judgement': 'judgement',
        'operate_desc': 'operate_desc',
        'group_id': 'group_id',
        'incident_satisfaction_list': 'incident_satisfaction_list'
    }

    def __init__(self, judgement=None, operate_desc=None, group_id=None, incident_satisfaction_list=None):
        """WorkOrderOperateV2Req - a model defined in huaweicloud sdk"""
        
        

        self._judgement = None
        self._operate_desc = None
        self._group_id = None
        self._incident_satisfaction_list = None
        self.discriminator = None

        if judgement is not None:
            self.judgement = judgement
        if operate_desc is not None:
            self.operate_desc = operate_desc
        if group_id is not None:
            self.group_id = group_id
        if incident_satisfaction_list is not None:
            self.incident_satisfaction_list = incident_satisfaction_list

    @property
    def judgement(self):
        """Gets the judgement of this WorkOrderOperateV2Req.

        评价内容

        :return: The judgement of this WorkOrderOperateV2Req.
        :rtype: str
        """
        return self._judgement

    @judgement.setter
    def judgement(self, judgement):
        """Sets the judgement of this WorkOrderOperateV2Req.

        评价内容

        :param judgement: The judgement of this WorkOrderOperateV2Req.
        :type: str
        """
        self._judgement = judgement

    @property
    def operate_desc(self):
        """Gets the operate_desc of this WorkOrderOperateV2Req.

        操作描述

        :return: The operate_desc of this WorkOrderOperateV2Req.
        :rtype: str
        """
        return self._operate_desc

    @operate_desc.setter
    def operate_desc(self, operate_desc):
        """Sets the operate_desc of this WorkOrderOperateV2Req.

        操作描述

        :param operate_desc: The operate_desc of this WorkOrderOperateV2Req.
        :type: str
        """
        self._operate_desc = operate_desc

    @property
    def group_id(self):
        """Gets the group_id of this WorkOrderOperateV2Req.

        组id

        :return: The group_id of this WorkOrderOperateV2Req.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this WorkOrderOperateV2Req.

        组id

        :param group_id: The group_id of this WorkOrderOperateV2Req.
        :type: str
        """
        self._group_id = group_id

    @property
    def incident_satisfaction_list(self):
        """Gets the incident_satisfaction_list of this WorkOrderOperateV2Req.

        工单满意度列表

        :return: The incident_satisfaction_list of this WorkOrderOperateV2Req.
        :rtype: list[IncidentSatisfactionV2Do]
        """
        return self._incident_satisfaction_list

    @incident_satisfaction_list.setter
    def incident_satisfaction_list(self, incident_satisfaction_list):
        """Sets the incident_satisfaction_list of this WorkOrderOperateV2Req.

        工单满意度列表

        :param incident_satisfaction_list: The incident_satisfaction_list of this WorkOrderOperateV2Req.
        :type: list[IncidentSatisfactionV2Do]
        """
        self._incident_satisfaction_list = incident_satisfaction_list

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
        if not isinstance(other, WorkOrderOperateV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other