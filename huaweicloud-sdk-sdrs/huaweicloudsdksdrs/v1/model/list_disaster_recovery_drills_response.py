# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDisasterRecoveryDrillsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'disaster_recovery_drills': 'list[ShowDisasterRecoveryDrillParams]',
        'count': 'int'
    }

    attribute_map = {
        'disaster_recovery_drills': 'disaster_recovery_drills',
        'count': 'count'
    }

    def __init__(self, disaster_recovery_drills=None, count=None):
        """ListDisasterRecoveryDrillsResponse

        The model defined in huaweicloud sdk

        :param disaster_recovery_drills: 容灾演练列表。
        :type disaster_recovery_drills: list[:class:`huaweicloudsdksdrs.v1.ShowDisasterRecoveryDrillParams`]
        :param count: 列表中包含的容灾演练个数。
        :type count: int
        """
        
        super(ListDisasterRecoveryDrillsResponse, self).__init__()

        self._disaster_recovery_drills = None
        self._count = None
        self.discriminator = None

        if disaster_recovery_drills is not None:
            self.disaster_recovery_drills = disaster_recovery_drills
        if count is not None:
            self.count = count

    @property
    def disaster_recovery_drills(self):
        """Gets the disaster_recovery_drills of this ListDisasterRecoveryDrillsResponse.

        容灾演练列表。

        :return: The disaster_recovery_drills of this ListDisasterRecoveryDrillsResponse.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ShowDisasterRecoveryDrillParams`]
        """
        return self._disaster_recovery_drills

    @disaster_recovery_drills.setter
    def disaster_recovery_drills(self, disaster_recovery_drills):
        """Sets the disaster_recovery_drills of this ListDisasterRecoveryDrillsResponse.

        容灾演练列表。

        :param disaster_recovery_drills: The disaster_recovery_drills of this ListDisasterRecoveryDrillsResponse.
        :type disaster_recovery_drills: list[:class:`huaweicloudsdksdrs.v1.ShowDisasterRecoveryDrillParams`]
        """
        self._disaster_recovery_drills = disaster_recovery_drills

    @property
    def count(self):
        """Gets the count of this ListDisasterRecoveryDrillsResponse.

        列表中包含的容灾演练个数。

        :return: The count of this ListDisasterRecoveryDrillsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListDisasterRecoveryDrillsResponse.

        列表中包含的容灾演练个数。

        :param count: The count of this ListDisasterRecoveryDrillsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListDisasterRecoveryDrillsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
