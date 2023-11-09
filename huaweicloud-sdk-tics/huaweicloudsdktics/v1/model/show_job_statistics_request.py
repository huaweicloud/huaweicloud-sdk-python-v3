# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'league_id': 'str',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'league_id': 'league_id',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, league_id=None, start_date=None, end_date=None):
        """ShowJobStatisticsRequest

        The model defined in huaweicloud sdk

        :param league_id: 联盟id，最大32位，字母和数字组成
        :type league_id: str
        :param start_date: 开始日期
        :type start_date: str
        :param end_date: 结束日期
        :type end_date: str
        """
        
        

        self._league_id = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        self.league_id = league_id
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def league_id(self):
        """Gets the league_id of this ShowJobStatisticsRequest.

        联盟id，最大32位，字母和数字组成

        :return: The league_id of this ShowJobStatisticsRequest.
        :rtype: str
        """
        return self._league_id

    @league_id.setter
    def league_id(self, league_id):
        """Sets the league_id of this ShowJobStatisticsRequest.

        联盟id，最大32位，字母和数字组成

        :param league_id: The league_id of this ShowJobStatisticsRequest.
        :type league_id: str
        """
        self._league_id = league_id

    @property
    def start_date(self):
        """Gets the start_date of this ShowJobStatisticsRequest.

        开始日期

        :return: The start_date of this ShowJobStatisticsRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ShowJobStatisticsRequest.

        开始日期

        :param start_date: The start_date of this ShowJobStatisticsRequest.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ShowJobStatisticsRequest.

        结束日期

        :return: The end_date of this ShowJobStatisticsRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ShowJobStatisticsRequest.

        结束日期

        :param end_date: The end_date of this ShowJobStatisticsRequest.
        :type end_date: str
        """
        self._end_date = end_date

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
        if not isinstance(other, ShowJobStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
