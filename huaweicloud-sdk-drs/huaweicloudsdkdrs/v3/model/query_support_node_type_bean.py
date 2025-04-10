# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySupportNodeTypeBean:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_type': 'str',
        'is_sellout': 'bool'
    }

    attribute_map = {
        'node_type': 'node_type',
        'is_sellout': 'is_sellout'
    }

    def __init__(self, node_type=None, is_sellout=None):
        r"""QuerySupportNodeTypeBean

        The model defined in huaweicloud sdk

        :param node_type: 规格类型
        :type node_type: str
        :param is_sellout: 是否售罄
        :type is_sellout: bool
        """
        
        

        self._node_type = None
        self._is_sellout = None
        self.discriminator = None

        if node_type is not None:
            self.node_type = node_type
        if is_sellout is not None:
            self.is_sellout = is_sellout

    @property
    def node_type(self):
        r"""Gets the node_type of this QuerySupportNodeTypeBean.

        规格类型

        :return: The node_type of this QuerySupportNodeTypeBean.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this QuerySupportNodeTypeBean.

        规格类型

        :param node_type: The node_type of this QuerySupportNodeTypeBean.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def is_sellout(self):
        r"""Gets the is_sellout of this QuerySupportNodeTypeBean.

        是否售罄

        :return: The is_sellout of this QuerySupportNodeTypeBean.
        :rtype: bool
        """
        return self._is_sellout

    @is_sellout.setter
    def is_sellout(self, is_sellout):
        r"""Sets the is_sellout of this QuerySupportNodeTypeBean.

        是否售罄

        :param is_sellout: The is_sellout of this QuerySupportNodeTypeBean.
        :type is_sellout: bool
        """
        self._is_sellout = is_sellout

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
        if not isinstance(other, QuerySupportNodeTypeBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
