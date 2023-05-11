# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScalingActivityV2LogsResponse(SdkResponse):

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
        'scaling_activity_log': 'list[ScalingActivityLogV2]'
    }

    attribute_map = {
        'total_number': 'total_number',
        'start_number': 'start_number',
        'limit': 'limit',
        'scaling_activity_log': 'scaling_activity_log'
    }

    def __init__(self, total_number=None, start_number=None, limit=None, scaling_activity_log=None):
        """ListScalingActivityV2LogsResponse

        The model defined in huaweicloud sdk

        :param total_number: 总记录数。
        :type total_number: int
        :param start_number: 查询的其实行号。
        :type start_number: int
        :param limit: 查询记录数。
        :type limit: int
        :param scaling_activity_log: 伸缩活动日志列表。
        :type scaling_activity_log: list[:class:`huaweicloudsdkas.v1.ScalingActivityLogV2`]
        """
        
        super(ListScalingActivityV2LogsResponse, self).__init__()

        self._total_number = None
        self._start_number = None
        self._limit = None
        self._scaling_activity_log = None
        self.discriminator = None

        if total_number is not None:
            self.total_number = total_number
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit
        if scaling_activity_log is not None:
            self.scaling_activity_log = scaling_activity_log

    @property
    def total_number(self):
        """Gets the total_number of this ListScalingActivityV2LogsResponse.

        总记录数。

        :return: The total_number of this ListScalingActivityV2LogsResponse.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        """Sets the total_number of this ListScalingActivityV2LogsResponse.

        总记录数。

        :param total_number: The total_number of this ListScalingActivityV2LogsResponse.
        :type total_number: int
        """
        self._total_number = total_number

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingActivityV2LogsResponse.

        查询的其实行号。

        :return: The start_number of this ListScalingActivityV2LogsResponse.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingActivityV2LogsResponse.

        查询的其实行号。

        :param start_number: The start_number of this ListScalingActivityV2LogsResponse.
        :type start_number: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingActivityV2LogsResponse.

        查询记录数。

        :return: The limit of this ListScalingActivityV2LogsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingActivityV2LogsResponse.

        查询记录数。

        :param limit: The limit of this ListScalingActivityV2LogsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def scaling_activity_log(self):
        """Gets the scaling_activity_log of this ListScalingActivityV2LogsResponse.

        伸缩活动日志列表。

        :return: The scaling_activity_log of this ListScalingActivityV2LogsResponse.
        :rtype: list[:class:`huaweicloudsdkas.v1.ScalingActivityLogV2`]
        """
        return self._scaling_activity_log

    @scaling_activity_log.setter
    def scaling_activity_log(self, scaling_activity_log):
        """Sets the scaling_activity_log of this ListScalingActivityV2LogsResponse.

        伸缩活动日志列表。

        :param scaling_activity_log: The scaling_activity_log of this ListScalingActivityV2LogsResponse.
        :type scaling_activity_log: list[:class:`huaweicloudsdkas.v1.ScalingActivityLogV2`]
        """
        self._scaling_activity_log = scaling_activity_log

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
        if not isinstance(other, ListScalingActivityV2LogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
