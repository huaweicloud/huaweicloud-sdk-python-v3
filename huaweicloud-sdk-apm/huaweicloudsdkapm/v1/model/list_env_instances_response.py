# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnvInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_info_list': 'list[InstanceInfo]',
        'total_count': 'int',
        'online_count': 'int',
        'offline_count': 'int',
        'disable_count': 'int'
    }

    attribute_map = {
        'instance_info_list': 'instance_info_list',
        'total_count': 'total_count',
        'online_count': 'online_count',
        'offline_count': 'offline_count',
        'disable_count': 'disable_count'
    }

    def __init__(self, instance_info_list=None, total_count=None, online_count=None, offline_count=None, disable_count=None):
        """ListEnvInstancesResponse

        The model defined in huaweicloud sdk

        :param instance_info_list: 实例信息列表。
        :type instance_info_list: list[:class:`huaweicloudsdkapm.v1.InstanceInfo`]
        :param total_count: 实例总数。
        :type total_count: int
        :param online_count: 在线实例总数。
        :type online_count: int
        :param offline_count: 离线实例总数。
        :type offline_count: int
        :param disable_count: 停止实例总数。
        :type disable_count: int
        """
        
        super(ListEnvInstancesResponse, self).__init__()

        self._instance_info_list = None
        self._total_count = None
        self._online_count = None
        self._offline_count = None
        self._disable_count = None
        self.discriminator = None

        if instance_info_list is not None:
            self.instance_info_list = instance_info_list
        if total_count is not None:
            self.total_count = total_count
        if online_count is not None:
            self.online_count = online_count
        if offline_count is not None:
            self.offline_count = offline_count
        if disable_count is not None:
            self.disable_count = disable_count

    @property
    def instance_info_list(self):
        """Gets the instance_info_list of this ListEnvInstancesResponse.

        实例信息列表。

        :return: The instance_info_list of this ListEnvInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.InstanceInfo`]
        """
        return self._instance_info_list

    @instance_info_list.setter
    def instance_info_list(self, instance_info_list):
        """Sets the instance_info_list of this ListEnvInstancesResponse.

        实例信息列表。

        :param instance_info_list: The instance_info_list of this ListEnvInstancesResponse.
        :type instance_info_list: list[:class:`huaweicloudsdkapm.v1.InstanceInfo`]
        """
        self._instance_info_list = instance_info_list

    @property
    def total_count(self):
        """Gets the total_count of this ListEnvInstancesResponse.

        实例总数。

        :return: The total_count of this ListEnvInstancesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListEnvInstancesResponse.

        实例总数。

        :param total_count: The total_count of this ListEnvInstancesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def online_count(self):
        """Gets the online_count of this ListEnvInstancesResponse.

        在线实例总数。

        :return: The online_count of this ListEnvInstancesResponse.
        :rtype: int
        """
        return self._online_count

    @online_count.setter
    def online_count(self, online_count):
        """Sets the online_count of this ListEnvInstancesResponse.

        在线实例总数。

        :param online_count: The online_count of this ListEnvInstancesResponse.
        :type online_count: int
        """
        self._online_count = online_count

    @property
    def offline_count(self):
        """Gets the offline_count of this ListEnvInstancesResponse.

        离线实例总数。

        :return: The offline_count of this ListEnvInstancesResponse.
        :rtype: int
        """
        return self._offline_count

    @offline_count.setter
    def offline_count(self, offline_count):
        """Sets the offline_count of this ListEnvInstancesResponse.

        离线实例总数。

        :param offline_count: The offline_count of this ListEnvInstancesResponse.
        :type offline_count: int
        """
        self._offline_count = offline_count

    @property
    def disable_count(self):
        """Gets the disable_count of this ListEnvInstancesResponse.

        停止实例总数。

        :return: The disable_count of this ListEnvInstancesResponse.
        :rtype: int
        """
        return self._disable_count

    @disable_count.setter
    def disable_count(self, disable_count):
        """Sets the disable_count of this ListEnvInstancesResponse.

        停止实例总数。

        :param disable_count: The disable_count of this ListEnvInstancesResponse.
        :type disable_count: int
        """
        self._disable_count = disable_count

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
        if not isinstance(other, ListEnvInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
