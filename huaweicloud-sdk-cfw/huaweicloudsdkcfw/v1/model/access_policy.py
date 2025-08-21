# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'changed': 'int',
        'eip': 'int',
        'nat': 'int',
        'total': 'int'
    }

    attribute_map = {
        'changed': 'changed',
        'eip': 'eip',
        'nat': 'nat',
        'total': 'total'
    }

    def __init__(self, changed=None, eip=None, nat=None, total=None):
        r"""AccessPolicy

        The model defined in huaweicloud sdk

        :param changed: **参数解释**： 变化数量 **取值范围**： 不涉及
        :type changed: int
        :param eip: **参数解释**： EIP访问控制策略 **取值范围**： 不涉及
        :type eip: int
        :param nat: **参数解释**： NAT访问控制策略 **取值范围**： 不涉及
        :type nat: int
        :param total: **参数解释**： 总数 **取值范围**： 不涉及
        :type total: int
        """
        
        

        self._changed = None
        self._eip = None
        self._nat = None
        self._total = None
        self.discriminator = None

        if changed is not None:
            self.changed = changed
        if eip is not None:
            self.eip = eip
        if nat is not None:
            self.nat = nat
        if total is not None:
            self.total = total

    @property
    def changed(self):
        r"""Gets the changed of this AccessPolicy.

        **参数解释**： 变化数量 **取值范围**： 不涉及

        :return: The changed of this AccessPolicy.
        :rtype: int
        """
        return self._changed

    @changed.setter
    def changed(self, changed):
        r"""Sets the changed of this AccessPolicy.

        **参数解释**： 变化数量 **取值范围**： 不涉及

        :param changed: The changed of this AccessPolicy.
        :type changed: int
        """
        self._changed = changed

    @property
    def eip(self):
        r"""Gets the eip of this AccessPolicy.

        **参数解释**： EIP访问控制策略 **取值范围**： 不涉及

        :return: The eip of this AccessPolicy.
        :rtype: int
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this AccessPolicy.

        **参数解释**： EIP访问控制策略 **取值范围**： 不涉及

        :param eip: The eip of this AccessPolicy.
        :type eip: int
        """
        self._eip = eip

    @property
    def nat(self):
        r"""Gets the nat of this AccessPolicy.

        **参数解释**： NAT访问控制策略 **取值范围**： 不涉及

        :return: The nat of this AccessPolicy.
        :rtype: int
        """
        return self._nat

    @nat.setter
    def nat(self, nat):
        r"""Sets the nat of this AccessPolicy.

        **参数解释**： NAT访问控制策略 **取值范围**： 不涉及

        :param nat: The nat of this AccessPolicy.
        :type nat: int
        """
        self._nat = nat

    @property
    def total(self):
        r"""Gets the total of this AccessPolicy.

        **参数解释**： 总数 **取值范围**： 不涉及

        :return: The total of this AccessPolicy.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this AccessPolicy.

        **参数解释**： 总数 **取值范围**： 不涉及

        :param total: The total of this AccessPolicy.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, AccessPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
