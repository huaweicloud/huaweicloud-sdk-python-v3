# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdentityStoreDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'identity_store_id': 'str',
        'identity_store_type': 'str',
        'authentication_type': 'str',
        'provisioning_type': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'identity_store_id': 'identity_store_id',
        'identity_store_type': 'identity_store_type',
        'authentication_type': 'authentication_type',
        'provisioning_type': 'provisioning_type',
        'status': 'status'
    }

    def __init__(self, identity_store_id=None, identity_store_type=None, authentication_type=None, provisioning_type=None, status=None):
        r"""IdentityStoreDto

        The model defined in huaweicloud sdk

        :param identity_store_id: 关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。
        :type identity_store_id: str
        :param identity_store_type: 身份源类型
        :type identity_store_type: str
        :param authentication_type: 登录认证类型
        :type authentication_type: str
        :param provisioning_type: 预配类型
        :type provisioning_type: list[str]
        :param status: 身份源是否启用状态
        :type status: str
        """
        
        

        self._identity_store_id = None
        self._identity_store_type = None
        self._authentication_type = None
        self._provisioning_type = None
        self._status = None
        self.discriminator = None

        self.identity_store_id = identity_store_id
        self.identity_store_type = identity_store_type
        self.authentication_type = authentication_type
        self.provisioning_type = provisioning_type
        self.status = status

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this IdentityStoreDto.

        关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。

        :return: The identity_store_id of this IdentityStoreDto.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this IdentityStoreDto.

        关联到IAM身份中心实例的身份源的全局唯一标识符（ID）。

        :param identity_store_id: The identity_store_id of this IdentityStoreDto.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def identity_store_type(self):
        r"""Gets the identity_store_type of this IdentityStoreDto.

        身份源类型

        :return: The identity_store_type of this IdentityStoreDto.
        :rtype: str
        """
        return self._identity_store_type

    @identity_store_type.setter
    def identity_store_type(self, identity_store_type):
        r"""Sets the identity_store_type of this IdentityStoreDto.

        身份源类型

        :param identity_store_type: The identity_store_type of this IdentityStoreDto.
        :type identity_store_type: str
        """
        self._identity_store_type = identity_store_type

    @property
    def authentication_type(self):
        r"""Gets the authentication_type of this IdentityStoreDto.

        登录认证类型

        :return: The authentication_type of this IdentityStoreDto.
        :rtype: str
        """
        return self._authentication_type

    @authentication_type.setter
    def authentication_type(self, authentication_type):
        r"""Sets the authentication_type of this IdentityStoreDto.

        登录认证类型

        :param authentication_type: The authentication_type of this IdentityStoreDto.
        :type authentication_type: str
        """
        self._authentication_type = authentication_type

    @property
    def provisioning_type(self):
        r"""Gets the provisioning_type of this IdentityStoreDto.

        预配类型

        :return: The provisioning_type of this IdentityStoreDto.
        :rtype: list[str]
        """
        return self._provisioning_type

    @provisioning_type.setter
    def provisioning_type(self, provisioning_type):
        r"""Sets the provisioning_type of this IdentityStoreDto.

        预配类型

        :param provisioning_type: The provisioning_type of this IdentityStoreDto.
        :type provisioning_type: list[str]
        """
        self._provisioning_type = provisioning_type

    @property
    def status(self):
        r"""Gets the status of this IdentityStoreDto.

        身份源是否启用状态

        :return: The status of this IdentityStoreDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IdentityStoreDto.

        身份源是否启用状态

        :param status: The status of this IdentityStoreDto.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, IdentityStoreDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
