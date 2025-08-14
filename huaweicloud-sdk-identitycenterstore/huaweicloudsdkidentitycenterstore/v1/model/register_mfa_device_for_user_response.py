# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterMfaDeviceForUserResponse(SdkResponse):

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
        'user_id': 'str',
        'work_flow': 'str',
        'redirect_url': 'str'
    }

    attribute_map = {
        'identity_store_id': 'identity_store_id',
        'user_id': 'user_id',
        'work_flow': 'work_flow',
        'redirect_url': 'redirect_url'
    }

    def __init__(self, identity_store_id=None, user_id=None, work_flow=None, redirect_url=None):
        r"""RegisterMfaDeviceForUserResponse

        The model defined in huaweicloud sdk

        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
        :param user_id: 身份源中用户唯一标识符（ID）
        :type user_id: str
        :param work_flow: 注册MFA需要的一次性随机字符
        :type work_flow: str
        :param redirect_url: MFA注册重定向地址
        :type redirect_url: str
        """
        
        super(RegisterMfaDeviceForUserResponse, self).__init__()

        self._identity_store_id = None
        self._user_id = None
        self._work_flow = None
        self._redirect_url = None
        self.discriminator = None

        if identity_store_id is not None:
            self.identity_store_id = identity_store_id
        if user_id is not None:
            self.user_id = user_id
        if work_flow is not None:
            self.work_flow = work_flow
        if redirect_url is not None:
            self.redirect_url = redirect_url

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this RegisterMfaDeviceForUserResponse.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this RegisterMfaDeviceForUserResponse.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this RegisterMfaDeviceForUserResponse.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this RegisterMfaDeviceForUserResponse.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def user_id(self):
        r"""Gets the user_id of this RegisterMfaDeviceForUserResponse.

        身份源中用户唯一标识符（ID）

        :return: The user_id of this RegisterMfaDeviceForUserResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this RegisterMfaDeviceForUserResponse.

        身份源中用户唯一标识符（ID）

        :param user_id: The user_id of this RegisterMfaDeviceForUserResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def work_flow(self):
        r"""Gets the work_flow of this RegisterMfaDeviceForUserResponse.

        注册MFA需要的一次性随机字符

        :return: The work_flow of this RegisterMfaDeviceForUserResponse.
        :rtype: str
        """
        return self._work_flow

    @work_flow.setter
    def work_flow(self, work_flow):
        r"""Sets the work_flow of this RegisterMfaDeviceForUserResponse.

        注册MFA需要的一次性随机字符

        :param work_flow: The work_flow of this RegisterMfaDeviceForUserResponse.
        :type work_flow: str
        """
        self._work_flow = work_flow

    @property
    def redirect_url(self):
        r"""Gets the redirect_url of this RegisterMfaDeviceForUserResponse.

        MFA注册重定向地址

        :return: The redirect_url of this RegisterMfaDeviceForUserResponse.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        r"""Sets the redirect_url of this RegisterMfaDeviceForUserResponse.

        MFA注册重定向地址

        :param redirect_url: The redirect_url of this RegisterMfaDeviceForUserResponse.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

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
        if not isinstance(other, RegisterMfaDeviceForUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
