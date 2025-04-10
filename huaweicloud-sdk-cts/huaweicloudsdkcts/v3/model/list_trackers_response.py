# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrackersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trackers': 'list[TrackerResponseBody]'
    }

    attribute_map = {
        'trackers': 'trackers'
    }

    def __init__(self, trackers=None):
        r"""ListTrackersResponse

        The model defined in huaweicloud sdk

        :param trackers: 本次查询追踪器列表返回的追踪器数组。
        :type trackers: list[:class:`huaweicloudsdkcts.v3.TrackerResponseBody`]
        """
        
        super(ListTrackersResponse, self).__init__()

        self._trackers = None
        self.discriminator = None

        if trackers is not None:
            self.trackers = trackers

    @property
    def trackers(self):
        r"""Gets the trackers of this ListTrackersResponse.

        本次查询追踪器列表返回的追踪器数组。

        :return: The trackers of this ListTrackersResponse.
        :rtype: list[:class:`huaweicloudsdkcts.v3.TrackerResponseBody`]
        """
        return self._trackers

    @trackers.setter
    def trackers(self, trackers):
        r"""Sets the trackers of this ListTrackersResponse.

        本次查询追踪器列表返回的追踪器数组。

        :param trackers: The trackers of this ListTrackersResponse.
        :type trackers: list[:class:`huaweicloudsdkcts.v3.TrackerResponseBody`]
        """
        self._trackers = trackers

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
        if not isinstance(other, ListTrackersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
