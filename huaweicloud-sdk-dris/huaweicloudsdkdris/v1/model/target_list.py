# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_rsu_ids': 'list[str]',
        'target_obu_ids': 'list[str]'
    }

    attribute_map = {
        'target_rsu_ids': 'target_rsu_ids',
        'target_obu_ids': 'target_obu_ids'
    }

    def __init__(self, target_rsu_ids=None, target_obu_ids=None):
        """TargetList

        The model defined in huaweicloud sdk

        :param target_rsu_ids: **参数说明**：通过LTE-PC5传输通道（by_lte_pc5参数值为true）下发的rsu id列表。如果rsu id列表为空，则匹配事件范围内的在线rsu进行下发。
        :type target_rsu_ids: list[str]
        :param target_obu_ids: **参数说明**：通过LTE-Uu的传输通道（by_lte_uu参数值为true）下发的obu id列表。注意obu id列表不能为空。
        :type target_obu_ids: list[str]
        """
        
        

        self._target_rsu_ids = None
        self._target_obu_ids = None
        self.discriminator = None

        if target_rsu_ids is not None:
            self.target_rsu_ids = target_rsu_ids
        if target_obu_ids is not None:
            self.target_obu_ids = target_obu_ids

    @property
    def target_rsu_ids(self):
        """Gets the target_rsu_ids of this TargetList.

        **参数说明**：通过LTE-PC5传输通道（by_lte_pc5参数值为true）下发的rsu id列表。如果rsu id列表为空，则匹配事件范围内的在线rsu进行下发。

        :return: The target_rsu_ids of this TargetList.
        :rtype: list[str]
        """
        return self._target_rsu_ids

    @target_rsu_ids.setter
    def target_rsu_ids(self, target_rsu_ids):
        """Sets the target_rsu_ids of this TargetList.

        **参数说明**：通过LTE-PC5传输通道（by_lte_pc5参数值为true）下发的rsu id列表。如果rsu id列表为空，则匹配事件范围内的在线rsu进行下发。

        :param target_rsu_ids: The target_rsu_ids of this TargetList.
        :type target_rsu_ids: list[str]
        """
        self._target_rsu_ids = target_rsu_ids

    @property
    def target_obu_ids(self):
        """Gets the target_obu_ids of this TargetList.

        **参数说明**：通过LTE-Uu的传输通道（by_lte_uu参数值为true）下发的obu id列表。注意obu id列表不能为空。

        :return: The target_obu_ids of this TargetList.
        :rtype: list[str]
        """
        return self._target_obu_ids

    @target_obu_ids.setter
    def target_obu_ids(self, target_obu_ids):
        """Sets the target_obu_ids of this TargetList.

        **参数说明**：通过LTE-Uu的传输通道（by_lte_uu参数值为true）下发的obu id列表。注意obu id列表不能为空。

        :param target_obu_ids: The target_obu_ids of this TargetList.
        :type target_obu_ids: list[str]
        """
        self._target_obu_ids = target_obu_ids

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
        if not isinstance(other, TargetList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
