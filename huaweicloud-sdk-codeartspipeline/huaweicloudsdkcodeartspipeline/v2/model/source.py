# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Source:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'codehub_name': 'str',
        'branches': 'list[str]',
        'scm_type': 'str',
        'hook_flag': 'bool',
        'branch': 'str',
        'git_url': 'str',
        'codehub_id': 'str',
        'web_url': 'str',
        'branch_list': 'list[str]',
        'init_id': 'str',
        'disable': 'bool'
    }

    attribute_map = {
        'codehub_name': 'codehub_name',
        'branches': 'branches',
        'scm_type': 'scm_type',
        'hook_flag': 'hook_flag',
        'branch': 'branch',
        'git_url': 'git_url',
        'codehub_id': 'codehub_id',
        'web_url': 'web_url',
        'branch_list': 'branch_list',
        'init_id': 'init_id',
        'disable': 'disable'
    }

    def __init__(self, codehub_name=None, branches=None, scm_type=None, hook_flag=None, branch=None, git_url=None, codehub_id=None, web_url=None, branch_list=None, init_id=None, disable=None):
        r"""Source

        The model defined in huaweicloud sdk

        :param codehub_name: 源码仓名字
        :type codehub_name: str
        :param branches: 触发分支
        :type branches: list[str]
        :param scm_type: 源码仓来源
        :type scm_type: str
        :param hook_flag: 是否开启触发执行流水线功能
        :type hook_flag: bool
        :param branch: 触发分支
        :type branch: str
        :param git_url: 源码仓ssh地址
        :type git_url: str
        :param codehub_id: 源码仓ID
        :type codehub_id: str
        :param web_url: 源码仓首页url
        :type web_url: str
        :param branch_list: 分支列表
        :type branch_list: list[str]
        :param init_id: 初始化ID
        :type init_id: str
        :param disable: 是否废弃
        :type disable: bool
        """
        
        

        self._codehub_name = None
        self._branches = None
        self._scm_type = None
        self._hook_flag = None
        self._branch = None
        self._git_url = None
        self._codehub_id = None
        self._web_url = None
        self._branch_list = None
        self._init_id = None
        self._disable = None
        self.discriminator = None

        self.codehub_name = codehub_name
        self.branches = branches
        self.scm_type = scm_type
        self.hook_flag = hook_flag
        self.branch = branch
        self.git_url = git_url
        self.codehub_id = codehub_id
        self.web_url = web_url
        self.branch_list = branch_list
        self.init_id = init_id
        self.disable = disable

    @property
    def codehub_name(self):
        r"""Gets the codehub_name of this Source.

        源码仓名字

        :return: The codehub_name of this Source.
        :rtype: str
        """
        return self._codehub_name

    @codehub_name.setter
    def codehub_name(self, codehub_name):
        r"""Sets the codehub_name of this Source.

        源码仓名字

        :param codehub_name: The codehub_name of this Source.
        :type codehub_name: str
        """
        self._codehub_name = codehub_name

    @property
    def branches(self):
        r"""Gets the branches of this Source.

        触发分支

        :return: The branches of this Source.
        :rtype: list[str]
        """
        return self._branches

    @branches.setter
    def branches(self, branches):
        r"""Sets the branches of this Source.

        触发分支

        :param branches: The branches of this Source.
        :type branches: list[str]
        """
        self._branches = branches

    @property
    def scm_type(self):
        r"""Gets the scm_type of this Source.

        源码仓来源

        :return: The scm_type of this Source.
        :rtype: str
        """
        return self._scm_type

    @scm_type.setter
    def scm_type(self, scm_type):
        r"""Sets the scm_type of this Source.

        源码仓来源

        :param scm_type: The scm_type of this Source.
        :type scm_type: str
        """
        self._scm_type = scm_type

    @property
    def hook_flag(self):
        r"""Gets the hook_flag of this Source.

        是否开启触发执行流水线功能

        :return: The hook_flag of this Source.
        :rtype: bool
        """
        return self._hook_flag

    @hook_flag.setter
    def hook_flag(self, hook_flag):
        r"""Sets the hook_flag of this Source.

        是否开启触发执行流水线功能

        :param hook_flag: The hook_flag of this Source.
        :type hook_flag: bool
        """
        self._hook_flag = hook_flag

    @property
    def branch(self):
        r"""Gets the branch of this Source.

        触发分支

        :return: The branch of this Source.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this Source.

        触发分支

        :param branch: The branch of this Source.
        :type branch: str
        """
        self._branch = branch

    @property
    def git_url(self):
        r"""Gets the git_url of this Source.

        源码仓ssh地址

        :return: The git_url of this Source.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this Source.

        源码仓ssh地址

        :param git_url: The git_url of this Source.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def codehub_id(self):
        r"""Gets the codehub_id of this Source.

        源码仓ID

        :return: The codehub_id of this Source.
        :rtype: str
        """
        return self._codehub_id

    @codehub_id.setter
    def codehub_id(self, codehub_id):
        r"""Sets the codehub_id of this Source.

        源码仓ID

        :param codehub_id: The codehub_id of this Source.
        :type codehub_id: str
        """
        self._codehub_id = codehub_id

    @property
    def web_url(self):
        r"""Gets the web_url of this Source.

        源码仓首页url

        :return: The web_url of this Source.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this Source.

        源码仓首页url

        :param web_url: The web_url of this Source.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def branch_list(self):
        r"""Gets the branch_list of this Source.

        分支列表

        :return: The branch_list of this Source.
        :rtype: list[str]
        """
        return self._branch_list

    @branch_list.setter
    def branch_list(self, branch_list):
        r"""Sets the branch_list of this Source.

        分支列表

        :param branch_list: The branch_list of this Source.
        :type branch_list: list[str]
        """
        self._branch_list = branch_list

    @property
    def init_id(self):
        r"""Gets the init_id of this Source.

        初始化ID

        :return: The init_id of this Source.
        :rtype: str
        """
        return self._init_id

    @init_id.setter
    def init_id(self, init_id):
        r"""Sets the init_id of this Source.

        初始化ID

        :param init_id: The init_id of this Source.
        :type init_id: str
        """
        self._init_id = init_id

    @property
    def disable(self):
        r"""Gets the disable of this Source.

        是否废弃

        :return: The disable of this Source.
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        r"""Sets the disable of this Source.

        是否废弃

        :param disable: The disable of this Source.
        :type disable: bool
        """
        self._disable = disable

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
        if not isinstance(other, Source):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
