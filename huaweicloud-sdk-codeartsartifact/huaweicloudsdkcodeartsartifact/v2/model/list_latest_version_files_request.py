# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLatestVersionFilesRequest:

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
        'name': 'str',
        'sort_by': 'str',
        'sort_dir': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'name': 'name',
        'sort_by': 'sort_by',
        'sort_dir': 'sort_dir',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, name=None, sort_by=None, sort_dir=None, offset=None, limit=None):
        r"""ListLatestVersionFilesRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**： 项目ID，对应\&quot;需求管理 CodeArts Req\&quot;项目唯一标识，私有依赖库首页地址栏url https://{host}/cloudartifact/project/{project_id}/repository中project_id变量的值。 **约束限制**： 字符串长度32。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type project_id: str
        :param name: **参数解释**： name。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param sort_by: **参数解释**： sort_by。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type sort_by: str
        :param sort_dir: **参数解释**： sort_dir。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type sort_dir: str
        :param offset: **参数解释**： offset。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type offset: int
        :param limit: **参数解释**： limit。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type limit: int
        """
        
        

        self._project_id = None
        self._name = None
        self._sort_by = None
        self._sort_dir = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        if name is not None:
            self.name = name
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ListLatestVersionFilesRequest.

        **参数解释**： 项目ID，对应\"需求管理 CodeArts Req\"项目唯一标识，私有依赖库首页地址栏url https://{host}/cloudartifact/project/{project_id}/repository中project_id变量的值。 **约束限制**： 字符串长度32。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The project_id of this ListLatestVersionFilesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListLatestVersionFilesRequest.

        **参数解释**： 项目ID，对应\"需求管理 CodeArts Req\"项目唯一标识，私有依赖库首页地址栏url https://{host}/cloudartifact/project/{project_id}/repository中project_id变量的值。 **约束限制**： 字符串长度32。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param project_id: The project_id of this ListLatestVersionFilesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this ListLatestVersionFilesRequest.

        **参数解释**： name。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this ListLatestVersionFilesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListLatestVersionFilesRequest.

        **参数解释**： name。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this ListLatestVersionFilesRequest.
        :type name: str
        """
        self._name = name

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListLatestVersionFilesRequest.

        **参数解释**： sort_by。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The sort_by of this ListLatestVersionFilesRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListLatestVersionFilesRequest.

        **参数解释**： sort_by。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param sort_by: The sort_by of this ListLatestVersionFilesRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListLatestVersionFilesRequest.

        **参数解释**： sort_dir。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The sort_dir of this ListLatestVersionFilesRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListLatestVersionFilesRequest.

        **参数解释**： sort_dir。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param sort_dir: The sort_dir of this ListLatestVersionFilesRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def offset(self):
        r"""Gets the offset of this ListLatestVersionFilesRequest.

        **参数解释**： offset。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The offset of this ListLatestVersionFilesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLatestVersionFilesRequest.

        **参数解释**： offset。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param offset: The offset of this ListLatestVersionFilesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLatestVersionFilesRequest.

        **参数解释**： limit。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The limit of this ListLatestVersionFilesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLatestVersionFilesRequest.

        **参数解释**： limit。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param limit: The limit of this ListLatestVersionFilesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListLatestVersionFilesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
