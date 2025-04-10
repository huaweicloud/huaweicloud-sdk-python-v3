# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VaultBatchUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'smn_notify': 'bool',
        'threshold': 'int'
    }

    attribute_map = {
        'smn_notify': 'smn_notify',
        'threshold': 'threshold'
    }

    def __init__(self, smn_notify=None, threshold=None):
        r"""VaultBatchUpdate

        The model defined in huaweicloud sdk

        :param smn_notify: 存储库smn消息通知开关
        :type smn_notify: bool
        :param threshold: 存储库容量阈值
        :type threshold: int
        """
        
        

        self._smn_notify = None
        self._threshold = None
        self.discriminator = None

        if smn_notify is not None:
            self.smn_notify = smn_notify
        if threshold is not None:
            self.threshold = threshold

    @property
    def smn_notify(self):
        r"""Gets the smn_notify of this VaultBatchUpdate.

        存储库smn消息通知开关

        :return: The smn_notify of this VaultBatchUpdate.
        :rtype: bool
        """
        return self._smn_notify

    @smn_notify.setter
    def smn_notify(self, smn_notify):
        r"""Sets the smn_notify of this VaultBatchUpdate.

        存储库smn消息通知开关

        :param smn_notify: The smn_notify of this VaultBatchUpdate.
        :type smn_notify: bool
        """
        self._smn_notify = smn_notify

    @property
    def threshold(self):
        r"""Gets the threshold of this VaultBatchUpdate.

        存储库容量阈值

        :return: The threshold of this VaultBatchUpdate.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this VaultBatchUpdate.

        存储库容量阈值

        :param threshold: The threshold of this VaultBatchUpdate.
        :type threshold: int
        """
        self._threshold = threshold

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
        if not isinstance(other, VaultBatchUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
