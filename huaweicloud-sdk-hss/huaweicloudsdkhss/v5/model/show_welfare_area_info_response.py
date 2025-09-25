# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWelfareAreaInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hot_info': 'HttpWelfareInfoResponseInfoHotInfo',
        'version_update_info': 'HttpWelfareInfoResponseInfoVersionUpdateInfo',
        'activities_info': 'HttpWelfareInfoResponseInfoActivitiesInfo'
    }

    attribute_map = {
        'hot_info': 'hot_info',
        'version_update_info': 'version_update_info',
        'activities_info': 'activities_info'
    }

    def __init__(self, hot_info=None, version_update_info=None, activities_info=None):
        r"""ShowWelfareAreaInfoResponse

        The model defined in huaweicloud sdk

        :param hot_info: 
        :type hot_info: :class:`huaweicloudsdkhss.v5.HttpWelfareInfoResponseInfoHotInfo`
        :param version_update_info: 
        :type version_update_info: :class:`huaweicloudsdkhss.v5.HttpWelfareInfoResponseInfoVersionUpdateInfo`
        :param activities_info: 
        :type activities_info: :class:`huaweicloudsdkhss.v5.HttpWelfareInfoResponseInfoActivitiesInfo`
        """
        
        super(ShowWelfareAreaInfoResponse, self).__init__()

        self._hot_info = None
        self._version_update_info = None
        self._activities_info = None
        self.discriminator = None

        if hot_info is not None:
            self.hot_info = hot_info
        if version_update_info is not None:
            self.version_update_info = version_update_info
        if activities_info is not None:
            self.activities_info = activities_info

    @property
    def hot_info(self):
        r"""Gets the hot_info of this ShowWelfareAreaInfoResponse.

        :return: The hot_info of this ShowWelfareAreaInfoResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.HttpWelfareInfoResponseInfoHotInfo`
        """
        return self._hot_info

    @hot_info.setter
    def hot_info(self, hot_info):
        r"""Sets the hot_info of this ShowWelfareAreaInfoResponse.

        :param hot_info: The hot_info of this ShowWelfareAreaInfoResponse.
        :type hot_info: :class:`huaweicloudsdkhss.v5.HttpWelfareInfoResponseInfoHotInfo`
        """
        self._hot_info = hot_info

    @property
    def version_update_info(self):
        r"""Gets the version_update_info of this ShowWelfareAreaInfoResponse.

        :return: The version_update_info of this ShowWelfareAreaInfoResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.HttpWelfareInfoResponseInfoVersionUpdateInfo`
        """
        return self._version_update_info

    @version_update_info.setter
    def version_update_info(self, version_update_info):
        r"""Sets the version_update_info of this ShowWelfareAreaInfoResponse.

        :param version_update_info: The version_update_info of this ShowWelfareAreaInfoResponse.
        :type version_update_info: :class:`huaweicloudsdkhss.v5.HttpWelfareInfoResponseInfoVersionUpdateInfo`
        """
        self._version_update_info = version_update_info

    @property
    def activities_info(self):
        r"""Gets the activities_info of this ShowWelfareAreaInfoResponse.

        :return: The activities_info of this ShowWelfareAreaInfoResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.HttpWelfareInfoResponseInfoActivitiesInfo`
        """
        return self._activities_info

    @activities_info.setter
    def activities_info(self, activities_info):
        r"""Sets the activities_info of this ShowWelfareAreaInfoResponse.

        :param activities_info: The activities_info of this ShowWelfareAreaInfoResponse.
        :type activities_info: :class:`huaweicloudsdkhss.v5.HttpWelfareInfoResponseInfoActivitiesInfo`
        """
        self._activities_info = activities_info

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
        if not isinstance(other, ShowWelfareAreaInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
