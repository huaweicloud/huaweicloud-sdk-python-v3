# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadPlanStageIdReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stage_id': 'str'
    }

    attribute_map = {
        'stage_id': 'stage_id'
    }

    def __init__(self, stage_id=None):
        r"""WorkloadPlanStageIdReq

        The model defined in huaweicloud sdk

        :param stage_id: **参数解释**： 资源管理计划阶段ID。 **取值范围**： 不涉及。
        :type stage_id: str
        """
        
        

        self._stage_id = None
        self.discriminator = None

        self.stage_id = stage_id

    @property
    def stage_id(self):
        r"""Gets the stage_id of this WorkloadPlanStageIdReq.

        **参数解释**： 资源管理计划阶段ID。 **取值范围**： 不涉及。

        :return: The stage_id of this WorkloadPlanStageIdReq.
        :rtype: str
        """
        return self._stage_id

    @stage_id.setter
    def stage_id(self, stage_id):
        r"""Sets the stage_id of this WorkloadPlanStageIdReq.

        **参数解释**： 资源管理计划阶段ID。 **取值范围**： 不涉及。

        :param stage_id: The stage_id of this WorkloadPlanStageIdReq.
        :type stage_id: str
        """
        self._stage_id = stage_id

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
        if not isinstance(other, WorkloadPlanStageIdReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
