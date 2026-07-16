# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkspaceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'grants': 'list[ViewWorkspaceResponseGrants]',
        'auth_type': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'grants': 'grants',
        'auth_type': 'auth_type',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, grants=None, auth_type=None, name=None, description=None):
        r"""UpdateWorkspaceReq

        The model defined in huaweicloud sdk

        :param grants: 训练作业使用的数据集。不可与data_url或dataset_id/dataset_version_id同时使用。
        :type grants: list[:class:`huaweicloudsdkmodelarts.v1.ViewWorkspaceResponseGrants`]
        :param auth_type: 授权类型。可选值有PUBLIC、PRIVATE、INTERNAL。默认值为PUBLIC。 - PUBLIC：租户内部公开访问。 - PRIVATE：仅创建者和主账号可访问。 - INTERNAL：创建者、主账号、指定IAM子账号可访问，需要与grants参数配合使用。
        :type auth_type: str
        :param name: 工作空间名称。长度限制为4-64字符[，支持中文、大小写字母、数字、中划线和下划线](tag:hc,hk)。同时&#39;default&#39;为系统预留的默认工作空间名称，用户无法自己创建名为&#39;default&#39;的工作空间。
        :type name: str
        :param description: 工作空间描述，默认为空。长度限制为0-256字符。
        :type description: str
        """
        
        

        self._grants = None
        self._auth_type = None
        self._name = None
        self._description = None
        self.discriminator = None

        if grants is not None:
            self.grants = grants
        if auth_type is not None:
            self.auth_type = auth_type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def grants(self):
        r"""Gets the grants of this UpdateWorkspaceReq.

        训练作业使用的数据集。不可与data_url或dataset_id/dataset_version_id同时使用。

        :return: The grants of this UpdateWorkspaceReq.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ViewWorkspaceResponseGrants`]
        """
        return self._grants

    @grants.setter
    def grants(self, grants):
        r"""Sets the grants of this UpdateWorkspaceReq.

        训练作业使用的数据集。不可与data_url或dataset_id/dataset_version_id同时使用。

        :param grants: The grants of this UpdateWorkspaceReq.
        :type grants: list[:class:`huaweicloudsdkmodelarts.v1.ViewWorkspaceResponseGrants`]
        """
        self._grants = grants

    @property
    def auth_type(self):
        r"""Gets the auth_type of this UpdateWorkspaceReq.

        授权类型。可选值有PUBLIC、PRIVATE、INTERNAL。默认值为PUBLIC。 - PUBLIC：租户内部公开访问。 - PRIVATE：仅创建者和主账号可访问。 - INTERNAL：创建者、主账号、指定IAM子账号可访问，需要与grants参数配合使用。

        :return: The auth_type of this UpdateWorkspaceReq.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this UpdateWorkspaceReq.

        授权类型。可选值有PUBLIC、PRIVATE、INTERNAL。默认值为PUBLIC。 - PUBLIC：租户内部公开访问。 - PRIVATE：仅创建者和主账号可访问。 - INTERNAL：创建者、主账号、指定IAM子账号可访问，需要与grants参数配合使用。

        :param auth_type: The auth_type of this UpdateWorkspaceReq.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def name(self):
        r"""Gets the name of this UpdateWorkspaceReq.

        工作空间名称。长度限制为4-64字符[，支持中文、大小写字母、数字、中划线和下划线](tag:hc,hk)。同时'default'为系统预留的默认工作空间名称，用户无法自己创建名为'default'的工作空间。

        :return: The name of this UpdateWorkspaceReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateWorkspaceReq.

        工作空间名称。长度限制为4-64字符[，支持中文、大小写字母、数字、中划线和下划线](tag:hc,hk)。同时'default'为系统预留的默认工作空间名称，用户无法自己创建名为'default'的工作空间。

        :param name: The name of this UpdateWorkspaceReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateWorkspaceReq.

        工作空间描述，默认为空。长度限制为0-256字符。

        :return: The description of this UpdateWorkspaceReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateWorkspaceReq.

        工作空间描述，默认为空。长度限制为0-256字符。

        :param description: The description of this UpdateWorkspaceReq.
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
        if not isinstance(other, UpdateWorkspaceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
