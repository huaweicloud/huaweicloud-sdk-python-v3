# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFollow302SwitchResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'follow_status': 'Follow302StatusBody'
    }

    attribute_map = {
        'follow_status': 'follow_status'
    }

    def __init__(self, follow_status=None):
        """UpdateFollow302SwitchResponse

        The model defined in huaweicloud sdk

        :param follow_status: 
        :type follow_status: :class:`huaweicloudsdkcdn.v1.Follow302StatusBody`
        """
        
        super(UpdateFollow302SwitchResponse, self).__init__()

        self._follow_status = None
        self.discriminator = None

        if follow_status is not None:
            self.follow_status = follow_status

    @property
    def follow_status(self):
        """Gets the follow_status of this UpdateFollow302SwitchResponse.


        :return: The follow_status of this UpdateFollow302SwitchResponse.
        :rtype: :class:`huaweicloudsdkcdn.v1.Follow302StatusBody`
        """
        return self._follow_status

    @follow_status.setter
    def follow_status(self, follow_status):
        """Sets the follow_status of this UpdateFollow302SwitchResponse.


        :param follow_status: The follow_status of this UpdateFollow302SwitchResponse.
        :type follow_status: :class:`huaweicloudsdkcdn.v1.Follow302StatusBody`
        """
        self._follow_status = follow_status

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
        if not isinstance(other, UpdateFollow302SwitchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
