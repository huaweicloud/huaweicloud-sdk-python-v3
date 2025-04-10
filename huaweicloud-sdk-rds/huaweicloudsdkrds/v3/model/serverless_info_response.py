# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerlessInfoResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_compute_unit': 'str',
        'max_compute_unit': 'str'
    }

    attribute_map = {
        'min_compute_unit': 'min_compute_unit',
        'max_compute_unit': 'max_compute_unit'
    }

    def __init__(self, min_compute_unit=None, max_compute_unit=None):
        r"""ServerlessInfoResponse

        The model defined in huaweicloud sdk

        :param min_compute_unit: Serverless型实例的算力范围最小值。取值范围：0.5 ~ 8，单位：RCU。
        :type min_compute_unit: str
        :param max_compute_unit: Serverless型实例的算力范围最大值。取值范围：0.5 ~ 8，单位：RCU。
        :type max_compute_unit: str
        """
        
        

        self._min_compute_unit = None
        self._max_compute_unit = None
        self.discriminator = None

        self.min_compute_unit = min_compute_unit
        self.max_compute_unit = max_compute_unit

    @property
    def min_compute_unit(self):
        r"""Gets the min_compute_unit of this ServerlessInfoResponse.

        Serverless型实例的算力范围最小值。取值范围：0.5 ~ 8，单位：RCU。

        :return: The min_compute_unit of this ServerlessInfoResponse.
        :rtype: str
        """
        return self._min_compute_unit

    @min_compute_unit.setter
    def min_compute_unit(self, min_compute_unit):
        r"""Sets the min_compute_unit of this ServerlessInfoResponse.

        Serverless型实例的算力范围最小值。取值范围：0.5 ~ 8，单位：RCU。

        :param min_compute_unit: The min_compute_unit of this ServerlessInfoResponse.
        :type min_compute_unit: str
        """
        self._min_compute_unit = min_compute_unit

    @property
    def max_compute_unit(self):
        r"""Gets the max_compute_unit of this ServerlessInfoResponse.

        Serverless型实例的算力范围最大值。取值范围：0.5 ~ 8，单位：RCU。

        :return: The max_compute_unit of this ServerlessInfoResponse.
        :rtype: str
        """
        return self._max_compute_unit

    @max_compute_unit.setter
    def max_compute_unit(self, max_compute_unit):
        r"""Sets the max_compute_unit of this ServerlessInfoResponse.

        Serverless型实例的算力范围最大值。取值范围：0.5 ~ 8，单位：RCU。

        :param max_compute_unit: The max_compute_unit of this ServerlessInfoResponse.
        :type max_compute_unit: str
        """
        self._max_compute_unit = max_compute_unit

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
        if not isinstance(other, ServerlessInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
