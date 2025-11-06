# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqSettingDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active': 'bool',
        'branches': 'str',
        'branches_type': 'str',
        'project_type': 'str',
        'categories': 'str',
        'category_codes': 'str',
        'exclude_statuses': 'str',
        'exclude_status_codes': 'str'
    }

    attribute_map = {
        'active': 'active',
        'branches': 'branches',
        'branches_type': 'branches_type',
        'project_type': 'project_type',
        'categories': 'categories',
        'category_codes': 'category_codes',
        'exclude_statuses': 'exclude_statuses',
        'exclude_status_codes': 'exclude_status_codes'
    }

    def __init__(self, active=None, branches=None, branches_type=None, project_type=None, categories=None, category_codes=None, exclude_statuses=None, exclude_status_codes=None):
        r"""ReqSettingDto

        The model defined in huaweicloud sdk

        :param active: **参数解释：** 是否开启集成CodeArts Req **取值范围：** true：开启集成CodeArts Req，false：未开启集成CodeArts Req。
        :type active: bool
        :param branches: **参数解释：** 应用排除状态和可关联类别限制的分支列表，该分支指代合并请求的目标分支，可支持多个分支用英文逗号拼接或者正则表达式，在项目层级和代码组层级只支持配置正则表达式。
        :type branches: str
        :param branches_type: **参数解释：** 分支的类型，文本或者正则表达式。 **取值范围：** plain代表文本，regex代表正则表达式。
        :type branches_type: str
        :param project_type: **参数解释：** 关联的CodeArts Req项目类型。 **取值范围：** scrum代表scrum类型项目，ipd代表IPD类型项目, xboard为看板类型项目。
        :type project_type: str
        :param categories: **参数解释：** 可关联类型列表，逗号分隔。
        :type categories: str
        :param category_codes: **参数解释：** 可关联类型编码列表，逗号分隔。
        :type category_codes: str
        :param exclude_statuses: **参数解释：** 排除状态列表，逗号分隔。
        :type exclude_statuses: str
        :param exclude_status_codes: **参数解释：** 排除状态编码列表，逗号分隔。
        :type exclude_status_codes: str
        """
        
        

        self._active = None
        self._branches = None
        self._branches_type = None
        self._project_type = None
        self._categories = None
        self._category_codes = None
        self._exclude_statuses = None
        self._exclude_status_codes = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if branches is not None:
            self.branches = branches
        if branches_type is not None:
            self.branches_type = branches_type
        if project_type is not None:
            self.project_type = project_type
        if categories is not None:
            self.categories = categories
        if category_codes is not None:
            self.category_codes = category_codes
        if exclude_statuses is not None:
            self.exclude_statuses = exclude_statuses
        if exclude_status_codes is not None:
            self.exclude_status_codes = exclude_status_codes

    @property
    def active(self):
        r"""Gets the active of this ReqSettingDto.

        **参数解释：** 是否开启集成CodeArts Req **取值范围：** true：开启集成CodeArts Req，false：未开启集成CodeArts Req。

        :return: The active of this ReqSettingDto.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        r"""Sets the active of this ReqSettingDto.

        **参数解释：** 是否开启集成CodeArts Req **取值范围：** true：开启集成CodeArts Req，false：未开启集成CodeArts Req。

        :param active: The active of this ReqSettingDto.
        :type active: bool
        """
        self._active = active

    @property
    def branches(self):
        r"""Gets the branches of this ReqSettingDto.

        **参数解释：** 应用排除状态和可关联类别限制的分支列表，该分支指代合并请求的目标分支，可支持多个分支用英文逗号拼接或者正则表达式，在项目层级和代码组层级只支持配置正则表达式。

        :return: The branches of this ReqSettingDto.
        :rtype: str
        """
        return self._branches

    @branches.setter
    def branches(self, branches):
        r"""Sets the branches of this ReqSettingDto.

        **参数解释：** 应用排除状态和可关联类别限制的分支列表，该分支指代合并请求的目标分支，可支持多个分支用英文逗号拼接或者正则表达式，在项目层级和代码组层级只支持配置正则表达式。

        :param branches: The branches of this ReqSettingDto.
        :type branches: str
        """
        self._branches = branches

    @property
    def branches_type(self):
        r"""Gets the branches_type of this ReqSettingDto.

        **参数解释：** 分支的类型，文本或者正则表达式。 **取值范围：** plain代表文本，regex代表正则表达式。

        :return: The branches_type of this ReqSettingDto.
        :rtype: str
        """
        return self._branches_type

    @branches_type.setter
    def branches_type(self, branches_type):
        r"""Sets the branches_type of this ReqSettingDto.

        **参数解释：** 分支的类型，文本或者正则表达式。 **取值范围：** plain代表文本，regex代表正则表达式。

        :param branches_type: The branches_type of this ReqSettingDto.
        :type branches_type: str
        """
        self._branches_type = branches_type

    @property
    def project_type(self):
        r"""Gets the project_type of this ReqSettingDto.

        **参数解释：** 关联的CodeArts Req项目类型。 **取值范围：** scrum代表scrum类型项目，ipd代表IPD类型项目, xboard为看板类型项目。

        :return: The project_type of this ReqSettingDto.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        r"""Sets the project_type of this ReqSettingDto.

        **参数解释：** 关联的CodeArts Req项目类型。 **取值范围：** scrum代表scrum类型项目，ipd代表IPD类型项目, xboard为看板类型项目。

        :param project_type: The project_type of this ReqSettingDto.
        :type project_type: str
        """
        self._project_type = project_type

    @property
    def categories(self):
        r"""Gets the categories of this ReqSettingDto.

        **参数解释：** 可关联类型列表，逗号分隔。

        :return: The categories of this ReqSettingDto.
        :rtype: str
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this ReqSettingDto.

        **参数解释：** 可关联类型列表，逗号分隔。

        :param categories: The categories of this ReqSettingDto.
        :type categories: str
        """
        self._categories = categories

    @property
    def category_codes(self):
        r"""Gets the category_codes of this ReqSettingDto.

        **参数解释：** 可关联类型编码列表，逗号分隔。

        :return: The category_codes of this ReqSettingDto.
        :rtype: str
        """
        return self._category_codes

    @category_codes.setter
    def category_codes(self, category_codes):
        r"""Sets the category_codes of this ReqSettingDto.

        **参数解释：** 可关联类型编码列表，逗号分隔。

        :param category_codes: The category_codes of this ReqSettingDto.
        :type category_codes: str
        """
        self._category_codes = category_codes

    @property
    def exclude_statuses(self):
        r"""Gets the exclude_statuses of this ReqSettingDto.

        **参数解释：** 排除状态列表，逗号分隔。

        :return: The exclude_statuses of this ReqSettingDto.
        :rtype: str
        """
        return self._exclude_statuses

    @exclude_statuses.setter
    def exclude_statuses(self, exclude_statuses):
        r"""Sets the exclude_statuses of this ReqSettingDto.

        **参数解释：** 排除状态列表，逗号分隔。

        :param exclude_statuses: The exclude_statuses of this ReqSettingDto.
        :type exclude_statuses: str
        """
        self._exclude_statuses = exclude_statuses

    @property
    def exclude_status_codes(self):
        r"""Gets the exclude_status_codes of this ReqSettingDto.

        **参数解释：** 排除状态编码列表，逗号分隔。

        :return: The exclude_status_codes of this ReqSettingDto.
        :rtype: str
        """
        return self._exclude_status_codes

    @exclude_status_codes.setter
    def exclude_status_codes(self, exclude_status_codes):
        r"""Sets the exclude_status_codes of this ReqSettingDto.

        **参数解释：** 排除状态编码列表，逗号分隔。

        :param exclude_status_codes: The exclude_status_codes of this ReqSettingDto.
        :type exclude_status_codes: str
        """
        self._exclude_status_codes = exclude_status_codes

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
        if not isinstance(other, ReqSettingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
