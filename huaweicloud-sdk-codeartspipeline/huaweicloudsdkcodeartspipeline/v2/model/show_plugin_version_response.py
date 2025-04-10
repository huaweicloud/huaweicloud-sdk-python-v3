# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPluginVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_name': 'str',
        'display_name': 'str',
        'op_user': 'str',
        'op_time': 'str',
        'version': 'str',
        'unique_id': 'str',
        'version_description': 'str',
        'version_attribution': 'str',
        'plugin_composition_type': 'str',
        'plugin_attribution': 'str',
        'input_info': 'list[PluginPartQueryVOListAgentPluginInputVOData]',
        'plugin_execution': 'object',
        'runtime_attribution': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'display_name': 'display_name',
        'op_user': 'op_user',
        'op_time': 'op_time',
        'version': 'version',
        'unique_id': 'unique_id',
        'version_description': 'version_description',
        'version_attribution': 'version_attribution',
        'plugin_composition_type': 'plugin_composition_type',
        'plugin_attribution': 'plugin_attribution',
        'input_info': 'input_info',
        'plugin_execution': 'plugin_execution',
        'runtime_attribution': 'runtime_attribution'
    }

    def __init__(self, plugin_name=None, display_name=None, op_user=None, op_time=None, version=None, unique_id=None, version_description=None, version_attribution=None, plugin_composition_type=None, plugin_attribution=None, input_info=None, plugin_execution=None, runtime_attribution=None):
        r"""ShowPluginVersionResponse

        The model defined in huaweicloud sdk

        :param plugin_name: 插件名
        :type plugin_name: str
        :param display_name: 展示名
        :type display_name: str
        :param op_user: 操作人
        :type op_user: str
        :param op_time: 操作时间
        :type op_time: str
        :param version: 版本
        :type version: str
        :param unique_id: 唯一ID
        :type unique_id: str
        :param version_description: 版本说明
        :type version_description: str
        :param version_attribution: 版本属性
        :type version_attribution: str
        :param plugin_composition_type: 组合插件类型
        :type plugin_composition_type: str
        :param plugin_attribution: 插件属性
        :type plugin_attribution: str
        :param input_info: 输入信息
        :type input_info: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginPartQueryVOListAgentPluginInputVOData`]
        :param plugin_execution: 执行信息
        :type plugin_execution: object
        :param runtime_attribution: 运行属性
        :type runtime_attribution: str
        """
        
        super(ShowPluginVersionResponse, self).__init__()

        self._plugin_name = None
        self._display_name = None
        self._op_user = None
        self._op_time = None
        self._version = None
        self._unique_id = None
        self._version_description = None
        self._version_attribution = None
        self._plugin_composition_type = None
        self._plugin_attribution = None
        self._input_info = None
        self._plugin_execution = None
        self._runtime_attribution = None
        self.discriminator = None

        if plugin_name is not None:
            self.plugin_name = plugin_name
        if display_name is not None:
            self.display_name = display_name
        if op_user is not None:
            self.op_user = op_user
        if op_time is not None:
            self.op_time = op_time
        if version is not None:
            self.version = version
        if unique_id is not None:
            self.unique_id = unique_id
        if version_description is not None:
            self.version_description = version_description
        if version_attribution is not None:
            self.version_attribution = version_attribution
        if plugin_composition_type is not None:
            self.plugin_composition_type = plugin_composition_type
        if plugin_attribution is not None:
            self.plugin_attribution = plugin_attribution
        if input_info is not None:
            self.input_info = input_info
        if plugin_execution is not None:
            self.plugin_execution = plugin_execution
        if runtime_attribution is not None:
            self.runtime_attribution = runtime_attribution

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this ShowPluginVersionResponse.

        插件名

        :return: The plugin_name of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this ShowPluginVersionResponse.

        插件名

        :param plugin_name: The plugin_name of this ShowPluginVersionResponse.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def display_name(self):
        r"""Gets the display_name of this ShowPluginVersionResponse.

        展示名

        :return: The display_name of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ShowPluginVersionResponse.

        展示名

        :param display_name: The display_name of this ShowPluginVersionResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def op_user(self):
        r"""Gets the op_user of this ShowPluginVersionResponse.

        操作人

        :return: The op_user of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._op_user

    @op_user.setter
    def op_user(self, op_user):
        r"""Sets the op_user of this ShowPluginVersionResponse.

        操作人

        :param op_user: The op_user of this ShowPluginVersionResponse.
        :type op_user: str
        """
        self._op_user = op_user

    @property
    def op_time(self):
        r"""Gets the op_time of this ShowPluginVersionResponse.

        操作时间

        :return: The op_time of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._op_time

    @op_time.setter
    def op_time(self, op_time):
        r"""Sets the op_time of this ShowPluginVersionResponse.

        操作时间

        :param op_time: The op_time of this ShowPluginVersionResponse.
        :type op_time: str
        """
        self._op_time = op_time

    @property
    def version(self):
        r"""Gets the version of this ShowPluginVersionResponse.

        版本

        :return: The version of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowPluginVersionResponse.

        版本

        :param version: The version of this ShowPluginVersionResponse.
        :type version: str
        """
        self._version = version

    @property
    def unique_id(self):
        r"""Gets the unique_id of this ShowPluginVersionResponse.

        唯一ID

        :return: The unique_id of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        r"""Sets the unique_id of this ShowPluginVersionResponse.

        唯一ID

        :param unique_id: The unique_id of this ShowPluginVersionResponse.
        :type unique_id: str
        """
        self._unique_id = unique_id

    @property
    def version_description(self):
        r"""Gets the version_description of this ShowPluginVersionResponse.

        版本说明

        :return: The version_description of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._version_description

    @version_description.setter
    def version_description(self, version_description):
        r"""Sets the version_description of this ShowPluginVersionResponse.

        版本说明

        :param version_description: The version_description of this ShowPluginVersionResponse.
        :type version_description: str
        """
        self._version_description = version_description

    @property
    def version_attribution(self):
        r"""Gets the version_attribution of this ShowPluginVersionResponse.

        版本属性

        :return: The version_attribution of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._version_attribution

    @version_attribution.setter
    def version_attribution(self, version_attribution):
        r"""Sets the version_attribution of this ShowPluginVersionResponse.

        版本属性

        :param version_attribution: The version_attribution of this ShowPluginVersionResponse.
        :type version_attribution: str
        """
        self._version_attribution = version_attribution

    @property
    def plugin_composition_type(self):
        r"""Gets the plugin_composition_type of this ShowPluginVersionResponse.

        组合插件类型

        :return: The plugin_composition_type of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._plugin_composition_type

    @plugin_composition_type.setter
    def plugin_composition_type(self, plugin_composition_type):
        r"""Sets the plugin_composition_type of this ShowPluginVersionResponse.

        组合插件类型

        :param plugin_composition_type: The plugin_composition_type of this ShowPluginVersionResponse.
        :type plugin_composition_type: str
        """
        self._plugin_composition_type = plugin_composition_type

    @property
    def plugin_attribution(self):
        r"""Gets the plugin_attribution of this ShowPluginVersionResponse.

        插件属性

        :return: The plugin_attribution of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._plugin_attribution

    @plugin_attribution.setter
    def plugin_attribution(self, plugin_attribution):
        r"""Sets the plugin_attribution of this ShowPluginVersionResponse.

        插件属性

        :param plugin_attribution: The plugin_attribution of this ShowPluginVersionResponse.
        :type plugin_attribution: str
        """
        self._plugin_attribution = plugin_attribution

    @property
    def input_info(self):
        r"""Gets the input_info of this ShowPluginVersionResponse.

        输入信息

        :return: The input_info of this ShowPluginVersionResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginPartQueryVOListAgentPluginInputVOData`]
        """
        return self._input_info

    @input_info.setter
    def input_info(self, input_info):
        r"""Sets the input_info of this ShowPluginVersionResponse.

        输入信息

        :param input_info: The input_info of this ShowPluginVersionResponse.
        :type input_info: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginPartQueryVOListAgentPluginInputVOData`]
        """
        self._input_info = input_info

    @property
    def plugin_execution(self):
        r"""Gets the plugin_execution of this ShowPluginVersionResponse.

        执行信息

        :return: The plugin_execution of this ShowPluginVersionResponse.
        :rtype: object
        """
        return self._plugin_execution

    @plugin_execution.setter
    def plugin_execution(self, plugin_execution):
        r"""Sets the plugin_execution of this ShowPluginVersionResponse.

        执行信息

        :param plugin_execution: The plugin_execution of this ShowPluginVersionResponse.
        :type plugin_execution: object
        """
        self._plugin_execution = plugin_execution

    @property
    def runtime_attribution(self):
        r"""Gets the runtime_attribution of this ShowPluginVersionResponse.

        运行属性

        :return: The runtime_attribution of this ShowPluginVersionResponse.
        :rtype: str
        """
        return self._runtime_attribution

    @runtime_attribution.setter
    def runtime_attribution(self, runtime_attribution):
        r"""Sets the runtime_attribution of this ShowPluginVersionResponse.

        运行属性

        :param runtime_attribution: The runtime_attribution of this ShowPluginVersionResponse.
        :type runtime_attribution: str
        """
        self._runtime_attribution = runtime_attribution

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowPluginVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
