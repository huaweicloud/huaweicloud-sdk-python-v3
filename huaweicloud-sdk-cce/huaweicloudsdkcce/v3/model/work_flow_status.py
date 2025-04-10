# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkFlowStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'WorkFlowPhase',
        'point_statuses': 'list[PointStatus]',
        'line_statuses': 'list[LineStatus]'
    }

    attribute_map = {
        'phase': 'phase',
        'point_statuses': 'pointStatuses',
        'line_statuses': 'lineStatuses'
    }

    def __init__(self, phase=None, point_statuses=None, line_statuses=None):
        r"""WorkFlowStatus

        The model defined in huaweicloud sdk

        :param phase: 
        :type phase: :class:`huaweicloudsdkcce.v3.WorkFlowPhase`
        :param point_statuses: 升级流程中的各个任务项的执行状态
        :type point_statuses: list[:class:`huaweicloudsdkcce.v3.PointStatus`]
        :param line_statuses: 表示该升级流程的任务执行线路
        :type line_statuses: list[:class:`huaweicloudsdkcce.v3.LineStatus`]
        """
        
        

        self._phase = None
        self._point_statuses = None
        self._line_statuses = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if point_statuses is not None:
            self.point_statuses = point_statuses
        if line_statuses is not None:
            self.line_statuses = line_statuses

    @property
    def phase(self):
        r"""Gets the phase of this WorkFlowStatus.

        :return: The phase of this WorkFlowStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.WorkFlowPhase`
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this WorkFlowStatus.

        :param phase: The phase of this WorkFlowStatus.
        :type phase: :class:`huaweicloudsdkcce.v3.WorkFlowPhase`
        """
        self._phase = phase

    @property
    def point_statuses(self):
        r"""Gets the point_statuses of this WorkFlowStatus.

        升级流程中的各个任务项的执行状态

        :return: The point_statuses of this WorkFlowStatus.
        :rtype: list[:class:`huaweicloudsdkcce.v3.PointStatus`]
        """
        return self._point_statuses

    @point_statuses.setter
    def point_statuses(self, point_statuses):
        r"""Sets the point_statuses of this WorkFlowStatus.

        升级流程中的各个任务项的执行状态

        :param point_statuses: The point_statuses of this WorkFlowStatus.
        :type point_statuses: list[:class:`huaweicloudsdkcce.v3.PointStatus`]
        """
        self._point_statuses = point_statuses

    @property
    def line_statuses(self):
        r"""Gets the line_statuses of this WorkFlowStatus.

        表示该升级流程的任务执行线路

        :return: The line_statuses of this WorkFlowStatus.
        :rtype: list[:class:`huaweicloudsdkcce.v3.LineStatus`]
        """
        return self._line_statuses

    @line_statuses.setter
    def line_statuses(self, line_statuses):
        r"""Sets the line_statuses of this WorkFlowStatus.

        表示该升级流程的任务执行线路

        :param line_statuses: The line_statuses of this WorkFlowStatus.
        :type line_statuses: list[:class:`huaweicloudsdkcce.v3.LineStatus`]
        """
        self._line_statuses = line_statuses

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
        if not isinstance(other, WorkFlowStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
