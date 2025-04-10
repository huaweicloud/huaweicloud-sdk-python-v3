# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailoverConditions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input_loss_threshold_msec': 'int',
        'input_preference': 'str'
    }

    attribute_map = {
        'input_loss_threshold_msec': 'input_loss_threshold_msec',
        'input_preference': 'input_preference'
    }

    def __init__(self, input_loss_threshold_msec=None, input_preference=None):
        r"""FailoverConditions

        The model defined in huaweicloud sdk

        :param input_loss_threshold_msec: 入流停止的时长阈值。到达此阈值后，自动触发主备切换。  单位：毫秒，取值范围：0 - 3600000。  非必填，默认填2000ms。
        :type input_loss_threshold_msec: int
        :param input_preference: 以主入流URL为第一优先级（PRIMARY）或主备URL平等切换（EQUAL）。  如果是平等切换时，使用的是备URL，不会自动切换至主URL。  非必填，默认值为EQUAL。
        :type input_preference: str
        """
        
        

        self._input_loss_threshold_msec = None
        self._input_preference = None
        self.discriminator = None

        if input_loss_threshold_msec is not None:
            self.input_loss_threshold_msec = input_loss_threshold_msec
        if input_preference is not None:
            self.input_preference = input_preference

    @property
    def input_loss_threshold_msec(self):
        r"""Gets the input_loss_threshold_msec of this FailoverConditions.

        入流停止的时长阈值。到达此阈值后，自动触发主备切换。  单位：毫秒，取值范围：0 - 3600000。  非必填，默认填2000ms。

        :return: The input_loss_threshold_msec of this FailoverConditions.
        :rtype: int
        """
        return self._input_loss_threshold_msec

    @input_loss_threshold_msec.setter
    def input_loss_threshold_msec(self, input_loss_threshold_msec):
        r"""Sets the input_loss_threshold_msec of this FailoverConditions.

        入流停止的时长阈值。到达此阈值后，自动触发主备切换。  单位：毫秒，取值范围：0 - 3600000。  非必填，默认填2000ms。

        :param input_loss_threshold_msec: The input_loss_threshold_msec of this FailoverConditions.
        :type input_loss_threshold_msec: int
        """
        self._input_loss_threshold_msec = input_loss_threshold_msec

    @property
    def input_preference(self):
        r"""Gets the input_preference of this FailoverConditions.

        以主入流URL为第一优先级（PRIMARY）或主备URL平等切换（EQUAL）。  如果是平等切换时，使用的是备URL，不会自动切换至主URL。  非必填，默认值为EQUAL。

        :return: The input_preference of this FailoverConditions.
        :rtype: str
        """
        return self._input_preference

    @input_preference.setter
    def input_preference(self, input_preference):
        r"""Sets the input_preference of this FailoverConditions.

        以主入流URL为第一优先级（PRIMARY）或主备URL平等切换（EQUAL）。  如果是平等切换时，使用的是备URL，不会自动切换至主URL。  非必填，默认值为EQUAL。

        :param input_preference: The input_preference of this FailoverConditions.
        :type input_preference: str
        """
        self._input_preference = input_preference

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
        if not isinstance(other, FailoverConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
