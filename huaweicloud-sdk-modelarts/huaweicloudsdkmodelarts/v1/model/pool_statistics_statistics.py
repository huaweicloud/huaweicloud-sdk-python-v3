# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolStatisticsStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'PoolStatisticsStatisticsStatus'
    }

    attribute_map = {
        'status': 'status'
    }

    def __init__(self, status=None):
        r"""PoolStatisticsStatistics

        The model defined in huaweicloud sdk

        :param status: 
        :type status: :class:`huaweicloudsdkmodelarts.v1.PoolStatisticsStatisticsStatus`
        """
        
        

        self._status = None
        self.discriminator = None

        if status is not None:
            self.status = status

    @property
    def status(self):
        r"""Gets the status of this PoolStatisticsStatistics.

        :return: The status of this PoolStatisticsStatistics.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolStatisticsStatisticsStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PoolStatisticsStatistics.

        :param status: The status of this PoolStatisticsStatistics.
        :type status: :class:`huaweicloudsdkmodelarts.v1.PoolStatisticsStatisticsStatus`
        """
        self._status = status

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
        if not isinstance(other, PoolStatisticsStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
