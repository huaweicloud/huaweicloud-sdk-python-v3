# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunPipelineDTOParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'git_type': 'str',
        'alias': 'str',
        'codehub_id': 'str',
        'default_branch': 'str',
        'git_url': 'str',
        'endpoint_id': 'str',
        'build_params': 'RunPipelineDTOParamsBuildParams'
    }

    attribute_map = {
        'git_type': 'git_type',
        'alias': 'alias',
        'codehub_id': 'codehub_id',
        'default_branch': 'default_branch',
        'git_url': 'git_url',
        'endpoint_id': 'endpoint_id',
        'build_params': 'build_params'
    }

    def __init__(self, git_type=None, alias=None, codehub_id=None, default_branch=None, git_url=None, endpoint_id=None, build_params=None):
        r"""RunPipelineDTOParams

        The model defined in huaweicloud sdk

        :param git_type: 代码仓类型
        :type git_type: str
        :param alias: 代码仓别名
        :type alias: str
        :param codehub_id: codehub代码库ID
        :type codehub_id: str
        :param default_branch: 默认分支
        :type default_branch: str
        :param git_url: git仓库https地址
        :type git_url: str
        :param endpoint_id: 扩展点ID
        :type endpoint_id: str
        :param build_params: 
        :type build_params: :class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOParamsBuildParams`
        """
        
        

        self._git_type = None
        self._alias = None
        self._codehub_id = None
        self._default_branch = None
        self._git_url = None
        self._endpoint_id = None
        self._build_params = None
        self.discriminator = None

        self.git_type = git_type
        if alias is not None:
            self.alias = alias
        if codehub_id is not None:
            self.codehub_id = codehub_id
        if default_branch is not None:
            self.default_branch = default_branch
        self.git_url = git_url
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if build_params is not None:
            self.build_params = build_params

    @property
    def git_type(self):
        r"""Gets the git_type of this RunPipelineDTOParams.

        代码仓类型

        :return: The git_type of this RunPipelineDTOParams.
        :rtype: str
        """
        return self._git_type

    @git_type.setter
    def git_type(self, git_type):
        r"""Sets the git_type of this RunPipelineDTOParams.

        代码仓类型

        :param git_type: The git_type of this RunPipelineDTOParams.
        :type git_type: str
        """
        self._git_type = git_type

    @property
    def alias(self):
        r"""Gets the alias of this RunPipelineDTOParams.

        代码仓别名

        :return: The alias of this RunPipelineDTOParams.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this RunPipelineDTOParams.

        代码仓别名

        :param alias: The alias of this RunPipelineDTOParams.
        :type alias: str
        """
        self._alias = alias

    @property
    def codehub_id(self):
        r"""Gets the codehub_id of this RunPipelineDTOParams.

        codehub代码库ID

        :return: The codehub_id of this RunPipelineDTOParams.
        :rtype: str
        """
        return self._codehub_id

    @codehub_id.setter
    def codehub_id(self, codehub_id):
        r"""Sets the codehub_id of this RunPipelineDTOParams.

        codehub代码库ID

        :param codehub_id: The codehub_id of this RunPipelineDTOParams.
        :type codehub_id: str
        """
        self._codehub_id = codehub_id

    @property
    def default_branch(self):
        r"""Gets the default_branch of this RunPipelineDTOParams.

        默认分支

        :return: The default_branch of this RunPipelineDTOParams.
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        r"""Sets the default_branch of this RunPipelineDTOParams.

        默认分支

        :param default_branch: The default_branch of this RunPipelineDTOParams.
        :type default_branch: str
        """
        self._default_branch = default_branch

    @property
    def git_url(self):
        r"""Gets the git_url of this RunPipelineDTOParams.

        git仓库https地址

        :return: The git_url of this RunPipelineDTOParams.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this RunPipelineDTOParams.

        git仓库https地址

        :param git_url: The git_url of this RunPipelineDTOParams.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this RunPipelineDTOParams.

        扩展点ID

        :return: The endpoint_id of this RunPipelineDTOParams.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this RunPipelineDTOParams.

        扩展点ID

        :param endpoint_id: The endpoint_id of this RunPipelineDTOParams.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def build_params(self):
        r"""Gets the build_params of this RunPipelineDTOParams.

        :return: The build_params of this RunPipelineDTOParams.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOParamsBuildParams`
        """
        return self._build_params

    @build_params.setter
    def build_params(self, build_params):
        r"""Sets the build_params of this RunPipelineDTOParams.

        :param build_params: The build_params of this RunPipelineDTOParams.
        :type build_params: :class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineDTOParamsBuildParams`
        """
        self._build_params = build_params

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
        if not isinstance(other, RunPipelineDTOParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
