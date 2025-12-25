# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAttentionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'domain_id': 'str',
        'repository_id': 'str',
        'repository_name': 'str',
        'format': 'str',
        'policy': 'str',
        'artifact_id': 'str',
        'path': 'str',
        'modified_user_name': 'str',
        'modified_user_id': 'str',
        'user_id': 'str',
        'modified_time': 'str',
        'region': 'str'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domainId',
        'repository_id': 'repositoryId',
        'repository_name': 'repositoryName',
        'format': 'format',
        'policy': 'policy',
        'artifact_id': 'artifactId',
        'path': 'path',
        'modified_user_name': 'modifiedUserName',
        'modified_user_id': 'modifiedUserId',
        'user_id': 'userId',
        'modified_time': 'modifiedTime',
        'region': 'region'
    }

    def __init__(self, id=None, domain_id=None, repository_id=None, repository_name=None, format=None, policy=None, artifact_id=None, path=None, modified_user_name=None, modified_user_id=None, user_id=None, modified_time=None, region=None):
        r"""ListAttentionResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 序号。 **取值范围**： 不涉及。 
        :type id: str
        :param domain_id: **参数解释**： 租户ID。 **取值范围**： 不涉及。 
        :type domain_id: str
        :param repository_id: **参数解释**： 仓库ID。 **取值范围**： 不涉及。 
        :type repository_id: str
        :param repository_name: **参数解释**： 仓库名称。 **取值范围**： 不涉及。 
        :type repository_name: str
        :param format: **参数解释**： 制品类型。 **取值范围**： maven2|docker|npm|go|pypi|rpm|composer|debian|conan|nuget|docker2|cocoapods|ohpm|generic。 
        :type format: str
        :param policy: **参数解释**： 仓库策略。 **取值范围**： - release：正式仓库。 - snapshot：快照仓库。 
        :type policy: str
        :param artifact_id: **参数解释**： 关注的组件序号。 **取值范围**： 不涉及。 
        :type artifact_id: str
        :param path: **参数解释**： 关注的组件路径。 **取值范围**： 不涉及。 
        :type path: str
        :param modified_user_name: **参数解释**： 修改人名称。 **取值范围**： 不涉及。 
        :type modified_user_name: str
        :param modified_user_id: **参数解释**： 修改人ID。 **取值范围**： 不涉及。 
        :type modified_user_id: str
        :param user_id: **参数解释**： 用户id。 **取值范围**： 只能由英文字母、数字组成，且长度为32个字符。 
        :type user_id: str
        :param modified_time: **参数解释**： 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。 
        :type modified_time: str
        :param region: **参数解释**： 区域。 **取值范围**： 不涉及。 
        :type region: str
        """
        
        

        self._id = None
        self._domain_id = None
        self._repository_id = None
        self._repository_name = None
        self._format = None
        self._policy = None
        self._artifact_id = None
        self._path = None
        self._modified_user_name = None
        self._modified_user_id = None
        self._user_id = None
        self._modified_time = None
        self._region = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if repository_id is not None:
            self.repository_id = repository_id
        if repository_name is not None:
            self.repository_name = repository_name
        if format is not None:
            self.format = format
        if policy is not None:
            self.policy = policy
        if artifact_id is not None:
            self.artifact_id = artifact_id
        if path is not None:
            self.path = path
        if modified_user_name is not None:
            self.modified_user_name = modified_user_name
        if modified_user_id is not None:
            self.modified_user_id = modified_user_id
        if user_id is not None:
            self.user_id = user_id
        if modified_time is not None:
            self.modified_time = modified_time
        if region is not None:
            self.region = region

    @property
    def id(self):
        r"""Gets the id of this ListAttentionResult.

        **参数解释**： 序号。 **取值范围**： 不涉及。 

        :return: The id of this ListAttentionResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAttentionResult.

        **参数解释**： 序号。 **取值范围**： 不涉及。 

        :param id: The id of this ListAttentionResult.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListAttentionResult.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。 

        :return: The domain_id of this ListAttentionResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListAttentionResult.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。 

        :param domain_id: The domain_id of this ListAttentionResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListAttentionResult.

        **参数解释**： 仓库ID。 **取值范围**： 不涉及。 

        :return: The repository_id of this ListAttentionResult.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListAttentionResult.

        **参数解释**： 仓库ID。 **取值范围**： 不涉及。 

        :param repository_id: The repository_id of this ListAttentionResult.
        :type repository_id: str
        """
        self._repository_id = repository_id

    @property
    def repository_name(self):
        r"""Gets the repository_name of this ListAttentionResult.

        **参数解释**： 仓库名称。 **取值范围**： 不涉及。 

        :return: The repository_name of this ListAttentionResult.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this ListAttentionResult.

        **参数解释**： 仓库名称。 **取值范围**： 不涉及。 

        :param repository_name: The repository_name of this ListAttentionResult.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def format(self):
        r"""Gets the format of this ListAttentionResult.

        **参数解释**： 制品类型。 **取值范围**： maven2|docker|npm|go|pypi|rpm|composer|debian|conan|nuget|docker2|cocoapods|ohpm|generic。 

        :return: The format of this ListAttentionResult.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ListAttentionResult.

        **参数解释**： 制品类型。 **取值范围**： maven2|docker|npm|go|pypi|rpm|composer|debian|conan|nuget|docker2|cocoapods|ohpm|generic。 

        :param format: The format of this ListAttentionResult.
        :type format: str
        """
        self._format = format

    @property
    def policy(self):
        r"""Gets the policy of this ListAttentionResult.

        **参数解释**： 仓库策略。 **取值范围**： - release：正式仓库。 - snapshot：快照仓库。 

        :return: The policy of this ListAttentionResult.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ListAttentionResult.

        **参数解释**： 仓库策略。 **取值范围**： - release：正式仓库。 - snapshot：快照仓库。 

        :param policy: The policy of this ListAttentionResult.
        :type policy: str
        """
        self._policy = policy

    @property
    def artifact_id(self):
        r"""Gets the artifact_id of this ListAttentionResult.

        **参数解释**： 关注的组件序号。 **取值范围**： 不涉及。 

        :return: The artifact_id of this ListAttentionResult.
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        r"""Sets the artifact_id of this ListAttentionResult.

        **参数解释**： 关注的组件序号。 **取值范围**： 不涉及。 

        :param artifact_id: The artifact_id of this ListAttentionResult.
        :type artifact_id: str
        """
        self._artifact_id = artifact_id

    @property
    def path(self):
        r"""Gets the path of this ListAttentionResult.

        **参数解释**： 关注的组件路径。 **取值范围**： 不涉及。 

        :return: The path of this ListAttentionResult.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ListAttentionResult.

        **参数解释**： 关注的组件路径。 **取值范围**： 不涉及。 

        :param path: The path of this ListAttentionResult.
        :type path: str
        """
        self._path = path

    @property
    def modified_user_name(self):
        r"""Gets the modified_user_name of this ListAttentionResult.

        **参数解释**： 修改人名称。 **取值范围**： 不涉及。 

        :return: The modified_user_name of this ListAttentionResult.
        :rtype: str
        """
        return self._modified_user_name

    @modified_user_name.setter
    def modified_user_name(self, modified_user_name):
        r"""Sets the modified_user_name of this ListAttentionResult.

        **参数解释**： 修改人名称。 **取值范围**： 不涉及。 

        :param modified_user_name: The modified_user_name of this ListAttentionResult.
        :type modified_user_name: str
        """
        self._modified_user_name = modified_user_name

    @property
    def modified_user_id(self):
        r"""Gets the modified_user_id of this ListAttentionResult.

        **参数解释**： 修改人ID。 **取值范围**： 不涉及。 

        :return: The modified_user_id of this ListAttentionResult.
        :rtype: str
        """
        return self._modified_user_id

    @modified_user_id.setter
    def modified_user_id(self, modified_user_id):
        r"""Sets the modified_user_id of this ListAttentionResult.

        **参数解释**： 修改人ID。 **取值范围**： 不涉及。 

        :param modified_user_id: The modified_user_id of this ListAttentionResult.
        :type modified_user_id: str
        """
        self._modified_user_id = modified_user_id

    @property
    def user_id(self):
        r"""Gets the user_id of this ListAttentionResult.

        **参数解释**： 用户id。 **取值范围**： 只能由英文字母、数字组成，且长度为32个字符。 

        :return: The user_id of this ListAttentionResult.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ListAttentionResult.

        **参数解释**： 用户id。 **取值范围**： 只能由英文字母、数字组成，且长度为32个字符。 

        :param user_id: The user_id of this ListAttentionResult.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def modified_time(self):
        r"""Gets the modified_time of this ListAttentionResult.

        **参数解释**： 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。 

        :return: The modified_time of this ListAttentionResult.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this ListAttentionResult.

        **参数解释**： 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。 

        :param modified_time: The modified_time of this ListAttentionResult.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def region(self):
        r"""Gets the region of this ListAttentionResult.

        **参数解释**： 区域。 **取值范围**： 不涉及。 

        :return: The region of this ListAttentionResult.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListAttentionResult.

        **参数解释**： 区域。 **取值范围**： 不涉及。 

        :param region: The region of this ListAttentionResult.
        :type region: str
        """
        self._region = region

    def to_dict(self):
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
        if not isinstance(other, ListAttentionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
