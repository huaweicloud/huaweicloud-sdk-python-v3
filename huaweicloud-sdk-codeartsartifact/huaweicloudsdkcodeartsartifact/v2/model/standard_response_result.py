# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StandardResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[ReleaseFileVersionDo]',
        'total_records': 'int',
        'total_pages': 'int'
    }

    attribute_map = {
        'data': 'data',
        'total_records': 'total_records',
        'total_pages': 'total_pages'
    }

    def __init__(self, data=None, total_records=None, total_pages=None):
        """StandardResponseResult

        The model defined in huaweicloud sdk

        :param data: 符合条件的结果列表
        :type data: list[:class:`huaweicloudsdkcodeartsartifact.v2.ReleaseFileVersionDo`]
        :param total_records: 符合条件的结果总数
        :type total_records: int
        :param total_pages: 符合条件的结果总页数
        :type total_pages: int
        """
        
        

        self._data = None
        self._total_records = None
        self._total_pages = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if total_records is not None:
            self.total_records = total_records
        if total_pages is not None:
            self.total_pages = total_pages

    @property
    def data(self):
        """Gets the data of this StandardResponseResult.

        符合条件的结果列表

        :return: The data of this StandardResponseResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsartifact.v2.ReleaseFileVersionDo`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this StandardResponseResult.

        符合条件的结果列表

        :param data: The data of this StandardResponseResult.
        :type data: list[:class:`huaweicloudsdkcodeartsartifact.v2.ReleaseFileVersionDo`]
        """
        self._data = data

    @property
    def total_records(self):
        """Gets the total_records of this StandardResponseResult.

        符合条件的结果总数

        :return: The total_records of this StandardResponseResult.
        :rtype: int
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this StandardResponseResult.

        符合条件的结果总数

        :param total_records: The total_records of this StandardResponseResult.
        :type total_records: int
        """
        self._total_records = total_records

    @property
    def total_pages(self):
        """Gets the total_pages of this StandardResponseResult.

        符合条件的结果总页数

        :return: The total_pages of this StandardResponseResult.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this StandardResponseResult.

        符合条件的结果总页数

        :param total_pages: The total_pages of this StandardResponseResult.
        :type total_pages: int
        """
        self._total_pages = total_pages

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
        if not isinstance(other, StandardResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
