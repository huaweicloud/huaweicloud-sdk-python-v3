# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoEnlargeStrategyForConsoleApi:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'option': 'bool',
        'limit_size': 'int',
        'trigger_available_percent': 'int',
        'step_percent': 'int'
    }

    attribute_map = {
        'option': 'option',
        'limit_size': 'limitSize',
        'trigger_available_percent': 'triggerAvailablePercent',
        'step_percent': 'stepPercent'
    }

    def __init__(self, option=None, limit_size=None, trigger_available_percent=None, step_percent=None):
        r"""AutoEnlargeStrategyForConsoleApi

        The model defined in huaweicloud sdk

        :param option: 是否开启自动扩容。
        :type option: bool
        :param limit_size: 扩容上限，单位GB。“option”为true时，该参数必填。
        :type limit_size: int
        :param trigger_available_percent: 可用存储空间百分比，小于等于此值或者为10GB时触发扩容。“option”为true时，该参数必填。
        :type trigger_available_percent: int
        :param step_percent: 每次自动扩容的步长，单位为百分比，即每次自动扩容当前存储空间的百分比。取值范围为5%~50%。
        :type step_percent: int
        """
        
        

        self._option = None
        self._limit_size = None
        self._trigger_available_percent = None
        self._step_percent = None
        self.discriminator = None

        if option is not None:
            self.option = option
        if limit_size is not None:
            self.limit_size = limit_size
        if trigger_available_percent is not None:
            self.trigger_available_percent = trigger_available_percent
        if step_percent is not None:
            self.step_percent = step_percent

    @property
    def option(self):
        r"""Gets the option of this AutoEnlargeStrategyForConsoleApi.

        是否开启自动扩容。

        :return: The option of this AutoEnlargeStrategyForConsoleApi.
        :rtype: bool
        """
        return self._option

    @option.setter
    def option(self, option):
        r"""Sets the option of this AutoEnlargeStrategyForConsoleApi.

        是否开启自动扩容。

        :param option: The option of this AutoEnlargeStrategyForConsoleApi.
        :type option: bool
        """
        self._option = option

    @property
    def limit_size(self):
        r"""Gets the limit_size of this AutoEnlargeStrategyForConsoleApi.

        扩容上限，单位GB。“option”为true时，该参数必填。

        :return: The limit_size of this AutoEnlargeStrategyForConsoleApi.
        :rtype: int
        """
        return self._limit_size

    @limit_size.setter
    def limit_size(self, limit_size):
        r"""Sets the limit_size of this AutoEnlargeStrategyForConsoleApi.

        扩容上限，单位GB。“option”为true时，该参数必填。

        :param limit_size: The limit_size of this AutoEnlargeStrategyForConsoleApi.
        :type limit_size: int
        """
        self._limit_size = limit_size

    @property
    def trigger_available_percent(self):
        r"""Gets the trigger_available_percent of this AutoEnlargeStrategyForConsoleApi.

        可用存储空间百分比，小于等于此值或者为10GB时触发扩容。“option”为true时，该参数必填。

        :return: The trigger_available_percent of this AutoEnlargeStrategyForConsoleApi.
        :rtype: int
        """
        return self._trigger_available_percent

    @trigger_available_percent.setter
    def trigger_available_percent(self, trigger_available_percent):
        r"""Sets the trigger_available_percent of this AutoEnlargeStrategyForConsoleApi.

        可用存储空间百分比，小于等于此值或者为10GB时触发扩容。“option”为true时，该参数必填。

        :param trigger_available_percent: The trigger_available_percent of this AutoEnlargeStrategyForConsoleApi.
        :type trigger_available_percent: int
        """
        self._trigger_available_percent = trigger_available_percent

    @property
    def step_percent(self):
        r"""Gets the step_percent of this AutoEnlargeStrategyForConsoleApi.

        每次自动扩容的步长，单位为百分比，即每次自动扩容当前存储空间的百分比。取值范围为5%~50%。

        :return: The step_percent of this AutoEnlargeStrategyForConsoleApi.
        :rtype: int
        """
        return self._step_percent

    @step_percent.setter
    def step_percent(self, step_percent):
        r"""Sets the step_percent of this AutoEnlargeStrategyForConsoleApi.

        每次自动扩容的步长，单位为百分比，即每次自动扩容当前存储空间的百分比。取值范围为5%~50%。

        :param step_percent: The step_percent of this AutoEnlargeStrategyForConsoleApi.
        :type step_percent: int
        """
        self._step_percent = step_percent

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
        if not isinstance(other, AutoEnlargeStrategyForConsoleApi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
