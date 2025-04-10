# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAgencyCredentialsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('access_token')

    openapi_types = {
        'access_token': 'str',
        'target_account_id': 'str',
        'agency_urn': 'str'
    }

    attribute_map = {
        'access_token': 'access-token',
        'target_account_id': 'target_account_id',
        'agency_urn': 'agency_urn'
    }

    def __init__(self, access_token=None, target_account_id=None, agency_urn=None):
        r"""GetAgencyCredentialsRequest

        The model defined in huaweicloud sdk

        :param access_token: 创建令牌接口调用签发的访问令牌
        :type access_token: str
        :param target_account_id: 目标账户的全局唯一标识符（ID）
        :type target_account_id: str
        :param agency_urn: 委托或信任委托的统一资源名称（URN）
        :type agency_urn: str
        """
        
        

        self._access_token = None
        self._target_account_id = None
        self._agency_urn = None
        self.discriminator = None

        self.access_token = access_token
        self.target_account_id = target_account_id
        self.agency_urn = agency_urn

    @property
    def access_token(self):
        r"""Gets the access_token of this GetAgencyCredentialsRequest.

        创建令牌接口调用签发的访问令牌

        :return: The access_token of this GetAgencyCredentialsRequest.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        r"""Sets the access_token of this GetAgencyCredentialsRequest.

        创建令牌接口调用签发的访问令牌

        :param access_token: The access_token of this GetAgencyCredentialsRequest.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def target_account_id(self):
        r"""Gets the target_account_id of this GetAgencyCredentialsRequest.

        目标账户的全局唯一标识符（ID）

        :return: The target_account_id of this GetAgencyCredentialsRequest.
        :rtype: str
        """
        return self._target_account_id

    @target_account_id.setter
    def target_account_id(self, target_account_id):
        r"""Sets the target_account_id of this GetAgencyCredentialsRequest.

        目标账户的全局唯一标识符（ID）

        :param target_account_id: The target_account_id of this GetAgencyCredentialsRequest.
        :type target_account_id: str
        """
        self._target_account_id = target_account_id

    @property
    def agency_urn(self):
        r"""Gets the agency_urn of this GetAgencyCredentialsRequest.

        委托或信任委托的统一资源名称（URN）

        :return: The agency_urn of this GetAgencyCredentialsRequest.
        :rtype: str
        """
        return self._agency_urn

    @agency_urn.setter
    def agency_urn(self, agency_urn):
        r"""Sets the agency_urn of this GetAgencyCredentialsRequest.

        委托或信任委托的统一资源名称（URN）

        :param agency_urn: The agency_urn of this GetAgencyCredentialsRequest.
        :type agency_urn: str
        """
        self._agency_urn = agency_urn

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
        if not isinstance(other, GetAgencyCredentialsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
