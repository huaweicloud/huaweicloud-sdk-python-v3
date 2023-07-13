# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSpecsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, spec_code=None, offset=None, limit=None):
        """ListSpecsRequest

        The model defined in huaweicloud sdk

        :param spec_code: 规格编码
        :type spec_code: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 单次查询个数
        :type limit: int
        """
        
        

        self._spec_code = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if spec_code is not None:
            self.spec_code = spec_code
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def spec_code(self):
        """Gets the spec_code of this ListSpecsRequest.

        规格编码

        :return: The spec_code of this ListSpecsRequest.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ListSpecsRequest.

        规格编码

        :param spec_code: The spec_code of this ListSpecsRequest.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def offset(self):
        """Gets the offset of this ListSpecsRequest.

        偏移量

        :return: The offset of this ListSpecsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSpecsRequest.

        偏移量

        :param offset: The offset of this ListSpecsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSpecsRequest.

        单次查询个数

        :return: The limit of this ListSpecsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSpecsRequest.

        单次查询个数

        :param limit: The limit of this ListSpecsRequest.
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
        if not isinstance(other, ListSpecsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
