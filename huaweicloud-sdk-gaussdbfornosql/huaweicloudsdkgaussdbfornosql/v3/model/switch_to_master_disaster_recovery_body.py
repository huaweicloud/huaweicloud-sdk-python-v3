# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchToMasterDisasterRecoveryBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'force': 'bool'
    }

    attribute_map = {
        'force': 'force'
    }

    def __init__(self, force=None):
        r"""SwitchToMasterDisasterRecoveryBody

        The model defined in huaweicloud sdk

        :param force: 是否强制备实例升主。 若为True，则强制备实例升主，用于在主实例异常的状态下，快速恢复服务的场景：允许备实例强制升为特殊主实例，独立提供读写服务。 默认为False，用于正常状态下备实例平缓升主。
        :type force: bool
        """
        
        

        self._force = None
        self.discriminator = None

        if force is not None:
            self.force = force

    @property
    def force(self):
        r"""Gets the force of this SwitchToMasterDisasterRecoveryBody.

        是否强制备实例升主。 若为True，则强制备实例升主，用于在主实例异常的状态下，快速恢复服务的场景：允许备实例强制升为特殊主实例，独立提供读写服务。 默认为False，用于正常状态下备实例平缓升主。

        :return: The force of this SwitchToMasterDisasterRecoveryBody.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        r"""Sets the force of this SwitchToMasterDisasterRecoveryBody.

        是否强制备实例升主。 若为True，则强制备实例升主，用于在主实例异常的状态下，快速恢复服务的场景：允许备实例强制升为特殊主实例，独立提供读写服务。 默认为False，用于正常状态下备实例平缓升主。

        :param force: The force of this SwitchToMasterDisasterRecoveryBody.
        :type force: bool
        """
        self._force = force

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
        if not isinstance(other, SwitchToMasterDisasterRecoveryBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
