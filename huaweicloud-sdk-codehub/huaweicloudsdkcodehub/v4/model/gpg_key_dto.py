# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GpgKeyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gpg_name': 'str',
        'open_gpg_verified': 'bool',
        'verification_status': 'int',
        'gpg_primary_key_id': 'str',
        'gpg_nick_name': 'str',
        'gpg_tenant_name': 'str',
        'gpg_user_name': 'str'
    }

    attribute_map = {
        'gpg_name': 'gpg_name',
        'open_gpg_verified': 'open_gpg_verified',
        'verification_status': 'verification_status',
        'gpg_primary_key_id': 'gpg_primary_key_id',
        'gpg_nick_name': 'gpg_nick_name',
        'gpg_tenant_name': 'gpg_tenant_name',
        'gpg_user_name': 'gpg_user_name'
    }

    def __init__(self, gpg_name=None, open_gpg_verified=None, verification_status=None, gpg_primary_key_id=None, gpg_nick_name=None, gpg_tenant_name=None, gpg_user_name=None):
        r"""GpgKeyDto

        The model defined in huaweicloud sdk

        :param gpg_name: gpg名称
        :type gpg_name: str
        :param open_gpg_verified: 是否开启gpg认证
        :type open_gpg_verified: bool
        :param verification_status: gpg认证状态
        :type verification_status: int
        :param gpg_primary_key_id: gpg初始化id
        :type gpg_primary_key_id: str
        :param gpg_nick_name: gpg昵称
        :type gpg_nick_name: str
        :param gpg_tenant_name: gpg租户昵称
        :type gpg_tenant_name: str
        :param gpg_user_name: gpg用户名称
        :type gpg_user_name: str
        """
        
        

        self._gpg_name = None
        self._open_gpg_verified = None
        self._verification_status = None
        self._gpg_primary_key_id = None
        self._gpg_nick_name = None
        self._gpg_tenant_name = None
        self._gpg_user_name = None
        self.discriminator = None

        if gpg_name is not None:
            self.gpg_name = gpg_name
        if open_gpg_verified is not None:
            self.open_gpg_verified = open_gpg_verified
        if verification_status is not None:
            self.verification_status = verification_status
        if gpg_primary_key_id is not None:
            self.gpg_primary_key_id = gpg_primary_key_id
        if gpg_nick_name is not None:
            self.gpg_nick_name = gpg_nick_name
        if gpg_tenant_name is not None:
            self.gpg_tenant_name = gpg_tenant_name
        if gpg_user_name is not None:
            self.gpg_user_name = gpg_user_name

    @property
    def gpg_name(self):
        r"""Gets the gpg_name of this GpgKeyDto.

        gpg名称

        :return: The gpg_name of this GpgKeyDto.
        :rtype: str
        """
        return self._gpg_name

    @gpg_name.setter
    def gpg_name(self, gpg_name):
        r"""Sets the gpg_name of this GpgKeyDto.

        gpg名称

        :param gpg_name: The gpg_name of this GpgKeyDto.
        :type gpg_name: str
        """
        self._gpg_name = gpg_name

    @property
    def open_gpg_verified(self):
        r"""Gets the open_gpg_verified of this GpgKeyDto.

        是否开启gpg认证

        :return: The open_gpg_verified of this GpgKeyDto.
        :rtype: bool
        """
        return self._open_gpg_verified

    @open_gpg_verified.setter
    def open_gpg_verified(self, open_gpg_verified):
        r"""Sets the open_gpg_verified of this GpgKeyDto.

        是否开启gpg认证

        :param open_gpg_verified: The open_gpg_verified of this GpgKeyDto.
        :type open_gpg_verified: bool
        """
        self._open_gpg_verified = open_gpg_verified

    @property
    def verification_status(self):
        r"""Gets the verification_status of this GpgKeyDto.

        gpg认证状态

        :return: The verification_status of this GpgKeyDto.
        :rtype: int
        """
        return self._verification_status

    @verification_status.setter
    def verification_status(self, verification_status):
        r"""Sets the verification_status of this GpgKeyDto.

        gpg认证状态

        :param verification_status: The verification_status of this GpgKeyDto.
        :type verification_status: int
        """
        self._verification_status = verification_status

    @property
    def gpg_primary_key_id(self):
        r"""Gets the gpg_primary_key_id of this GpgKeyDto.

        gpg初始化id

        :return: The gpg_primary_key_id of this GpgKeyDto.
        :rtype: str
        """
        return self._gpg_primary_key_id

    @gpg_primary_key_id.setter
    def gpg_primary_key_id(self, gpg_primary_key_id):
        r"""Sets the gpg_primary_key_id of this GpgKeyDto.

        gpg初始化id

        :param gpg_primary_key_id: The gpg_primary_key_id of this GpgKeyDto.
        :type gpg_primary_key_id: str
        """
        self._gpg_primary_key_id = gpg_primary_key_id

    @property
    def gpg_nick_name(self):
        r"""Gets the gpg_nick_name of this GpgKeyDto.

        gpg昵称

        :return: The gpg_nick_name of this GpgKeyDto.
        :rtype: str
        """
        return self._gpg_nick_name

    @gpg_nick_name.setter
    def gpg_nick_name(self, gpg_nick_name):
        r"""Sets the gpg_nick_name of this GpgKeyDto.

        gpg昵称

        :param gpg_nick_name: The gpg_nick_name of this GpgKeyDto.
        :type gpg_nick_name: str
        """
        self._gpg_nick_name = gpg_nick_name

    @property
    def gpg_tenant_name(self):
        r"""Gets the gpg_tenant_name of this GpgKeyDto.

        gpg租户昵称

        :return: The gpg_tenant_name of this GpgKeyDto.
        :rtype: str
        """
        return self._gpg_tenant_name

    @gpg_tenant_name.setter
    def gpg_tenant_name(self, gpg_tenant_name):
        r"""Sets the gpg_tenant_name of this GpgKeyDto.

        gpg租户昵称

        :param gpg_tenant_name: The gpg_tenant_name of this GpgKeyDto.
        :type gpg_tenant_name: str
        """
        self._gpg_tenant_name = gpg_tenant_name

    @property
    def gpg_user_name(self):
        r"""Gets the gpg_user_name of this GpgKeyDto.

        gpg用户名称

        :return: The gpg_user_name of this GpgKeyDto.
        :rtype: str
        """
        return self._gpg_user_name

    @gpg_user_name.setter
    def gpg_user_name(self, gpg_user_name):
        r"""Sets the gpg_user_name of this GpgKeyDto.

        gpg用户名称

        :param gpg_user_name: The gpg_user_name of this GpgKeyDto.
        :type gpg_user_name: str
        """
        self._gpg_user_name = gpg_user_name

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
        if not isinstance(other, GpgKeyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
