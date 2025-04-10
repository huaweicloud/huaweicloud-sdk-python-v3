# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CacheConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ignore_url_parameter': 'bool',
        'follow_origin': 'bool',
        'compress': 'CompressRequest',
        'rules': 'list[Rules]'
    }

    attribute_map = {
        'ignore_url_parameter': 'ignore_url_parameter',
        'follow_origin': 'follow_origin',
        'compress': 'compress',
        'rules': 'rules'
    }

    def __init__(self, ignore_url_parameter=None, follow_origin=None, compress=None, rules=None):
        r"""CacheConfigRequest

        The model defined in huaweicloud sdk

        :param ignore_url_parameter: 是否忽略url中的参数。
        :type ignore_url_parameter: bool
        :param follow_origin: 缓存规则是否遵循源站。
        :type follow_origin: bool
        :param compress: 
        :type compress: :class:`huaweicloudsdkcdn.v1.CompressRequest`
        :param rules: 缓存规则，将覆盖之前的规则配置。规则为空重置为默认规则。
        :type rules: list[:class:`huaweicloudsdkcdn.v1.Rules`]
        """
        
        

        self._ignore_url_parameter = None
        self._follow_origin = None
        self._compress = None
        self._rules = None
        self.discriminator = None

        if ignore_url_parameter is not None:
            self.ignore_url_parameter = ignore_url_parameter
        if follow_origin is not None:
            self.follow_origin = follow_origin
        if compress is not None:
            self.compress = compress
        if rules is not None:
            self.rules = rules

    @property
    def ignore_url_parameter(self):
        r"""Gets the ignore_url_parameter of this CacheConfigRequest.

        是否忽略url中的参数。

        :return: The ignore_url_parameter of this CacheConfigRequest.
        :rtype: bool
        """
        return self._ignore_url_parameter

    @ignore_url_parameter.setter
    def ignore_url_parameter(self, ignore_url_parameter):
        r"""Sets the ignore_url_parameter of this CacheConfigRequest.

        是否忽略url中的参数。

        :param ignore_url_parameter: The ignore_url_parameter of this CacheConfigRequest.
        :type ignore_url_parameter: bool
        """
        self._ignore_url_parameter = ignore_url_parameter

    @property
    def follow_origin(self):
        r"""Gets the follow_origin of this CacheConfigRequest.

        缓存规则是否遵循源站。

        :return: The follow_origin of this CacheConfigRequest.
        :rtype: bool
        """
        return self._follow_origin

    @follow_origin.setter
    def follow_origin(self, follow_origin):
        r"""Sets the follow_origin of this CacheConfigRequest.

        缓存规则是否遵循源站。

        :param follow_origin: The follow_origin of this CacheConfigRequest.
        :type follow_origin: bool
        """
        self._follow_origin = follow_origin

    @property
    def compress(self):
        r"""Gets the compress of this CacheConfigRequest.

        :return: The compress of this CacheConfigRequest.
        :rtype: :class:`huaweicloudsdkcdn.v1.CompressRequest`
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        r"""Sets the compress of this CacheConfigRequest.

        :param compress: The compress of this CacheConfigRequest.
        :type compress: :class:`huaweicloudsdkcdn.v1.CompressRequest`
        """
        self._compress = compress

    @property
    def rules(self):
        r"""Gets the rules of this CacheConfigRequest.

        缓存规则，将覆盖之前的规则配置。规则为空重置为默认规则。

        :return: The rules of this CacheConfigRequest.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.Rules`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this CacheConfigRequest.

        缓存规则，将覆盖之前的规则配置。规则为空重置为默认规则。

        :param rules: The rules of this CacheConfigRequest.
        :type rules: list[:class:`huaweicloudsdkcdn.v1.Rules`]
        """
        self._rules = rules

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
        if not isinstance(other, CacheConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
