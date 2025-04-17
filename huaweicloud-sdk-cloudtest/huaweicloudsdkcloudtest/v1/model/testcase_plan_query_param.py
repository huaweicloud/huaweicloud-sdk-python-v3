# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestcasePlanQueryParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_uri_list': 'list[str]',
        'case_number_list': 'list[str]'
    }

    attribute_map = {
        'case_uri_list': 'case_uri_list',
        'case_number_list': 'case_number_list'
    }

    def __init__(self, case_uri_list=None, case_number_list=None):
        r"""TestcasePlanQueryParam

        The model defined in huaweicloud sdk

        :param case_uri_list: 测试用例URI列表（测试用例URI和编号填其中一个即可）
        :type case_uri_list: list[str]
        :param case_number_list: 测试用例编号列表（测试用例URI和编号填其中一个即可
        :type case_number_list: list[str]
        """
        
        

        self._case_uri_list = None
        self._case_number_list = None
        self.discriminator = None

        if case_uri_list is not None:
            self.case_uri_list = case_uri_list
        if case_number_list is not None:
            self.case_number_list = case_number_list

    @property
    def case_uri_list(self):
        r"""Gets the case_uri_list of this TestcasePlanQueryParam.

        测试用例URI列表（测试用例URI和编号填其中一个即可）

        :return: The case_uri_list of this TestcasePlanQueryParam.
        :rtype: list[str]
        """
        return self._case_uri_list

    @case_uri_list.setter
    def case_uri_list(self, case_uri_list):
        r"""Sets the case_uri_list of this TestcasePlanQueryParam.

        测试用例URI列表（测试用例URI和编号填其中一个即可）

        :param case_uri_list: The case_uri_list of this TestcasePlanQueryParam.
        :type case_uri_list: list[str]
        """
        self._case_uri_list = case_uri_list

    @property
    def case_number_list(self):
        r"""Gets the case_number_list of this TestcasePlanQueryParam.

        测试用例编号列表（测试用例URI和编号填其中一个即可

        :return: The case_number_list of this TestcasePlanQueryParam.
        :rtype: list[str]
        """
        return self._case_number_list

    @case_number_list.setter
    def case_number_list(self, case_number_list):
        r"""Sets the case_number_list of this TestcasePlanQueryParam.

        测试用例编号列表（测试用例URI和编号填其中一个即可

        :param case_number_list: The case_number_list of this TestcasePlanQueryParam.
        :type case_number_list: list[str]
        """
        self._case_number_list = case_number_list

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
        if not isinstance(other, TestcasePlanQueryParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
