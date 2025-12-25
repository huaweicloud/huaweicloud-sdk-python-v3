# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCollectConfigV2RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config': 'list[ConfigInfo]',
        'dataspace_id': 'str',
        'dataspace_name': 'str',
        'domain_id': 'str',
        'lts_config': 'list[LtsRquestVo]',
        'workspace_id': 'str'
    }

    attribute_map = {
        'config': 'config',
        'dataspace_id': 'dataspace_id',
        'dataspace_name': 'dataspace_name',
        'domain_id': 'domain_id',
        'lts_config': 'lts_config',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, config=None, dataspace_id=None, dataspace_name=None, domain_id=None, lts_config=None, workspace_id=None):
        r"""CreateCollectConfigV2RequestBody

        The model defined in huaweicloud sdk

        :param config: 数据集列表
        :type config: list[:class:`huaweicloudsdksecmaster.v1.ConfigInfo`]
        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param dataspace_name: 数据空间名称
        :type dataspace_name: str
        :param domain_id: 账号ID
        :type domain_id: str
        :param lts_config: lts配置
        :type lts_config: list[:class:`huaweicloudsdksecmaster.v1.LtsRquestVo`]
        :param workspace_id: 工作空间 id
        :type workspace_id: str
        """
        
        

        self._config = None
        self._dataspace_id = None
        self._dataspace_name = None
        self._domain_id = None
        self._lts_config = None
        self._workspace_id = None
        self.discriminator = None

        self.config = config
        self.dataspace_id = dataspace_id
        self.dataspace_name = dataspace_name
        if domain_id is not None:
            self.domain_id = domain_id
        if lts_config is not None:
            self.lts_config = lts_config
        self.workspace_id = workspace_id

    @property
    def config(self):
        r"""Gets the config of this CreateCollectConfigV2RequestBody.

        数据集列表

        :return: The config of this CreateCollectConfigV2RequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ConfigInfo`]
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this CreateCollectConfigV2RequestBody.

        数据集列表

        :param config: The config of this CreateCollectConfigV2RequestBody.
        :type config: list[:class:`huaweicloudsdksecmaster.v1.ConfigInfo`]
        """
        self._config = config

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this CreateCollectConfigV2RequestBody.

        数据空间ID

        :return: The dataspace_id of this CreateCollectConfigV2RequestBody.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this CreateCollectConfigV2RequestBody.

        数据空间ID

        :param dataspace_id: The dataspace_id of this CreateCollectConfigV2RequestBody.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def dataspace_name(self):
        r"""Gets the dataspace_name of this CreateCollectConfigV2RequestBody.

        数据空间名称

        :return: The dataspace_name of this CreateCollectConfigV2RequestBody.
        :rtype: str
        """
        return self._dataspace_name

    @dataspace_name.setter
    def dataspace_name(self, dataspace_name):
        r"""Sets the dataspace_name of this CreateCollectConfigV2RequestBody.

        数据空间名称

        :param dataspace_name: The dataspace_name of this CreateCollectConfigV2RequestBody.
        :type dataspace_name: str
        """
        self._dataspace_name = dataspace_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateCollectConfigV2RequestBody.

        账号ID

        :return: The domain_id of this CreateCollectConfigV2RequestBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateCollectConfigV2RequestBody.

        账号ID

        :param domain_id: The domain_id of this CreateCollectConfigV2RequestBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def lts_config(self):
        r"""Gets the lts_config of this CreateCollectConfigV2RequestBody.

        lts配置

        :return: The lts_config of this CreateCollectConfigV2RequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.LtsRquestVo`]
        """
        return self._lts_config

    @lts_config.setter
    def lts_config(self, lts_config):
        r"""Sets the lts_config of this CreateCollectConfigV2RequestBody.

        lts配置

        :param lts_config: The lts_config of this CreateCollectConfigV2RequestBody.
        :type lts_config: list[:class:`huaweicloudsdksecmaster.v1.LtsRquestVo`]
        """
        self._lts_config = lts_config

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateCollectConfigV2RequestBody.

        工作空间 id

        :return: The workspace_id of this CreateCollectConfigV2RequestBody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateCollectConfigV2RequestBody.

        工作空间 id

        :param workspace_id: The workspace_id of this CreateCollectConfigV2RequestBody.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, CreateCollectConfigV2RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
