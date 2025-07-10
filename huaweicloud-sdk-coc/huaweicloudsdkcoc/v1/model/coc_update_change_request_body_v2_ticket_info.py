# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocUpdateChangeRequestBodyV2TicketInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'work_flow_status': 'str'
    }

    attribute_map = {
        'phase': 'phase',
        'work_flow_status': 'work_flow_status'
    }

    def __init__(self, phase=None, work_flow_status=None):
        r"""CocUpdateChangeRequestBodyV2TicketInfo

        The model defined in huaweicloud sdk

        :param phase: 阶段
        :type phase: str
        :param work_flow_status: 状态
        :type work_flow_status: str
        """
        
        

        self._phase = None
        self._work_flow_status = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if work_flow_status is not None:
            self.work_flow_status = work_flow_status

    @property
    def phase(self):
        r"""Gets the phase of this CocUpdateChangeRequestBodyV2TicketInfo.

        阶段

        :return: The phase of this CocUpdateChangeRequestBodyV2TicketInfo.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this CocUpdateChangeRequestBodyV2TicketInfo.

        阶段

        :param phase: The phase of this CocUpdateChangeRequestBodyV2TicketInfo.
        :type phase: str
        """
        self._phase = phase

    @property
    def work_flow_status(self):
        r"""Gets the work_flow_status of this CocUpdateChangeRequestBodyV2TicketInfo.

        状态

        :return: The work_flow_status of this CocUpdateChangeRequestBodyV2TicketInfo.
        :rtype: str
        """
        return self._work_flow_status

    @work_flow_status.setter
    def work_flow_status(self, work_flow_status):
        r"""Sets the work_flow_status of this CocUpdateChangeRequestBodyV2TicketInfo.

        状态

        :param work_flow_status: The work_flow_status of this CocUpdateChangeRequestBodyV2TicketInfo.
        :type work_flow_status: str
        """
        self._work_flow_status = work_flow_status

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
        if not isinstance(other, CocUpdateChangeRequestBodyV2TicketInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
