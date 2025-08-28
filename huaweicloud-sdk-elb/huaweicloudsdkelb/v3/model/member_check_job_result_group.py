# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberCheckJobResultGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_result': 'bool',
        'check_items': 'list[MemberCheckJobResultItem]',
        'check_status': 'str'
    }

    attribute_map = {
        'check_result': 'check_result',
        'check_items': 'check_items',
        'check_status': 'check_status'
    }

    def __init__(self, check_result=None, check_items=None, check_status=None):
        r"""MemberCheckJobResultGroup

        The model defined in huaweicloud sdk

        :param check_result: **参数解释**：检查结果，true表示检查通过，false为检查不通过。  **取值范围**：不涉及
        :type check_result: bool
        :param check_items: 
        :type check_items: list[:class:`huaweicloudsdkelb.v3.MemberCheckJobResultItem`]
        :param check_status: **参数解释**：processed检查完成，processing检查中，failed检查失败。  **取值范围**：不涉及
        :type check_status: str
        """
        
        

        self._check_result = None
        self._check_items = None
        self._check_status = None
        self.discriminator = None

        if check_result is not None:
            self.check_result = check_result
        if check_items is not None:
            self.check_items = check_items
        if check_status is not None:
            self.check_status = check_status

    @property
    def check_result(self):
        r"""Gets the check_result of this MemberCheckJobResultGroup.

        **参数解释**：检查结果，true表示检查通过，false为检查不通过。  **取值范围**：不涉及

        :return: The check_result of this MemberCheckJobResultGroup.
        :rtype: bool
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        r"""Sets the check_result of this MemberCheckJobResultGroup.

        **参数解释**：检查结果，true表示检查通过，false为检查不通过。  **取值范围**：不涉及

        :param check_result: The check_result of this MemberCheckJobResultGroup.
        :type check_result: bool
        """
        self._check_result = check_result

    @property
    def check_items(self):
        r"""Gets the check_items of this MemberCheckJobResultGroup.

        :return: The check_items of this MemberCheckJobResultGroup.
        :rtype: list[:class:`huaweicloudsdkelb.v3.MemberCheckJobResultItem`]
        """
        return self._check_items

    @check_items.setter
    def check_items(self, check_items):
        r"""Sets the check_items of this MemberCheckJobResultGroup.

        :param check_items: The check_items of this MemberCheckJobResultGroup.
        :type check_items: list[:class:`huaweicloudsdkelb.v3.MemberCheckJobResultItem`]
        """
        self._check_items = check_items

    @property
    def check_status(self):
        r"""Gets the check_status of this MemberCheckJobResultGroup.

        **参数解释**：processed检查完成，processing检查中，failed检查失败。  **取值范围**：不涉及

        :return: The check_status of this MemberCheckJobResultGroup.
        :rtype: str
        """
        return self._check_status

    @check_status.setter
    def check_status(self, check_status):
        r"""Sets the check_status of this MemberCheckJobResultGroup.

        **参数解释**：processed检查完成，processing检查中，failed检查失败。  **取值范围**：不涉及

        :param check_status: The check_status of this MemberCheckJobResultGroup.
        :type check_status: str
        """
        self._check_status = check_status

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
        if not isinstance(other, MemberCheckJobResultGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
