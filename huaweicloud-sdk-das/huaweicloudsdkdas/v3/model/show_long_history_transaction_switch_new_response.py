# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLongHistoryTransactionSwitchNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_on': 'bool',
        'threshold': 'int',
        'can_open': 'bool',
        'cant_open_msg': 'str'
    }

    attribute_map = {
        'switch_on': 'switch_on',
        'threshold': 'threshold',
        'can_open': 'can_open',
        'cant_open_msg': 'cant_open_msg'
    }

    def __init__(self, switch_on=None, threshold=None, can_open=None, cant_open_msg=None):
        r"""ShowLongHistoryTransactionSwitchNewResponse

        The model defined in huaweicloud sdk

        :param switch_on: 开关状态
        :type switch_on: bool
        :param threshold: 长事务阈值
        :type threshold: int
        :param can_open: 是否可以开启
        :type can_open: bool
        :param cant_open_msg: 无法开启原因
        :type cant_open_msg: str
        """
        
        super().__init__()

        self._switch_on = None
        self._threshold = None
        self._can_open = None
        self._cant_open_msg = None
        self.discriminator = None

        if switch_on is not None:
            self.switch_on = switch_on
        if threshold is not None:
            self.threshold = threshold
        if can_open is not None:
            self.can_open = can_open
        if cant_open_msg is not None:
            self.cant_open_msg = cant_open_msg

    @property
    def switch_on(self):
        r"""Gets the switch_on of this ShowLongHistoryTransactionSwitchNewResponse.

        开关状态

        :return: The switch_on of this ShowLongHistoryTransactionSwitchNewResponse.
        :rtype: bool
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        r"""Sets the switch_on of this ShowLongHistoryTransactionSwitchNewResponse.

        开关状态

        :param switch_on: The switch_on of this ShowLongHistoryTransactionSwitchNewResponse.
        :type switch_on: bool
        """
        self._switch_on = switch_on

    @property
    def threshold(self):
        r"""Gets the threshold of this ShowLongHistoryTransactionSwitchNewResponse.

        长事务阈值

        :return: The threshold of this ShowLongHistoryTransactionSwitchNewResponse.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this ShowLongHistoryTransactionSwitchNewResponse.

        长事务阈值

        :param threshold: The threshold of this ShowLongHistoryTransactionSwitchNewResponse.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def can_open(self):
        r"""Gets the can_open of this ShowLongHistoryTransactionSwitchNewResponse.

        是否可以开启

        :return: The can_open of this ShowLongHistoryTransactionSwitchNewResponse.
        :rtype: bool
        """
        return self._can_open

    @can_open.setter
    def can_open(self, can_open):
        r"""Sets the can_open of this ShowLongHistoryTransactionSwitchNewResponse.

        是否可以开启

        :param can_open: The can_open of this ShowLongHistoryTransactionSwitchNewResponse.
        :type can_open: bool
        """
        self._can_open = can_open

    @property
    def cant_open_msg(self):
        r"""Gets the cant_open_msg of this ShowLongHistoryTransactionSwitchNewResponse.

        无法开启原因

        :return: The cant_open_msg of this ShowLongHistoryTransactionSwitchNewResponse.
        :rtype: str
        """
        return self._cant_open_msg

    @cant_open_msg.setter
    def cant_open_msg(self, cant_open_msg):
        r"""Sets the cant_open_msg of this ShowLongHistoryTransactionSwitchNewResponse.

        无法开启原因

        :param cant_open_msg: The cant_open_msg of this ShowLongHistoryTransactionSwitchNewResponse.
        :type cant_open_msg: str
        """
        self._cant_open_msg = cant_open_msg

    def to_dict(self):
        import warnings
        warnings.warn("ShowLongHistoryTransactionSwitchNewResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowLongHistoryTransactionSwitchNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
