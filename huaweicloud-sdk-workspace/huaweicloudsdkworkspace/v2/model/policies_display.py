# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesDisplay:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_level': 'str',
        'options': 'PoliciesDisplayOptions',
        'rendering_acceleration_enable': 'bool',
        'rendering_acceleration_options': 'PoliciesDisplayRenderingAccelerationOptions',
        'adaptive_bitrate_control_enable': 'bool',
        'adaptive_bitrate_control_options': 'PoliciesDisplayAdaptiveBitrateControlOptions',
        'video_card_memory_size': 'int',
        'configuration1_enable': 'bool',
        'driver_delegation_mode_enable': 'bool',
        'driver_delegation_latency': 'int',
        'video_latency': 'int',
        'change_resolution_vm': 'bool',
        'application_recognition': 'str',
        'duplicate_display_enable': 'bool',
        'default_mapping_order': 'str',
        'duplicate_display_mode': 'str'
    }

    attribute_map = {
        'display_level': 'display_level',
        'options': 'options',
        'rendering_acceleration_enable': 'rendering_acceleration_enable',
        'rendering_acceleration_options': 'rendering_acceleration_options',
        'adaptive_bitrate_control_enable': 'adaptive_bitrate_control_enable',
        'adaptive_bitrate_control_options': 'adaptive_bitrate_control_options',
        'video_card_memory_size': 'video_card_memory_size',
        'configuration1_enable': 'configuration1_enable',
        'driver_delegation_mode_enable': 'driver_delegation_mode_enable',
        'driver_delegation_latency': 'driver_delegation_latency',
        'video_latency': 'video_latency',
        'change_resolution_vm': 'change_resolution_vm',
        'application_recognition': 'application_recognition',
        'duplicate_display_enable': 'duplicate_display_enable',
        'default_mapping_order': 'default_mapping_order',
        'duplicate_display_mode': 'duplicate_display_mode'
    }

    def __init__(self, display_level=None, options=None, rendering_acceleration_enable=None, rendering_acceleration_options=None, adaptive_bitrate_control_enable=None, adaptive_bitrate_control_options=None, video_card_memory_size=None, configuration1_enable=None, driver_delegation_mode_enable=None, driver_delegation_latency=None, video_latency=None, change_resolution_vm=None, application_recognition=None, duplicate_display_enable=None, default_mapping_order=None, duplicate_display_mode=None):
        r"""PoliciesDisplay

        The model defined in huaweicloud sdk

        :param display_level: 显示级别。取值为： LEVEL1：表示等级1。 LEVEL2：表示等级2。 LEVEL3：表示等级3。 LEVEL4：表示等级4（默认/推荐）。 LEVEL5：表示等级5。
        :type display_level: str
        :param options: 
        :type options: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplayOptions`
        :param rendering_acceleration_enable: 是否开启渲染加速。取值为： false：表示关闭。 true：表示开启。
        :type rendering_acceleration_enable: bool
        :param rendering_acceleration_options: 
        :type rendering_acceleration_options: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplayRenderingAccelerationOptions`
        :param adaptive_bitrate_control_enable: 是否开启自适应流控。取值为： false：表示关闭。 true：表示开启。
        :type adaptive_bitrate_control_enable: bool
        :param adaptive_bitrate_control_options: 
        :type adaptive_bitrate_control_options: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplayAdaptiveBitrateControlOptions`
        :param video_card_memory_size: 显卡缓存（MB）。取值范围为[0-64]。默认：64。
        :type video_card_memory_size: int
        :param configuration1_enable: 是否开启配置项1。取值为： false：表示关闭。 true：表示开启。
        :type configuration1_enable: bool
        :param driver_delegation_mode_enable: 是否开启驱动托管模式。取值为： false：表示关闭。 true：表示开启。
        :type driver_delegation_mode_enable: bool
        :param driver_delegation_latency: 驱动托管延时（*30ms）。取值范围为[1-100]。默认：80。
        :type driver_delegation_latency: int
        :param video_latency: 驱动托管视频延时（*30ms）。取值范围为[1-100]。默认：80。
        :type video_latency: int
        :param change_resolution_vm: 计算机修改分辨率：取值为： false：表示关闭。 true：表示开启。
        :type change_resolution_vm: bool
        :param application_recognition: 应用感知配置。长度不能超过1024个字符。
        :type application_recognition: str
        :param duplicate_display_enable: 同屏显示。取值为： false：表示关闭。 true：表示开启。
        :type duplicate_display_enable: bool
        :param default_mapping_order: 默认屏幕映射顺序。默认：1,2,3,4。
        :type default_mapping_order: str
        :param duplicate_display_mode: 同屏显示模式。取值为： One-to-One：表示仅支持单路。 One-to-Many：表示支持多路。
        :type duplicate_display_mode: str
        """
        
        

        self._display_level = None
        self._options = None
        self._rendering_acceleration_enable = None
        self._rendering_acceleration_options = None
        self._adaptive_bitrate_control_enable = None
        self._adaptive_bitrate_control_options = None
        self._video_card_memory_size = None
        self._configuration1_enable = None
        self._driver_delegation_mode_enable = None
        self._driver_delegation_latency = None
        self._video_latency = None
        self._change_resolution_vm = None
        self._application_recognition = None
        self._duplicate_display_enable = None
        self._default_mapping_order = None
        self._duplicate_display_mode = None
        self.discriminator = None

        if display_level is not None:
            self.display_level = display_level
        if options is not None:
            self.options = options
        if rendering_acceleration_enable is not None:
            self.rendering_acceleration_enable = rendering_acceleration_enable
        if rendering_acceleration_options is not None:
            self.rendering_acceleration_options = rendering_acceleration_options
        if adaptive_bitrate_control_enable is not None:
            self.adaptive_bitrate_control_enable = adaptive_bitrate_control_enable
        if adaptive_bitrate_control_options is not None:
            self.adaptive_bitrate_control_options = adaptive_bitrate_control_options
        if video_card_memory_size is not None:
            self.video_card_memory_size = video_card_memory_size
        if configuration1_enable is not None:
            self.configuration1_enable = configuration1_enable
        if driver_delegation_mode_enable is not None:
            self.driver_delegation_mode_enable = driver_delegation_mode_enable
        if driver_delegation_latency is not None:
            self.driver_delegation_latency = driver_delegation_latency
        if video_latency is not None:
            self.video_latency = video_latency
        if change_resolution_vm is not None:
            self.change_resolution_vm = change_resolution_vm
        if application_recognition is not None:
            self.application_recognition = application_recognition
        if duplicate_display_enable is not None:
            self.duplicate_display_enable = duplicate_display_enable
        if default_mapping_order is not None:
            self.default_mapping_order = default_mapping_order
        if duplicate_display_mode is not None:
            self.duplicate_display_mode = duplicate_display_mode

    @property
    def display_level(self):
        r"""Gets the display_level of this PoliciesDisplay.

        显示级别。取值为： LEVEL1：表示等级1。 LEVEL2：表示等级2。 LEVEL3：表示等级3。 LEVEL4：表示等级4（默认/推荐）。 LEVEL5：表示等级5。

        :return: The display_level of this PoliciesDisplay.
        :rtype: str
        """
        return self._display_level

    @display_level.setter
    def display_level(self, display_level):
        r"""Sets the display_level of this PoliciesDisplay.

        显示级别。取值为： LEVEL1：表示等级1。 LEVEL2：表示等级2。 LEVEL3：表示等级3。 LEVEL4：表示等级4（默认/推荐）。 LEVEL5：表示等级5。

        :param display_level: The display_level of this PoliciesDisplay.
        :type display_level: str
        """
        self._display_level = display_level

    @property
    def options(self):
        r"""Gets the options of this PoliciesDisplay.

        :return: The options of this PoliciesDisplay.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplayOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PoliciesDisplay.

        :param options: The options of this PoliciesDisplay.
        :type options: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplayOptions`
        """
        self._options = options

    @property
    def rendering_acceleration_enable(self):
        r"""Gets the rendering_acceleration_enable of this PoliciesDisplay.

        是否开启渲染加速。取值为： false：表示关闭。 true：表示开启。

        :return: The rendering_acceleration_enable of this PoliciesDisplay.
        :rtype: bool
        """
        return self._rendering_acceleration_enable

    @rendering_acceleration_enable.setter
    def rendering_acceleration_enable(self, rendering_acceleration_enable):
        r"""Sets the rendering_acceleration_enable of this PoliciesDisplay.

        是否开启渲染加速。取值为： false：表示关闭。 true：表示开启。

        :param rendering_acceleration_enable: The rendering_acceleration_enable of this PoliciesDisplay.
        :type rendering_acceleration_enable: bool
        """
        self._rendering_acceleration_enable = rendering_acceleration_enable

    @property
    def rendering_acceleration_options(self):
        r"""Gets the rendering_acceleration_options of this PoliciesDisplay.

        :return: The rendering_acceleration_options of this PoliciesDisplay.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplayRenderingAccelerationOptions`
        """
        return self._rendering_acceleration_options

    @rendering_acceleration_options.setter
    def rendering_acceleration_options(self, rendering_acceleration_options):
        r"""Sets the rendering_acceleration_options of this PoliciesDisplay.

        :param rendering_acceleration_options: The rendering_acceleration_options of this PoliciesDisplay.
        :type rendering_acceleration_options: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplayRenderingAccelerationOptions`
        """
        self._rendering_acceleration_options = rendering_acceleration_options

    @property
    def adaptive_bitrate_control_enable(self):
        r"""Gets the adaptive_bitrate_control_enable of this PoliciesDisplay.

        是否开启自适应流控。取值为： false：表示关闭。 true：表示开启。

        :return: The adaptive_bitrate_control_enable of this PoliciesDisplay.
        :rtype: bool
        """
        return self._adaptive_bitrate_control_enable

    @adaptive_bitrate_control_enable.setter
    def adaptive_bitrate_control_enable(self, adaptive_bitrate_control_enable):
        r"""Sets the adaptive_bitrate_control_enable of this PoliciesDisplay.

        是否开启自适应流控。取值为： false：表示关闭。 true：表示开启。

        :param adaptive_bitrate_control_enable: The adaptive_bitrate_control_enable of this PoliciesDisplay.
        :type adaptive_bitrate_control_enable: bool
        """
        self._adaptive_bitrate_control_enable = adaptive_bitrate_control_enable

    @property
    def adaptive_bitrate_control_options(self):
        r"""Gets the adaptive_bitrate_control_options of this PoliciesDisplay.

        :return: The adaptive_bitrate_control_options of this PoliciesDisplay.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplayAdaptiveBitrateControlOptions`
        """
        return self._adaptive_bitrate_control_options

    @adaptive_bitrate_control_options.setter
    def adaptive_bitrate_control_options(self, adaptive_bitrate_control_options):
        r"""Sets the adaptive_bitrate_control_options of this PoliciesDisplay.

        :param adaptive_bitrate_control_options: The adaptive_bitrate_control_options of this PoliciesDisplay.
        :type adaptive_bitrate_control_options: :class:`huaweicloudsdkworkspace.v2.PoliciesDisplayAdaptiveBitrateControlOptions`
        """
        self._adaptive_bitrate_control_options = adaptive_bitrate_control_options

    @property
    def video_card_memory_size(self):
        r"""Gets the video_card_memory_size of this PoliciesDisplay.

        显卡缓存（MB）。取值范围为[0-64]。默认：64。

        :return: The video_card_memory_size of this PoliciesDisplay.
        :rtype: int
        """
        return self._video_card_memory_size

    @video_card_memory_size.setter
    def video_card_memory_size(self, video_card_memory_size):
        r"""Sets the video_card_memory_size of this PoliciesDisplay.

        显卡缓存（MB）。取值范围为[0-64]。默认：64。

        :param video_card_memory_size: The video_card_memory_size of this PoliciesDisplay.
        :type video_card_memory_size: int
        """
        self._video_card_memory_size = video_card_memory_size

    @property
    def configuration1_enable(self):
        r"""Gets the configuration1_enable of this PoliciesDisplay.

        是否开启配置项1。取值为： false：表示关闭。 true：表示开启。

        :return: The configuration1_enable of this PoliciesDisplay.
        :rtype: bool
        """
        return self._configuration1_enable

    @configuration1_enable.setter
    def configuration1_enable(self, configuration1_enable):
        r"""Sets the configuration1_enable of this PoliciesDisplay.

        是否开启配置项1。取值为： false：表示关闭。 true：表示开启。

        :param configuration1_enable: The configuration1_enable of this PoliciesDisplay.
        :type configuration1_enable: bool
        """
        self._configuration1_enable = configuration1_enable

    @property
    def driver_delegation_mode_enable(self):
        r"""Gets the driver_delegation_mode_enable of this PoliciesDisplay.

        是否开启驱动托管模式。取值为： false：表示关闭。 true：表示开启。

        :return: The driver_delegation_mode_enable of this PoliciesDisplay.
        :rtype: bool
        """
        return self._driver_delegation_mode_enable

    @driver_delegation_mode_enable.setter
    def driver_delegation_mode_enable(self, driver_delegation_mode_enable):
        r"""Sets the driver_delegation_mode_enable of this PoliciesDisplay.

        是否开启驱动托管模式。取值为： false：表示关闭。 true：表示开启。

        :param driver_delegation_mode_enable: The driver_delegation_mode_enable of this PoliciesDisplay.
        :type driver_delegation_mode_enable: bool
        """
        self._driver_delegation_mode_enable = driver_delegation_mode_enable

    @property
    def driver_delegation_latency(self):
        r"""Gets the driver_delegation_latency of this PoliciesDisplay.

        驱动托管延时（*30ms）。取值范围为[1-100]。默认：80。

        :return: The driver_delegation_latency of this PoliciesDisplay.
        :rtype: int
        """
        return self._driver_delegation_latency

    @driver_delegation_latency.setter
    def driver_delegation_latency(self, driver_delegation_latency):
        r"""Sets the driver_delegation_latency of this PoliciesDisplay.

        驱动托管延时（*30ms）。取值范围为[1-100]。默认：80。

        :param driver_delegation_latency: The driver_delegation_latency of this PoliciesDisplay.
        :type driver_delegation_latency: int
        """
        self._driver_delegation_latency = driver_delegation_latency

    @property
    def video_latency(self):
        r"""Gets the video_latency of this PoliciesDisplay.

        驱动托管视频延时（*30ms）。取值范围为[1-100]。默认：80。

        :return: The video_latency of this PoliciesDisplay.
        :rtype: int
        """
        return self._video_latency

    @video_latency.setter
    def video_latency(self, video_latency):
        r"""Sets the video_latency of this PoliciesDisplay.

        驱动托管视频延时（*30ms）。取值范围为[1-100]。默认：80。

        :param video_latency: The video_latency of this PoliciesDisplay.
        :type video_latency: int
        """
        self._video_latency = video_latency

    @property
    def change_resolution_vm(self):
        r"""Gets the change_resolution_vm of this PoliciesDisplay.

        计算机修改分辨率：取值为： false：表示关闭。 true：表示开启。

        :return: The change_resolution_vm of this PoliciesDisplay.
        :rtype: bool
        """
        return self._change_resolution_vm

    @change_resolution_vm.setter
    def change_resolution_vm(self, change_resolution_vm):
        r"""Sets the change_resolution_vm of this PoliciesDisplay.

        计算机修改分辨率：取值为： false：表示关闭。 true：表示开启。

        :param change_resolution_vm: The change_resolution_vm of this PoliciesDisplay.
        :type change_resolution_vm: bool
        """
        self._change_resolution_vm = change_resolution_vm

    @property
    def application_recognition(self):
        r"""Gets the application_recognition of this PoliciesDisplay.

        应用感知配置。长度不能超过1024个字符。

        :return: The application_recognition of this PoliciesDisplay.
        :rtype: str
        """
        return self._application_recognition

    @application_recognition.setter
    def application_recognition(self, application_recognition):
        r"""Sets the application_recognition of this PoliciesDisplay.

        应用感知配置。长度不能超过1024个字符。

        :param application_recognition: The application_recognition of this PoliciesDisplay.
        :type application_recognition: str
        """
        self._application_recognition = application_recognition

    @property
    def duplicate_display_enable(self):
        r"""Gets the duplicate_display_enable of this PoliciesDisplay.

        同屏显示。取值为： false：表示关闭。 true：表示开启。

        :return: The duplicate_display_enable of this PoliciesDisplay.
        :rtype: bool
        """
        return self._duplicate_display_enable

    @duplicate_display_enable.setter
    def duplicate_display_enable(self, duplicate_display_enable):
        r"""Sets the duplicate_display_enable of this PoliciesDisplay.

        同屏显示。取值为： false：表示关闭。 true：表示开启。

        :param duplicate_display_enable: The duplicate_display_enable of this PoliciesDisplay.
        :type duplicate_display_enable: bool
        """
        self._duplicate_display_enable = duplicate_display_enable

    @property
    def default_mapping_order(self):
        r"""Gets the default_mapping_order of this PoliciesDisplay.

        默认屏幕映射顺序。默认：1,2,3,4。

        :return: The default_mapping_order of this PoliciesDisplay.
        :rtype: str
        """
        return self._default_mapping_order

    @default_mapping_order.setter
    def default_mapping_order(self, default_mapping_order):
        r"""Sets the default_mapping_order of this PoliciesDisplay.

        默认屏幕映射顺序。默认：1,2,3,4。

        :param default_mapping_order: The default_mapping_order of this PoliciesDisplay.
        :type default_mapping_order: str
        """
        self._default_mapping_order = default_mapping_order

    @property
    def duplicate_display_mode(self):
        r"""Gets the duplicate_display_mode of this PoliciesDisplay.

        同屏显示模式。取值为： One-to-One：表示仅支持单路。 One-to-Many：表示支持多路。

        :return: The duplicate_display_mode of this PoliciesDisplay.
        :rtype: str
        """
        return self._duplicate_display_mode

    @duplicate_display_mode.setter
    def duplicate_display_mode(self, duplicate_display_mode):
        r"""Sets the duplicate_display_mode of this PoliciesDisplay.

        同屏显示模式。取值为： One-to-One：表示仅支持单路。 One-to-Many：表示支持多路。

        :param duplicate_display_mode: The duplicate_display_mode of this PoliciesDisplay.
        :type duplicate_display_mode: str
        """
        self._duplicate_display_mode = duplicate_display_mode

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
        if not isinstance(other, PoliciesDisplay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
