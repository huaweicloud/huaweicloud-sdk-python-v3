# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PromLimits:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compactor_blocks_retention_period': 'str'
    }

    attribute_map = {
        'compactor_blocks_retention_period': 'compactor_blocks_retention_period'
    }

    def __init__(self, compactor_blocks_retention_period=None):
        r"""PromLimits

        The model defined in huaweicloud sdk

        :param compactor_blocks_retention_period: 指标存储时长，只支持 15天，30天，60天 ，90天
        :type compactor_blocks_retention_period: str
        """
        
        

        self._compactor_blocks_retention_period = None
        self.discriminator = None

        self.compactor_blocks_retention_period = compactor_blocks_retention_period

    @property
    def compactor_blocks_retention_period(self):
        r"""Gets the compactor_blocks_retention_period of this PromLimits.

        指标存储时长，只支持 15天，30天，60天 ，90天

        :return: The compactor_blocks_retention_period of this PromLimits.
        :rtype: str
        """
        return self._compactor_blocks_retention_period

    @compactor_blocks_retention_period.setter
    def compactor_blocks_retention_period(self, compactor_blocks_retention_period):
        r"""Sets the compactor_blocks_retention_period of this PromLimits.

        指标存储时长，只支持 15天，30天，60天 ，90天

        :param compactor_blocks_retention_period: The compactor_blocks_retention_period of this PromLimits.
        :type compactor_blocks_retention_period: str
        """
        self._compactor_blocks_retention_period = compactor_blocks_retention_period

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
        if not isinstance(other, PromLimits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
