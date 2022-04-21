# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificateAuthorityObsBucketResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'obs_buckets': 'list[ObsBuckets]'
    }

    attribute_map = {
        'total': 'total',
        'obs_buckets': 'obs_buckets'
    }

    def __init__(self, total=None, obs_buckets=None):
        """ListCertificateAuthorityObsBucketResponse

        The model defined in huaweicloud sdk

        :param total: OBS桶总数。
        :type total: int
        :param obs_buckets: OBS桶列表，详情请参见**ObsBuckets**字段数据结构说明。
        :type obs_buckets: list[:class:`huaweicloudsdkccm.v1.ObsBuckets`]
        """
        
        super(ListCertificateAuthorityObsBucketResponse, self).__init__()

        self._total = None
        self._obs_buckets = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if obs_buckets is not None:
            self.obs_buckets = obs_buckets

    @property
    def total(self):
        """Gets the total of this ListCertificateAuthorityObsBucketResponse.

        OBS桶总数。

        :return: The total of this ListCertificateAuthorityObsBucketResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCertificateAuthorityObsBucketResponse.

        OBS桶总数。

        :param total: The total of this ListCertificateAuthorityObsBucketResponse.
        :type total: int
        """
        self._total = total

    @property
    def obs_buckets(self):
        """Gets the obs_buckets of this ListCertificateAuthorityObsBucketResponse.

        OBS桶列表，详情请参见**ObsBuckets**字段数据结构说明。

        :return: The obs_buckets of this ListCertificateAuthorityObsBucketResponse.
        :rtype: list[:class:`huaweicloudsdkccm.v1.ObsBuckets`]
        """
        return self._obs_buckets

    @obs_buckets.setter
    def obs_buckets(self, obs_buckets):
        """Sets the obs_buckets of this ListCertificateAuthorityObsBucketResponse.

        OBS桶列表，详情请参见**ObsBuckets**字段数据结构说明。

        :param obs_buckets: The obs_buckets of this ListCertificateAuthorityObsBucketResponse.
        :type obs_buckets: list[:class:`huaweicloudsdkccm.v1.ObsBuckets`]
        """
        self._obs_buckets = obs_buckets

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
        if not isinstance(other, ListCertificateAuthorityObsBucketResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
