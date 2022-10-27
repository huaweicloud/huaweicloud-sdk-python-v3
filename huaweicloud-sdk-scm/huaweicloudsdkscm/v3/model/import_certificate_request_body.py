# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportCertificateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'certificate': 'str',
        'certificate_chain': 'str',
        'private_key': 'str',
        'enterprise_project_id': 'str',
        'enc_certificate': 'str',
        'enc_private_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'certificate': 'certificate',
        'certificate_chain': 'certificate_chain',
        'private_key': 'private_key',
        'enterprise_project_id': 'enterprise_project_id',
        'enc_certificate': 'enc_certificate',
        'enc_private_key': 'enc_private_key'
    }

    def __init__(self, name=None, certificate=None, certificate_chain=None, private_key=None, enterprise_project_id=None, enc_certificate=None, enc_private_key=None):
        """ImportCertificateRequestBody

        The model defined in huaweicloud sdk

        :param name: 证书名称。字符长度为3~63位。
        :type name: str
        :param certificate: 证书内容。回车换行需要使用转义字符\\n或者\\r\\n替换。
        :type certificate: str
        :param certificate_chain: 证书链。回车换行需要使用转义字符\\n或者\\r\\n替换。
        :type certificate_chain: str
        :param private_key: 证书私钥。 不能上传带有口令保护的私钥，回车换行需要使用转义字符\\n或者\\r\\n替换。
        :type private_key: str
        :param enterprise_project_id: 企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.  取值为“all”  取值为“0”  满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”
        :type enterprise_project_id: str
        :param enc_certificate: 可选参数，国密证书的加密证书内容。书回车换行需要使用转义字符\\n或者\\r\\n替换。
        :type enc_certificate: str
        :param enc_private_key: 可选参数，国密证书的加密私钥。 不能上传带有口令保护的私钥，回车换行需要使用转义字符\\n或者\\r\\n替换。
        :type enc_private_key: str
        """
        
        

        self._name = None
        self._certificate = None
        self._certificate_chain = None
        self._private_key = None
        self._enterprise_project_id = None
        self._enc_certificate = None
        self._enc_private_key = None
        self.discriminator = None

        self.name = name
        self.certificate = certificate
        self.certificate_chain = certificate_chain
        self.private_key = private_key
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enc_certificate is not None:
            self.enc_certificate = enc_certificate
        if enc_private_key is not None:
            self.enc_private_key = enc_private_key

    @property
    def name(self):
        """Gets the name of this ImportCertificateRequestBody.

        证书名称。字符长度为3~63位。

        :return: The name of this ImportCertificateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportCertificateRequestBody.

        证书名称。字符长度为3~63位。

        :param name: The name of this ImportCertificateRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def certificate(self):
        """Gets the certificate of this ImportCertificateRequestBody.

        证书内容。回车换行需要使用转义字符\\n或者\\r\\n替换。

        :return: The certificate of this ImportCertificateRequestBody.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this ImportCertificateRequestBody.

        证书内容。回车换行需要使用转义字符\\n或者\\r\\n替换。

        :param certificate: The certificate of this ImportCertificateRequestBody.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def certificate_chain(self):
        """Gets the certificate_chain of this ImportCertificateRequestBody.

        证书链。回车换行需要使用转义字符\\n或者\\r\\n替换。

        :return: The certificate_chain of this ImportCertificateRequestBody.
        :rtype: str
        """
        return self._certificate_chain

    @certificate_chain.setter
    def certificate_chain(self, certificate_chain):
        """Sets the certificate_chain of this ImportCertificateRequestBody.

        证书链。回车换行需要使用转义字符\\n或者\\r\\n替换。

        :param certificate_chain: The certificate_chain of this ImportCertificateRequestBody.
        :type certificate_chain: str
        """
        self._certificate_chain = certificate_chain

    @property
    def private_key(self):
        """Gets the private_key of this ImportCertificateRequestBody.

        证书私钥。 不能上传带有口令保护的私钥，回车换行需要使用转义字符\\n或者\\r\\n替换。

        :return: The private_key of this ImportCertificateRequestBody.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this ImportCertificateRequestBody.

        证书私钥。 不能上传带有口令保护的私钥，回车换行需要使用转义字符\\n或者\\r\\n替换。

        :param private_key: The private_key of this ImportCertificateRequestBody.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ImportCertificateRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.  取值为“all”  取值为“0”  满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :return: The enterprise_project_id of this ImportCertificateRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ImportCertificateRequestBody.

        企业多项目ID。用户未开通企业多项目时，不需要输入该字段。 用户开通企业多项目时，查询资源可以输入该字段。 若用户不输入该字段，默认查询租户所有有权限的企业多项目下的资源。 此时“enterprise_project_id”取值为“all”。 若用户输入该字段，取值满足以下任一条件.  取值为“all”  取值为“0”  满足正则匹配：“^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$”

        :param enterprise_project_id: The enterprise_project_id of this ImportCertificateRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enc_certificate(self):
        """Gets the enc_certificate of this ImportCertificateRequestBody.

        可选参数，国密证书的加密证书内容。书回车换行需要使用转义字符\\n或者\\r\\n替换。

        :return: The enc_certificate of this ImportCertificateRequestBody.
        :rtype: str
        """
        return self._enc_certificate

    @enc_certificate.setter
    def enc_certificate(self, enc_certificate):
        """Sets the enc_certificate of this ImportCertificateRequestBody.

        可选参数，国密证书的加密证书内容。书回车换行需要使用转义字符\\n或者\\r\\n替换。

        :param enc_certificate: The enc_certificate of this ImportCertificateRequestBody.
        :type enc_certificate: str
        """
        self._enc_certificate = enc_certificate

    @property
    def enc_private_key(self):
        """Gets the enc_private_key of this ImportCertificateRequestBody.

        可选参数，国密证书的加密私钥。 不能上传带有口令保护的私钥，回车换行需要使用转义字符\\n或者\\r\\n替换。

        :return: The enc_private_key of this ImportCertificateRequestBody.
        :rtype: str
        """
        return self._enc_private_key

    @enc_private_key.setter
    def enc_private_key(self, enc_private_key):
        """Sets the enc_private_key of this ImportCertificateRequestBody.

        可选参数，国密证书的加密私钥。 不能上传带有口令保护的私钥，回车换行需要使用转义字符\\n或者\\r\\n替换。

        :param enc_private_key: The enc_private_key of this ImportCertificateRequestBody.
        :type enc_private_key: str
        """
        self._enc_private_key = enc_private_key

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
        if not isinstance(other, ImportCertificateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
