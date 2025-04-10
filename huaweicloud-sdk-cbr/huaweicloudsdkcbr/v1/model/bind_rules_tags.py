# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindRulesTags:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        r"""BindRulesTags

        The model defined in huaweicloud sdk

        :param key: key不能包含非打印字符ASCII(0-31)，“&#x3D;”,“*”,“&lt;”,“&gt;”,“\\\\”,“,”,“|”,“/”。 [key只能由中文，字母，数字，“-”，“_”组成。](tag:hws,hws_hk,fcs_vm,ctc)   [key只能由字母，数字，“_”，“-”组成。](tag:dt,ocb,tlf,sbc,g42,hcso_dt)
        :type key: str
        :param value: value不能包含非打印字符ASCII(0-31)，“&#x3D;”,“*”,“&lt;”,“&gt;”,“\\”,“,”,“|”,“/”。  [value只能由中文，字母，数字，“-”，“_”，“.”组成。](tag:hws,hws_hk,fcs_vm,ctc) [value只能由字母，数字，“_”，“-”组成。](tag:dt,ocb,tlf,sbc,g42,hcso_dt)
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        self.key = key
        self.value = value

    @property
    def key(self):
        r"""Gets the key of this BindRulesTags.

        key不能包含非打印字符ASCII(0-31)，“=”,“*”,“<”,“>”,“\\\\”,“,”,“|”,“/”。 [key只能由中文，字母，数字，“-”，“_”组成。](tag:hws,hws_hk,fcs_vm,ctc)   [key只能由字母，数字，“_”，“-”组成。](tag:dt,ocb,tlf,sbc,g42,hcso_dt)

        :return: The key of this BindRulesTags.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this BindRulesTags.

        key不能包含非打印字符ASCII(0-31)，“=”,“*”,“<”,“>”,“\\\\”,“,”,“|”,“/”。 [key只能由中文，字母，数字，“-”，“_”组成。](tag:hws,hws_hk,fcs_vm,ctc)   [key只能由字母，数字，“_”，“-”组成。](tag:dt,ocb,tlf,sbc,g42,hcso_dt)

        :param key: The key of this BindRulesTags.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this BindRulesTags.

        value不能包含非打印字符ASCII(0-31)，“=”,“*”,“<”,“>”,“\\”,“,”,“|”,“/”。  [value只能由中文，字母，数字，“-”，“_”，“.”组成。](tag:hws,hws_hk,fcs_vm,ctc) [value只能由字母，数字，“_”，“-”组成。](tag:dt,ocb,tlf,sbc,g42,hcso_dt)

        :return: The value of this BindRulesTags.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this BindRulesTags.

        value不能包含非打印字符ASCII(0-31)，“=”,“*”,“<”,“>”,“\\”,“,”,“|”,“/”。  [value只能由中文，字母，数字，“-”，“_”，“.”组成。](tag:hws,hws_hk,fcs_vm,ctc) [value只能由字母，数字，“_”，“-”组成。](tag:dt,ocb,tlf,sbc,g42,hcso_dt)

        :param value: The value of this BindRulesTags.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, BindRulesTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
