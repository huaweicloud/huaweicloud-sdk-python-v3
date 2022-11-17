# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRuleCheckCaseResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_description': 'str',
        'current_value': 'str',
        'suggest_value': 'str'
    }

    attribute_map = {
        'check_description': 'check_description',
        'current_value': 'current_value',
        'suggest_value': 'suggest_value'
    }

    def __init__(self, check_description=None, current_value=None, suggest_value=None):
        """CheckRuleCheckCaseResponseInfo

        The model defined in huaweicloud sdk

        :param check_description: 检测用例描述
        :type check_description: str
        :param current_value: 当前结果
        :type current_value: str
        :param suggest_value: 期待结果
        :type suggest_value: str
        """
        
        

        self._check_description = None
        self._current_value = None
        self._suggest_value = None
        self.discriminator = None

        if check_description is not None:
            self.check_description = check_description
        if current_value is not None:
            self.current_value = current_value
        if suggest_value is not None:
            self.suggest_value = suggest_value

    @property
    def check_description(self):
        """Gets the check_description of this CheckRuleCheckCaseResponseInfo.

        检测用例描述

        :return: The check_description of this CheckRuleCheckCaseResponseInfo.
        :rtype: str
        """
        return self._check_description

    @check_description.setter
    def check_description(self, check_description):
        """Sets the check_description of this CheckRuleCheckCaseResponseInfo.

        检测用例描述

        :param check_description: The check_description of this CheckRuleCheckCaseResponseInfo.
        :type check_description: str
        """
        self._check_description = check_description

    @property
    def current_value(self):
        """Gets the current_value of this CheckRuleCheckCaseResponseInfo.

        当前结果

        :return: The current_value of this CheckRuleCheckCaseResponseInfo.
        :rtype: str
        """
        return self._current_value

    @current_value.setter
    def current_value(self, current_value):
        """Sets the current_value of this CheckRuleCheckCaseResponseInfo.

        当前结果

        :param current_value: The current_value of this CheckRuleCheckCaseResponseInfo.
        :type current_value: str
        """
        self._current_value = current_value

    @property
    def suggest_value(self):
        """Gets the suggest_value of this CheckRuleCheckCaseResponseInfo.

        期待结果

        :return: The suggest_value of this CheckRuleCheckCaseResponseInfo.
        :rtype: str
        """
        return self._suggest_value

    @suggest_value.setter
    def suggest_value(self, suggest_value):
        """Sets the suggest_value of this CheckRuleCheckCaseResponseInfo.

        期待结果

        :param suggest_value: The suggest_value of this CheckRuleCheckCaseResponseInfo.
        :type suggest_value: str
        """
        self._suggest_value = suggest_value

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
        if not isinstance(other, CheckRuleCheckCaseResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
