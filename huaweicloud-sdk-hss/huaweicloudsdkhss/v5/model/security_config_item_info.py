# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityConfigItemInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_name': 'str',
        'check_item_rule': 'str',
        'scan_result': 'str'
    }

    attribute_map = {
        'check_name': 'check_name',
        'check_item_rule': 'check_item_rule',
        'scan_result': 'scan_result'
    }

    def __init__(self, check_name=None, check_item_rule=None, scan_result=None):
        r"""SecurityConfigItemInfo

        The model defined in huaweicloud sdk

        :param check_name: **参数解释**： 基线名称 **取值范围**： 不涉及 
        :type check_name: str
        :param check_item_rule: **参数解释**： 检查项规则 **取值范围**： 不涉及 
        :type check_item_rule: str
        :param scan_result: **参数解释**： 检测结果 **取值范围**： - pass：通过 - failed：未通过 
        :type scan_result: str
        """
        
        

        self._check_name = None
        self._check_item_rule = None
        self._scan_result = None
        self.discriminator = None

        if check_name is not None:
            self.check_name = check_name
        if check_item_rule is not None:
            self.check_item_rule = check_item_rule
        if scan_result is not None:
            self.scan_result = scan_result

    @property
    def check_name(self):
        r"""Gets the check_name of this SecurityConfigItemInfo.

        **参数解释**： 基线名称 **取值范围**： 不涉及 

        :return: The check_name of this SecurityConfigItemInfo.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this SecurityConfigItemInfo.

        **参数解释**： 基线名称 **取值范围**： 不涉及 

        :param check_name: The check_name of this SecurityConfigItemInfo.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_item_rule(self):
        r"""Gets the check_item_rule of this SecurityConfigItemInfo.

        **参数解释**： 检查项规则 **取值范围**： 不涉及 

        :return: The check_item_rule of this SecurityConfigItemInfo.
        :rtype: str
        """
        return self._check_item_rule

    @check_item_rule.setter
    def check_item_rule(self, check_item_rule):
        r"""Sets the check_item_rule of this SecurityConfigItemInfo.

        **参数解释**： 检查项规则 **取值范围**： 不涉及 

        :param check_item_rule: The check_item_rule of this SecurityConfigItemInfo.
        :type check_item_rule: str
        """
        self._check_item_rule = check_item_rule

    @property
    def scan_result(self):
        r"""Gets the scan_result of this SecurityConfigItemInfo.

        **参数解释**： 检测结果 **取值范围**： - pass：通过 - failed：未通过 

        :return: The scan_result of this SecurityConfigItemInfo.
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        r"""Sets the scan_result of this SecurityConfigItemInfo.

        **参数解释**： 检测结果 **取值范围**： - pass：通过 - failed：未通过 

        :param scan_result: The scan_result of this SecurityConfigItemInfo.
        :type scan_result: str
        """
        self._scan_result = scan_result

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
        if not isinstance(other, SecurityConfigItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
