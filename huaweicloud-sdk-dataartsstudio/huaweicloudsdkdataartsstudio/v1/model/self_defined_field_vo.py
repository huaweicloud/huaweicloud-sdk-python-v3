# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SelfDefinedFieldVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fd_name_ch': 'str',
        'fd_name_en': 'str',
        'not_null': 'bool',
        'fd_value': 'str'
    }

    attribute_map = {
        'fd_name_ch': 'fd_name_ch',
        'fd_name_en': 'fd_name_en',
        'not_null': 'not_null',
        'fd_value': 'fd_value'
    }

    def __init__(self, fd_name_ch=None, fd_name_en=None, not_null=None, fd_value=None):
        r"""SelfDefinedFieldVO

        The model defined in huaweicloud sdk

        :param fd_name_ch: 自定义项中文名。
        :type fd_name_ch: str
        :param fd_name_en: 自定义项英文名。
        :type fd_name_en: str
        :param not_null: 是否必填。
        :type not_null: bool
        :param fd_value: 属性值。
        :type fd_value: str
        """
        
        

        self._fd_name_ch = None
        self._fd_name_en = None
        self._not_null = None
        self._fd_value = None
        self.discriminator = None

        if fd_name_ch is not None:
            self.fd_name_ch = fd_name_ch
        if fd_name_en is not None:
            self.fd_name_en = fd_name_en
        if not_null is not None:
            self.not_null = not_null
        if fd_value is not None:
            self.fd_value = fd_value

    @property
    def fd_name_ch(self):
        r"""Gets the fd_name_ch of this SelfDefinedFieldVO.

        自定义项中文名。

        :return: The fd_name_ch of this SelfDefinedFieldVO.
        :rtype: str
        """
        return self._fd_name_ch

    @fd_name_ch.setter
    def fd_name_ch(self, fd_name_ch):
        r"""Sets the fd_name_ch of this SelfDefinedFieldVO.

        自定义项中文名。

        :param fd_name_ch: The fd_name_ch of this SelfDefinedFieldVO.
        :type fd_name_ch: str
        """
        self._fd_name_ch = fd_name_ch

    @property
    def fd_name_en(self):
        r"""Gets the fd_name_en of this SelfDefinedFieldVO.

        自定义项英文名。

        :return: The fd_name_en of this SelfDefinedFieldVO.
        :rtype: str
        """
        return self._fd_name_en

    @fd_name_en.setter
    def fd_name_en(self, fd_name_en):
        r"""Sets the fd_name_en of this SelfDefinedFieldVO.

        自定义项英文名。

        :param fd_name_en: The fd_name_en of this SelfDefinedFieldVO.
        :type fd_name_en: str
        """
        self._fd_name_en = fd_name_en

    @property
    def not_null(self):
        r"""Gets the not_null of this SelfDefinedFieldVO.

        是否必填。

        :return: The not_null of this SelfDefinedFieldVO.
        :rtype: bool
        """
        return self._not_null

    @not_null.setter
    def not_null(self, not_null):
        r"""Sets the not_null of this SelfDefinedFieldVO.

        是否必填。

        :param not_null: The not_null of this SelfDefinedFieldVO.
        :type not_null: bool
        """
        self._not_null = not_null

    @property
    def fd_value(self):
        r"""Gets the fd_value of this SelfDefinedFieldVO.

        属性值。

        :return: The fd_value of this SelfDefinedFieldVO.
        :rtype: str
        """
        return self._fd_value

    @fd_value.setter
    def fd_value(self, fd_value):
        r"""Sets the fd_value of this SelfDefinedFieldVO.

        属性值。

        :param fd_value: The fd_value of this SelfDefinedFieldVO.
        :type fd_value: str
        """
        self._fd_value = fd_value

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
        if not isinstance(other, SelfDefinedFieldVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
