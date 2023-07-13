# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScalingConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_number': 'int',
        'start_number': 'int',
        'limit': 'int',
        'scaling_configurations': 'list[ScalingConfiguration]'
    }

    attribute_map = {
        'total_number': 'total_number',
        'start_number': 'start_number',
        'limit': 'limit',
        'scaling_configurations': 'scaling_configurations'
    }

    def __init__(self, total_number=None, start_number=None, limit=None, scaling_configurations=None):
        """ListScalingConfigsResponse

        The model defined in huaweicloud sdk

        :param total_number: 总记录数。
        :type total_number: int
        :param start_number: 查询的起始行号。
        :type start_number: int
        :param limit: 查询记录数。
        :type limit: int
        :param scaling_configurations: 伸缩配置列表
        :type scaling_configurations: list[:class:`huaweicloudsdkas.v1.ScalingConfiguration`]
        """
        
        super(ListScalingConfigsResponse, self).__init__()

        self._total_number = None
        self._start_number = None
        self._limit = None
        self._scaling_configurations = None
        self.discriminator = None

        if total_number is not None:
            self.total_number = total_number
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit
        if scaling_configurations is not None:
            self.scaling_configurations = scaling_configurations

    @property
    def total_number(self):
        """Gets the total_number of this ListScalingConfigsResponse.

        总记录数。

        :return: The total_number of this ListScalingConfigsResponse.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        """Sets the total_number of this ListScalingConfigsResponse.

        总记录数。

        :param total_number: The total_number of this ListScalingConfigsResponse.
        :type total_number: int
        """
        self._total_number = total_number

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingConfigsResponse.

        查询的起始行号。

        :return: The start_number of this ListScalingConfigsResponse.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingConfigsResponse.

        查询的起始行号。

        :param start_number: The start_number of this ListScalingConfigsResponse.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingConfigsResponse.

        查询记录数。

        :return: The limit of this ListScalingConfigsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingConfigsResponse.

        查询记录数。

        :param limit: The limit of this ListScalingConfigsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def scaling_configurations(self):
        """Gets the scaling_configurations of this ListScalingConfigsResponse.

        伸缩配置列表

        :return: The scaling_configurations of this ListScalingConfigsResponse.
        :rtype: list[:class:`huaweicloudsdkas.v1.ScalingConfiguration`]
        """
        return self._scaling_configurations

    @scaling_configurations.setter
    def scaling_configurations(self, scaling_configurations):
        """Sets the scaling_configurations of this ListScalingConfigsResponse.

        伸缩配置列表

        :param scaling_configurations: The scaling_configurations of this ListScalingConfigsResponse.
        :type scaling_configurations: list[:class:`huaweicloudsdkas.v1.ScalingConfiguration`]
        """
        self._scaling_configurations = scaling_configurations

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
        if not isinstance(other, ListScalingConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
