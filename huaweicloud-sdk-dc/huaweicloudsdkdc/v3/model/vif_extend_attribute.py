# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VifExtendAttribute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ha_type': 'str',
        'ha_mode': 'str',
        'detect_multiplier': 'int',
        'min_rx_interval': 'int',
        'min_tx_interval': 'int',
        'remote_disclaim': 'int',
        'local_disclaim': 'int',
        'ipv6_remote_disclaim': 'int',
        'ipv6_local_disclaim': 'int'
    }

    attribute_map = {
        'ha_type': 'ha_type',
        'ha_mode': 'ha_mode',
        'detect_multiplier': 'detect_multiplier',
        'min_rx_interval': 'min_rx_interval',
        'min_tx_interval': 'min_tx_interval',
        'remote_disclaim': 'remote_disclaim',
        'local_disclaim': 'local_disclaim',
        'ipv6_remote_disclaim': 'ipv6_remote_disclaim',
        'ipv6_local_disclaim': 'ipv6_local_disclaim'
    }

    def __init__(self, ha_type=None, ha_mode=None, detect_multiplier=None, min_rx_interval=None, min_tx_interval=None, remote_disclaim=None, local_disclaim=None, ipv6_remote_disclaim=None, ipv6_local_disclaim=None):
        r"""VifExtendAttribute

        The model defined in huaweicloud sdk

        :param ha_type: 虚拟接口的可用性检测类型。取值范围： - nqa：网络质量分析 - bfd：双向转发检测
        :type ha_type: str
        :param ha_mode: 虚拟接口可用性检测的配置模式。取值范围： - auto_single：自动单跳bfd - auto_multi：自动多跳bfd - static_single：静态单跳bfd - static_multi：静态多跳bfd - enhance_nqa：增强型nqa
        :type ha_mode: str
        :param detect_multiplier: 检测的重试次数
        :type detect_multiplier: int
        :param min_rx_interval: 检测的接收时长间隔，单位为毫秒。   - 当ha_type为nqa时，实际生效的时间间隔为按秒为单位将输入的数值向上取整，例如输入1500毫秒，实际时间间隔为2秒；   - 当ha_type为bfd时，实际生效的时间间隔为按毫秒为单位的输入数值。最小值为200毫秒，最大值为1000毫秒。
        :type min_rx_interval: int
        :param min_tx_interval: 检测的发送时长间隔，单位为毫秒。   - 当ha_type为nqa时，实际生效的时间间隔为按秒为单位将输入的数值向上取整，例如输入1500毫秒，实际时间间隔为2秒；   - 当ha_type为bfd时，实际生效的时间间隔为按毫秒为单位的输入数值。最小值为200毫秒，最大值为1000毫秒。
        :type min_tx_interval: int
        :param remote_disclaim: 检测的远端的标识，用于静态BFD
        :type remote_disclaim: int
        :param local_disclaim: 检测的本端的标识，用于静态BFD
        :type local_disclaim: int
        :param ipv6_remote_disclaim: 检测的远端的标识，用于静态ipv6 BFD
        :type ipv6_remote_disclaim: int
        :param ipv6_local_disclaim: 检测的本端的标识，用于静态ipv6 BFD
        :type ipv6_local_disclaim: int
        """
        
        

        self._ha_type = None
        self._ha_mode = None
        self._detect_multiplier = None
        self._min_rx_interval = None
        self._min_tx_interval = None
        self._remote_disclaim = None
        self._local_disclaim = None
        self._ipv6_remote_disclaim = None
        self._ipv6_local_disclaim = None
        self.discriminator = None

        if ha_type is not None:
            self.ha_type = ha_type
        if ha_mode is not None:
            self.ha_mode = ha_mode
        if detect_multiplier is not None:
            self.detect_multiplier = detect_multiplier
        if min_rx_interval is not None:
            self.min_rx_interval = min_rx_interval
        if min_tx_interval is not None:
            self.min_tx_interval = min_tx_interval
        if remote_disclaim is not None:
            self.remote_disclaim = remote_disclaim
        if local_disclaim is not None:
            self.local_disclaim = local_disclaim
        if ipv6_remote_disclaim is not None:
            self.ipv6_remote_disclaim = ipv6_remote_disclaim
        if ipv6_local_disclaim is not None:
            self.ipv6_local_disclaim = ipv6_local_disclaim

    @property
    def ha_type(self):
        r"""Gets the ha_type of this VifExtendAttribute.

        虚拟接口的可用性检测类型。取值范围： - nqa：网络质量分析 - bfd：双向转发检测

        :return: The ha_type of this VifExtendAttribute.
        :rtype: str
        """
        return self._ha_type

    @ha_type.setter
    def ha_type(self, ha_type):
        r"""Sets the ha_type of this VifExtendAttribute.

        虚拟接口的可用性检测类型。取值范围： - nqa：网络质量分析 - bfd：双向转发检测

        :param ha_type: The ha_type of this VifExtendAttribute.
        :type ha_type: str
        """
        self._ha_type = ha_type

    @property
    def ha_mode(self):
        r"""Gets the ha_mode of this VifExtendAttribute.

        虚拟接口可用性检测的配置模式。取值范围： - auto_single：自动单跳bfd - auto_multi：自动多跳bfd - static_single：静态单跳bfd - static_multi：静态多跳bfd - enhance_nqa：增强型nqa

        :return: The ha_mode of this VifExtendAttribute.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        r"""Sets the ha_mode of this VifExtendAttribute.

        虚拟接口可用性检测的配置模式。取值范围： - auto_single：自动单跳bfd - auto_multi：自动多跳bfd - static_single：静态单跳bfd - static_multi：静态多跳bfd - enhance_nqa：增强型nqa

        :param ha_mode: The ha_mode of this VifExtendAttribute.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def detect_multiplier(self):
        r"""Gets the detect_multiplier of this VifExtendAttribute.

        检测的重试次数

        :return: The detect_multiplier of this VifExtendAttribute.
        :rtype: int
        """
        return self._detect_multiplier

    @detect_multiplier.setter
    def detect_multiplier(self, detect_multiplier):
        r"""Sets the detect_multiplier of this VifExtendAttribute.

        检测的重试次数

        :param detect_multiplier: The detect_multiplier of this VifExtendAttribute.
        :type detect_multiplier: int
        """
        self._detect_multiplier = detect_multiplier

    @property
    def min_rx_interval(self):
        r"""Gets the min_rx_interval of this VifExtendAttribute.

        检测的接收时长间隔，单位为毫秒。   - 当ha_type为nqa时，实际生效的时间间隔为按秒为单位将输入的数值向上取整，例如输入1500毫秒，实际时间间隔为2秒；   - 当ha_type为bfd时，实际生效的时间间隔为按毫秒为单位的输入数值。最小值为200毫秒，最大值为1000毫秒。

        :return: The min_rx_interval of this VifExtendAttribute.
        :rtype: int
        """
        return self._min_rx_interval

    @min_rx_interval.setter
    def min_rx_interval(self, min_rx_interval):
        r"""Sets the min_rx_interval of this VifExtendAttribute.

        检测的接收时长间隔，单位为毫秒。   - 当ha_type为nqa时，实际生效的时间间隔为按秒为单位将输入的数值向上取整，例如输入1500毫秒，实际时间间隔为2秒；   - 当ha_type为bfd时，实际生效的时间间隔为按毫秒为单位的输入数值。最小值为200毫秒，最大值为1000毫秒。

        :param min_rx_interval: The min_rx_interval of this VifExtendAttribute.
        :type min_rx_interval: int
        """
        self._min_rx_interval = min_rx_interval

    @property
    def min_tx_interval(self):
        r"""Gets the min_tx_interval of this VifExtendAttribute.

        检测的发送时长间隔，单位为毫秒。   - 当ha_type为nqa时，实际生效的时间间隔为按秒为单位将输入的数值向上取整，例如输入1500毫秒，实际时间间隔为2秒；   - 当ha_type为bfd时，实际生效的时间间隔为按毫秒为单位的输入数值。最小值为200毫秒，最大值为1000毫秒。

        :return: The min_tx_interval of this VifExtendAttribute.
        :rtype: int
        """
        return self._min_tx_interval

    @min_tx_interval.setter
    def min_tx_interval(self, min_tx_interval):
        r"""Sets the min_tx_interval of this VifExtendAttribute.

        检测的发送时长间隔，单位为毫秒。   - 当ha_type为nqa时，实际生效的时间间隔为按秒为单位将输入的数值向上取整，例如输入1500毫秒，实际时间间隔为2秒；   - 当ha_type为bfd时，实际生效的时间间隔为按毫秒为单位的输入数值。最小值为200毫秒，最大值为1000毫秒。

        :param min_tx_interval: The min_tx_interval of this VifExtendAttribute.
        :type min_tx_interval: int
        """
        self._min_tx_interval = min_tx_interval

    @property
    def remote_disclaim(self):
        r"""Gets the remote_disclaim of this VifExtendAttribute.

        检测的远端的标识，用于静态BFD

        :return: The remote_disclaim of this VifExtendAttribute.
        :rtype: int
        """
        return self._remote_disclaim

    @remote_disclaim.setter
    def remote_disclaim(self, remote_disclaim):
        r"""Sets the remote_disclaim of this VifExtendAttribute.

        检测的远端的标识，用于静态BFD

        :param remote_disclaim: The remote_disclaim of this VifExtendAttribute.
        :type remote_disclaim: int
        """
        self._remote_disclaim = remote_disclaim

    @property
    def local_disclaim(self):
        r"""Gets the local_disclaim of this VifExtendAttribute.

        检测的本端的标识，用于静态BFD

        :return: The local_disclaim of this VifExtendAttribute.
        :rtype: int
        """
        return self._local_disclaim

    @local_disclaim.setter
    def local_disclaim(self, local_disclaim):
        r"""Sets the local_disclaim of this VifExtendAttribute.

        检测的本端的标识，用于静态BFD

        :param local_disclaim: The local_disclaim of this VifExtendAttribute.
        :type local_disclaim: int
        """
        self._local_disclaim = local_disclaim

    @property
    def ipv6_remote_disclaim(self):
        r"""Gets the ipv6_remote_disclaim of this VifExtendAttribute.

        检测的远端的标识，用于静态ipv6 BFD

        :return: The ipv6_remote_disclaim of this VifExtendAttribute.
        :rtype: int
        """
        return self._ipv6_remote_disclaim

    @ipv6_remote_disclaim.setter
    def ipv6_remote_disclaim(self, ipv6_remote_disclaim):
        r"""Sets the ipv6_remote_disclaim of this VifExtendAttribute.

        检测的远端的标识，用于静态ipv6 BFD

        :param ipv6_remote_disclaim: The ipv6_remote_disclaim of this VifExtendAttribute.
        :type ipv6_remote_disclaim: int
        """
        self._ipv6_remote_disclaim = ipv6_remote_disclaim

    @property
    def ipv6_local_disclaim(self):
        r"""Gets the ipv6_local_disclaim of this VifExtendAttribute.

        检测的本端的标识，用于静态ipv6 BFD

        :return: The ipv6_local_disclaim of this VifExtendAttribute.
        :rtype: int
        """
        return self._ipv6_local_disclaim

    @ipv6_local_disclaim.setter
    def ipv6_local_disclaim(self, ipv6_local_disclaim):
        r"""Sets the ipv6_local_disclaim of this VifExtendAttribute.

        检测的本端的标识，用于静态ipv6 BFD

        :param ipv6_local_disclaim: The ipv6_local_disclaim of this VifExtendAttribute.
        :type ipv6_local_disclaim: int
        """
        self._ipv6_local_disclaim = ipv6_local_disclaim

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
        if not isinstance(other, VifExtendAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
