# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificatesV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'common_name': 'str',
        'signature_algorithm': 'str',
        'type': 'str',
        'instance_id': 'str',
        'algorithm_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'common_name': 'common_name',
        'signature_algorithm': 'signature_algorithm',
        'type': 'type',
        'instance_id': 'instance_id',
        'algorithm_type': 'algorithm_type'
    }

    def __init__(self, offset=None, limit=None, name=None, common_name=None, signature_algorithm=None, type=None, instance_id=None, algorithm_type=None):
        r"""ListCertificatesV2Request

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param name: 证书名称
        :type name: str
        :param common_name: 证书域名
        :type common_name: str
        :param signature_algorithm: 证书签名算法
        :type signature_algorithm: str
        :param type: 证书可见范围
        :type type: str
        :param instance_id: 证书所属实例ID
        :type instance_id: str
        :param algorithm_type: 证书算法类型： - RSA - ECC - SM2  [暂不支持](tag:hws;hws_hk;g42;Site)
        :type algorithm_type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self._common_name = None
        self._signature_algorithm = None
        self._type = None
        self._instance_id = None
        self._algorithm_type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if common_name is not None:
            self.common_name = common_name
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if type is not None:
            self.type = type
        self.instance_id = instance_id
        if algorithm_type is not None:
            self.algorithm_type = algorithm_type

    @property
    def offset(self):
        r"""Gets the offset of this ListCertificatesV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListCertificatesV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCertificatesV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListCertificatesV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCertificatesV2Request.

        每页显示的条目数量

        :return: The limit of this ListCertificatesV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCertificatesV2Request.

        每页显示的条目数量

        :param limit: The limit of this ListCertificatesV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListCertificatesV2Request.

        证书名称

        :return: The name of this ListCertificatesV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCertificatesV2Request.

        证书名称

        :param name: The name of this ListCertificatesV2Request.
        :type name: str
        """
        self._name = name

    @property
    def common_name(self):
        r"""Gets the common_name of this ListCertificatesV2Request.

        证书域名

        :return: The common_name of this ListCertificatesV2Request.
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        r"""Sets the common_name of this ListCertificatesV2Request.

        证书域名

        :param common_name: The common_name of this ListCertificatesV2Request.
        :type common_name: str
        """
        self._common_name = common_name

    @property
    def signature_algorithm(self):
        r"""Gets the signature_algorithm of this ListCertificatesV2Request.

        证书签名算法

        :return: The signature_algorithm of this ListCertificatesV2Request.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        r"""Sets the signature_algorithm of this ListCertificatesV2Request.

        证书签名算法

        :param signature_algorithm: The signature_algorithm of this ListCertificatesV2Request.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def type(self):
        r"""Gets the type of this ListCertificatesV2Request.

        证书可见范围

        :return: The type of this ListCertificatesV2Request.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListCertificatesV2Request.

        证书可见范围

        :param type: The type of this ListCertificatesV2Request.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListCertificatesV2Request.

        证书所属实例ID

        :return: The instance_id of this ListCertificatesV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListCertificatesV2Request.

        证书所属实例ID

        :param instance_id: The instance_id of this ListCertificatesV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def algorithm_type(self):
        r"""Gets the algorithm_type of this ListCertificatesV2Request.

        证书算法类型： - RSA - ECC - SM2  [暂不支持](tag:hws;hws_hk;g42;Site)

        :return: The algorithm_type of this ListCertificatesV2Request.
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        r"""Sets the algorithm_type of this ListCertificatesV2Request.

        证书算法类型： - RSA - ECC - SM2  [暂不支持](tag:hws;hws_hk;g42;Site)

        :param algorithm_type: The algorithm_type of this ListCertificatesV2Request.
        :type algorithm_type: str
        """
        self._algorithm_type = algorithm_type

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
        if not isinstance(other, ListCertificatesV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
