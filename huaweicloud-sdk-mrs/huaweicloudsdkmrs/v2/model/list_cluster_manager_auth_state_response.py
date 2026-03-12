# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterManagerAuthStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_type': 'float',
        'authorized': 'bool',
        'expiration_time': 'str'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'authorized': 'authorized',
        'expiration_time': 'expiration_time'
    }

    def __init__(self, auth_type=None, authorized=None, expiration_time=None):
        r"""ListClusterManagerAuthStateResponse

        The model defined in huaweicloud sdk

        :param auth_type: 查询指定集群界面授权类型，0为界面普通授权，当前仅开放普通授权
        :type auth_type: float
        :param authorized: 查询集群是否已开启界面授权
        :type authorized: bool
        :param expiration_time: 集群界面授权的过期时间
        :type expiration_time: str
        """
        
        super().__init__()

        self._auth_type = None
        self._authorized = None
        self._expiration_time = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if authorized is not None:
            self.authorized = authorized
        if expiration_time is not None:
            self.expiration_time = expiration_time

    @property
    def auth_type(self):
        r"""Gets the auth_type of this ListClusterManagerAuthStateResponse.

        查询指定集群界面授权类型，0为界面普通授权，当前仅开放普通授权

        :return: The auth_type of this ListClusterManagerAuthStateResponse.
        :rtype: float
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this ListClusterManagerAuthStateResponse.

        查询指定集群界面授权类型，0为界面普通授权，当前仅开放普通授权

        :param auth_type: The auth_type of this ListClusterManagerAuthStateResponse.
        :type auth_type: float
        """
        self._auth_type = auth_type

    @property
    def authorized(self):
        r"""Gets the authorized of this ListClusterManagerAuthStateResponse.

        查询集群是否已开启界面授权

        :return: The authorized of this ListClusterManagerAuthStateResponse.
        :rtype: bool
        """
        return self._authorized

    @authorized.setter
    def authorized(self, authorized):
        r"""Sets the authorized of this ListClusterManagerAuthStateResponse.

        查询集群是否已开启界面授权

        :param authorized: The authorized of this ListClusterManagerAuthStateResponse.
        :type authorized: bool
        """
        self._authorized = authorized

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this ListClusterManagerAuthStateResponse.

        集群界面授权的过期时间

        :return: The expiration_time of this ListClusterManagerAuthStateResponse.
        :rtype: str
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this ListClusterManagerAuthStateResponse.

        集群界面授权的过期时间

        :param expiration_time: The expiration_time of this ListClusterManagerAuthStateResponse.
        :type expiration_time: str
        """
        self._expiration_time = expiration_time

    def to_dict(self):
        import warnings
        warnings.warn("ListClusterManagerAuthStateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListClusterManagerAuthStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
