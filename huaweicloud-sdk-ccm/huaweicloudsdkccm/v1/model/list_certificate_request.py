# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificateRequest:

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
        'name': 'str',
        'offset': 'int',
        'status': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'status': 'status',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, limit=None, name=None, offset=None, status=None, sort_key=None, sort_dir=None):
        r"""ListCertificateRequest

        The model defined in huaweicloud sdk

        :param limit: 指定查询返回记录条数，默认值10。
        :type limit: int
        :param name: 私有证书名称，返回名称带有name字段的证书集合。
        :type name: str
        :param offset: 索引位置，从offset指定的下一条数据开始查询。
        :type offset: int
        :param status: 私有证书状态，通过状态过滤证书集合。   - **ISSUED** : 已签发；   - **REVOKED** : 已吊销；   - **EXPIRED** : 已过期。
        :type status: str
        :param sort_key: 排序属性，目前支持以下属性： - **create_time** : 证书创建时间（默认） - **common_name** : 证书名称 - **issuer_name** : 签发CA名称 - **not_after** : 证书到期时间
        :type sort_key: str
        :param sort_dir: 排序方向，支持以下值：   - **DESC** : 降序（默认）   - **ASC** : 升序
        :type sort_dir: str
        """
        
        

        self._limit = None
        self._name = None
        self._offset = None
        self._status = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListCertificateRequest.

        指定查询返回记录条数，默认值10。

        :return: The limit of this ListCertificateRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCertificateRequest.

        指定查询返回记录条数，默认值10。

        :param limit: The limit of this ListCertificateRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListCertificateRequest.

        私有证书名称，返回名称带有name字段的证书集合。

        :return: The name of this ListCertificateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCertificateRequest.

        私有证书名称，返回名称带有name字段的证书集合。

        :param name: The name of this ListCertificateRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListCertificateRequest.

        索引位置，从offset指定的下一条数据开始查询。

        :return: The offset of this ListCertificateRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCertificateRequest.

        索引位置，从offset指定的下一条数据开始查询。

        :param offset: The offset of this ListCertificateRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListCertificateRequest.

        私有证书状态，通过状态过滤证书集合。   - **ISSUED** : 已签发；   - **REVOKED** : 已吊销；   - **EXPIRED** : 已过期。

        :return: The status of this ListCertificateRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListCertificateRequest.

        私有证书状态，通过状态过滤证书集合。   - **ISSUED** : 已签发；   - **REVOKED** : 已吊销；   - **EXPIRED** : 已过期。

        :param status: The status of this ListCertificateRequest.
        :type status: str
        """
        self._status = status

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListCertificateRequest.

        排序属性，目前支持以下属性： - **create_time** : 证书创建时间（默认） - **common_name** : 证书名称 - **issuer_name** : 签发CA名称 - **not_after** : 证书到期时间

        :return: The sort_key of this ListCertificateRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListCertificateRequest.

        排序属性，目前支持以下属性： - **create_time** : 证书创建时间（默认） - **common_name** : 证书名称 - **issuer_name** : 签发CA名称 - **not_after** : 证书到期时间

        :param sort_key: The sort_key of this ListCertificateRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListCertificateRequest.

        排序方向，支持以下值：   - **DESC** : 降序（默认）   - **ASC** : 升序

        :return: The sort_dir of this ListCertificateRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListCertificateRequest.

        排序方向，支持以下值：   - **DESC** : 降序（默认）   - **ASC** : 升序

        :param sort_dir: The sort_dir of this ListCertificateRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
