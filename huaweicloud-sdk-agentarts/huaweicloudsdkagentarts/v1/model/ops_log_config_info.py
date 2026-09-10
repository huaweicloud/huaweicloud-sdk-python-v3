# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsLogConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'project_id': 'str',
        'storage_mode': 'str',
        'group_id': 'str',
        'stream_id': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'project_id': 'project_id',
        'storage_mode': 'storage_mode',
        'group_id': 'group_id',
        'stream_id': 'stream_id'
    }

    def __init__(self, enabled=None, project_id=None, storage_mode=None, group_id=None, stream_id=None):
        r"""OpsLogConfigInfo

        The model defined in huaweicloud sdk

        :param enabled: **参数解释：** 是否开启日志采集。  **约束限制：** 不涉及  **取值范围：** true或false。  **默认取值：** false
        :type enabled: bool
        :param project_id: **参数解释：** 项目ID。  **约束限制：** 不涉及  **取值范围：** 长度为 0 - 64 个字符。  **默认取值：** 无
        :type project_id: str
        :param storage_mode: **参数解释：** 日志存储方式。  **约束限制：** 不涉及  **取值范围：** prefabricate：预制，customize：自定义。  **默认取值：** 无
        :type storage_mode: str
        :param group_id: **参数解释：** 日志组ID，可以通过LTS的控制台页面或者LTS日志组查询接口获取。日志组ID和日志流ID都没有指定时，使用默认的日志组和日志流。  **约束限制：** 不涉及  **取值范围：** 长度为 0 - 64 个字符。  **默认取值：** 无
        :type group_id: str
        :param stream_id: **参数解释：** 日志流ID，可以通过LTS的控制台页面或者LTS日志流查询接口获取。  **约束限制：** 日志组ID指定时，日志流ID必填。  **取值范围：** 长度为 0 - 64 个字符。  **默认取值：** 无
        :type stream_id: str
        """
        
        

        self._enabled = None
        self._project_id = None
        self._storage_mode = None
        self._group_id = None
        self._stream_id = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if project_id is not None:
            self.project_id = project_id
        if storage_mode is not None:
            self.storage_mode = storage_mode
        if group_id is not None:
            self.group_id = group_id
        if stream_id is not None:
            self.stream_id = stream_id

    @property
    def enabled(self):
        r"""Gets the enabled of this OpsLogConfigInfo.

        **参数解释：** 是否开启日志采集。  **约束限制：** 不涉及  **取值范围：** true或false。  **默认取值：** false

        :return: The enabled of this OpsLogConfigInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this OpsLogConfigInfo.

        **参数解释：** 是否开启日志采集。  **约束限制：** 不涉及  **取值范围：** true或false。  **默认取值：** false

        :param enabled: The enabled of this OpsLogConfigInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def project_id(self):
        r"""Gets the project_id of this OpsLogConfigInfo.

        **参数解释：** 项目ID。  **约束限制：** 不涉及  **取值范围：** 长度为 0 - 64 个字符。  **默认取值：** 无

        :return: The project_id of this OpsLogConfigInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this OpsLogConfigInfo.

        **参数解释：** 项目ID。  **约束限制：** 不涉及  **取值范围：** 长度为 0 - 64 个字符。  **默认取值：** 无

        :param project_id: The project_id of this OpsLogConfigInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def storage_mode(self):
        r"""Gets the storage_mode of this OpsLogConfigInfo.

        **参数解释：** 日志存储方式。  **约束限制：** 不涉及  **取值范围：** prefabricate：预制，customize：自定义。  **默认取值：** 无

        :return: The storage_mode of this OpsLogConfigInfo.
        :rtype: str
        """
        return self._storage_mode

    @storage_mode.setter
    def storage_mode(self, storage_mode):
        r"""Sets the storage_mode of this OpsLogConfigInfo.

        **参数解释：** 日志存储方式。  **约束限制：** 不涉及  **取值范围：** prefabricate：预制，customize：自定义。  **默认取值：** 无

        :param storage_mode: The storage_mode of this OpsLogConfigInfo.
        :type storage_mode: str
        """
        self._storage_mode = storage_mode

    @property
    def group_id(self):
        r"""Gets the group_id of this OpsLogConfigInfo.

        **参数解释：** 日志组ID，可以通过LTS的控制台页面或者LTS日志组查询接口获取。日志组ID和日志流ID都没有指定时，使用默认的日志组和日志流。  **约束限制：** 不涉及  **取值范围：** 长度为 0 - 64 个字符。  **默认取值：** 无

        :return: The group_id of this OpsLogConfigInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this OpsLogConfigInfo.

        **参数解释：** 日志组ID，可以通过LTS的控制台页面或者LTS日志组查询接口获取。日志组ID和日志流ID都没有指定时，使用默认的日志组和日志流。  **约束限制：** 不涉及  **取值范围：** 长度为 0 - 64 个字符。  **默认取值：** 无

        :param group_id: The group_id of this OpsLogConfigInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def stream_id(self):
        r"""Gets the stream_id of this OpsLogConfigInfo.

        **参数解释：** 日志流ID，可以通过LTS的控制台页面或者LTS日志流查询接口获取。  **约束限制：** 日志组ID指定时，日志流ID必填。  **取值范围：** 长度为 0 - 64 个字符。  **默认取值：** 无

        :return: The stream_id of this OpsLogConfigInfo.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this OpsLogConfigInfo.

        **参数解释：** 日志流ID，可以通过LTS的控制台页面或者LTS日志流查询接口获取。  **约束限制：** 日志组ID指定时，日志流ID必填。  **取值范围：** 长度为 0 - 64 个字符。  **默认取值：** 无

        :param stream_id: The stream_id of this OpsLogConfigInfo.
        :type stream_id: str
        """
        self._stream_id = stream_id

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
        if not isinstance(other, OpsLogConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
