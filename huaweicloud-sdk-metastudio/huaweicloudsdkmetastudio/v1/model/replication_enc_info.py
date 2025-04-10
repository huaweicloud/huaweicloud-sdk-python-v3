# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplicationEncInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm': 'str',
        'key_id': 'str',
        'iv': 'str'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'key_id': 'key_id',
        'iv': 'iv'
    }

    def __init__(self, algorithm=None, key_id=None, iv=None):
        r"""ReplicationEncInfo

        The model defined in huaweicloud sdk

        :param algorithm: 加密算法
        :type algorithm: str
        :param key_id: 秘钥id
        :type key_id: str
        :param iv: 初始化向量
        :type iv: str
        """
        
        

        self._algorithm = None
        self._key_id = None
        self._iv = None
        self.discriminator = None

        if algorithm is not None:
            self.algorithm = algorithm
        if key_id is not None:
            self.key_id = key_id
        if iv is not None:
            self.iv = iv

    @property
    def algorithm(self):
        r"""Gets the algorithm of this ReplicationEncInfo.

        加密算法

        :return: The algorithm of this ReplicationEncInfo.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this ReplicationEncInfo.

        加密算法

        :param algorithm: The algorithm of this ReplicationEncInfo.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def key_id(self):
        r"""Gets the key_id of this ReplicationEncInfo.

        秘钥id

        :return: The key_id of this ReplicationEncInfo.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this ReplicationEncInfo.

        秘钥id

        :param key_id: The key_id of this ReplicationEncInfo.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def iv(self):
        r"""Gets the iv of this ReplicationEncInfo.

        初始化向量

        :return: The iv of this ReplicationEncInfo.
        :rtype: str
        """
        return self._iv

    @iv.setter
    def iv(self, iv):
        r"""Sets the iv of this ReplicationEncInfo.

        初始化向量

        :param iv: The iv of this ReplicationEncInfo.
        :type iv: str
        """
        self._iv = iv

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
        if not isinstance(other, ReplicationEncInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
