# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrimaryRegionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'primary_region': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'primary_region': 'primary_region'
    }

    def __init__(self, key_id=None, primary_region=None):
        r"""UpdatePrimaryRegionRequestBody

        The model defined in huaweicloud sdk

        :param key_id: 待复制的密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。
        :type key_id: str
        :param primary_region: 指定密钥所属新的主区域的区域编码。如cn-north-4。
        :type primary_region: str
        """
        
        

        self._key_id = None
        self._primary_region = None
        self.discriminator = None

        self.key_id = key_id
        self.primary_region = primary_region

    @property
    def key_id(self):
        r"""Gets the key_id of this UpdatePrimaryRegionRequestBody.

        待复制的密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :return: The key_id of this UpdatePrimaryRegionRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this UpdatePrimaryRegionRequestBody.

        待复制的密钥ID，36字节，满足正则匹配“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”。 例如：0d0466b0-e727-4d9c-b35d-f84bb474a37f。

        :param key_id: The key_id of this UpdatePrimaryRegionRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def primary_region(self):
        r"""Gets the primary_region of this UpdatePrimaryRegionRequestBody.

        指定密钥所属新的主区域的区域编码。如cn-north-4。

        :return: The primary_region of this UpdatePrimaryRegionRequestBody.
        :rtype: str
        """
        return self._primary_region

    @primary_region.setter
    def primary_region(self, primary_region):
        r"""Sets the primary_region of this UpdatePrimaryRegionRequestBody.

        指定密钥所属新的主区域的区域编码。如cn-north-4。

        :param primary_region: The primary_region of this UpdatePrimaryRegionRequestBody.
        :type primary_region: str
        """
        self._primary_region = primary_region

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
        if not isinstance(other, UpdatePrimaryRegionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
