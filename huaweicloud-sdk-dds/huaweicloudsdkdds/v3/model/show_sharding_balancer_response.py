# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShardingBalancerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_open': 'bool',
        'active_window': 'BalancerActiveWindow'
    }

    attribute_map = {
        'is_open': 'is_open',
        'active_window': 'active_window'
    }

    def __init__(self, is_open=None, active_window=None):
        r"""ShowShardingBalancerResponse

        The model defined in huaweicloud sdk

        :param is_open: 集群均衡是否打开。
        :type is_open: bool
        :param active_window: 
        :type active_window: :class:`huaweicloudsdkdds.v3.BalancerActiveWindow`
        """
        
        super(ShowShardingBalancerResponse, self).__init__()

        self._is_open = None
        self._active_window = None
        self.discriminator = None

        if is_open is not None:
            self.is_open = is_open
        if active_window is not None:
            self.active_window = active_window

    @property
    def is_open(self):
        r"""Gets the is_open of this ShowShardingBalancerResponse.

        集群均衡是否打开。

        :return: The is_open of this ShowShardingBalancerResponse.
        :rtype: bool
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        r"""Sets the is_open of this ShowShardingBalancerResponse.

        集群均衡是否打开。

        :param is_open: The is_open of this ShowShardingBalancerResponse.
        :type is_open: bool
        """
        self._is_open = is_open

    @property
    def active_window(self):
        r"""Gets the active_window of this ShowShardingBalancerResponse.

        :return: The active_window of this ShowShardingBalancerResponse.
        :rtype: :class:`huaweicloudsdkdds.v3.BalancerActiveWindow`
        """
        return self._active_window

    @active_window.setter
    def active_window(self, active_window):
        r"""Sets the active_window of this ShowShardingBalancerResponse.

        :param active_window: The active_window of this ShowShardingBalancerResponse.
        :type active_window: :class:`huaweicloudsdkdds.v3.BalancerActiveWindow`
        """
        self._active_window = active_window

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
        if not isinstance(other, ShowShardingBalancerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
