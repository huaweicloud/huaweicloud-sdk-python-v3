# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableResourceIdsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'current_time': 'str',
        'shared_quota': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'current_time': 'current_time',
        'shared_quota': 'shared_quota'
    }

    def __init__(self, resource_id=None, current_time=None, shared_quota=None):
        r"""AvailableResourceIdsInfo

        The model defined in huaweicloud sdk

        :param resource_id: **参数解释**： 资源ID **取值范围**： 字符长度1-256位
        :type resource_id: str
        :param current_time: **参数解释**： 当前时间 **取值范围**： 字符长度1-64位
        :type current_time: str
        :param shared_quota: **参数解释**： 是否共享配额 **取值范围**：   - shared：共享的   - unshared：非共享的
        :type shared_quota: str
        """
        
        

        self._resource_id = None
        self._current_time = None
        self._shared_quota = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if current_time is not None:
            self.current_time = current_time
        if shared_quota is not None:
            self.shared_quota = shared_quota

    @property
    def resource_id(self):
        r"""Gets the resource_id of this AvailableResourceIdsInfo.

        **参数解释**： 资源ID **取值范围**： 字符长度1-256位

        :return: The resource_id of this AvailableResourceIdsInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this AvailableResourceIdsInfo.

        **参数解释**： 资源ID **取值范围**： 字符长度1-256位

        :param resource_id: The resource_id of this AvailableResourceIdsInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def current_time(self):
        r"""Gets the current_time of this AvailableResourceIdsInfo.

        **参数解释**： 当前时间 **取值范围**： 字符长度1-64位

        :return: The current_time of this AvailableResourceIdsInfo.
        :rtype: str
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        r"""Sets the current_time of this AvailableResourceIdsInfo.

        **参数解释**： 当前时间 **取值范围**： 字符长度1-64位

        :param current_time: The current_time of this AvailableResourceIdsInfo.
        :type current_time: str
        """
        self._current_time = current_time

    @property
    def shared_quota(self):
        r"""Gets the shared_quota of this AvailableResourceIdsInfo.

        **参数解释**： 是否共享配额 **取值范围**：   - shared：共享的   - unshared：非共享的

        :return: The shared_quota of this AvailableResourceIdsInfo.
        :rtype: str
        """
        return self._shared_quota

    @shared_quota.setter
    def shared_quota(self, shared_quota):
        r"""Sets the shared_quota of this AvailableResourceIdsInfo.

        **参数解释**： 是否共享配额 **取值范围**：   - shared：共享的   - unshared：非共享的

        :param shared_quota: The shared_quota of this AvailableResourceIdsInfo.
        :type shared_quota: str
        """
        self._shared_quota = shared_quota

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
        if not isinstance(other, AvailableResourceIdsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
