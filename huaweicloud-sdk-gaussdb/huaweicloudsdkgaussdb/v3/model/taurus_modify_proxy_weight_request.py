# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaurusModifyProxyWeightRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_weight': 'int',
        'readonly_nodes': 'list[ModifyProxyWeightReadonlyNode]'
    }

    attribute_map = {
        'master_weight': 'master_weight',
        'readonly_nodes': 'readonly_nodes'
    }

    def __init__(self, master_weight=None, readonly_nodes=None):
        """TaurusModifyProxyWeightRequest

        The model defined in huaweicloud sdk

        :param master_weight: 主节点权重
        :type master_weight: int
        :param readonly_nodes: 只读节点权重配置信息
        :type readonly_nodes: list[:class:`huaweicloudsdkgaussdb.v3.ModifyProxyWeightReadonlyNode`]
        """
        
        

        self._master_weight = None
        self._readonly_nodes = None
        self.discriminator = None

        if master_weight is not None:
            self.master_weight = master_weight
        if readonly_nodes is not None:
            self.readonly_nodes = readonly_nodes

    @property
    def master_weight(self):
        """Gets the master_weight of this TaurusModifyProxyWeightRequest.

        主节点权重

        :return: The master_weight of this TaurusModifyProxyWeightRequest.
        :rtype: int
        """
        return self._master_weight

    @master_weight.setter
    def master_weight(self, master_weight):
        """Sets the master_weight of this TaurusModifyProxyWeightRequest.

        主节点权重

        :param master_weight: The master_weight of this TaurusModifyProxyWeightRequest.
        :type master_weight: int
        """
        self._master_weight = master_weight

    @property
    def readonly_nodes(self):
        """Gets the readonly_nodes of this TaurusModifyProxyWeightRequest.

        只读节点权重配置信息

        :return: The readonly_nodes of this TaurusModifyProxyWeightRequest.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ModifyProxyWeightReadonlyNode`]
        """
        return self._readonly_nodes

    @readonly_nodes.setter
    def readonly_nodes(self, readonly_nodes):
        """Sets the readonly_nodes of this TaurusModifyProxyWeightRequest.

        只读节点权重配置信息

        :param readonly_nodes: The readonly_nodes of this TaurusModifyProxyWeightRequest.
        :type readonly_nodes: list[:class:`huaweicloudsdkgaussdb.v3.ModifyProxyWeightReadonlyNode`]
        """
        self._readonly_nodes = readonly_nodes

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
        if not isinstance(other, TaurusModifyProxyWeightRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
