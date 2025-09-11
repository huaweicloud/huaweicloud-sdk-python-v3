# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateReportRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_ids': 'str',
        'end_date': 'datetime',
        'end_time': 'str',
        'start_date': 'datetime',
        'start_time': 'str',
        'template_id': 'str'
    }

    attribute_map = {
        'db_ids': 'db_ids',
        'end_date': 'end_date',
        'end_time': 'end_time',
        'start_date': 'start_date',
        'start_time': 'start_time',
        'template_id': 'template_id'
    }

    def __init__(self, db_ids=None, end_date=None, end_time=None, start_date=None, start_time=None, template_id=None):
        r"""CreateReportRequestBody

        The model defined in huaweicloud sdk

        :param db_ids: 数据库ID列表，多个用英文逗号分割
        :type db_ids: str
        :param end_date: 结束日期
        :type end_date: datetime
        :param end_time: 结束时间
        :type end_time: str
        :param start_date: 开始日期
        :type start_date: datetime
        :param start_time: 开始时间
        :type start_time: str
        :param template_id: 模板ID
        :type template_id: str
        """
        
        

        self._db_ids = None
        self._end_date = None
        self._end_time = None
        self._start_date = None
        self._start_time = None
        self._template_id = None
        self.discriminator = None

        if db_ids is not None:
            self.db_ids = db_ids
        if end_date is not None:
            self.end_date = end_date
        self.end_time = end_time
        if start_date is not None:
            self.start_date = start_date
        self.start_time = start_time
        self.template_id = template_id

    @property
    def db_ids(self):
        r"""Gets the db_ids of this CreateReportRequestBody.

        数据库ID列表，多个用英文逗号分割

        :return: The db_ids of this CreateReportRequestBody.
        :rtype: str
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        r"""Sets the db_ids of this CreateReportRequestBody.

        数据库ID列表，多个用英文逗号分割

        :param db_ids: The db_ids of this CreateReportRequestBody.
        :type db_ids: str
        """
        self._db_ids = db_ids

    @property
    def end_date(self):
        r"""Gets the end_date of this CreateReportRequestBody.

        结束日期

        :return: The end_date of this CreateReportRequestBody.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this CreateReportRequestBody.

        结束日期

        :param end_date: The end_date of this CreateReportRequestBody.
        :type end_date: datetime
        """
        self._end_date = end_date

    @property
    def end_time(self):
        r"""Gets the end_time of this CreateReportRequestBody.

        结束时间

        :return: The end_time of this CreateReportRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CreateReportRequestBody.

        结束时间

        :param end_time: The end_time of this CreateReportRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def start_date(self):
        r"""Gets the start_date of this CreateReportRequestBody.

        开始日期

        :return: The start_date of this CreateReportRequestBody.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this CreateReportRequestBody.

        开始日期

        :param start_date: The start_date of this CreateReportRequestBody.
        :type start_date: datetime
        """
        self._start_date = start_date

    @property
    def start_time(self):
        r"""Gets the start_time of this CreateReportRequestBody.

        开始时间

        :return: The start_time of this CreateReportRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CreateReportRequestBody.

        开始时间

        :param start_time: The start_time of this CreateReportRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def template_id(self):
        r"""Gets the template_id of this CreateReportRequestBody.

        模板ID

        :return: The template_id of this CreateReportRequestBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this CreateReportRequestBody.

        模板ID

        :param template_id: The template_id of this CreateReportRequestBody.
        :type template_id: str
        """
        self._template_id = template_id

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
        if not isinstance(other, CreateReportRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
