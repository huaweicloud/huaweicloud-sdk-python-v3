# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmsCountryResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'country_id': 'int',
        'country_name_en': 'str',
        'country_name_zh': 'str'
    }

    attribute_map = {
        'country_id': 'country_id',
        'country_name_en': 'country_name_en',
        'country_name_zh': 'country_name_zh'
    }

    def __init__(self, country_id=None, country_name_en=None, country_name_zh=None):
        r"""SmsCountryResp

        The model defined in huaweicloud sdk

        :param country_id: 国家id
        :type country_id: int
        :param country_name_en: 国家(英文)
        :type country_name_en: str
        :param country_name_zh: 国家(中文)
        :type country_name_zh: str
        """
        
        

        self._country_id = None
        self._country_name_en = None
        self._country_name_zh = None
        self.discriminator = None

        if country_id is not None:
            self.country_id = country_id
        if country_name_en is not None:
            self.country_name_en = country_name_en
        if country_name_zh is not None:
            self.country_name_zh = country_name_zh

    @property
    def country_id(self):
        r"""Gets the country_id of this SmsCountryResp.

        国家id

        :return: The country_id of this SmsCountryResp.
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        r"""Sets the country_id of this SmsCountryResp.

        国家id

        :param country_id: The country_id of this SmsCountryResp.
        :type country_id: int
        """
        self._country_id = country_id

    @property
    def country_name_en(self):
        r"""Gets the country_name_en of this SmsCountryResp.

        国家(英文)

        :return: The country_name_en of this SmsCountryResp.
        :rtype: str
        """
        return self._country_name_en

    @country_name_en.setter
    def country_name_en(self, country_name_en):
        r"""Sets the country_name_en of this SmsCountryResp.

        国家(英文)

        :param country_name_en: The country_name_en of this SmsCountryResp.
        :type country_name_en: str
        """
        self._country_name_en = country_name_en

    @property
    def country_name_zh(self):
        r"""Gets the country_name_zh of this SmsCountryResp.

        国家(中文)

        :return: The country_name_zh of this SmsCountryResp.
        :rtype: str
        """
        return self._country_name_zh

    @country_name_zh.setter
    def country_name_zh(self, country_name_zh):
        r"""Sets the country_name_zh of this SmsCountryResp.

        国家(中文)

        :param country_name_zh: The country_name_zh of this SmsCountryResp.
        :type country_name_zh: str
        """
        self._country_name_zh = country_name_zh

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
        if not isinstance(other, SmsCountryResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
