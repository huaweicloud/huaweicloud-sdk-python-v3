# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVersionListRequest:

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
        'build_version': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'build_version': 'build_version',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, build_version=None, offset=None, limit=None):
        r"""ShowVersionListRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**： 项目ID，可以调用API获取，也可以从控制台获取，获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**： 不涉及。 **取值范围**： 只能由英文字母、数字组成，且长度为32个字符。 **默认取值**： 不涉及。
        :type project_id: str
        :param build_version: **参数解释**： 表示发布库版本的名称。 **约束限制**： 不涉及。 **取值范围**： 英文字母、数字、特殊字符支持中划线、下划线和英文句号，长度为1-128个字符。 **默认取值**： 不涉及。
        :type build_version: str
        :param offset: **参数解释**： 分页查询的起始位置。 **约束限制**： 不涉及。 **取值范围**： 0-10000000 **默认取值**： 0
        :type offset: int
        :param limit: **参数解释**： 分页查询每页的数据量。 **约束限制**： 不涉及。 **取值范围**： 1-100 **默认取值**： 10
        :type limit: int
        """
        
        

        self._project_id = None
        self._build_version = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        if build_version is not None:
            self.build_version = build_version
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowVersionListRequest.

        **参数解释**： 项目ID，可以调用API获取，也可以从控制台获取，获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**： 不涉及。 **取值范围**： 只能由英文字母、数字组成，且长度为32个字符。 **默认取值**： 不涉及。

        :return: The project_id of this ShowVersionListRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowVersionListRequest.

        **参数解释**： 项目ID，可以调用API获取，也可以从控制台获取，获取方式请参考[获取项目ID](CloudArtifact_api_0015.xml)。 **约束限制**： 不涉及。 **取值范围**： 只能由英文字母、数字组成，且长度为32个字符。 **默认取值**： 不涉及。

        :param project_id: The project_id of this ShowVersionListRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def build_version(self):
        r"""Gets the build_version of this ShowVersionListRequest.

        **参数解释**： 表示发布库版本的名称。 **约束限制**： 不涉及。 **取值范围**： 英文字母、数字、特殊字符支持中划线、下划线和英文句号，长度为1-128个字符。 **默认取值**： 不涉及。

        :return: The build_version of this ShowVersionListRequest.
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        r"""Sets the build_version of this ShowVersionListRequest.

        **参数解释**： 表示发布库版本的名称。 **约束限制**： 不涉及。 **取值范围**： 英文字母、数字、特殊字符支持中划线、下划线和英文句号，长度为1-128个字符。 **默认取值**： 不涉及。

        :param build_version: The build_version of this ShowVersionListRequest.
        :type build_version: str
        """
        self._build_version = build_version

    @property
    def offset(self):
        r"""Gets the offset of this ShowVersionListRequest.

        **参数解释**： 分页查询的起始位置。 **约束限制**： 不涉及。 **取值范围**： 0-10000000 **默认取值**： 0

        :return: The offset of this ShowVersionListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowVersionListRequest.

        **参数解释**： 分页查询的起始位置。 **约束限制**： 不涉及。 **取值范围**： 0-10000000 **默认取值**： 0

        :param offset: The offset of this ShowVersionListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowVersionListRequest.

        **参数解释**： 分页查询每页的数据量。 **约束限制**： 不涉及。 **取值范围**： 1-100 **默认取值**： 10

        :return: The limit of this ShowVersionListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowVersionListRequest.

        **参数解释**： 分页查询每页的数据量。 **约束限制**： 不涉及。 **取值范围**： 1-100 **默认取值**： 10

        :param limit: The limit of this ShowVersionListRequest.
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
        if not isinstance(other, ShowVersionListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
