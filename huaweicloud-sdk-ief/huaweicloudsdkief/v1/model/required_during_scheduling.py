# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequiredDuringScheduling:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_selector_terms': 'list[MatchExpressions]'
    }

    attribute_map = {
        'node_selector_terms': 'nodeSelectorTerms'
    }

    def __init__(self, node_selector_terms=None):
        r"""RequiredDuringScheduling

        The model defined in huaweicloud sdk

        :param node_selector_terms: 节点选择规则
        :type node_selector_terms: list[:class:`huaweicloudsdkief.v1.MatchExpressions`]
        """
        
        

        self._node_selector_terms = None
        self.discriminator = None

        if node_selector_terms is not None:
            self.node_selector_terms = node_selector_terms

    @property
    def node_selector_terms(self):
        r"""Gets the node_selector_terms of this RequiredDuringScheduling.

        节点选择规则

        :return: The node_selector_terms of this RequiredDuringScheduling.
        :rtype: list[:class:`huaweicloudsdkief.v1.MatchExpressions`]
        """
        return self._node_selector_terms

    @node_selector_terms.setter
    def node_selector_terms(self, node_selector_terms):
        r"""Sets the node_selector_terms of this RequiredDuringScheduling.

        节点选择规则

        :param node_selector_terms: The node_selector_terms of this RequiredDuringScheduling.
        :type node_selector_terms: list[:class:`huaweicloudsdkief.v1.MatchExpressions`]
        """
        self._node_selector_terms = node_selector_terms

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
        if not isinstance(other, RequiredDuringScheduling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
