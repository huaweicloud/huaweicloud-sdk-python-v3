# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrustProcessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'hash': 'str'
    }

    attribute_map = {
        'path': 'path',
        'hash': 'hash'
    }

    def __init__(self, path=None, hash=None):
        r"""TrustProcessInfo

        The model defined in huaweicloud sdk

        :param path: **参数解释**: 进程路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及
        :type path: str
        :param hash: **参数解释**: 进程hash **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及
        :type hash: str
        """
        
        

        self._path = None
        self._hash = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if hash is not None:
            self.hash = hash

    @property
    def path(self):
        r"""Gets the path of this TrustProcessInfo.

        **参数解释**: 进程路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及

        :return: The path of this TrustProcessInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this TrustProcessInfo.

        **参数解释**: 进程路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及

        :param path: The path of this TrustProcessInfo.
        :type path: str
        """
        self._path = path

    @property
    def hash(self):
        r"""Gets the hash of this TrustProcessInfo.

        **参数解释**: 进程hash **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及

        :return: The hash of this TrustProcessInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this TrustProcessInfo.

        **参数解释**: 进程hash **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及

        :param hash: The hash of this TrustProcessInfo.
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
        if not isinstance(other, TrustProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
