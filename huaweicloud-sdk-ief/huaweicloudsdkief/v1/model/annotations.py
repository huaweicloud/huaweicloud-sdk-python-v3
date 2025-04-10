# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Annotations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ring_controller': 'str',
        'autonomy_edge_selector': 'str'
    }

    attribute_map = {
        'ring_controller': 'ring_controller',
        'autonomy_edge_selector': 'autonomy_edge_selector'
    }

    def __init__(self, ring_controller=None, autonomy_edge_selector=None):
        r"""Annotations

        The model defined in huaweicloud sdk

        :param ring_controller: 生成ranktablefile。该参数目前只支持赋值\&quot;ascend-1980\&quot;。
        :type ring_controller: str
        :param autonomy_edge_selector: 离线自愈功能配置字段，须填写调度的节点组id
        :type autonomy_edge_selector: str
        """
        
        

        self._ring_controller = None
        self._autonomy_edge_selector = None
        self.discriminator = None

        if ring_controller is not None:
            self.ring_controller = ring_controller
        if autonomy_edge_selector is not None:
            self.autonomy_edge_selector = autonomy_edge_selector

    @property
    def ring_controller(self):
        r"""Gets the ring_controller of this Annotations.

        生成ranktablefile。该参数目前只支持赋值\"ascend-1980\"。

        :return: The ring_controller of this Annotations.
        :rtype: str
        """
        return self._ring_controller

    @ring_controller.setter
    def ring_controller(self, ring_controller):
        r"""Sets the ring_controller of this Annotations.

        生成ranktablefile。该参数目前只支持赋值\"ascend-1980\"。

        :param ring_controller: The ring_controller of this Annotations.
        :type ring_controller: str
        """
        self._ring_controller = ring_controller

    @property
    def autonomy_edge_selector(self):
        r"""Gets the autonomy_edge_selector of this Annotations.

        离线自愈功能配置字段，须填写调度的节点组id

        :return: The autonomy_edge_selector of this Annotations.
        :rtype: str
        """
        return self._autonomy_edge_selector

    @autonomy_edge_selector.setter
    def autonomy_edge_selector(self, autonomy_edge_selector):
        r"""Sets the autonomy_edge_selector of this Annotations.

        离线自愈功能配置字段，须填写调度的节点组id

        :param autonomy_edge_selector: The autonomy_edge_selector of this Annotations.
        :type autonomy_edge_selector: str
        """
        self._autonomy_edge_selector = autonomy_edge_selector

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
        if not isinstance(other, Annotations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
