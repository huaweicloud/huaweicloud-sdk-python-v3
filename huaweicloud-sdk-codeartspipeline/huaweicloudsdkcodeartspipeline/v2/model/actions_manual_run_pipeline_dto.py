# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionsManualRunPipelineDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'https_url': 'str',
        'file_path': 'str',
        'file_content': 'str',
        'branch': 'str',
        'encoding': 'str',
        'tag': 'str',
        'commit_id': 'str',
        'access_token': 'str'
    }

    attribute_map = {
        'https_url': 'https_url',
        'file_path': 'file_path',
        'file_content': 'file_content',
        'branch': 'branch',
        'encoding': 'encoding',
        'tag': 'tag',
        'commit_id': 'commit_id',
        'access_token': 'access_token'
    }

    def __init__(self, https_url=None, file_path=None, file_content=None, branch=None, encoding=None, tag=None, commit_id=None, access_token=None):
        r"""ActionsManualRunPipelineDTO

        The model defined in huaweicloud sdk

        :param https_url: **参数解释**： 触发URL。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type https_url: str
        :param file_path: **参数解释**： 文件存储路径。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type file_path: str
        :param file_content: **参数解释**： 文件详情。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type file_content: str
        :param branch: **参数解释**： 代码源分支名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type branch: str
        :param encoding: **参数解释**： 文件编码方式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type encoding: str
        :param tag: **参数解释**： 代码源标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type tag: str
        :param commit_id: **参数解释**： 代码源提交记录id。 **约束限制**： 不涉及。 **取值范围**： 40位字符。 **默认取值**： 不涉及。 
        :type commit_id: str
        :param access_token: **参数解释**： 代码源访问权限token。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type access_token: str
        """
        
        

        self._https_url = None
        self._file_path = None
        self._file_content = None
        self._branch = None
        self._encoding = None
        self._tag = None
        self._commit_id = None
        self._access_token = None
        self.discriminator = None

        if https_url is not None:
            self.https_url = https_url
        if file_path is not None:
            self.file_path = file_path
        if file_content is not None:
            self.file_content = file_content
        if branch is not None:
            self.branch = branch
        if encoding is not None:
            self.encoding = encoding
        if tag is not None:
            self.tag = tag
        if commit_id is not None:
            self.commit_id = commit_id
        if access_token is not None:
            self.access_token = access_token

    @property
    def https_url(self):
        r"""Gets the https_url of this ActionsManualRunPipelineDTO.

        **参数解释**： 触发URL。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The https_url of this ActionsManualRunPipelineDTO.
        :rtype: str
        """
        return self._https_url

    @https_url.setter
    def https_url(self, https_url):
        r"""Sets the https_url of this ActionsManualRunPipelineDTO.

        **参数解释**： 触发URL。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param https_url: The https_url of this ActionsManualRunPipelineDTO.
        :type https_url: str
        """
        self._https_url = https_url

    @property
    def file_path(self):
        r"""Gets the file_path of this ActionsManualRunPipelineDTO.

        **参数解释**： 文件存储路径。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The file_path of this ActionsManualRunPipelineDTO.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ActionsManualRunPipelineDTO.

        **参数解释**： 文件存储路径。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param file_path: The file_path of this ActionsManualRunPipelineDTO.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_content(self):
        r"""Gets the file_content of this ActionsManualRunPipelineDTO.

        **参数解释**： 文件详情。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The file_content of this ActionsManualRunPipelineDTO.
        :rtype: str
        """
        return self._file_content

    @file_content.setter
    def file_content(self, file_content):
        r"""Sets the file_content of this ActionsManualRunPipelineDTO.

        **参数解释**： 文件详情。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param file_content: The file_content of this ActionsManualRunPipelineDTO.
        :type file_content: str
        """
        self._file_content = file_content

    @property
    def branch(self):
        r"""Gets the branch of this ActionsManualRunPipelineDTO.

        **参数解释**： 代码源分支名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The branch of this ActionsManualRunPipelineDTO.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this ActionsManualRunPipelineDTO.

        **参数解释**： 代码源分支名。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param branch: The branch of this ActionsManualRunPipelineDTO.
        :type branch: str
        """
        self._branch = branch

    @property
    def encoding(self):
        r"""Gets the encoding of this ActionsManualRunPipelineDTO.

        **参数解释**： 文件编码方式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The encoding of this ActionsManualRunPipelineDTO.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        r"""Sets the encoding of this ActionsManualRunPipelineDTO.

        **参数解释**： 文件编码方式。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param encoding: The encoding of this ActionsManualRunPipelineDTO.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def tag(self):
        r"""Gets the tag of this ActionsManualRunPipelineDTO.

        **参数解释**： 代码源标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The tag of this ActionsManualRunPipelineDTO.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ActionsManualRunPipelineDTO.

        **参数解释**： 代码源标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param tag: The tag of this ActionsManualRunPipelineDTO.
        :type tag: str
        """
        self._tag = tag

    @property
    def commit_id(self):
        r"""Gets the commit_id of this ActionsManualRunPipelineDTO.

        **参数解释**： 代码源提交记录id。 **约束限制**： 不涉及。 **取值范围**： 40位字符。 **默认取值**： 不涉及。 

        :return: The commit_id of this ActionsManualRunPipelineDTO.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this ActionsManualRunPipelineDTO.

        **参数解释**： 代码源提交记录id。 **约束限制**： 不涉及。 **取值范围**： 40位字符。 **默认取值**： 不涉及。 

        :param commit_id: The commit_id of this ActionsManualRunPipelineDTO.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def access_token(self):
        r"""Gets the access_token of this ActionsManualRunPipelineDTO.

        **参数解释**： 代码源访问权限token。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The access_token of this ActionsManualRunPipelineDTO.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        r"""Sets the access_token of this ActionsManualRunPipelineDTO.

        **参数解释**： 代码源访问权限token。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param access_token: The access_token of this ActionsManualRunPipelineDTO.
        :type access_token: str
        """
        self._access_token = access_token

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
        if not isinstance(other, ActionsManualRunPipelineDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
