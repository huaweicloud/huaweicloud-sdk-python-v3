# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScanClientsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'clean_cache': 'bool'
    }

    attribute_map = {
        'node_id': 'node_id',
        'clean_cache': 'clean_cache'
    }

    def __init__(self, node_id=None, clean_cache=None):
        r"""ScanClientsRequestBody

        The model defined in huaweicloud sdk

        :param node_id: 节点ID
        :type node_id: str
        :param clean_cache: 是否重新查询并保存会话列表
        :type clean_cache: bool
        """
        
        

        self._node_id = None
        self._clean_cache = None
        self.discriminator = None

        self.node_id = node_id
        if clean_cache is not None:
            self.clean_cache = clean_cache

    @property
    def node_id(self):
        r"""Gets the node_id of this ScanClientsRequestBody.

        节点ID

        :return: The node_id of this ScanClientsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ScanClientsRequestBody.

        节点ID

        :param node_id: The node_id of this ScanClientsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def clean_cache(self):
        r"""Gets the clean_cache of this ScanClientsRequestBody.

        是否重新查询并保存会话列表

        :return: The clean_cache of this ScanClientsRequestBody.
        :rtype: bool
        """
        return self._clean_cache

    @clean_cache.setter
    def clean_cache(self, clean_cache):
        r"""Sets the clean_cache of this ScanClientsRequestBody.

        是否重新查询并保存会话列表

        :param clean_cache: The clean_cache of this ScanClientsRequestBody.
        :type clean_cache: bool
        """
        self._clean_cache = clean_cache

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
        if not isinstance(other, ScanClientsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
