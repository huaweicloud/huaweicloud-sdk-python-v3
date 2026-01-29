# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectVersionsCountRequest:

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
        'build_version': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'build_version': 'build_version'
    }

    def __init__(self, project_id=None, build_version=None):
        r"""ShowProjectVersionsCountRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**： 项目ID，可以调用API获取，也可以从控制台获取，获取方式请参考[项目ID](CloudArtifact_api_0015.xml)。 **约束限制**： 不涉及。 **取值范围**： 只能由英文字母、数字组成，且长度为32个字符。 **默认取值**： 不涉及。
        :type project_id: str
        :param build_version: **参数解释**： 发布库版本的名称。 **约束限制**： 不涉及。 **取值范围**： 英文字母、数字、特殊字符支持中划线、下划线和英文句号，长度为1-128个字符。 **默认取值**： 不涉及。
        :type build_version: str
        """
        
        

        self._project_id = None
        self._build_version = None
        self.discriminator = None

        self.project_id = project_id
        if build_version is not None:
            self.build_version = build_version

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowProjectVersionsCountRequest.

        **参数解释**： 项目ID，可以调用API获取，也可以从控制台获取，获取方式请参考[项目ID](CloudArtifact_api_0015.xml)。 **约束限制**： 不涉及。 **取值范围**： 只能由英文字母、数字组成，且长度为32个字符。 **默认取值**： 不涉及。

        :return: The project_id of this ShowProjectVersionsCountRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowProjectVersionsCountRequest.

        **参数解释**： 项目ID，可以调用API获取，也可以从控制台获取，获取方式请参考[项目ID](CloudArtifact_api_0015.xml)。 **约束限制**： 不涉及。 **取值范围**： 只能由英文字母、数字组成，且长度为32个字符。 **默认取值**： 不涉及。

        :param project_id: The project_id of this ShowProjectVersionsCountRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def build_version(self):
        r"""Gets the build_version of this ShowProjectVersionsCountRequest.

        **参数解释**： 发布库版本的名称。 **约束限制**： 不涉及。 **取值范围**： 英文字母、数字、特殊字符支持中划线、下划线和英文句号，长度为1-128个字符。 **默认取值**： 不涉及。

        :return: The build_version of this ShowProjectVersionsCountRequest.
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        r"""Sets the build_version of this ShowProjectVersionsCountRequest.

        **参数解释**： 发布库版本的名称。 **约束限制**： 不涉及。 **取值范围**： 英文字母、数字、特殊字符支持中划线、下划线和英文句号，长度为1-128个字符。 **默认取值**： 不涉及。

        :param build_version: The build_version of this ShowProjectVersionsCountRequest.
        :type build_version: str
        """
        self._build_version = build_version

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
        if not isinstance(other, ShowProjectVersionsCountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
