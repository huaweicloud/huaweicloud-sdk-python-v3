# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePreBootPolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'is_pre_boot': 'bool'
    }

    attribute_map = {
        'ids': 'ids',
        'is_pre_boot': 'is_pre_boot'
    }

    def __init__(self, ids=None, is_pre_boot=None):
        r"""UpdatePreBootPolicyReq

        The model defined in huaweicloud sdk

        :param ids: 应用ID,最多同时操作5个。
        :type ids: list[str]
        :param is_pre_boot: 是否设置应用预启动。
        :type is_pre_boot: bool
        """
        
        

        self._ids = None
        self._is_pre_boot = None
        self.discriminator = None

        self.ids = ids
        self.is_pre_boot = is_pre_boot

    @property
    def ids(self):
        r"""Gets the ids of this UpdatePreBootPolicyReq.

        应用ID,最多同时操作5个。

        :return: The ids of this UpdatePreBootPolicyReq.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this UpdatePreBootPolicyReq.

        应用ID,最多同时操作5个。

        :param ids: The ids of this UpdatePreBootPolicyReq.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def is_pre_boot(self):
        r"""Gets the is_pre_boot of this UpdatePreBootPolicyReq.

        是否设置应用预启动。

        :return: The is_pre_boot of this UpdatePreBootPolicyReq.
        :rtype: bool
        """
        return self._is_pre_boot

    @is_pre_boot.setter
    def is_pre_boot(self, is_pre_boot):
        r"""Sets the is_pre_boot of this UpdatePreBootPolicyReq.

        是否设置应用预启动。

        :param is_pre_boot: The is_pre_boot of this UpdatePreBootPolicyReq.
        :type is_pre_boot: bool
        """
        self._is_pre_boot = is_pre_boot

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
        if not isinstance(other, UpdatePreBootPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
