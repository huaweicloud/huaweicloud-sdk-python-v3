# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIterationHistoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iteration_id': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'iteration_id': 'iteration_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, iteration_id=None, offset=None, limit=None):
        """ListIterationHistoriesRequest

        The model defined in huaweicloud sdk

        :param iteration_id: 迭代id
        :type iteration_id: int
        :param offset: 偏移量
        :type offset: int
        :param limit: 每页数量，最大为100
        :type limit: int
        """
        
        

        self._iteration_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.iteration_id = iteration_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def iteration_id(self):
        """Gets the iteration_id of this ListIterationHistoriesRequest.

        迭代id

        :return: The iteration_id of this ListIterationHistoriesRequest.
        :rtype: int
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this ListIterationHistoriesRequest.

        迭代id

        :param iteration_id: The iteration_id of this ListIterationHistoriesRequest.
        :type iteration_id: int
        """
        self._iteration_id = iteration_id

    @property
    def offset(self):
        """Gets the offset of this ListIterationHistoriesRequest.

        偏移量

        :return: The offset of this ListIterationHistoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIterationHistoriesRequest.

        偏移量

        :param offset: The offset of this ListIterationHistoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListIterationHistoriesRequest.

        每页数量，最大为100

        :return: The limit of this ListIterationHistoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIterationHistoriesRequest.

        每页数量，最大为100

        :param limit: The limit of this ListIterationHistoriesRequest.
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
        if not isinstance(other, ListIterationHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
