# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_info': 'SpanEventInfo'
    }

    attribute_map = {
        'event_info': 'event_info'
    }

    def __init__(self, event_info=None):
        """ShowEventDetailResponse

        The model defined in huaweicloud sdk

        :param event_info: 
        :type event_info: :class:`huaweicloudsdkapm.v1.SpanEventInfo`
        """
        
        super(ShowEventDetailResponse, self).__init__()

        self._event_info = None
        self.discriminator = None

        if event_info is not None:
            self.event_info = event_info

    @property
    def event_info(self):
        """Gets the event_info of this ShowEventDetailResponse.

        :return: The event_info of this ShowEventDetailResponse.
        :rtype: :class:`huaweicloudsdkapm.v1.SpanEventInfo`
        """
        return self._event_info

    @event_info.setter
    def event_info(self, event_info):
        """Sets the event_info of this ShowEventDetailResponse.

        :param event_info: The event_info of this ShowEventDetailResponse.
        :type event_info: :class:`huaweicloudsdkapm.v1.SpanEventInfo`
        """
        self._event_info = event_info

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
        if not isinstance(other, ShowEventDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
