# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccountAssignmentsForPrincipalRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'instance_id': 'str',
        'principal_id': 'str',
        'principal_type': 'str',
        'limit': 'int',
        'marker': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'instance_id': 'instance_id',
        'principal_id': 'principal_id',
        'principal_type': 'principal_type',
        'limit': 'limit',
        'marker': 'marker',
        'account_id': 'account_id'
    }

    def __init__(self, x_security_token=None, instance_id=None, principal_id=None, principal_type=None, limit=None, marker=None, account_id=None):
        r"""ListAccountAssignmentsForPrincipalRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param instance_id: IAM Identity Center实例的全局唯一标识符（ID）
        :type instance_id: str
        :param principal_id: IAM Identity Center 身份主体的全局唯一标识符（ID）
        :type principal_id: str
        :param principal_type: IAM Identity Center 身份主体类型.
        :type principal_type: str
        :param limit: 每个请求返回的最大结果数。
        :type limit: int
        :param marker: 分页标记
        :type marker: str
        :param account_id: 指定账户的唯一身份标识
        :type account_id: str
        """
        
        

        self._x_security_token = None
        self._instance_id = None
        self._principal_id = None
        self._principal_type = None
        self._limit = None
        self._marker = None
        self._account_id = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.instance_id = instance_id
        self.principal_id = principal_id
        self.principal_type = principal_type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if account_id is not None:
            self.account_id = account_id

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ListAccountAssignmentsForPrincipalRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ListAccountAssignmentsForPrincipalRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ListAccountAssignmentsForPrincipalRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ListAccountAssignmentsForPrincipalRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListAccountAssignmentsForPrincipalRequest.

        IAM Identity Center实例的全局唯一标识符（ID）

        :return: The instance_id of this ListAccountAssignmentsForPrincipalRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListAccountAssignmentsForPrincipalRequest.

        IAM Identity Center实例的全局唯一标识符（ID）

        :param instance_id: The instance_id of this ListAccountAssignmentsForPrincipalRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def principal_id(self):
        r"""Gets the principal_id of this ListAccountAssignmentsForPrincipalRequest.

        IAM Identity Center 身份主体的全局唯一标识符（ID）

        :return: The principal_id of this ListAccountAssignmentsForPrincipalRequest.
        :rtype: str
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        r"""Sets the principal_id of this ListAccountAssignmentsForPrincipalRequest.

        IAM Identity Center 身份主体的全局唯一标识符（ID）

        :param principal_id: The principal_id of this ListAccountAssignmentsForPrincipalRequest.
        :type principal_id: str
        """
        self._principal_id = principal_id

    @property
    def principal_type(self):
        r"""Gets the principal_type of this ListAccountAssignmentsForPrincipalRequest.

        IAM Identity Center 身份主体类型.

        :return: The principal_type of this ListAccountAssignmentsForPrincipalRequest.
        :rtype: str
        """
        return self._principal_type

    @principal_type.setter
    def principal_type(self, principal_type):
        r"""Sets the principal_type of this ListAccountAssignmentsForPrincipalRequest.

        IAM Identity Center 身份主体类型.

        :param principal_type: The principal_type of this ListAccountAssignmentsForPrincipalRequest.
        :type principal_type: str
        """
        self._principal_type = principal_type

    @property
    def limit(self):
        r"""Gets the limit of this ListAccountAssignmentsForPrincipalRequest.

        每个请求返回的最大结果数。

        :return: The limit of this ListAccountAssignmentsForPrincipalRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAccountAssignmentsForPrincipalRequest.

        每个请求返回的最大结果数。

        :param limit: The limit of this ListAccountAssignmentsForPrincipalRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListAccountAssignmentsForPrincipalRequest.

        分页标记

        :return: The marker of this ListAccountAssignmentsForPrincipalRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAccountAssignmentsForPrincipalRequest.

        分页标记

        :param marker: The marker of this ListAccountAssignmentsForPrincipalRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def account_id(self):
        r"""Gets the account_id of this ListAccountAssignmentsForPrincipalRequest.

        指定账户的唯一身份标识

        :return: The account_id of this ListAccountAssignmentsForPrincipalRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this ListAccountAssignmentsForPrincipalRequest.

        指定账户的唯一身份标识

        :param account_id: The account_id of this ListAccountAssignmentsForPrincipalRequest.
        :type account_id: str
        """
        self._account_id = account_id

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
        if not isinstance(other, ListAccountAssignmentsForPrincipalRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
