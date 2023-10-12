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
        'options': 'DisplayOptions',
        'rendering_acceleration_enable': 'bool',
        'rendering_acceleration_options': 'PoliciesDisplayRenderingAccelerationOptions',
        'video_card_memory_size': 'int',
        'driver_delegation_mode_enable': 'bool',
        'driver_delegation_latency': 'int',
        'video_latency': 'int',
        'change_resolution_vm': 'bool'
    }

    attribute_map = {
        'display_level': 'display_level',
        'options': 'options',
        'rendering_acceleration_enable': 'rendering_acceleration_enable',
        'rendering_acceleration_options': 'rendering_acceleration_options',
        'video_card_memory_size': 'video_card_memory_size',
        'driver_delegation_mode_enable': 'driver_delegation_mode_enable',
        'driver_delegation_latency': 'driver_delegation_latency',
        'video_latency': 'video_latency',
        'change_resolution_vm': 'change_resolution_vm'
    }

    def __init__(self, display_level=None, options=None, rendering_acceleration_enable=None, rendering_acceleration_options=None, video_card_memory_size=None, driver_delegation_mode_enable=None, driver_delegation_latency=None, video_latency=None, change_resolution_vm=None):
        """PoliciesDisplay

        The model defined in huaweicloud sdk

        :param display_level: 显示级别。取值为： LEVEL1：表示等级1。 LEVEL2：表示等级2。 LEVEL3：表示等级3。 LEVEL4：表示等级4（默认/推荐）。 LEVEL5：表示等级5。
        :type display_level: str
        :param options: 
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptions`
        :param rendering_acceleration_enable: 是否开启渲染加速。取值为： false：表示关闭。 true：表示开启。
        :type rendering_acceleration_enable: bool
        :param rendering_acceleration_options: 
        :type rendering_acceleration_options: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesDisplayRenderingAccelerationOptions`
        :param video_card_memory_size: 显卡缓存（MB）。取值范围为[0-64]。默认：64。
        :type video_card_memory_size: int
        :param driver_delegation_mode_enable: 是否开启驱动托管模式。取值为： false：表示关闭。 true：表示开启。
        :type driver_delegation_mode_enable: bool
        :param driver_delegation_latency: 驱动托管延时（*30ms）。取值范围为[1-100]。默认：80。
        :type driver_delegation_latency: int
        :param video_latency: 驱动托管视频延时（*30ms）。取值范围为[1-100]。默认：80。
        :type video_latency: int
        :param change_resolution_vm: 计算机修改分辨率：取值为： false：表示关闭。 true：表示开启。
        :type change_resolution_vm: bool
        """
        
        

        self._display_level = None
        self._options = None
        self._rendering_acceleration_enable = None
        self._rendering_acceleration_options = None
        self._video_card_memory_size = None
        self._driver_delegation_mode_enable = None
        self._driver_delegation_latency = None
        self._video_latency = None
        self._change_resolution_vm = None
        self.discriminator = None

        if display_level is not None:
            self.display_level = display_level
        if options is not None:
            self.options = options
        if rendering_acceleration_enable is not None:
            self.rendering_acceleration_enable = rendering_acceleration_enable
        if rendering_acceleration_options is not None:
            self.rendering_acceleration_options = rendering_acceleration_options
        if video_card_memory_size is not None:
            self.video_card_memory_size = video_card_memory_size
        if driver_delegation_mode_enable is not None:
            self.driver_delegation_mode_enable = driver_delegation_mode_enable
        if driver_delegation_latency is not None:
            self.driver_delegation_latency = driver_delegation_latency
        if video_latency is not None:
            self.video_latency = video_latency
        if change_resolution_vm is not None:
            self.change_resolution_vm = change_resolution_vm

    @property
    def display_level(self):
        """Gets the display_level of this PoliciesDisplay.

        显示级别。取值为： LEVEL1：表示等级1。 LEVEL2：表示等级2。 LEVEL3：表示等级3。 LEVEL4：表示等级4（默认/推荐）。 LEVEL5：表示等级5。

        :return: The display_level of this PoliciesDisplay.
        :rtype: str
        """
        return self._display_level

    @display_level.setter
    def display_level(self, display_level):
        """Sets the display_level of this PoliciesDisplay.

        显示级别。取值为： LEVEL1：表示等级1。 LEVEL2：表示等级2。 LEVEL3：表示等级3。 LEVEL4：表示等级4（默认/推荐）。 LEVEL5：表示等级5。

        :param display_level: The display_level of this PoliciesDisplay.
        :type display_level: str
        """
        self._display_level = display_level

    @property
    def options(self):
        """Gets the options of this PoliciesDisplay.

        :return: The options of this PoliciesDisplay.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this PoliciesDisplay.

        :param options: The options of this PoliciesDisplay.
        :type options: :class:`huaweicloudsdkworkspaceapp.v1.DisplayOptions`
        """
        self._options = options

    @property
    def rendering_acceleration_enable(self):
        """Gets the rendering_acceleration_enable of this PoliciesDisplay.

        是否开启渲染加速。取值为： false：表示关闭。 true：表示开启。

        :return: The rendering_acceleration_enable of this PoliciesDisplay.
        :rtype: bool
        """
        return self._rendering_acceleration_enable

    @rendering_acceleration_enable.setter
    def rendering_acceleration_enable(self, rendering_acceleration_enable):
        """Sets the rendering_acceleration_enable of this PoliciesDisplay.

        是否开启渲染加速。取值为： false：表示关闭。 true：表示开启。

        :param rendering_acceleration_enable: The rendering_acceleration_enable of this PoliciesDisplay.
        :type rendering_acceleration_enable: bool
        """
        self._rendering_acceleration_enable = rendering_acceleration_enable

    @property
    def rendering_acceleration_options(self):
        """Gets the rendering_acceleration_options of this PoliciesDisplay.

        :return: The rendering_acceleration_options of this PoliciesDisplay.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesDisplayRenderingAccelerationOptions`
        """
        return self._rendering_acceleration_options

    @rendering_acceleration_options.setter
    def rendering_acceleration_options(self, rendering_acceleration_options):
        """Sets the rendering_acceleration_options of this PoliciesDisplay.

        :param rendering_acceleration_options: The rendering_acceleration_options of this PoliciesDisplay.
        :type rendering_acceleration_options: :class:`huaweicloudsdkworkspaceapp.v1.PoliciesDisplayRenderingAccelerationOptions`
        """
        self._rendering_acceleration_options = rendering_acceleration_options

    @property
    def video_card_memory_size(self):
        """Gets the video_card_memory_size of this PoliciesDisplay.

        显卡缓存（MB）。取值范围为[0-64]。默认：64。

        :return: The video_card_memory_size of this PoliciesDisplay.
        :rtype: int
        """
        return self._video_card_memory_size

    @video_card_memory_size.setter
    def video_card_memory_size(self, video_card_memory_size):
        """Sets the video_card_memory_size of this PoliciesDisplay.

        显卡缓存（MB）。取值范围为[0-64]。默认：64。

        :param video_card_memory_size: The video_card_memory_size of this PoliciesDisplay.
        :type video_card_memory_size: int
        """
        self._video_card_memory_size = video_card_memory_size

    @property
    def driver_delegation_mode_enable(self):
        """Gets the driver_delegation_mode_enable of this PoliciesDisplay.

        是否开启驱动托管模式。取值为： false：表示关闭。 true：表示开启。

        :return: The driver_delegation_mode_enable of this PoliciesDisplay.
        :rtype: bool
        """
        return self._driver_delegation_mode_enable

    @driver_delegation_mode_enable.setter
    def driver_delegation_mode_enable(self, driver_delegation_mode_enable):
        """Sets the driver_delegation_mode_enable of this PoliciesDisplay.

        是否开启驱动托管模式。取值为： false：表示关闭。 true：表示开启。

        :param driver_delegation_mode_enable: The driver_delegation_mode_enable of this PoliciesDisplay.
        :type driver_delegation_mode_enable: bool
        """
        self._driver_delegation_mode_enable = driver_delegation_mode_enable

    @property
    def driver_delegation_latency(self):
        """Gets the driver_delegation_latency of this PoliciesDisplay.

        驱动托管延时（*30ms）。取值范围为[1-100]。默认：80。

        :return: The driver_delegation_latency of this PoliciesDisplay.
        :rtype: int
        """
        return self._driver_delegation_latency

    @driver_delegation_latency.setter
    def driver_delegation_latency(self, driver_delegation_latency):
        """Sets the driver_delegation_latency of this PoliciesDisplay.

        驱动托管延时（*30ms）。取值范围为[1-100]。默认：80。

        :param driver_delegation_latency: The driver_delegation_latency of this PoliciesDisplay.
        :type driver_delegation_latency: int
        """
        self._driver_delegation_latency = driver_delegation_latency

    @property
    def video_latency(self):
        """Gets the video_latency of this PoliciesDisplay.

        驱动托管视频延时（*30ms）。取值范围为[1-100]。默认：80。

        :return: The video_latency of this PoliciesDisplay.
        :rtype: int
        """
        return self._video_latency

    @video_latency.setter
    def video_latency(self, video_latency):
        """Sets the video_latency of this PoliciesDisplay.

        驱动托管视频延时（*30ms）。取值范围为[1-100]。默认：80。

        :param video_latency: The video_latency of this PoliciesDisplay.
        :type video_latency: int
        """
        self._video_latency = video_latency

    @property
    def change_resolution_vm(self):
        """Gets the change_resolution_vm of this PoliciesDisplay.

        计算机修改分辨率：取值为： false：表示关闭。 true：表示开启。

        :return: The change_resolution_vm of this PoliciesDisplay.
        :rtype: bool
        """
        return self._change_resolution_vm

    @change_resolution_vm.setter
    def change_resolution_vm(self, change_resolution_vm):
        """Sets the change_resolution_vm of this PoliciesDisplay.

        计算机修改分辨率：取值为： false：表示关闭。 true：表示开启。

        :param change_resolution_vm: The change_resolution_vm of this PoliciesDisplay.
        :type change_resolution_vm: bool
        """
        self._change_resolution_vm = change_resolution_vm

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
