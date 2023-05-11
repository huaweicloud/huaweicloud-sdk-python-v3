# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExtensionEvaluationStarRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extension_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'extension_id': 'extension_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, extension_id=None, limit=None, offset=None):
        """ShowExtensionEvaluationStarRequest

        The model defined in huaweicloud sdk

        :param extension_id: 插件id
        :type extension_id: str
        :param limit: 每页显示的条目数量
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询
        :type offset: int
        """
        
        

        self._extension_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.extension_id = extension_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def extension_id(self):
        """Gets the extension_id of this ShowExtensionEvaluationStarRequest.

        插件id

        :return: The extension_id of this ShowExtensionEvaluationStarRequest.
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this ShowExtensionEvaluationStarRequest.

        插件id

        :param extension_id: The extension_id of this ShowExtensionEvaluationStarRequest.
        :type extension_id: str
        """
        self._extension_id = extension_id

    @property
    def limit(self):
        """Gets the limit of this ShowExtensionEvaluationStarRequest.

        每页显示的条目数量

        :return: The limit of this ShowExtensionEvaluationStarRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowExtensionEvaluationStarRequest.

        每页显示的条目数量

        :param limit: The limit of this ShowExtensionEvaluationStarRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowExtensionEvaluationStarRequest.

        偏移量，表示从此偏移量开始查询

        :return: The offset of this ShowExtensionEvaluationStarRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowExtensionEvaluationStarRequest.

        偏移量，表示从此偏移量开始查询

        :param offset: The offset of this ShowExtensionEvaluationStarRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowExtensionEvaluationStarRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
