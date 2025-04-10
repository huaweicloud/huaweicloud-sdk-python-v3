# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomPlatformAuthConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str'
    }

    attribute_map = {
        'key': 'key'
    }

    def __init__(self, key=None):
        r"""UpdateCustomPlatformAuthConfig

        The model defined in huaweicloud sdk

        :param key: 密钥Key。调用自定义直播平台时使用。 使用方式： 调用接口时，增加两个头域：x-hw-mss-time，x-hw-mss-secret * x-hw-mss-time：当前时间戳。Unix时间戳的十六进制结果。1分钟内有效。   示例： 66df9308（即2024.09.10 08:30:00） * x-hw-mss-secret：鉴权串。hmac_sha256(Key, URI（product_query_url,query参数按照Key的字典序排列）+ x-hw-mss-time)  示例： URL  https://api.example.com/v1/products?live_id&#x3D;111&amp;limit&#x3D;10&amp;offset&#x3D;0   Key：GCTbw44s6MPLh4GqgDpnfuFHgy25Enly   hwTime：66df9308   x-hw-mss-secret&#x3D;hmac_sha256(GCTbw44s6MPLh4GqgDpnfuFHgy25Enly,api.example.com/v1/products?limit&#x3D;10&amp;live_id&#x3D;111&amp;offset&#x3D;066df9308)&#x3D;5e7fe8869a12a87ea966d9edbc02e38cd4ce62c73b8b05c638f15835e78902d7   x-hw-mss-secret: 5e7fe8869a12a87ea966d9edbc02e38cd4ce62c73b8b05c638f15835e78902d7
        :type key: str
        """
        
        

        self._key = None
        self.discriminator = None

        if key is not None:
            self.key = key

    @property
    def key(self):
        r"""Gets the key of this UpdateCustomPlatformAuthConfig.

        密钥Key。调用自定义直播平台时使用。 使用方式： 调用接口时，增加两个头域：x-hw-mss-time，x-hw-mss-secret * x-hw-mss-time：当前时间戳。Unix时间戳的十六进制结果。1分钟内有效。   示例： 66df9308（即2024.09.10 08:30:00） * x-hw-mss-secret：鉴权串。hmac_sha256(Key, URI（product_query_url,query参数按照Key的字典序排列）+ x-hw-mss-time)  示例： URL  https://api.example.com/v1/products?live_id=111&limit=10&offset=0   Key：GCTbw44s6MPLh4GqgDpnfuFHgy25Enly   hwTime：66df9308   x-hw-mss-secret=hmac_sha256(GCTbw44s6MPLh4GqgDpnfuFHgy25Enly,api.example.com/v1/products?limit=10&live_id=111&offset=066df9308)=5e7fe8869a12a87ea966d9edbc02e38cd4ce62c73b8b05c638f15835e78902d7   x-hw-mss-secret: 5e7fe8869a12a87ea966d9edbc02e38cd4ce62c73b8b05c638f15835e78902d7

        :return: The key of this UpdateCustomPlatformAuthConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this UpdateCustomPlatformAuthConfig.

        密钥Key。调用自定义直播平台时使用。 使用方式： 调用接口时，增加两个头域：x-hw-mss-time，x-hw-mss-secret * x-hw-mss-time：当前时间戳。Unix时间戳的十六进制结果。1分钟内有效。   示例： 66df9308（即2024.09.10 08:30:00） * x-hw-mss-secret：鉴权串。hmac_sha256(Key, URI（product_query_url,query参数按照Key的字典序排列）+ x-hw-mss-time)  示例： URL  https://api.example.com/v1/products?live_id=111&limit=10&offset=0   Key：GCTbw44s6MPLh4GqgDpnfuFHgy25Enly   hwTime：66df9308   x-hw-mss-secret=hmac_sha256(GCTbw44s6MPLh4GqgDpnfuFHgy25Enly,api.example.com/v1/products?limit=10&live_id=111&offset=066df9308)=5e7fe8869a12a87ea966d9edbc02e38cd4ce62c73b8b05c638f15835e78902d7   x-hw-mss-secret: 5e7fe8869a12a87ea966d9edbc02e38cd4ce62c73b8b05c638f15835e78902d7

        :param key: The key of this UpdateCustomPlatformAuthConfig.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, UpdateCustomPlatformAuthConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
