# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizeObsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_end_point': 'str',
        'bucket_name': 'str',
        'directory': 'str',
        'ak': 'str',
        'sk': 'str',
        'expires_at': 'str',
        'policy': 'Policy',
        'security_token': 'str'
    }

    attribute_map = {
        'server_end_point': 'server_end_point',
        'bucket_name': 'bucket_name',
        'directory': 'directory',
        'ak': 'ak',
        'sk': 'sk',
        'expires_at': 'expires_at',
        'policy': 'policy',
        'security_token': 'security_token'
    }

    def __init__(self, server_end_point=None, bucket_name=None, directory=None, ak=None, sk=None, expires_at=None, policy=None, security_token=None):
        """AuthorizeObsResponse

        The model defined in huaweicloud sdk

        :param server_end_point: 访问的服务终端节点。
        :type server_end_point: str
        :param bucket_name: 存放的桶名称。
        :type bucket_name: str
        :param directory: 存放目录。
        :type directory: str
        :param ak: 获取的AK。。
        :type ak: str
        :param sk: 获取的SK。
        :type sk: str
        :param expires_at: AK/SK和securitytoken的过期时间。。
        :type expires_at: str
        :param policy: 
        :type policy: :class:`huaweicloudsdkworkspaceapp.v1.Policy`
        :param security_token: 安全校验token，将所获的AK、SK等信息进行加密后的字符串。
        :type security_token: str
        """
        
        super(AuthorizeObsResponse, self).__init__()

        self._server_end_point = None
        self._bucket_name = None
        self._directory = None
        self._ak = None
        self._sk = None
        self._expires_at = None
        self._policy = None
        self._security_token = None
        self.discriminator = None

        if server_end_point is not None:
            self.server_end_point = server_end_point
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if directory is not None:
            self.directory = directory
        if ak is not None:
            self.ak = ak
        if sk is not None:
            self.sk = sk
        if expires_at is not None:
            self.expires_at = expires_at
        if policy is not None:
            self.policy = policy
        if security_token is not None:
            self.security_token = security_token

    @property
    def server_end_point(self):
        """Gets the server_end_point of this AuthorizeObsResponse.

        访问的服务终端节点。

        :return: The server_end_point of this AuthorizeObsResponse.
        :rtype: str
        """
        return self._server_end_point

    @server_end_point.setter
    def server_end_point(self, server_end_point):
        """Sets the server_end_point of this AuthorizeObsResponse.

        访问的服务终端节点。

        :param server_end_point: The server_end_point of this AuthorizeObsResponse.
        :type server_end_point: str
        """
        self._server_end_point = server_end_point

    @property
    def bucket_name(self):
        """Gets the bucket_name of this AuthorizeObsResponse.

        存放的桶名称。

        :return: The bucket_name of this AuthorizeObsResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this AuthorizeObsResponse.

        存放的桶名称。

        :param bucket_name: The bucket_name of this AuthorizeObsResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def directory(self):
        """Gets the directory of this AuthorizeObsResponse.

        存放目录。

        :return: The directory of this AuthorizeObsResponse.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this AuthorizeObsResponse.

        存放目录。

        :param directory: The directory of this AuthorizeObsResponse.
        :type directory: str
        """
        self._directory = directory

    @property
    def ak(self):
        """Gets the ak of this AuthorizeObsResponse.

        获取的AK。。

        :return: The ak of this AuthorizeObsResponse.
        :rtype: str
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the ak of this AuthorizeObsResponse.

        获取的AK。。

        :param ak: The ak of this AuthorizeObsResponse.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the sk of this AuthorizeObsResponse.

        获取的SK。

        :return: The sk of this AuthorizeObsResponse.
        :rtype: str
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the sk of this AuthorizeObsResponse.

        获取的SK。

        :param sk: The sk of this AuthorizeObsResponse.
        :type sk: str
        """
        self._sk = sk

    @property
    def expires_at(self):
        """Gets the expires_at of this AuthorizeObsResponse.

        AK/SK和securitytoken的过期时间。。

        :return: The expires_at of this AuthorizeObsResponse.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this AuthorizeObsResponse.

        AK/SK和securitytoken的过期时间。。

        :param expires_at: The expires_at of this AuthorizeObsResponse.
        :type expires_at: str
        """
        self._expires_at = expires_at

    @property
    def policy(self):
        """Gets the policy of this AuthorizeObsResponse.

        :return: The policy of this AuthorizeObsResponse.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Policy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this AuthorizeObsResponse.

        :param policy: The policy of this AuthorizeObsResponse.
        :type policy: :class:`huaweicloudsdkworkspaceapp.v1.Policy`
        """
        self._policy = policy

    @property
    def security_token(self):
        """Gets the security_token of this AuthorizeObsResponse.

        安全校验token，将所获的AK、SK等信息进行加密后的字符串。

        :return: The security_token of this AuthorizeObsResponse.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        """Sets the security_token of this AuthorizeObsResponse.

        安全校验token，将所获的AK、SK等信息进行加密后的字符串。

        :param security_token: The security_token of this AuthorizeObsResponse.
        :type security_token: str
        """
        self._security_token = security_token

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
        if not isinstance(other, AuthorizeObsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
