# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClearGraph2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'graph_id': 'str',
        'clear_metadata': 'bool'
    }

    attribute_map = {
        'graph_id': 'graph_id',
        'clear_metadata': 'clear_metadata'
    }

    def __init__(self, graph_id=None, clear_metadata=None):
        """ClearGraph2Request

        The model defined in huaweicloud sdk

        :param graph_id: 图ID。
        :type graph_id: str
        :param clear_metadata: 是否清空图关联的元数据。建议清除。
        :type clear_metadata: bool
        """
        
        

        self._graph_id = None
        self._clear_metadata = None
        self.discriminator = None

        self.graph_id = graph_id
        if clear_metadata is not None:
            self.clear_metadata = clear_metadata

    @property
    def graph_id(self):
        """Gets the graph_id of this ClearGraph2Request.

        图ID。

        :return: The graph_id of this ClearGraph2Request.
        :rtype: str
        """
        return self._graph_id

    @graph_id.setter
    def graph_id(self, graph_id):
        """Sets the graph_id of this ClearGraph2Request.

        图ID。

        :param graph_id: The graph_id of this ClearGraph2Request.
        :type graph_id: str
        """
        self._graph_id = graph_id

    @property
    def clear_metadata(self):
        """Gets the clear_metadata of this ClearGraph2Request.

        是否清空图关联的元数据。建议清除。

        :return: The clear_metadata of this ClearGraph2Request.
        :rtype: bool
        """
        return self._clear_metadata

    @clear_metadata.setter
    def clear_metadata(self, clear_metadata):
        """Sets the clear_metadata of this ClearGraph2Request.

        是否清空图关联的元数据。建议清除。

        :param clear_metadata: The clear_metadata of this ClearGraph2Request.
        :type clear_metadata: bool
        """
        self._clear_metadata = clear_metadata

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
        if not isinstance(other, ClearGraph2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
