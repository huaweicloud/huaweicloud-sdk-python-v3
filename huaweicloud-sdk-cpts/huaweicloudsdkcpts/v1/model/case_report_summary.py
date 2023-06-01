# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseReportSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_aw_info_list': 'list[CaseAwInfo]',
        'err_message': 'str'
    }

    attribute_map = {
        'case_aw_info_list': 'case_aw_info_list',
        'err_message': 'err_message'
    }

    def __init__(self, case_aw_info_list=None, err_message=None):
        """CaseReportSummary

        The model defined in huaweicloud sdk

        :param case_aw_info_list: 用例和aw信息视图
        :type case_aw_info_list: list[:class:`huaweicloudsdkcpts.v1.CaseAwInfo`]
        :param err_message: 错误信息
        :type err_message: str
        """
        
        

        self._case_aw_info_list = None
        self._err_message = None
        self.discriminator = None

        if case_aw_info_list is not None:
            self.case_aw_info_list = case_aw_info_list
        if err_message is not None:
            self.err_message = err_message

    @property
    def case_aw_info_list(self):
        """Gets the case_aw_info_list of this CaseReportSummary.

        用例和aw信息视图

        :return: The case_aw_info_list of this CaseReportSummary.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.CaseAwInfo`]
        """
        return self._case_aw_info_list

    @case_aw_info_list.setter
    def case_aw_info_list(self, case_aw_info_list):
        """Sets the case_aw_info_list of this CaseReportSummary.

        用例和aw信息视图

        :param case_aw_info_list: The case_aw_info_list of this CaseReportSummary.
        :type case_aw_info_list: list[:class:`huaweicloudsdkcpts.v1.CaseAwInfo`]
        """
        self._case_aw_info_list = case_aw_info_list

    @property
    def err_message(self):
        """Gets the err_message of this CaseReportSummary.

        错误信息

        :return: The err_message of this CaseReportSummary.
        :rtype: str
        """
        return self._err_message

    @err_message.setter
    def err_message(self, err_message):
        """Sets the err_message of this CaseReportSummary.

        错误信息

        :param err_message: The err_message of this CaseReportSummary.
        :type err_message: str
        """
        self._err_message = err_message

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
        if not isinstance(other, CaseReportSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
