# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DateTitleDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'day': 'str',
        'commits_count': 'int'
    }

    attribute_map = {
        'day': 'day',
        'commits_count': 'commits_count'
    }

    def __init__(self, day=None, commits_count=None):
        r"""DateTitleDto

        The model defined in huaweicloud sdk

        :param day: 时间（天）
        :type day: str
        :param commits_count: 提交数量
        :type commits_count: int
        """
        
        

        self._day = None
        self._commits_count = None
        self.discriminator = None

        if day is not None:
            self.day = day
        if commits_count is not None:
            self.commits_count = commits_count

    @property
    def day(self):
        r"""Gets the day of this DateTitleDto.

        时间（天）

        :return: The day of this DateTitleDto.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        r"""Sets the day of this DateTitleDto.

        时间（天）

        :param day: The day of this DateTitleDto.
        :type day: str
        """
        self._day = day

    @property
    def commits_count(self):
        r"""Gets the commits_count of this DateTitleDto.

        提交数量

        :return: The commits_count of this DateTitleDto.
        :rtype: int
        """
        return self._commits_count

    @commits_count.setter
    def commits_count(self, commits_count):
        r"""Sets the commits_count of this DateTitleDto.

        提交数量

        :param commits_count: The commits_count of this DateTitleDto.
        :type commits_count: int
        """
        self._commits_count = commits_count

    def to_dict(self):
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
        if not isinstance(other, DateTitleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
