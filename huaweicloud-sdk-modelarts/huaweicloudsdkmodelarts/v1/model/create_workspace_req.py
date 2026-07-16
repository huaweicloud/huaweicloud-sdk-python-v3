# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWorkspaceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'grants': 'list[CreateWorkspaceReqGrants]',
        'auth_type': 'str',
        'enterprise_project_id': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'grants': 'grants',
        'auth_type': 'auth_type',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, grants=None, auth_type=None, enterprise_project_id=None, name=None, description=None):
        r"""CreateWorkspaceReq

        The model defined in huaweicloud sdk

        :param grants: 授权用户列表，默认为空。需要与“auth_type”参数配合使用，且仅当授权类型为“INTERNAL”时才会生效。
        :type grants: list[:class:`huaweicloudsdkmodelarts.v1.CreateWorkspaceReqGrants`]
        :param auth_type: 授权类型。可选值有PUBLIC、PRIVATE、INTERNAL。默认值为PUBLIC。 - PUBLIC：租户内部公开访问。 - PRIVATE：仅创建者和主账号可访问。 - INTERNAL：创建者、主账号、指定IAM子账号可访问，需要与grants参数配合使用。
        :type auth_type: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param name: 工作空间名称。长度限制为4-64字符[，支持中文、大小写字母、数字、中划线和下划线](tag:hc,hk)。同时&#39;default&#39;为系统预留的默认工作空间名称，用户无法自己创建名为&#39;default&#39;的工作空间。
        :type name: str
        :param description: 工作空间描述，默认为空。长度限制为0-256字符。
        :type description: str
        """
        
        

        self._grants = None
        self._auth_type = None
        self._enterprise_project_id = None
        self._name = None
        self._description = None
        self.discriminator = None

        if grants is not None:
            self.grants = grants
        if auth_type is not None:
            self.auth_type = auth_type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.name = name
        if description is not None:
            self.description = description

    @property
    def grants(self):
        r"""Gets the grants of this CreateWorkspaceReq.

        授权用户列表，默认为空。需要与“auth_type”参数配合使用，且仅当授权类型为“INTERNAL”时才会生效。

        :return: The grants of this CreateWorkspaceReq.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.CreateWorkspaceReqGrants`]
        """
        return self._grants

    @grants.setter
    def grants(self, grants):
        r"""Sets the grants of this CreateWorkspaceReq.

        授权用户列表，默认为空。需要与“auth_type”参数配合使用，且仅当授权类型为“INTERNAL”时才会生效。

        :param grants: The grants of this CreateWorkspaceReq.
        :type grants: list[:class:`huaweicloudsdkmodelarts.v1.CreateWorkspaceReqGrants`]
        """
        self._grants = grants

    @property
    def auth_type(self):
        r"""Gets the auth_type of this CreateWorkspaceReq.

        授权类型。可选值有PUBLIC、PRIVATE、INTERNAL。默认值为PUBLIC。 - PUBLIC：租户内部公开访问。 - PRIVATE：仅创建者和主账号可访问。 - INTERNAL：创建者、主账号、指定IAM子账号可访问，需要与grants参数配合使用。

        :return: The auth_type of this CreateWorkspaceReq.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this CreateWorkspaceReq.

        授权类型。可选值有PUBLIC、PRIVATE、INTERNAL。默认值为PUBLIC。 - PUBLIC：租户内部公开访问。 - PRIVATE：仅创建者和主账号可访问。 - INTERNAL：创建者、主账号、指定IAM子账号可访问，需要与grants参数配合使用。

        :param auth_type: The auth_type of this CreateWorkspaceReq.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateWorkspaceReq.

        企业项目ID。

        :return: The enterprise_project_id of this CreateWorkspaceReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateWorkspaceReq.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreateWorkspaceReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this CreateWorkspaceReq.

        工作空间名称。长度限制为4-64字符[，支持中文、大小写字母、数字、中划线和下划线](tag:hc,hk)。同时'default'为系统预留的默认工作空间名称，用户无法自己创建名为'default'的工作空间。

        :return: The name of this CreateWorkspaceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateWorkspaceReq.

        工作空间名称。长度限制为4-64字符[，支持中文、大小写字母、数字、中划线和下划线](tag:hc,hk)。同时'default'为系统预留的默认工作空间名称，用户无法自己创建名为'default'的工作空间。

        :param name: The name of this CreateWorkspaceReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateWorkspaceReq.

        工作空间描述，默认为空。长度限制为0-256字符。

        :return: The description of this CreateWorkspaceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateWorkspaceReq.

        工作空间描述，默认为空。长度限制为0-256字符。

        :param description: The description of this CreateWorkspaceReq.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateWorkspaceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
