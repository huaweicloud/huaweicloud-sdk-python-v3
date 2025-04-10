# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IteratorListFilterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pi_sprints': 'list[IssueListPiFilterInfo]',
        'plan_end_date_start': 'datetime',
        'plan_end_date_end': 'datetime'
    }

    attribute_map = {
        'pi_sprints': 'pi_sprints',
        'plan_end_date_start': 'plan_end_date_start',
        'plan_end_date_end': 'plan_end_date_end'
    }

    def __init__(self, pi_sprints=None, plan_end_date_start=None, plan_end_date_end=None):
        r"""IteratorListFilterInfo

        The model defined in huaweicloud sdk

        :param pi_sprints: pi过滤条件
        :type pi_sprints: list[:class:`huaweicloudsdkcloudtest.v1.IssueListPiFilterInfo`]
        :param plan_end_date_start: 计划结束间过滤开始时间点
        :type plan_end_date_start: datetime
        :param plan_end_date_end: 计划结束时间过滤结束时间点
        :type plan_end_date_end: datetime
        """
        
        

        self._pi_sprints = None
        self._plan_end_date_start = None
        self._plan_end_date_end = None
        self.discriminator = None

        if pi_sprints is not None:
            self.pi_sprints = pi_sprints
        if plan_end_date_start is not None:
            self.plan_end_date_start = plan_end_date_start
        if plan_end_date_end is not None:
            self.plan_end_date_end = plan_end_date_end

    @property
    def pi_sprints(self):
        r"""Gets the pi_sprints of this IteratorListFilterInfo.

        pi过滤条件

        :return: The pi_sprints of this IteratorListFilterInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.IssueListPiFilterInfo`]
        """
        return self._pi_sprints

    @pi_sprints.setter
    def pi_sprints(self, pi_sprints):
        r"""Sets the pi_sprints of this IteratorListFilterInfo.

        pi过滤条件

        :param pi_sprints: The pi_sprints of this IteratorListFilterInfo.
        :type pi_sprints: list[:class:`huaweicloudsdkcloudtest.v1.IssueListPiFilterInfo`]
        """
        self._pi_sprints = pi_sprints

    @property
    def plan_end_date_start(self):
        r"""Gets the plan_end_date_start of this IteratorListFilterInfo.

        计划结束间过滤开始时间点

        :return: The plan_end_date_start of this IteratorListFilterInfo.
        :rtype: datetime
        """
        return self._plan_end_date_start

    @plan_end_date_start.setter
    def plan_end_date_start(self, plan_end_date_start):
        r"""Sets the plan_end_date_start of this IteratorListFilterInfo.

        计划结束间过滤开始时间点

        :param plan_end_date_start: The plan_end_date_start of this IteratorListFilterInfo.
        :type plan_end_date_start: datetime
        """
        self._plan_end_date_start = plan_end_date_start

    @property
    def plan_end_date_end(self):
        r"""Gets the plan_end_date_end of this IteratorListFilterInfo.

        计划结束时间过滤结束时间点

        :return: The plan_end_date_end of this IteratorListFilterInfo.
        :rtype: datetime
        """
        return self._plan_end_date_end

    @plan_end_date_end.setter
    def plan_end_date_end(self, plan_end_date_end):
        r"""Sets the plan_end_date_end of this IteratorListFilterInfo.

        计划结束时间过滤结束时间点

        :param plan_end_date_end: The plan_end_date_end of this IteratorListFilterInfo.
        :type plan_end_date_end: datetime
        """
        self._plan_end_date_end = plan_end_date_end

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
        if not isinstance(other, IteratorListFilterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
