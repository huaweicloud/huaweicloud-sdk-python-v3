# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchoverRatioInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'switchover_ratio': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'switchover_ratio': 'switchover_ratio'
    }

    def __init__(self, instance_id=None, switchover_ratio=None):
        r"""SwitchoverRatioInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param switchover_ratio: 容灾切换的故障节点比例，下限是50，步长是10，最大是100，默认为100。
        :type switchover_ratio: int
        """
        
        

        self._instance_id = None
        self._switchover_ratio = None
        self.discriminator = None

        self.instance_id = instance_id
        if switchover_ratio is not None:
            self.switchover_ratio = switchover_ratio

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SwitchoverRatioInfo.

        实例ID。

        :return: The instance_id of this SwitchoverRatioInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SwitchoverRatioInfo.

        实例ID。

        :param instance_id: The instance_id of this SwitchoverRatioInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def switchover_ratio(self):
        r"""Gets the switchover_ratio of this SwitchoverRatioInfo.

        容灾切换的故障节点比例，下限是50，步长是10，最大是100，默认为100。

        :return: The switchover_ratio of this SwitchoverRatioInfo.
        :rtype: int
        """
        return self._switchover_ratio

    @switchover_ratio.setter
    def switchover_ratio(self, switchover_ratio):
        r"""Sets the switchover_ratio of this SwitchoverRatioInfo.

        容灾切换的故障节点比例，下限是50，步长是10，最大是100，默认为100。

        :param switchover_ratio: The switchover_ratio of this SwitchoverRatioInfo.
        :type switchover_ratio: int
        """
        self._switchover_ratio = switchover_ratio

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
        if not isinstance(other, SwitchoverRatioInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
