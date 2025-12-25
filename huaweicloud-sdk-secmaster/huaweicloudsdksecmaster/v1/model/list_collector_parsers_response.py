# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectorParsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'records': 'list[Parser]'
    }

    attribute_map = {
        'count': 'count',
        'records': 'records'
    }

    def __init__(self, count=None, records=None):
        r"""ListCollectorParsersResponse

        The model defined in huaweicloud sdk

        :param count: 计数
        :type count: int
        :param records: 相关描述信息
        :type records: list[:class:`huaweicloudsdksecmaster.v1.Parser`]
        """
        
        super().__init__()

        self._count = None
        self._records = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if records is not None:
            self.records = records

    @property
    def count(self):
        r"""Gets the count of this ListCollectorParsersResponse.

        计数

        :return: The count of this ListCollectorParsersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListCollectorParsersResponse.

        计数

        :param count: The count of this ListCollectorParsersResponse.
        :type count: int
        """
        self._count = count

    @property
    def records(self):
        r"""Gets the records of this ListCollectorParsersResponse.

        相关描述信息

        :return: The records of this ListCollectorParsersResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Parser`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListCollectorParsersResponse.

        相关描述信息

        :param records: The records of this ListCollectorParsersResponse.
        :type records: list[:class:`huaweicloudsdksecmaster.v1.Parser`]
        """
        self._records = records

    def to_dict(self):
        import warnings
        warnings.warn("ListCollectorParsersResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListCollectorParsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
