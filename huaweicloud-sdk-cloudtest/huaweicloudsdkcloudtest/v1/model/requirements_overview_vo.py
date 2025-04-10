# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequirementsOverviewVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_number': 'int',
        'requirement_overview_list': 'list[RequirementOverviewVo]'
    }

    attribute_map = {
        'total_number': 'total_number',
        'requirement_overview_list': 'requirement_overview_list'
    }

    def __init__(self, total_number=None, requirement_overview_list=None):
        r"""RequirementsOverviewVo

        The model defined in huaweicloud sdk

        :param total_number: 质量报告需求测试情况总数
        :type total_number: int
        :param requirement_overview_list: 质量报告需求测试情况列表
        :type requirement_overview_list: list[:class:`huaweicloudsdkcloudtest.v1.RequirementOverviewVo`]
        """
        
        

        self._total_number = None
        self._requirement_overview_list = None
        self.discriminator = None

        if total_number is not None:
            self.total_number = total_number
        if requirement_overview_list is not None:
            self.requirement_overview_list = requirement_overview_list

    @property
    def total_number(self):
        r"""Gets the total_number of this RequirementsOverviewVo.

        质量报告需求测试情况总数

        :return: The total_number of this RequirementsOverviewVo.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        r"""Sets the total_number of this RequirementsOverviewVo.

        质量报告需求测试情况总数

        :param total_number: The total_number of this RequirementsOverviewVo.
        :type total_number: int
        """
        self._total_number = total_number

    @property
    def requirement_overview_list(self):
        r"""Gets the requirement_overview_list of this RequirementsOverviewVo.

        质量报告需求测试情况列表

        :return: The requirement_overview_list of this RequirementsOverviewVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.RequirementOverviewVo`]
        """
        return self._requirement_overview_list

    @requirement_overview_list.setter
    def requirement_overview_list(self, requirement_overview_list):
        r"""Sets the requirement_overview_list of this RequirementsOverviewVo.

        质量报告需求测试情况列表

        :param requirement_overview_list: The requirement_overview_list of this RequirementsOverviewVo.
        :type requirement_overview_list: list[:class:`huaweicloudsdkcloudtest.v1.RequirementOverviewVo`]
        """
        self._requirement_overview_list = requirement_overview_list

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
        if not isinstance(other, RequirementsOverviewVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
