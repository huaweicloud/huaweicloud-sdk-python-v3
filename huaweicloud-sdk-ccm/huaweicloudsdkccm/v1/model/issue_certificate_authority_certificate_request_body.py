# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueCertificateAuthorityCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'issuer_id': 'str',
        'path_length': 'int',
        'signature_algorithm': 'str',
        'validity': 'Validity',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'issuer_id': 'issuer_id',
        'path_length': 'path_length',
        'signature_algorithm': 'signature_algorithm',
        'validity': 'validity',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, issuer_id=None, path_length=None, signature_algorithm=None, validity=None, enterprise_project_id=None):
        """IssueCertificateAuthorityCertificateRequestBody

        The model defined in huaweicloud sdk

        :param issuer_id: 父CA证书ID。
        :type issuer_id: str
        :param path_length: 路径长度。
        :type path_length: int
        :param signature_algorithm: 签名哈希算法，可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**   - **SM3**（中国站）
        :type signature_algorithm: str
        :param validity: 
        :type validity: :class:`huaweicloudsdkccm.v1.Validity`
        :param enterprise_project_id: 企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.   取值为“all”   取值为“0”   满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”
        :type enterprise_project_id: str
        """
        
        

        self._issuer_id = None
        self._path_length = None
        self._signature_algorithm = None
        self._validity = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.issuer_id = issuer_id
        self.path_length = path_length
        self.signature_algorithm = signature_algorithm
        self.validity = validity
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def issuer_id(self):
        """Gets the issuer_id of this IssueCertificateAuthorityCertificateRequestBody.

        父CA证书ID。

        :return: The issuer_id of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this IssueCertificateAuthorityCertificateRequestBody.

        父CA证书ID。

        :param issuer_id: The issuer_id of this IssueCertificateAuthorityCertificateRequestBody.
        :type issuer_id: str
        """
        self._issuer_id = issuer_id

    @property
    def path_length(self):
        """Gets the path_length of this IssueCertificateAuthorityCertificateRequestBody.

        路径长度。

        :return: The path_length of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: int
        """
        return self._path_length

    @path_length.setter
    def path_length(self, path_length):
        """Sets the path_length of this IssueCertificateAuthorityCertificateRequestBody.

        路径长度。

        :param path_length: The path_length of this IssueCertificateAuthorityCertificateRequestBody.
        :type path_length: int
        """
        self._path_length = path_length

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this IssueCertificateAuthorityCertificateRequestBody.

        签名哈希算法，可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**   - **SM3**（中国站）

        :return: The signature_algorithm of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this IssueCertificateAuthorityCertificateRequestBody.

        签名哈希算法，可选值如下：   - **SHA256**   - **SHA384**   - **SHA512**   - **SM3**（中国站）

        :param signature_algorithm: The signature_algorithm of this IssueCertificateAuthorityCertificateRequestBody.
        :type signature_algorithm: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def validity(self):
        """Gets the validity of this IssueCertificateAuthorityCertificateRequestBody.

        :return: The validity of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.Validity`
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this IssueCertificateAuthorityCertificateRequestBody.

        :param validity: The validity of this IssueCertificateAuthorityCertificateRequestBody.
        :type validity: :class:`huaweicloudsdkccm.v1.Validity`
        """
        self._validity = validity

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this IssueCertificateAuthorityCertificateRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.   取值为“all”   取值为“0”   满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :return: The enterprise_project_id of this IssueCertificateAuthorityCertificateRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this IssueCertificateAuthorityCertificateRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.   取值为“all”   取值为“0”   满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :param enterprise_project_id: The enterprise_project_id of this IssueCertificateAuthorityCertificateRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, IssueCertificateAuthorityCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
