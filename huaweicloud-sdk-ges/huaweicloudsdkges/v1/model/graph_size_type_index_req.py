# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GraphSizeTypeIndexReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'graph_size_type_index': 'str'
    }

    attribute_map = {
        'graph_size_type_index': 'graphSizeTypeIndex'
    }

    def __init__(self, graph_size_type_index=None):
        r"""GraphSizeTypeIndexReq

        The model defined in huaweicloud sdk

        :param graph_size_type_index: 图规格类型，当前支持取值为\&quot;2\&quot;,\&quot;3\&quot;,\&quot;4\&quot;,\&quot;5\&quot;分别代表扩容成千万边、一亿边、十亿边、百亿边规格的图
        :type graph_size_type_index: str
        """
        
        

        self._graph_size_type_index = None
        self.discriminator = None

        self.graph_size_type_index = graph_size_type_index

    @property
    def graph_size_type_index(self):
        r"""Gets the graph_size_type_index of this GraphSizeTypeIndexReq.

        图规格类型，当前支持取值为\"2\",\"3\",\"4\",\"5\"分别代表扩容成千万边、一亿边、十亿边、百亿边规格的图

        :return: The graph_size_type_index of this GraphSizeTypeIndexReq.
        :rtype: str
        """
        return self._graph_size_type_index

    @graph_size_type_index.setter
    def graph_size_type_index(self, graph_size_type_index):
        r"""Sets the graph_size_type_index of this GraphSizeTypeIndexReq.

        图规格类型，当前支持取值为\"2\",\"3\",\"4\",\"5\"分别代表扩容成千万边、一亿边、十亿边、百亿边规格的图

        :param graph_size_type_index: The graph_size_type_index of this GraphSizeTypeIndexReq.
        :type graph_size_type_index: str
        """
        self._graph_size_type_index = graph_size_type_index

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
        if not isinstance(other, GraphSizeTypeIndexReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
