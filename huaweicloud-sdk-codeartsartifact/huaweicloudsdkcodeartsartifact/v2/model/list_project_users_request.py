# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectUsersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'repo_id': 'str',
        'scene': 'str',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'repo_id': 'repo_id',
        'scene': 'scene',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, project_id=None, repo_id=None, scene=None, page_no=None, page_size=None):
        r"""ListProjectUsersRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type project_id: str
        :param repo_id: **参数解释**: 仓库id。可在私有库仓库**概览**界面查看。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type repo_id: str
        :param scene: **参数解释**: scene。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type scene: str
        :param page_no: **参数解释**: 分页查询的页数。 **约束限制**: 不涉及。 **取值范围**: 最小值1，最大值2147483647。 **默认取值**: 1
        :type page_no: int
        :param page_size: **参数解释**: 分页查询的每页数据量。 **约束限制**: 不涉及。 **取值范围**: 最小值1，最大值100。 **默认取值**: 10
        :type page_size: int
        """
        
        

        self._project_id = None
        self._repo_id = None
        self._scene = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        self.project_id = project_id
        self.repo_id = repo_id
        if scene is not None:
            self.scene = scene
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def project_id(self):
        r"""Gets the project_id of this ListProjectUsersRequest.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The project_id of this ListProjectUsersRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListProjectUsersRequest.

        **参数解释**: 项目ID，可以从调用API处获取，也可以从控制台获取。获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**: 只能由英文字母、数字组成，且长度为32个字符。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param project_id: The project_id of this ListProjectUsersRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def repo_id(self):
        r"""Gets the repo_id of this ListProjectUsersRequest.

        **参数解释**: 仓库id。可在私有库仓库**概览**界面查看。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The repo_id of this ListProjectUsersRequest.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this ListProjectUsersRequest.

        **参数解释**: 仓库id。可在私有库仓库**概览**界面查看。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param repo_id: The repo_id of this ListProjectUsersRequest.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def scene(self):
        r"""Gets the scene of this ListProjectUsersRequest.

        **参数解释**: scene。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The scene of this ListProjectUsersRequest.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ListProjectUsersRequest.

        **参数解释**: scene。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param scene: The scene of this ListProjectUsersRequest.
        :type scene: str
        """
        self._scene = scene

    @property
    def page_no(self):
        r"""Gets the page_no of this ListProjectUsersRequest.

        **参数解释**: 分页查询的页数。 **约束限制**: 不涉及。 **取值范围**: 最小值1，最大值2147483647。 **默认取值**: 1

        :return: The page_no of this ListProjectUsersRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListProjectUsersRequest.

        **参数解释**: 分页查询的页数。 **约束限制**: 不涉及。 **取值范围**: 最小值1，最大值2147483647。 **默认取值**: 1

        :param page_no: The page_no of this ListProjectUsersRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListProjectUsersRequest.

        **参数解释**: 分页查询的每页数据量。 **约束限制**: 不涉及。 **取值范围**: 最小值1，最大值100。 **默认取值**: 10

        :return: The page_size of this ListProjectUsersRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListProjectUsersRequest.

        **参数解释**: 分页查询的每页数据量。 **约束限制**: 不涉及。 **取值范围**: 最小值1，最大值100。 **默认取值**: 10

        :param page_size: The page_size of this ListProjectUsersRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ListProjectUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
