# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowAppCertificateResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cert_id': 'str',
        'name': 'str',
        'file_name': 'str',
        'state': 'str',
        'owner': 'str',
        'issuer': 'str',
        'effective_date': 'str',
        'expiry_date': 'str',
        'cn_name': 'str',
        'format': 'str',
        'update_time': 'str',
        'content': 'str'
    }

    attribute_map = {
        'cert_id': 'cert_id',
        'name': 'name',
        'file_name': 'file_name',
        'state': 'state',
        'owner': 'owner',
        'issuer': 'issuer',
        'effective_date': 'effective_date',
        'expiry_date': 'expiry_date',
        'cn_name': 'cn_name',
        'format': 'format',
        'update_time': 'update_time',
        'content': 'content'
    }

    def __init__(self, cert_id=None, name=None, file_name=None, state=None, owner=None, issuer=None, effective_date=None, expiry_date=None, cn_name='*', format=None, update_time=None, content=None):
        """ShowAppCertificateResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._cert_id = None
        self._name = None
        self._file_name = None
        self._state = None
        self._owner = None
        self._issuer = None
        self._effective_date = None
        self._expiry_date = None
        self._cn_name = None
        self._format = None
        self._update_time = None
        self._content = None
        self.discriminator = None

        if cert_id is not None:
            self.cert_id = cert_id
        if name is not None:
            self.name = name
        if file_name is not None:
            self.file_name = file_name
        if state is not None:
            self.state = state
        if owner is not None:
            self.owner = owner
        if issuer is not None:
            self.issuer = issuer
        if effective_date is not None:
            self.effective_date = effective_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if cn_name is not None:
            self.cn_name = cn_name
        if format is not None:
            self.format = format
        if update_time is not None:
            self.update_time = update_time
        if content is not None:
            self.content = content

    @property
    def cert_id(self):
        """Gets the cert_id of this ShowAppCertificateResponse.

        证书ID，用于唯一标识一个证书，在物联网平台上传证书后由平台分配获得

        :return: The cert_id of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._cert_id

    @cert_id.setter
    def cert_id(self, cert_id):
        """Sets the cert_id of this ShowAppCertificateResponse.

        证书ID，用于唯一标识一个证书，在物联网平台上传证书后由平台分配获得

        :param cert_id: The cert_id of this ShowAppCertificateResponse.
        :type: str
        """
        self._cert_id = cert_id

    @property
    def name(self):
        """Gets the name of this ShowAppCertificateResponse.

        证书名称

        :return: The name of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowAppCertificateResponse.

        证书名称

        :param name: The name of this ShowAppCertificateResponse.
        :type: str
        """
        self._name = name

    @property
    def file_name(self):
        """Gets the file_name of this ShowAppCertificateResponse.

        证书文件名称

        :return: The file_name of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ShowAppCertificateResponse.

        证书文件名称

        :param file_name: The file_name of this ShowAppCertificateResponse.
        :type: str
        """
        self._file_name = file_name

    @property
    def state(self):
        """Gets the state of this ShowAppCertificateResponse.

        证书状态,NORMAL代表证书正常,TOEXPIRE代表即将过期,EXPIRED代表证书已过期

        :return: The state of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowAppCertificateResponse.

        证书状态,NORMAL代表证书正常,TOEXPIRE代表即将过期,EXPIRED代表证书已过期

        :param state: The state of this ShowAppCertificateResponse.
        :type: str
        """
        self._state = state

    @property
    def owner(self):
        """Gets the owner of this ShowAppCertificateResponse.

        证书所有者

        :return: The owner of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowAppCertificateResponse.

        证书所有者

        :param owner: The owner of this ShowAppCertificateResponse.
        :type: str
        """
        self._owner = owner

    @property
    def issuer(self):
        """Gets the issuer of this ShowAppCertificateResponse.

        证书颁发者信息

        :return: The issuer of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this ShowAppCertificateResponse.

        证书颁发者信息

        :param issuer: The issuer of this ShowAppCertificateResponse.
        :type: str
        """
        self._issuer = issuer

    @property
    def effective_date(self):
        """Gets the effective_date of this ShowAppCertificateResponse.

        证书生效日期

        :return: The effective_date of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this ShowAppCertificateResponse.

        证书生效日期

        :param effective_date: The effective_date of this ShowAppCertificateResponse.
        :type: str
        """
        self._effective_date = effective_date

    @property
    def expiry_date(self):
        """Gets the expiry_date of this ShowAppCertificateResponse.

        证书失效日期

        :return: The expiry_date of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this ShowAppCertificateResponse.

        证书失效日期

        :param expiry_date: The expiry_date of this ShowAppCertificateResponse.
        :type: str
        """
        self._expiry_date = expiry_date

    @property
    def cn_name(self):
        """Gets the cn_name of this ShowAppCertificateResponse.

        证书CN名称

        :return: The cn_name of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._cn_name

    @cn_name.setter
    def cn_name(self, cn_name):
        """Sets the cn_name of this ShowAppCertificateResponse.

        证书CN名称

        :param cn_name: The cn_name of this ShowAppCertificateResponse.
        :type: str
        """
        self._cn_name = cn_name

    @property
    def format(self):
        """Gets the format of this ShowAppCertificateResponse.

        CA证书格式

        :return: The format of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ShowAppCertificateResponse.

        CA证书格式

        :param format: The format of this ShowAppCertificateResponse.
        :type: str
        """
        self._format = format

    @property
    def update_time(self):
        """Gets the update_time of this ShowAppCertificateResponse.

        证书修改日期

        :return: The update_time of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowAppCertificateResponse.

        证书修改日期

        :param update_time: The update_time of this ShowAppCertificateResponse.
        :type: str
        """
        self._update_time = update_time

    @property
    def content(self):
        """Gets the content of this ShowAppCertificateResponse.

        证书内容

        :return: The content of this ShowAppCertificateResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ShowAppCertificateResponse.

        证书内容

        :param content: The content of this ShowAppCertificateResponse.
        :type: str
        """
        self._content = content

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowAppCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
