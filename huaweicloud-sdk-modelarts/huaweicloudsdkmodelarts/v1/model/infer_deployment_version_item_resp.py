# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InferDeploymentVersionItemResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'infer_name': 'str',
        'version': 'str',
        'version_status': 'str',
        'description': 'str',
        'create_at': 'datetime',
        'update_at': 'datetime',
        'deploy_type': 'str'
    }

    attribute_map = {
        'infer_name': 'infer_name',
        'version': 'version',
        'version_status': 'version_status',
        'description': 'description',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'deploy_type': 'deploy_type'
    }

    def __init__(self, infer_name=None, version=None, version_status=None, description=None, create_at=None, update_at=None, deploy_type=None):
        r"""InferDeploymentVersionItemResp

        The model defined in huaweicloud sdk

        :param infer_name: **参数解释：** 部署id。 **取值范围：** 不涉及。
        :type infer_name: str
        :param version: **参数解释：** 部署版本 **取值范围：** 不涉及。
        :type version: str
        :param version_status: **参数解释：** 版本状态 **取值范围：** 不涉及。
        :type version_status: str
        :param description: **参数解释：** 版本描述 **取值范围：** 不涉及。
        :type description: str
        :param create_at: **参数解释：** 创建时间 **取值范围：** 不涉及。
        :type create_at: datetime
        :param update_at: **参数解释：** 更新时间 **取值范围：** 不涉及。
        :type update_at: datetime
        :param deploy_type: **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。
        :type deploy_type: str
        """
        
        

        self._infer_name = None
        self._version = None
        self._version_status = None
        self._description = None
        self._create_at = None
        self._update_at = None
        self._deploy_type = None
        self.discriminator = None

        if infer_name is not None:
            self.infer_name = infer_name
        if version is not None:
            self.version = version
        if version_status is not None:
            self.version_status = version_status
        if description is not None:
            self.description = description
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if deploy_type is not None:
            self.deploy_type = deploy_type

    @property
    def infer_name(self):
        r"""Gets the infer_name of this InferDeploymentVersionItemResp.

        **参数解释：** 部署id。 **取值范围：** 不涉及。

        :return: The infer_name of this InferDeploymentVersionItemResp.
        :rtype: str
        """
        return self._infer_name

    @infer_name.setter
    def infer_name(self, infer_name):
        r"""Sets the infer_name of this InferDeploymentVersionItemResp.

        **参数解释：** 部署id。 **取值范围：** 不涉及。

        :param infer_name: The infer_name of this InferDeploymentVersionItemResp.
        :type infer_name: str
        """
        self._infer_name = infer_name

    @property
    def version(self):
        r"""Gets the version of this InferDeploymentVersionItemResp.

        **参数解释：** 部署版本 **取值范围：** 不涉及。

        :return: The version of this InferDeploymentVersionItemResp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this InferDeploymentVersionItemResp.

        **参数解释：** 部署版本 **取值范围：** 不涉及。

        :param version: The version of this InferDeploymentVersionItemResp.
        :type version: str
        """
        self._version = version

    @property
    def version_status(self):
        r"""Gets the version_status of this InferDeploymentVersionItemResp.

        **参数解释：** 版本状态 **取值范围：** 不涉及。

        :return: The version_status of this InferDeploymentVersionItemResp.
        :rtype: str
        """
        return self._version_status

    @version_status.setter
    def version_status(self, version_status):
        r"""Sets the version_status of this InferDeploymentVersionItemResp.

        **参数解释：** 版本状态 **取值范围：** 不涉及。

        :param version_status: The version_status of this InferDeploymentVersionItemResp.
        :type version_status: str
        """
        self._version_status = version_status

    @property
    def description(self):
        r"""Gets the description of this InferDeploymentVersionItemResp.

        **参数解释：** 版本描述 **取值范围：** 不涉及。

        :return: The description of this InferDeploymentVersionItemResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this InferDeploymentVersionItemResp.

        **参数解释：** 版本描述 **取值范围：** 不涉及。

        :param description: The description of this InferDeploymentVersionItemResp.
        :type description: str
        """
        self._description = description

    @property
    def create_at(self):
        r"""Gets the create_at of this InferDeploymentVersionItemResp.

        **参数解释：** 创建时间 **取值范围：** 不涉及。

        :return: The create_at of this InferDeploymentVersionItemResp.
        :rtype: datetime
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this InferDeploymentVersionItemResp.

        **参数解释：** 创建时间 **取值范围：** 不涉及。

        :param create_at: The create_at of this InferDeploymentVersionItemResp.
        :type create_at: datetime
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this InferDeploymentVersionItemResp.

        **参数解释：** 更新时间 **取值范围：** 不涉及。

        :return: The update_at of this InferDeploymentVersionItemResp.
        :rtype: datetime
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this InferDeploymentVersionItemResp.

        **参数解释：** 更新时间 **取值范围：** 不涉及。

        :param update_at: The update_at of this InferDeploymentVersionItemResp.
        :type update_at: datetime
        """
        self._update_at = update_at

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this InferDeploymentVersionItemResp.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :return: The deploy_type of this InferDeploymentVersionItemResp.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this InferDeploymentVersionItemResp.

        **参数解释：** 部署类型。 **取值范围：** - SINGLE：单机单卡。 - MULTI：多机多卡。

        :param deploy_type: The deploy_type of this InferDeploymentVersionItemResp.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

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
        if not isinstance(other, InferDeploymentVersionItemResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
