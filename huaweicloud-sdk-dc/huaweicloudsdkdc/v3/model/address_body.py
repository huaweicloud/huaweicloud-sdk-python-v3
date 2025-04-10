# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'en_us': 'str',
        'zh_cn': 'str'
    }

    attribute_map = {
        'en_us': 'en_us',
        'zh_cn': 'zh_cn'
    }

    def __init__(self, en_us=None, zh_cn=None):
        r"""AddressBody

        The model defined in huaweicloud sdk

        :param en_us: 英文名称。
        :type en_us: str
        :param zh_cn: 中文信息。
        :type zh_cn: str
        """
        
        

        self._en_us = None
        self._zh_cn = None
        self.discriminator = None

        if en_us is not None:
            self.en_us = en_us
        if zh_cn is not None:
            self.zh_cn = zh_cn

    @property
    def en_us(self):
        r"""Gets the en_us of this AddressBody.

        英文名称。

        :return: The en_us of this AddressBody.
        :rtype: str
        """
        return self._en_us

    @en_us.setter
    def en_us(self, en_us):
        r"""Sets the en_us of this AddressBody.

        英文名称。

        :param en_us: The en_us of this AddressBody.
        :type en_us: str
        """
        self._en_us = en_us

    @property
    def zh_cn(self):
        r"""Gets the zh_cn of this AddressBody.

        中文信息。

        :return: The zh_cn of this AddressBody.
        :rtype: str
        """
        return self._zh_cn

    @zh_cn.setter
    def zh_cn(self, zh_cn):
        r"""Sets the zh_cn of this AddressBody.

        中文信息。

        :param zh_cn: The zh_cn of this AddressBody.
        :type zh_cn: str
        """
        self._zh_cn = zh_cn

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
        if not isinstance(other, AddressBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
