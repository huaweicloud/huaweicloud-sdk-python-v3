# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestartSparkSqlClusterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restart_strategy': 'SparkSqlRestartStrategy'
    }

    attribute_map = {
        'restart_strategy': 'restart_strategy'
    }

    def __init__(self, restart_strategy=None):
        r"""RestartSparkSqlClusterRequestBody

        The model defined in huaweicloud sdk

        :param restart_strategy: 
        :type restart_strategy: :class:`huaweicloudsdkaidatalake.v2.SparkSqlRestartStrategy`
        """
        
        

        self._restart_strategy = None
        self.discriminator = None

        self.restart_strategy = restart_strategy

    @property
    def restart_strategy(self):
        r"""Gets the restart_strategy of this RestartSparkSqlClusterRequestBody.

        :return: The restart_strategy of this RestartSparkSqlClusterRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.SparkSqlRestartStrategy`
        """
        return self._restart_strategy

    @restart_strategy.setter
    def restart_strategy(self, restart_strategy):
        r"""Sets the restart_strategy of this RestartSparkSqlClusterRequestBody.

        :param restart_strategy: The restart_strategy of this RestartSparkSqlClusterRequestBody.
        :type restart_strategy: :class:`huaweicloudsdkaidatalake.v2.SparkSqlRestartStrategy`
        """
        self._restart_strategy = restart_strategy

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
        if not isinstance(other, RestartSparkSqlClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
