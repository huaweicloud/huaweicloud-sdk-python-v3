# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizationVO:

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
        'repo_type': 'str',
        'repo_host': 'str',
        'repo_home': 'str',
        'repo_user': 'str',
        'avartar': 'str',
        'token_type': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'status': 'int',
        'tag': 'str'
    }

    attribute_map = {
        'name': 'name',
        'repo_type': 'repo_type',
        'repo_host': 'repo_host',
        'repo_home': 'repo_home',
        'repo_user': 'repo_user',
        'avartar': 'avartar',
        'token_type': 'token_type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'status': 'status',
        'tag': 'tag'
    }

    def __init__(self, name=None, repo_type=None, repo_host=None, repo_home=None, repo_user=None, avartar=None, token_type=None, create_time=None, update_time=None, status=None, tag=None):
        r"""AuthorizationVO

        The model defined in huaweicloud sdk

        :param name: 授权名称。
        :type name: str
        :param repo_type: 仓库类型。 取值范围：github、gitlab、gitee、bitbucket、devcloud。 
        :type repo_type: str
        :param repo_host: 仓库地址。
        :type repo_host: str
        :param repo_home: 仓库主页。
        :type repo_home: str
        :param repo_user: 仓库用户名。
        :type repo_user: str
        :param avartar: 头像。
        :type avartar: str
        :param token_type: 授权方式。
        :type token_type: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 修改时间。
        :type update_time: int
        :param status: 状态。
        :type status: int
        :param tag: 授权局点的类型，默认为null。
        :type tag: str
        """
        
        

        self._name = None
        self._repo_type = None
        self._repo_host = None
        self._repo_home = None
        self._repo_user = None
        self._avartar = None
        self._token_type = None
        self._create_time = None
        self._update_time = None
        self._status = None
        self._tag = None
        self.discriminator = None

        self.name = name
        self.repo_type = repo_type
        self.repo_host = repo_host
        self.repo_home = repo_home
        self.repo_user = repo_user
        self.avartar = avartar
        self.token_type = token_type
        self.create_time = create_time
        self.update_time = update_time
        self.status = status
        self.tag = tag

    @property
    def name(self):
        r"""Gets the name of this AuthorizationVO.

        授权名称。

        :return: The name of this AuthorizationVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AuthorizationVO.

        授权名称。

        :param name: The name of this AuthorizationVO.
        :type name: str
        """
        self._name = name

    @property
    def repo_type(self):
        r"""Gets the repo_type of this AuthorizationVO.

        仓库类型。 取值范围：github、gitlab、gitee、bitbucket、devcloud。 

        :return: The repo_type of this AuthorizationVO.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        r"""Sets the repo_type of this AuthorizationVO.

        仓库类型。 取值范围：github、gitlab、gitee、bitbucket、devcloud。 

        :param repo_type: The repo_type of this AuthorizationVO.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def repo_host(self):
        r"""Gets the repo_host of this AuthorizationVO.

        仓库地址。

        :return: The repo_host of this AuthorizationVO.
        :rtype: str
        """
        return self._repo_host

    @repo_host.setter
    def repo_host(self, repo_host):
        r"""Sets the repo_host of this AuthorizationVO.

        仓库地址。

        :param repo_host: The repo_host of this AuthorizationVO.
        :type repo_host: str
        """
        self._repo_host = repo_host

    @property
    def repo_home(self):
        r"""Gets the repo_home of this AuthorizationVO.

        仓库主页。

        :return: The repo_home of this AuthorizationVO.
        :rtype: str
        """
        return self._repo_home

    @repo_home.setter
    def repo_home(self, repo_home):
        r"""Sets the repo_home of this AuthorizationVO.

        仓库主页。

        :param repo_home: The repo_home of this AuthorizationVO.
        :type repo_home: str
        """
        self._repo_home = repo_home

    @property
    def repo_user(self):
        r"""Gets the repo_user of this AuthorizationVO.

        仓库用户名。

        :return: The repo_user of this AuthorizationVO.
        :rtype: str
        """
        return self._repo_user

    @repo_user.setter
    def repo_user(self, repo_user):
        r"""Sets the repo_user of this AuthorizationVO.

        仓库用户名。

        :param repo_user: The repo_user of this AuthorizationVO.
        :type repo_user: str
        """
        self._repo_user = repo_user

    @property
    def avartar(self):
        r"""Gets the avartar of this AuthorizationVO.

        头像。

        :return: The avartar of this AuthorizationVO.
        :rtype: str
        """
        return self._avartar

    @avartar.setter
    def avartar(self, avartar):
        r"""Sets the avartar of this AuthorizationVO.

        头像。

        :param avartar: The avartar of this AuthorizationVO.
        :type avartar: str
        """
        self._avartar = avartar

    @property
    def token_type(self):
        r"""Gets the token_type of this AuthorizationVO.

        授权方式。

        :return: The token_type of this AuthorizationVO.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        r"""Sets the token_type of this AuthorizationVO.

        授权方式。

        :param token_type: The token_type of this AuthorizationVO.
        :type token_type: str
        """
        self._token_type = token_type

    @property
    def create_time(self):
        r"""Gets the create_time of this AuthorizationVO.

        创建时间。

        :return: The create_time of this AuthorizationVO.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AuthorizationVO.

        创建时间。

        :param create_time: The create_time of this AuthorizationVO.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AuthorizationVO.

        修改时间。

        :return: The update_time of this AuthorizationVO.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AuthorizationVO.

        修改时间。

        :param update_time: The update_time of this AuthorizationVO.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def status(self):
        r"""Gets the status of this AuthorizationVO.

        状态。

        :return: The status of this AuthorizationVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AuthorizationVO.

        状态。

        :param status: The status of this AuthorizationVO.
        :type status: int
        """
        self._status = status

    @property
    def tag(self):
        r"""Gets the tag of this AuthorizationVO.

        授权局点的类型，默认为null。

        :return: The tag of this AuthorizationVO.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this AuthorizationVO.

        授权局点的类型，默认为null。

        :param tag: The tag of this AuthorizationVO.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, AuthorizationVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
