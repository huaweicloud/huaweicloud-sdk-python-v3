# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResultDetailResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyword': 'str',
        'hash': 'str'
    }

    attribute_map = {
        'keyword': 'keyword',
        'hash': 'hash'
    }

    def __init__(self, keyword=None, hash=None):
        r"""ResultDetailResponseInfo

        The model defined in huaweicloud sdk

        :param keyword: 告警事件关键字，仅用于告警白名单
        :type keyword: str
        :param hash: 告警事件hash，仅用于告警白名单
        :type hash: str
        """
        
        

        self._keyword = None
        self._hash = None
        self.discriminator = None

        if keyword is not None:
            self.keyword = keyword
        if hash is not None:
            self.hash = hash

    @property
    def keyword(self):
        r"""Gets the keyword of this ResultDetailResponseInfo.

        告警事件关键字，仅用于告警白名单

        :return: The keyword of this ResultDetailResponseInfo.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ResultDetailResponseInfo.

        告警事件关键字，仅用于告警白名单

        :param keyword: The keyword of this ResultDetailResponseInfo.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def hash(self):
        r"""Gets the hash of this ResultDetailResponseInfo.

        告警事件hash，仅用于告警白名单

        :return: The hash of this ResultDetailResponseInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this ResultDetailResponseInfo.

        告警事件hash，仅用于告警白名单

        :param hash: The hash of this ResultDetailResponseInfo.
        :type hash: str
        """
        self._hash = hash

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
        if not isinstance(other, ResultDetailResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
