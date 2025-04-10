# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOffSiteInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offsite_backup_instances': 'list[OffsiteBackupInstance]',
        'total_count': 'int'
    }

    attribute_map = {
        'offsite_backup_instances': 'offsite_backup_instances',
        'total_count': 'total_count'
    }

    def __init__(self, offsite_backup_instances=None, total_count=None):
        r"""ListOffSiteInstancesResponse

        The model defined in huaweicloud sdk

        :param offsite_backup_instances: 跨区域备份实例信息。
        :type offsite_backup_instances: list[:class:`huaweicloudsdkrds.v3.OffsiteBackupInstance`]
        :param total_count: 总记录数。
        :type total_count: int
        """
        
        super(ListOffSiteInstancesResponse, self).__init__()

        self._offsite_backup_instances = None
        self._total_count = None
        self.discriminator = None

        if offsite_backup_instances is not None:
            self.offsite_backup_instances = offsite_backup_instances
        if total_count is not None:
            self.total_count = total_count

    @property
    def offsite_backup_instances(self):
        r"""Gets the offsite_backup_instances of this ListOffSiteInstancesResponse.

        跨区域备份实例信息。

        :return: The offsite_backup_instances of this ListOffSiteInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.OffsiteBackupInstance`]
        """
        return self._offsite_backup_instances

    @offsite_backup_instances.setter
    def offsite_backup_instances(self, offsite_backup_instances):
        r"""Sets the offsite_backup_instances of this ListOffSiteInstancesResponse.

        跨区域备份实例信息。

        :param offsite_backup_instances: The offsite_backup_instances of this ListOffSiteInstancesResponse.
        :type offsite_backup_instances: list[:class:`huaweicloudsdkrds.v3.OffsiteBackupInstance`]
        """
        self._offsite_backup_instances = offsite_backup_instances

    @property
    def total_count(self):
        r"""Gets the total_count of this ListOffSiteInstancesResponse.

        总记录数。

        :return: The total_count of this ListOffSiteInstancesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListOffSiteInstancesResponse.

        总记录数。

        :param total_count: The total_count of this ListOffSiteInstancesResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListOffSiteInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
