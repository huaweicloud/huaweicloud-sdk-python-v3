# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCertificateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'certificate_id': 'str',
        'cn_name': 'str',
        'owner': 'str',
        'status': 'bool',
        'verify_code': 'str',
        'provision_enable': 'bool',
        'template_id': 'str',
        'create_date': 'str',
        'effective_date': 'str',
        'expiry_date': 'str'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'cn_name': 'cn_name',
        'owner': 'owner',
        'status': 'status',
        'verify_code': 'verify_code',
        'provision_enable': 'provision_enable',
        'template_id': 'template_id',
        'create_date': 'create_date',
        'effective_date': 'effective_date',
        'expiry_date': 'expiry_date'
    }

    def __init__(self, certificate_id=None, cn_name=None, owner=None, status=None, verify_code=None, provision_enable=None, template_id=None, create_date=None, effective_date=None, expiry_date=None):
        r"""UpdateCertificateResponse

        The model defined in huaweicloud sdk

        :param certificate_id: CA证书ID，在上传CA证书时由平台分配的唯一标识。
        :type certificate_id: str
        :param cn_name: CA证书CN名称。
        :type cn_name: str
        :param owner: CA证书所有者。
        :type owner: str
        :param status: CA证书验证状态。true代表证书已通过验证，可进行设备证书认证接入。false代表证书未通过验证。
        :type status: bool
        :param verify_code: CA证书验证码。
        :type verify_code: str
        :param provision_enable: 是否开启自注册能力，当为true时该功能必须配合自注册模板使用，true：是，false：否。
        :type provision_enable: bool
        :param template_id: 绑定的自注册模板ID。
        :type template_id: str
        :param create_date: 创建证书日期。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type create_date: str
        :param effective_date: CA证书生效日期。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type effective_date: str
        :param expiry_date: CA证书失效日期。格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type expiry_date: str
        """
        
        super(UpdateCertificateResponse, self).__init__()

        self._certificate_id = None
        self._cn_name = None
        self._owner = None
        self._status = None
        self._verify_code = None
        self._provision_enable = None
        self._template_id = None
        self._create_date = None
        self._effective_date = None
        self._expiry_date = None
        self.discriminator = None

        if certificate_id is not None:
            self.certificate_id = certificate_id
        if cn_name is not None:
            self.cn_name = cn_name
        if owner is not None:
            self.owner = owner
        if status is not None:
            self.status = status
        if verify_code is not None:
            self.verify_code = verify_code
        if provision_enable is not None:
            self.provision_enable = provision_enable
        if template_id is not None:
            self.template_id = template_id
        if create_date is not None:
            self.create_date = create_date
        if effective_date is not None:
            self.effective_date = effective_date
        if expiry_date is not None:
            self.expiry_date = expiry_date

    @property
    def certificate_id(self):
        r"""Gets the certificate_id of this UpdateCertificateResponse.

        CA证书ID，在上传CA证书时由平台分配的唯一标识。

        :return: The certificate_id of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        r"""Sets the certificate_id of this UpdateCertificateResponse.

        CA证书ID，在上传CA证书时由平台分配的唯一标识。

        :param certificate_id: The certificate_id of this UpdateCertificateResponse.
        :type certificate_id: str
        """
        self._certificate_id = certificate_id

    @property
    def cn_name(self):
        r"""Gets the cn_name of this UpdateCertificateResponse.

        CA证书CN名称。

        :return: The cn_name of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._cn_name

    @cn_name.setter
    def cn_name(self, cn_name):
        r"""Sets the cn_name of this UpdateCertificateResponse.

        CA证书CN名称。

        :param cn_name: The cn_name of this UpdateCertificateResponse.
        :type cn_name: str
        """
        self._cn_name = cn_name

    @property
    def owner(self):
        r"""Gets the owner of this UpdateCertificateResponse.

        CA证书所有者。

        :return: The owner of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this UpdateCertificateResponse.

        CA证书所有者。

        :param owner: The owner of this UpdateCertificateResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def status(self):
        r"""Gets the status of this UpdateCertificateResponse.

        CA证书验证状态。true代表证书已通过验证，可进行设备证书认证接入。false代表证书未通过验证。

        :return: The status of this UpdateCertificateResponse.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateCertificateResponse.

        CA证书验证状态。true代表证书已通过验证，可进行设备证书认证接入。false代表证书未通过验证。

        :param status: The status of this UpdateCertificateResponse.
        :type status: bool
        """
        self._status = status

    @property
    def verify_code(self):
        r"""Gets the verify_code of this UpdateCertificateResponse.

        CA证书验证码。

        :return: The verify_code of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._verify_code

    @verify_code.setter
    def verify_code(self, verify_code):
        r"""Sets the verify_code of this UpdateCertificateResponse.

        CA证书验证码。

        :param verify_code: The verify_code of this UpdateCertificateResponse.
        :type verify_code: str
        """
        self._verify_code = verify_code

    @property
    def provision_enable(self):
        r"""Gets the provision_enable of this UpdateCertificateResponse.

        是否开启自注册能力，当为true时该功能必须配合自注册模板使用，true：是，false：否。

        :return: The provision_enable of this UpdateCertificateResponse.
        :rtype: bool
        """
        return self._provision_enable

    @provision_enable.setter
    def provision_enable(self, provision_enable):
        r"""Sets the provision_enable of this UpdateCertificateResponse.

        是否开启自注册能力，当为true时该功能必须配合自注册模板使用，true：是，false：否。

        :param provision_enable: The provision_enable of this UpdateCertificateResponse.
        :type provision_enable: bool
        """
        self._provision_enable = provision_enable

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateCertificateResponse.

        绑定的自注册模板ID。

        :return: The template_id of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateCertificateResponse.

        绑定的自注册模板ID。

        :param template_id: The template_id of this UpdateCertificateResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def create_date(self):
        r"""Gets the create_date of this UpdateCertificateResponse.

        创建证书日期。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_date of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        r"""Sets the create_date of this UpdateCertificateResponse.

        创建证书日期。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_date: The create_date of this UpdateCertificateResponse.
        :type create_date: str
        """
        self._create_date = create_date

    @property
    def effective_date(self):
        r"""Gets the effective_date of this UpdateCertificateResponse.

        CA证书生效日期。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The effective_date of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        r"""Sets the effective_date of this UpdateCertificateResponse.

        CA证书生效日期。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param effective_date: The effective_date of this UpdateCertificateResponse.
        :type effective_date: str
        """
        self._effective_date = effective_date

    @property
    def expiry_date(self):
        r"""Gets the expiry_date of this UpdateCertificateResponse.

        CA证书失效日期。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The expiry_date of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        r"""Sets the expiry_date of this UpdateCertificateResponse.

        CA证书失效日期。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param expiry_date: The expiry_date of this UpdateCertificateResponse.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

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
        if not isinstance(other, UpdateCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
