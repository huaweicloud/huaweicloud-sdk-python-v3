# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelFlinkJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cancel_strategy': 'FlinkJobCancelStrategy'
    }

    attribute_map = {
        'cancel_strategy': 'cancel_strategy'
    }

    def __init__(self, cancel_strategy=None):
        r"""CancelFlinkJobRequestBody

        The model defined in huaweicloud sdk

        :param cancel_strategy: 
        :type cancel_strategy: :class:`huaweicloudsdkaidatalake.v2.FlinkJobCancelStrategy`
        """
        
        

        self._cancel_strategy = None
        self.discriminator = None

        self.cancel_strategy = cancel_strategy

    @property
    def cancel_strategy(self):
        r"""Gets the cancel_strategy of this CancelFlinkJobRequestBody.

        :return: The cancel_strategy of this CancelFlinkJobRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkJobCancelStrategy`
        """
        return self._cancel_strategy

    @cancel_strategy.setter
    def cancel_strategy(self, cancel_strategy):
        r"""Sets the cancel_strategy of this CancelFlinkJobRequestBody.

        :param cancel_strategy: The cancel_strategy of this CancelFlinkJobRequestBody.
        :type cancel_strategy: :class:`huaweicloudsdkaidatalake.v2.FlinkJobCancelStrategy`
        """
        self._cancel_strategy = cancel_strategy

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
        if not isinstance(other, CancelFlinkJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
