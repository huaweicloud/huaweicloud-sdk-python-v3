# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLineageBulkRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance': 'instance',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance=None, offset=None, limit=None):
        """ShowLineageBulkRequest

        The model defined in huaweicloud sdk

        :param instance: 实例id
        :type instance: str
        :param offset: 分页参数偏移量，默认值0
        :type offset: int
        :param limit: 分页参每页数量，默认值100
        :type limit: int
        """
        
        

        self._instance = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance = instance
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance(self):
        """Gets the instance of this ShowLineageBulkRequest.

        实例id

        :return: The instance of this ShowLineageBulkRequest.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ShowLineageBulkRequest.

        实例id

        :param instance: The instance of this ShowLineageBulkRequest.
        :type instance: str
        """
        self._instance = instance

    @property
    def offset(self):
        """Gets the offset of this ShowLineageBulkRequest.

        分页参数偏移量，默认值0

        :return: The offset of this ShowLineageBulkRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowLineageBulkRequest.

        分页参数偏移量，默认值0

        :param offset: The offset of this ShowLineageBulkRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowLineageBulkRequest.

        分页参每页数量，默认值100

        :return: The limit of this ShowLineageBulkRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowLineageBulkRequest.

        分页参每页数量，默认值100

        :param limit: The limit of this ShowLineageBulkRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowLineageBulkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
