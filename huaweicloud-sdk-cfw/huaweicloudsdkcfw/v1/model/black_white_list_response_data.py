# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlackWhiteListResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'total': 'int',
        'records': 'list[BlackWhiteListResponseDataRecords]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total',
        'records': 'records'
    }

    def __init__(self, offset=None, limit=None, total=None, records=None):
        r"""BlackWhiteListResponseData

        The model defined in huaweicloud sdk

        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param total: 查询黑白名单总条数
        :type total: int
        :param records: 黑白名单列表
        :type records: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteListResponseDataRecords`]
        """
        
        

        self._offset = None
        self._limit = None
        self._total = None
        self._records = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if records is not None:
            self.records = records

    @property
    def offset(self):
        r"""Gets the offset of this BlackWhiteListResponseData.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this BlackWhiteListResponseData.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BlackWhiteListResponseData.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this BlackWhiteListResponseData.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this BlackWhiteListResponseData.

        每页显示个数，范围为1-1024

        :return: The limit of this BlackWhiteListResponseData.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BlackWhiteListResponseData.

        每页显示个数，范围为1-1024

        :param limit: The limit of this BlackWhiteListResponseData.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this BlackWhiteListResponseData.

        查询黑白名单总条数

        :return: The total of this BlackWhiteListResponseData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this BlackWhiteListResponseData.

        查询黑白名单总条数

        :param total: The total of this BlackWhiteListResponseData.
        :type total: int
        """
        self._total = total

    @property
    def records(self):
        r"""Gets the records of this BlackWhiteListResponseData.

        黑白名单列表

        :return: The records of this BlackWhiteListResponseData.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteListResponseDataRecords`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this BlackWhiteListResponseData.

        黑白名单列表

        :param records: The records of this BlackWhiteListResponseData.
        :type records: list[:class:`huaweicloudsdkcfw.v1.BlackWhiteListResponseDataRecords`]
        """
        self._records = records

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
        if not isinstance(other, BlackWhiteListResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
