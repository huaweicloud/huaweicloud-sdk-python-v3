# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageCreateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'name': 'str',
        'namespace': 'str',
        'tag': 'str',
        'workspace_id': 'str',
        'swr_instance_id': 'str',
        'swr_instance_domain': 'str'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'namespace': 'namespace',
        'tag': 'tag',
        'workspace_id': 'workspace_id',
        'swr_instance_id': 'swr_instance_id',
        'swr_instance_domain': 'swr_instance_domain'
    }

    def __init__(self, description=None, name=None, namespace=None, tag=None, workspace_id=None, swr_instance_id=None, swr_instance_domain=None):
        r"""ImageCreateReq

        The model defined in huaweicloud sdk

        :param description: **参数解释**：该镜像所对应的描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制512个字符。 **默认取值**：不涉及。
        :type description: str
        :param name: **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持小写字母、数字、中划线、下划线和点，字符串必须以小写字母或数字开头和结尾。 **默认取值**：不涉及。
        :type name: str
        :param namespace: **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **约束限制**：不涉及。 **取值范围**：长度限制为64个字符，支持大小写字母、数字、中划线、下划线和点号，且必须是小写字母开头。 **默认取值**：不涉及。
        :type namespace: str
        :param tag: **参数解释**：镜像tag。 **约束限制**：不涉及。 **取值范围**：长度限制64个字符，支持大小写字母、数字、中划线、下划线和点号。 **默认取值**：不涉及。
        :type tag: str
        :param workspace_id: **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。
        :type workspace_id: str
        :param swr_instance_id: **参数解释**：企业版SWR仓库ID。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type swr_instance_id: str
        :param swr_instance_domain: **参数解释**：企业版SWR仓库域名。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type swr_instance_domain: str
        """
        
        

        self._description = None
        self._name = None
        self._namespace = None
        self._tag = None
        self._workspace_id = None
        self._swr_instance_id = None
        self._swr_instance_domain = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.name = name
        self.namespace = namespace
        if tag is not None:
            self.tag = tag
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if swr_instance_id is not None:
            self.swr_instance_id = swr_instance_id
        if swr_instance_domain is not None:
            self.swr_instance_domain = swr_instance_domain

    @property
    def description(self):
        r"""Gets the description of this ImageCreateReq.

        **参数解释**：该镜像所对应的描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制512个字符。 **默认取值**：不涉及。

        :return: The description of this ImageCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageCreateReq.

        **参数解释**：该镜像所对应的描述信息。 **约束限制**：不涉及。 **取值范围**：长度限制512个字符。 **默认取值**：不涉及。

        :param description: The description of this ImageCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this ImageCreateReq.

        **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持小写字母、数字、中划线、下划线和点，字符串必须以小写字母或数字开头和结尾。 **默认取值**：不涉及。

        :return: The name of this ImageCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImageCreateReq.

        **参数解释**：镜像名称。 **约束限制**：不涉及。 **取值范围**：长度限制为128个字符，支持小写字母、数字、中划线、下划线和点，字符串必须以小写字母或数字开头和结尾。 **默认取值**：不涉及。

        :param name: The name of this ImageCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this ImageCreateReq.

        **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **约束限制**：不涉及。 **取值范围**：长度限制为64个字符，支持大小写字母、数字、中划线、下划线和点号，且必须是小写字母开头。 **默认取值**：不涉及。

        :return: The namespace of this ImageCreateReq.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ImageCreateReq.

        **参数解释**：镜像所属组织，可以在SWR控制台“组织管理”创建和查看。 **约束限制**：不涉及。 **取值范围**：长度限制为64个字符，支持大小写字母、数字、中划线、下划线和点号，且必须是小写字母开头。 **默认取值**：不涉及。

        :param namespace: The namespace of this ImageCreateReq.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def tag(self):
        r"""Gets the tag of this ImageCreateReq.

        **参数解释**：镜像tag。 **约束限制**：不涉及。 **取值范围**：长度限制64个字符，支持大小写字母、数字、中划线、下划线和点号。 **默认取值**：不涉及。

        :return: The tag of this ImageCreateReq.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ImageCreateReq.

        **参数解释**：镜像tag。 **约束限制**：不涉及。 **取值范围**：长度限制64个字符，支持大小写字母、数字、中划线、下划线和点号。 **默认取值**：不涉及。

        :param tag: The tag of this ImageCreateReq.
        :type tag: str
        """
        self._tag = tag

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ImageCreateReq.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。

        :return: The workspace_id of this ImageCreateReq.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ImageCreateReq.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。

        :param workspace_id: The workspace_id of this ImageCreateReq.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def swr_instance_id(self):
        r"""Gets the swr_instance_id of this ImageCreateReq.

        **参数解释**：企业版SWR仓库ID。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The swr_instance_id of this ImageCreateReq.
        :rtype: str
        """
        return self._swr_instance_id

    @swr_instance_id.setter
    def swr_instance_id(self, swr_instance_id):
        r"""Sets the swr_instance_id of this ImageCreateReq.

        **参数解释**：企业版SWR仓库ID。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param swr_instance_id: The swr_instance_id of this ImageCreateReq.
        :type swr_instance_id: str
        """
        self._swr_instance_id = swr_instance_id

    @property
    def swr_instance_domain(self):
        r"""Gets the swr_instance_domain of this ImageCreateReq.

        **参数解释**：企业版SWR仓库域名。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The swr_instance_domain of this ImageCreateReq.
        :rtype: str
        """
        return self._swr_instance_domain

    @swr_instance_domain.setter
    def swr_instance_domain(self, swr_instance_domain):
        r"""Sets the swr_instance_domain of this ImageCreateReq.

        **参数解释**：企业版SWR仓库域名。 **参数约束**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param swr_instance_domain: The swr_instance_domain of this ImageCreateReq.
        :type swr_instance_domain: str
        """
        self._swr_instance_domain = swr_instance_domain

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
        if not isinstance(other, ImageCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
