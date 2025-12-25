# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectStorageInfoRequest:

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
        'parent_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'parent_id': 'parent_id'
    }

    def __init__(self, project_id=None, parent_id=None):
        r"""ShowProjectStorageInfoRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**： 项目ID，对应\&quot;需求管理 CodeArts Req\&quot;项目唯一标识，私有依赖库首页地址栏url https://{host}/cloudartifact/project/{project_id}/repository中project_id变量的值。 **约束限制**： 字符串长度32。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type project_id: str
        :param parent_id: **参数解释**： parent_id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type parent_id: str
        """
        
        

        self._project_id = None
        self._parent_id = None
        self.discriminator = None

        self.project_id = project_id
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowProjectStorageInfoRequest.

        **参数解释**： 项目ID，对应\"需求管理 CodeArts Req\"项目唯一标识，私有依赖库首页地址栏url https://{host}/cloudartifact/project/{project_id}/repository中project_id变量的值。 **约束限制**： 字符串长度32。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The project_id of this ShowProjectStorageInfoRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowProjectStorageInfoRequest.

        **参数解释**： 项目ID，对应\"需求管理 CodeArts Req\"项目唯一标识，私有依赖库首页地址栏url https://{host}/cloudartifact/project/{project_id}/repository中project_id变量的值。 **约束限制**： 字符串长度32。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param project_id: The project_id of this ShowProjectStorageInfoRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ShowProjectStorageInfoRequest.

        **参数解释**： parent_id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The parent_id of this ShowProjectStorageInfoRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ShowProjectStorageInfoRequest.

        **参数解释**： parent_id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param parent_id: The parent_id of this ShowProjectStorageInfoRequest.
        :type parent_id: str
        """
        self._parent_id = parent_id

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
        if not isinstance(other, ShowProjectStorageInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
