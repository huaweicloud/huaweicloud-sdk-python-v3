# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseAutomationDetailsVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_automation_rate': 'str',
        'service_type_number_list': 'list[NameAndValueVo]'
    }

    attribute_map = {
        'case_automation_rate': 'case_automation_rate',
        'service_type_number_list': 'service_type_number_list'
    }

    def __init__(self, case_automation_rate=None, service_type_number_list=None):
        r"""CaseAutomationDetailsVo

        The model defined in huaweicloud sdk

        :param case_automation_rate: 用例自动化率
        :type case_automation_rate: str
        :param service_type_number_list: 服务类型对应的用例数目
        :type service_type_number_list: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        
        

        self._case_automation_rate = None
        self._service_type_number_list = None
        self.discriminator = None

        if case_automation_rate is not None:
            self.case_automation_rate = case_automation_rate
        if service_type_number_list is not None:
            self.service_type_number_list = service_type_number_list

    @property
    def case_automation_rate(self):
        r"""Gets the case_automation_rate of this CaseAutomationDetailsVo.

        用例自动化率

        :return: The case_automation_rate of this CaseAutomationDetailsVo.
        :rtype: str
        """
        return self._case_automation_rate

    @case_automation_rate.setter
    def case_automation_rate(self, case_automation_rate):
        r"""Sets the case_automation_rate of this CaseAutomationDetailsVo.

        用例自动化率

        :param case_automation_rate: The case_automation_rate of this CaseAutomationDetailsVo.
        :type case_automation_rate: str
        """
        self._case_automation_rate = case_automation_rate

    @property
    def service_type_number_list(self):
        r"""Gets the service_type_number_list of this CaseAutomationDetailsVo.

        服务类型对应的用例数目

        :return: The service_type_number_list of this CaseAutomationDetailsVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        return self._service_type_number_list

    @service_type_number_list.setter
    def service_type_number_list(self, service_type_number_list):
        r"""Sets the service_type_number_list of this CaseAutomationDetailsVo.

        服务类型对应的用例数目

        :param service_type_number_list: The service_type_number_list of this CaseAutomationDetailsVo.
        :type service_type_number_list: list[:class:`huaweicloudsdkcloudtest.v1.NameAndValueVo`]
        """
        self._service_type_number_list = service_type_number_list

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
        if not isinstance(other, CaseAutomationDetailsVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
