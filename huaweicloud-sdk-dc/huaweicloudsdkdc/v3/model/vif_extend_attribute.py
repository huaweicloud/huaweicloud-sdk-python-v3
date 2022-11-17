# coding: utf-8

import re
import six



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
        'local_disclaim': 'int'
    }

    attribute_map = {
        'ha_type': 'ha_type',
        'ha_mode': 'ha_mode',
        'detect_multiplier': 'detect_multiplier',
        'min_rx_interval': 'min_rx_interval',
        'min_tx_interval': 'min_tx_interval',
        'remote_disclaim': 'remote_disclaim',
        'local_disclaim': 'local_disclaim'
    }

    def __init__(self, ha_type=None, ha_mode=None, detect_multiplier=None, min_rx_interval=None, min_tx_interval=None, remote_disclaim=None, local_disclaim=None):
        """VifExtendAttribute

        The model defined in huaweicloud sdk

        :param ha_type: 虚拟接口的可用性检测类型
        :type ha_type: str
        :param ha_mode: 检测的具体的配置模式
        :type ha_mode: str
        :param detect_multiplier: 检测的重试次数
        :type detect_multiplier: int
        :param min_rx_interval: 检测的接收时长间隔
        :type min_rx_interval: int
        :param min_tx_interval: 检测的发送时长间隔
        :type min_tx_interval: int
        :param remote_disclaim: 检测的远端的标识，用于静态BFD
        :type remote_disclaim: int
        :param local_disclaim: 检测的本端的标识，用于静态BFD
        :type local_disclaim: int
        """
        
        

        self._ha_type = None
        self._ha_mode = None
        self._detect_multiplier = None
        self._min_rx_interval = None
        self._min_tx_interval = None
        self._remote_disclaim = None
        self._local_disclaim = None
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

    @property
    def ha_type(self):
        """Gets the ha_type of this VifExtendAttribute.

        虚拟接口的可用性检测类型

        :return: The ha_type of this VifExtendAttribute.
        :rtype: str
        """
        return self._ha_type

    @ha_type.setter
    def ha_type(self, ha_type):
        """Sets the ha_type of this VifExtendAttribute.

        虚拟接口的可用性检测类型

        :param ha_type: The ha_type of this VifExtendAttribute.
        :type ha_type: str
        """
        self._ha_type = ha_type

    @property
    def ha_mode(self):
        """Gets the ha_mode of this VifExtendAttribute.

        检测的具体的配置模式

        :return: The ha_mode of this VifExtendAttribute.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        """Sets the ha_mode of this VifExtendAttribute.

        检测的具体的配置模式

        :param ha_mode: The ha_mode of this VifExtendAttribute.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def detect_multiplier(self):
        """Gets the detect_multiplier of this VifExtendAttribute.

        检测的重试次数

        :return: The detect_multiplier of this VifExtendAttribute.
        :rtype: int
        """
        return self._detect_multiplier

    @detect_multiplier.setter
    def detect_multiplier(self, detect_multiplier):
        """Sets the detect_multiplier of this VifExtendAttribute.

        检测的重试次数

        :param detect_multiplier: The detect_multiplier of this VifExtendAttribute.
        :type detect_multiplier: int
        """
        self._detect_multiplier = detect_multiplier

    @property
    def min_rx_interval(self):
        """Gets the min_rx_interval of this VifExtendAttribute.

        检测的接收时长间隔

        :return: The min_rx_interval of this VifExtendAttribute.
        :rtype: int
        """
        return self._min_rx_interval

    @min_rx_interval.setter
    def min_rx_interval(self, min_rx_interval):
        """Sets the min_rx_interval of this VifExtendAttribute.

        检测的接收时长间隔

        :param min_rx_interval: The min_rx_interval of this VifExtendAttribute.
        :type min_rx_interval: int
        """
        self._min_rx_interval = min_rx_interval

    @property
    def min_tx_interval(self):
        """Gets the min_tx_interval of this VifExtendAttribute.

        检测的发送时长间隔

        :return: The min_tx_interval of this VifExtendAttribute.
        :rtype: int
        """
        return self._min_tx_interval

    @min_tx_interval.setter
    def min_tx_interval(self, min_tx_interval):
        """Sets the min_tx_interval of this VifExtendAttribute.

        检测的发送时长间隔

        :param min_tx_interval: The min_tx_interval of this VifExtendAttribute.
        :type min_tx_interval: int
        """
        self._min_tx_interval = min_tx_interval

    @property
    def remote_disclaim(self):
        """Gets the remote_disclaim of this VifExtendAttribute.

        检测的远端的标识，用于静态BFD

        :return: The remote_disclaim of this VifExtendAttribute.
        :rtype: int
        """
        return self._remote_disclaim

    @remote_disclaim.setter
    def remote_disclaim(self, remote_disclaim):
        """Sets the remote_disclaim of this VifExtendAttribute.

        检测的远端的标识，用于静态BFD

        :param remote_disclaim: The remote_disclaim of this VifExtendAttribute.
        :type remote_disclaim: int
        """
        self._remote_disclaim = remote_disclaim

    @property
    def local_disclaim(self):
        """Gets the local_disclaim of this VifExtendAttribute.

        检测的本端的标识，用于静态BFD

        :return: The local_disclaim of this VifExtendAttribute.
        :rtype: int
        """
        return self._local_disclaim

    @local_disclaim.setter
    def local_disclaim(self, local_disclaim):
        """Sets the local_disclaim of this VifExtendAttribute.

        检测的本端的标识，用于静态BFD

        :param local_disclaim: The local_disclaim of this VifExtendAttribute.
        :type local_disclaim: int
        """
        self._local_disclaim = local_disclaim

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
        if not isinstance(other, VifExtendAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
