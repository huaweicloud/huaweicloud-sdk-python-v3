# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCertificateByCsrRequestBody:

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
        'csr': 'str',
        'validity': 'Validity',
        'type': 'str',
        'path_length': 'int',
        'subject_alternative_names': 'list[SubjectAlternativeName]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'issuer_id': 'issuer_id',
        'csr': 'csr',
        'validity': 'validity',
        'type': 'type',
        'path_length': 'path_length',
        'subject_alternative_names': 'subject_alternative_names',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, issuer_id=None, csr=None, validity=None, type=None, path_length=None, subject_alternative_names=None, enterprise_project_id=None):
        """CreateCertificateByCsrRequestBody

        The model defined in huaweicloud sdk

        :param issuer_id: 父CA证书ID。
        :type issuer_id: str
        :param csr: 证书签名请求。请使用“\\r\\n”或“\\n”替代证书签名请求中的换行符，若通过console端请求此接口，则无需做符号转换。
        :type csr: str
        :param validity: 
        :type validity: :class:`huaweicloudsdkccm.v1.Validity`
        :param type: 证书类型，用于区分从属CA与私有证书。   - **ENTITY_CERT** : 签发私有证书，为缺省值；   - **INTERMEDIATE_CA** : 签发从属CA。
        :type type: str
        :param path_length: 路径长度，仅当签发从属CA时有效。
        :type path_length: int
        :param subject_alternative_names: 主体备用名称(本接口预留参数，当前在后端被忽略)，详情请参见**SubjectAlternativeName**字段数据结构说明。
        :type subject_alternative_names: list[:class:`huaweicloudsdkccm.v1.SubjectAlternativeName`]
        :param enterprise_project_id: 企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.   取值为“all”   取值为“0”   满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”
        :type enterprise_project_id: str
        """
        
        

        self._issuer_id = None
        self._csr = None
        self._validity = None
        self._type = None
        self._path_length = None
        self._subject_alternative_names = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.issuer_id = issuer_id
        self.csr = csr
        self.validity = validity
        if type is not None:
            self.type = type
        if path_length is not None:
            self.path_length = path_length
        if subject_alternative_names is not None:
            self.subject_alternative_names = subject_alternative_names
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def issuer_id(self):
        """Gets the issuer_id of this CreateCertificateByCsrRequestBody.

        父CA证书ID。

        :return: The issuer_id of this CreateCertificateByCsrRequestBody.
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this CreateCertificateByCsrRequestBody.

        父CA证书ID。

        :param issuer_id: The issuer_id of this CreateCertificateByCsrRequestBody.
        :type issuer_id: str
        """
        self._issuer_id = issuer_id

    @property
    def csr(self):
        """Gets the csr of this CreateCertificateByCsrRequestBody.

        证书签名请求。请使用“\\r\\n”或“\\n”替代证书签名请求中的换行符，若通过console端请求此接口，则无需做符号转换。

        :return: The csr of this CreateCertificateByCsrRequestBody.
        :rtype: str
        """
        return self._csr

    @csr.setter
    def csr(self, csr):
        """Sets the csr of this CreateCertificateByCsrRequestBody.

        证书签名请求。请使用“\\r\\n”或“\\n”替代证书签名请求中的换行符，若通过console端请求此接口，则无需做符号转换。

        :param csr: The csr of this CreateCertificateByCsrRequestBody.
        :type csr: str
        """
        self._csr = csr

    @property
    def validity(self):
        """Gets the validity of this CreateCertificateByCsrRequestBody.

        :return: The validity of this CreateCertificateByCsrRequestBody.
        :rtype: :class:`huaweicloudsdkccm.v1.Validity`
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this CreateCertificateByCsrRequestBody.

        :param validity: The validity of this CreateCertificateByCsrRequestBody.
        :type validity: :class:`huaweicloudsdkccm.v1.Validity`
        """
        self._validity = validity

    @property
    def type(self):
        """Gets the type of this CreateCertificateByCsrRequestBody.

        证书类型，用于区分从属CA与私有证书。   - **ENTITY_CERT** : 签发私有证书，为缺省值；   - **INTERMEDIATE_CA** : 签发从属CA。

        :return: The type of this CreateCertificateByCsrRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCertificateByCsrRequestBody.

        证书类型，用于区分从属CA与私有证书。   - **ENTITY_CERT** : 签发私有证书，为缺省值；   - **INTERMEDIATE_CA** : 签发从属CA。

        :param type: The type of this CreateCertificateByCsrRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def path_length(self):
        """Gets the path_length of this CreateCertificateByCsrRequestBody.

        路径长度，仅当签发从属CA时有效。

        :return: The path_length of this CreateCertificateByCsrRequestBody.
        :rtype: int
        """
        return self._path_length

    @path_length.setter
    def path_length(self, path_length):
        """Sets the path_length of this CreateCertificateByCsrRequestBody.

        路径长度，仅当签发从属CA时有效。

        :param path_length: The path_length of this CreateCertificateByCsrRequestBody.
        :type path_length: int
        """
        self._path_length = path_length

    @property
    def subject_alternative_names(self):
        """Gets the subject_alternative_names of this CreateCertificateByCsrRequestBody.

        主体备用名称(本接口预留参数，当前在后端被忽略)，详情请参见**SubjectAlternativeName**字段数据结构说明。

        :return: The subject_alternative_names of this CreateCertificateByCsrRequestBody.
        :rtype: list[:class:`huaweicloudsdkccm.v1.SubjectAlternativeName`]
        """
        return self._subject_alternative_names

    @subject_alternative_names.setter
    def subject_alternative_names(self, subject_alternative_names):
        """Sets the subject_alternative_names of this CreateCertificateByCsrRequestBody.

        主体备用名称(本接口预留参数，当前在后端被忽略)，详情请参见**SubjectAlternativeName**字段数据结构说明。

        :param subject_alternative_names: The subject_alternative_names of this CreateCertificateByCsrRequestBody.
        :type subject_alternative_names: list[:class:`huaweicloudsdkccm.v1.SubjectAlternativeName`]
        """
        self._subject_alternative_names = subject_alternative_names

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateCertificateByCsrRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.   取值为“all”   取值为“0”   满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :return: The enterprise_project_id of this CreateCertificateByCsrRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateCertificateByCsrRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.   取值为“all”   取值为“0”   满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :param enterprise_project_id: The enterprise_project_id of this CreateCertificateByCsrRequestBody.
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
        if not isinstance(other, CreateCertificateByCsrRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
