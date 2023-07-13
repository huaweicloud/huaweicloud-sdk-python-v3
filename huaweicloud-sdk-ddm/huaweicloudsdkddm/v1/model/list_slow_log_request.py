# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'cur_page': 'str',
        'per_page': 'str',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'cur_page': 'curPage',
        'per_page': 'perPage',
        'start_date': 'startDate',
        'end_date': 'endDate'
    }

    def __init__(self, instance_id=None, cur_page=None, per_page=None, start_date=None, end_date=None):
        """ListSlowLogRequest

        The model defined in huaweicloud sdk

        :param instance_id: DDM实例ID。
        :type instance_id: str
        :param cur_page: 分页参数：起始值 [大于等于0] 。
        :type cur_page: str
        :param per_page: 分页参数：每页多少条。
        :type per_page: str
        :param start_date: 开始时间，UTC time，精确到毫秒。
        :type start_date: str
        :param end_date: 结束时间，UTC time，精确到毫秒。结束时间与开始时间，间隔不能超过7天。
        :type end_date: str
        """
        
        

        self._instance_id = None
        self._cur_page = None
        self._per_page = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        self.instance_id = instance_id
        self.cur_page = cur_page
        self.per_page = per_page
        self.start_date = start_date
        self.end_date = end_date

    @property
    def instance_id(self):
        """Gets the instance_id of this ListSlowLogRequest.

        DDM实例ID。

        :return: The instance_id of this ListSlowLogRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListSlowLogRequest.

        DDM实例ID。

        :param instance_id: The instance_id of this ListSlowLogRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def cur_page(self):
        """Gets the cur_page of this ListSlowLogRequest.

        分页参数：起始值 [大于等于0] 。

        :return: The cur_page of this ListSlowLogRequest.
        :rtype: str
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        """Sets the cur_page of this ListSlowLogRequest.

        分页参数：起始值 [大于等于0] 。

        :param cur_page: The cur_page of this ListSlowLogRequest.
        :type cur_page: str
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        """Gets the per_page of this ListSlowLogRequest.

        分页参数：每页多少条。

        :return: The per_page of this ListSlowLogRequest.
        :rtype: str
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this ListSlowLogRequest.

        分页参数：每页多少条。

        :param per_page: The per_page of this ListSlowLogRequest.
        :type per_page: str
        """
        self._per_page = per_page

    @property
    def start_date(self):
        """Gets the start_date of this ListSlowLogRequest.

        开始时间，UTC time，精确到毫秒。

        :return: The start_date of this ListSlowLogRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ListSlowLogRequest.

        开始时间，UTC time，精确到毫秒。

        :param start_date: The start_date of this ListSlowLogRequest.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ListSlowLogRequest.

        结束时间，UTC time，精确到毫秒。结束时间与开始时间，间隔不能超过7天。

        :return: The end_date of this ListSlowLogRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ListSlowLogRequest.

        结束时间，UTC time，精确到毫秒。结束时间与开始时间，间隔不能超过7天。

        :param end_date: The end_date of this ListSlowLogRequest.
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
        if not isinstance(other, ListSlowLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
