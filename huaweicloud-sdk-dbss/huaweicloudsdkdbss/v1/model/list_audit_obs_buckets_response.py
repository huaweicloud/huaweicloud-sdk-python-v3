# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditObsBucketsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_list': 'list[ObsBucketObject]'
    }

    attribute_map = {
        'obs_list': 'obs_list'
    }

    def __init__(self, obs_list=None):
        r"""ListAuditObsBucketsResponse

        The model defined in huaweicloud sdk

        :param obs_list: OBS桶列表
        :type obs_list: list[:class:`huaweicloudsdkdbss.v1.ObsBucketObject`]
        """
        
        super(ListAuditObsBucketsResponse, self).__init__()

        self._obs_list = None
        self.discriminator = None

        if obs_list is not None:
            self.obs_list = obs_list

    @property
    def obs_list(self):
        r"""Gets the obs_list of this ListAuditObsBucketsResponse.

        OBS桶列表

        :return: The obs_list of this ListAuditObsBucketsResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.ObsBucketObject`]
        """
        return self._obs_list

    @obs_list.setter
    def obs_list(self, obs_list):
        r"""Sets the obs_list of this ListAuditObsBucketsResponse.

        OBS桶列表

        :param obs_list: The obs_list of this ListAuditObsBucketsResponse.
        :type obs_list: list[:class:`huaweicloudsdkdbss.v1.ObsBucketObject`]
        """
        self._obs_list = obs_list

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
        if not isinstance(other, ListAuditObsBucketsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
