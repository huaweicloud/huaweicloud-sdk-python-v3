# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductExtendResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'value': 'str'
    }

    attribute_map = {
        'code': 'code',
        'value': 'value'
    }

    def __init__(self, code=None, value=None):
        r"""ProductExtendResp

        The model defined in huaweicloud sdk

        :param code: **参数解释**： 集群维度规格扩展信息编号。 **取值范围**： 不涉及。
        :type code: str
        :param value: **参数解释**： 集群维度规格扩展信息值。 **取值范围**： 不涉及。
        :type value: str
        """
        
        

        self._code = None
        self._value = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if value is not None:
            self.value = value

    @property
    def code(self):
        r"""Gets the code of this ProductExtendResp.

        **参数解释**： 集群维度规格扩展信息编号。 **取值范围**： 不涉及。

        :return: The code of this ProductExtendResp.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ProductExtendResp.

        **参数解释**： 集群维度规格扩展信息编号。 **取值范围**： 不涉及。

        :param code: The code of this ProductExtendResp.
        :type code: str
        """
        self._code = code

    @property
    def value(self):
        r"""Gets the value of this ProductExtendResp.

        **参数解释**： 集群维度规格扩展信息值。 **取值范围**： 不涉及。

        :return: The value of this ProductExtendResp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ProductExtendResp.

        **参数解释**： 集群维度规格扩展信息值。 **取值范围**： 不涉及。

        :param value: The value of this ProductExtendResp.
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
        if not isinstance(other, ProductExtendResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
