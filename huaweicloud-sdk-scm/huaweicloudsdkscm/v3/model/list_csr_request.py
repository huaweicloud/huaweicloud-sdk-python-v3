# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCsrRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'name': 'str',
        'private_key_algo': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'private_key_algo': 'private_key_algo'
    }

    def __init__(self, limit=None, offset=None, name=None, private_key_algo=None):
        r"""ListCsrRequest

        The model defined in huaweicloud sdk

        :param limit: 每页条目数量，取值如下： - 10：每页显示10条证书信息。 - 20：每页显示20条证书信息。 - 50：每页显示50条证书信息。
        :type limit: int
        :param offset: 偏移量。
        :type offset: int
        :param name: csr名称。
        :type name: str
        :param private_key_algo: 密钥算法的类型。取值如下： - RSA_2048 - RSA_3072 - RSA_4096 - EC_P256 - EC_P384 - SM2
        :type private_key_algo: str
        """
        
        

        self._limit = None
        self._offset = None
        self._name = None
        self._private_key_algo = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if private_key_algo is not None:
            self.private_key_algo = private_key_algo

    @property
    def limit(self):
        r"""Gets the limit of this ListCsrRequest.

        每页条目数量，取值如下： - 10：每页显示10条证书信息。 - 20：每页显示20条证书信息。 - 50：每页显示50条证书信息。

        :return: The limit of this ListCsrRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCsrRequest.

        每页条目数量，取值如下： - 10：每页显示10条证书信息。 - 20：每页显示20条证书信息。 - 50：每页显示50条证书信息。

        :param limit: The limit of this ListCsrRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCsrRequest.

        偏移量。

        :return: The offset of this ListCsrRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCsrRequest.

        偏移量。

        :param offset: The offset of this ListCsrRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListCsrRequest.

        csr名称。

        :return: The name of this ListCsrRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCsrRequest.

        csr名称。

        :param name: The name of this ListCsrRequest.
        :type name: str
        """
        self._name = name

    @property
    def private_key_algo(self):
        r"""Gets the private_key_algo of this ListCsrRequest.

        密钥算法的类型。取值如下： - RSA_2048 - RSA_3072 - RSA_4096 - EC_P256 - EC_P384 - SM2

        :return: The private_key_algo of this ListCsrRequest.
        :rtype: str
        """
        return self._private_key_algo

    @private_key_algo.setter
    def private_key_algo(self, private_key_algo):
        r"""Sets the private_key_algo of this ListCsrRequest.

        密钥算法的类型。取值如下： - RSA_2048 - RSA_3072 - RSA_4096 - EC_P256 - EC_P384 - SM2

        :param private_key_algo: The private_key_algo of this ListCsrRequest.
        :type private_key_algo: str
        """
        self._private_key_algo = private_key_algo

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
        if not isinstance(other, ListCsrRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
