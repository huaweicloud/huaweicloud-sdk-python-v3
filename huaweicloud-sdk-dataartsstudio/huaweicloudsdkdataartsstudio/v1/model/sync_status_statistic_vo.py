# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncStatusStatisticVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'str',
        'failed': 'str',
        'running': 'str',
        'other': 'str'
    }

    attribute_map = {
        'success': 'success',
        'failed': 'failed',
        'running': 'running',
        'other': 'other'
    }

    def __init__(self, success=None, failed=None, running=None, other=None):
        """SyncStatusStatisticVO

        The model defined in huaweicloud sdk

        :param success: 成功数，填写String类型替代Long类型。
        :type success: str
        :param failed: 失败数，填写String类型替代Long类型。
        :type failed: str
        :param running: 同步中，填写String类型替代Long类型。
        :type running: str
        :param other: 未同步数，填写String类型替代Long类型。
        :type other: str
        """
        
        

        self._success = None
        self._failed = None
        self._running = None
        self._other = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if failed is not None:
            self.failed = failed
        if running is not None:
            self.running = running
        if other is not None:
            self.other = other

    @property
    def success(self):
        """Gets the success of this SyncStatusStatisticVO.

        成功数，填写String类型替代Long类型。

        :return: The success of this SyncStatusStatisticVO.
        :rtype: str
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this SyncStatusStatisticVO.

        成功数，填写String类型替代Long类型。

        :param success: The success of this SyncStatusStatisticVO.
        :type success: str
        """
        self._success = success

    @property
    def failed(self):
        """Gets the failed of this SyncStatusStatisticVO.

        失败数，填写String类型替代Long类型。

        :return: The failed of this SyncStatusStatisticVO.
        :rtype: str
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this SyncStatusStatisticVO.

        失败数，填写String类型替代Long类型。

        :param failed: The failed of this SyncStatusStatisticVO.
        :type failed: str
        """
        self._failed = failed

    @property
    def running(self):
        """Gets the running of this SyncStatusStatisticVO.

        同步中，填写String类型替代Long类型。

        :return: The running of this SyncStatusStatisticVO.
        :rtype: str
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this SyncStatusStatisticVO.

        同步中，填写String类型替代Long类型。

        :param running: The running of this SyncStatusStatisticVO.
        :type running: str
        """
        self._running = running

    @property
    def other(self):
        """Gets the other of this SyncStatusStatisticVO.

        未同步数，填写String类型替代Long类型。

        :return: The other of this SyncStatusStatisticVO.
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this SyncStatusStatisticVO.

        未同步数，填写String类型替代Long类型。

        :param other: The other of this SyncStatusStatisticVO.
        :type other: str
        """
        self._other = other

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
        if not isinstance(other, SyncStatusStatisticVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
