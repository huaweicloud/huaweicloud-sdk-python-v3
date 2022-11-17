# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetupSyncPolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[SyncPolicyReq]'
    }

    attribute_map = {
        'jobs': 'jobs'
    }

    def __init__(self, jobs=None):
        """BatchSetupSyncPolicyReq

        The model defined in huaweicloud sdk

        :param jobs: 批量设置同步策略请求列表。
        :type jobs: list[:class:`huaweicloudsdkdrs.v3.SyncPolicyReq`]
        """
        
        

        self._jobs = None
        self.discriminator = None

        self.jobs = jobs

    @property
    def jobs(self):
        """Gets the jobs of this BatchSetupSyncPolicyReq.

        批量设置同步策略请求列表。

        :return: The jobs of this BatchSetupSyncPolicyReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.SyncPolicyReq`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this BatchSetupSyncPolicyReq.

        批量设置同步策略请求列表。

        :param jobs: The jobs of this BatchSetupSyncPolicyReq.
        :type jobs: list[:class:`huaweicloudsdkdrs.v3.SyncPolicyReq`]
        """
        self._jobs = jobs

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
        if not isinstance(other, BatchSetupSyncPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
