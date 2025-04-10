# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyLb:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lbaas_listener': 'LbaasListener',
        'listener': 'str',
        'failed_reason': 'str',
        'failed_details': 'str'
    }

    attribute_map = {
        'lbaas_listener': 'lbaas_listener',
        'listener': 'listener',
        'failed_reason': 'failed_reason',
        'failed_details': 'failed_details'
    }

    def __init__(self, lbaas_listener=None, listener=None, failed_reason=None, failed_details=None):
        r"""ModifyLb

        The model defined in huaweicloud sdk

        :param lbaas_listener: 
        :type lbaas_listener: :class:`huaweicloudsdkas.v1.LbaasListener`
        :param listener: 经典型负载均衡器信息
        :type listener: str
        :param failed_reason: 负载均衡器迁移失败原因。
        :type failed_reason: str
        :param failed_details: 负载均衡器迁移失败详情。
        :type failed_details: str
        """
        
        

        self._lbaas_listener = None
        self._listener = None
        self._failed_reason = None
        self._failed_details = None
        self.discriminator = None

        if lbaas_listener is not None:
            self.lbaas_listener = lbaas_listener
        if listener is not None:
            self.listener = listener
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if failed_details is not None:
            self.failed_details = failed_details

    @property
    def lbaas_listener(self):
        r"""Gets the lbaas_listener of this ModifyLb.

        :return: The lbaas_listener of this ModifyLb.
        :rtype: :class:`huaweicloudsdkas.v1.LbaasListener`
        """
        return self._lbaas_listener

    @lbaas_listener.setter
    def lbaas_listener(self, lbaas_listener):
        r"""Sets the lbaas_listener of this ModifyLb.

        :param lbaas_listener: The lbaas_listener of this ModifyLb.
        :type lbaas_listener: :class:`huaweicloudsdkas.v1.LbaasListener`
        """
        self._lbaas_listener = lbaas_listener

    @property
    def listener(self):
        r"""Gets the listener of this ModifyLb.

        经典型负载均衡器信息

        :return: The listener of this ModifyLb.
        :rtype: str
        """
        return self._listener

    @listener.setter
    def listener(self, listener):
        r"""Sets the listener of this ModifyLb.

        经典型负载均衡器信息

        :param listener: The listener of this ModifyLb.
        :type listener: str
        """
        self._listener = listener

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ModifyLb.

        负载均衡器迁移失败原因。

        :return: The failed_reason of this ModifyLb.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ModifyLb.

        负载均衡器迁移失败原因。

        :param failed_reason: The failed_reason of this ModifyLb.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def failed_details(self):
        r"""Gets the failed_details of this ModifyLb.

        负载均衡器迁移失败详情。

        :return: The failed_details of this ModifyLb.
        :rtype: str
        """
        return self._failed_details

    @failed_details.setter
    def failed_details(self, failed_details):
        r"""Sets the failed_details of this ModifyLb.

        负载均衡器迁移失败详情。

        :param failed_details: The failed_details of this ModifyLb.
        :type failed_details: str
        """
        self._failed_details = failed_details

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
        if not isinstance(other, ModifyLb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
