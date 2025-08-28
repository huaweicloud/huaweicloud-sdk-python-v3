# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecycleBinPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recycle_threshold_hour': 'int',
        'retention_hour': 'int'
    }

    attribute_map = {
        'recycle_threshold_hour': 'recycle_threshold_hour',
        'retention_hour': 'retention_hour'
    }

    def __init__(self, recycle_threshold_hour=None, retention_hour=None):
        r"""RecycleBinPolicy

        The model defined in huaweicloud sdk

        :param recycle_threshold_hour: **参数解释**：允许进入回收站的最小创建时间，不足此时长则删除时不满足进入回收站的条件。  **取值范围**：不涉及
        :type recycle_threshold_hour: int
        :param retention_hour: **参数解释**：进入回收站的最大保留时长。  **取值范围**：不涉及
        :type retention_hour: int
        """
        
        

        self._recycle_threshold_hour = None
        self._retention_hour = None
        self.discriminator = None

        if recycle_threshold_hour is not None:
            self.recycle_threshold_hour = recycle_threshold_hour
        if retention_hour is not None:
            self.retention_hour = retention_hour

    @property
    def recycle_threshold_hour(self):
        r"""Gets the recycle_threshold_hour of this RecycleBinPolicy.

        **参数解释**：允许进入回收站的最小创建时间，不足此时长则删除时不满足进入回收站的条件。  **取值范围**：不涉及

        :return: The recycle_threshold_hour of this RecycleBinPolicy.
        :rtype: int
        """
        return self._recycle_threshold_hour

    @recycle_threshold_hour.setter
    def recycle_threshold_hour(self, recycle_threshold_hour):
        r"""Sets the recycle_threshold_hour of this RecycleBinPolicy.

        **参数解释**：允许进入回收站的最小创建时间，不足此时长则删除时不满足进入回收站的条件。  **取值范围**：不涉及

        :param recycle_threshold_hour: The recycle_threshold_hour of this RecycleBinPolicy.
        :type recycle_threshold_hour: int
        """
        self._recycle_threshold_hour = recycle_threshold_hour

    @property
    def retention_hour(self):
        r"""Gets the retention_hour of this RecycleBinPolicy.

        **参数解释**：进入回收站的最大保留时长。  **取值范围**：不涉及

        :return: The retention_hour of this RecycleBinPolicy.
        :rtype: int
        """
        return self._retention_hour

    @retention_hour.setter
    def retention_hour(self, retention_hour):
        r"""Sets the retention_hour of this RecycleBinPolicy.

        **参数解释**：进入回收站的最大保留时长。  **取值范围**：不涉及

        :param retention_hour: The retention_hour of this RecycleBinPolicy.
        :type retention_hour: int
        """
        self._retention_hour = retention_hour

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
        if not isinstance(other, RecycleBinPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
