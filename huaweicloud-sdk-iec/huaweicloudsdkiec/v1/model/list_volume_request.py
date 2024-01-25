# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVolumeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'name': 'str',
        'offset': 'int',
        'status': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'status': 'status'
    }

    def __init__(self, limit=None, name=None, offset=None, status=None):
        """ListVolumeRequest

        The model defined in huaweicloud sdk

        :param limit: 查询硬盘列表当前页面的数量。 取值范围：0~1000
        :type limit: int
        :param name: 根据名称查询硬盘列表。
        :type name: str
        :param offset: 查询的偏移量。默认为0
        :type offset: int
        :param status: 根据状态查询硬盘列表。
        :type status: str
        """
        
        

        self._limit = None
        self._name = None
        self._offset = None
        self._status = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status

    @property
    def limit(self):
        """Gets the limit of this ListVolumeRequest.

        查询硬盘列表当前页面的数量。 取值范围：0~1000

        :return: The limit of this ListVolumeRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVolumeRequest.

        查询硬盘列表当前页面的数量。 取值范围：0~1000

        :param limit: The limit of this ListVolumeRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListVolumeRequest.

        根据名称查询硬盘列表。

        :return: The name of this ListVolumeRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListVolumeRequest.

        根据名称查询硬盘列表。

        :param name: The name of this ListVolumeRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListVolumeRequest.

        查询的偏移量。默认为0

        :return: The offset of this ListVolumeRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVolumeRequest.

        查询的偏移量。默认为0

        :param offset: The offset of this ListVolumeRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        """Gets the status of this ListVolumeRequest.

        根据状态查询硬盘列表。

        :return: The status of this ListVolumeRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListVolumeRequest.

        根据状态查询硬盘列表。

        :param status: The status of this ListVolumeRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListVolumeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
