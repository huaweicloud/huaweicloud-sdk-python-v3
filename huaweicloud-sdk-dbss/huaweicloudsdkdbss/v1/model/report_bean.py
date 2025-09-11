# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportBean:

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
        'db_names': 'str',
        'end_time': 'str',
        'finish_time': 'str',
        'format': 'str',
        'id': 'str',
        'name': 'str',
        'percentum': 'int',
        'start_time': 'str',
        'template_type': 'str',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'db_ids': 'db_ids',
        'db_names': 'db_names',
        'end_time': 'end_time',
        'finish_time': 'finish_time',
        'format': 'format',
        'id': 'id',
        'name': 'name',
        'percentum': 'percentum',
        'start_time': 'start_time',
        'template_type': 'template_type',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, db_ids=None, db_names=None, end_time=None, finish_time=None, format=None, id=None, name=None, percentum=None, start_time=None, template_type=None, type=None, url=None):
        r"""ReportBean

        The model defined in huaweicloud sdk

        :param db_ids: 数据库ID
        :type db_ids: str
        :param db_names: 数据库名称
        :type db_names: str
        :param end_time: 结束时间
        :type end_time: str
        :param finish_time: 完成时间
        :type finish_time: str
        :param format: 格式  - pdf: PDF文件  - zip: zip文件
        :type format: str
        :param id: 报表ID
        :type id: str
        :param name: 报表名称
        :type name: str
        :param percentum: 进度
        :type percentum: int
        :param start_time: 开始时间
        :type start_time: str
        :param template_type: 报表类型 - PDF - ZIP
        :type template_type: str
        :param type: 周期 - AUDIT_REPORT_DAY: 按天 - AUDIT_REPORT_WEEK： 按周 - AUDIT_REPORT_MONTH： 按月 - AUDIT_REPORT_YEAR：按年 - AUDIT_REPORT_REAL_TIME：立即
        :type type: str
        :param url: 地址URL
        :type url: str
        """
        
        

        self._db_ids = None
        self._db_names = None
        self._end_time = None
        self._finish_time = None
        self._format = None
        self._id = None
        self._name = None
        self._percentum = None
        self._start_time = None
        self._template_type = None
        self._type = None
        self._url = None
        self.discriminator = None

        if db_ids is not None:
            self.db_ids = db_ids
        if db_names is not None:
            self.db_names = db_names
        if end_time is not None:
            self.end_time = end_time
        if finish_time is not None:
            self.finish_time = finish_time
        if format is not None:
            self.format = format
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if percentum is not None:
            self.percentum = percentum
        if start_time is not None:
            self.start_time = start_time
        if template_type is not None:
            self.template_type = template_type
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def db_ids(self):
        r"""Gets the db_ids of this ReportBean.

        数据库ID

        :return: The db_ids of this ReportBean.
        :rtype: str
        """
        return self._db_ids

    @db_ids.setter
    def db_ids(self, db_ids):
        r"""Sets the db_ids of this ReportBean.

        数据库ID

        :param db_ids: The db_ids of this ReportBean.
        :type db_ids: str
        """
        self._db_ids = db_ids

    @property
    def db_names(self):
        r"""Gets the db_names of this ReportBean.

        数据库名称

        :return: The db_names of this ReportBean.
        :rtype: str
        """
        return self._db_names

    @db_names.setter
    def db_names(self, db_names):
        r"""Sets the db_names of this ReportBean.

        数据库名称

        :param db_names: The db_names of this ReportBean.
        :type db_names: str
        """
        self._db_names = db_names

    @property
    def end_time(self):
        r"""Gets the end_time of this ReportBean.

        结束时间

        :return: The end_time of this ReportBean.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ReportBean.

        结束时间

        :param end_time: The end_time of this ReportBean.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this ReportBean.

        完成时间

        :return: The finish_time of this ReportBean.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this ReportBean.

        完成时间

        :param finish_time: The finish_time of this ReportBean.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def format(self):
        r"""Gets the format of this ReportBean.

        格式  - pdf: PDF文件  - zip: zip文件

        :return: The format of this ReportBean.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ReportBean.

        格式  - pdf: PDF文件  - zip: zip文件

        :param format: The format of this ReportBean.
        :type format: str
        """
        self._format = format

    @property
    def id(self):
        r"""Gets the id of this ReportBean.

        报表ID

        :return: The id of this ReportBean.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ReportBean.

        报表ID

        :param id: The id of this ReportBean.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ReportBean.

        报表名称

        :return: The name of this ReportBean.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ReportBean.

        报表名称

        :param name: The name of this ReportBean.
        :type name: str
        """
        self._name = name

    @property
    def percentum(self):
        r"""Gets the percentum of this ReportBean.

        进度

        :return: The percentum of this ReportBean.
        :rtype: int
        """
        return self._percentum

    @percentum.setter
    def percentum(self, percentum):
        r"""Sets the percentum of this ReportBean.

        进度

        :param percentum: The percentum of this ReportBean.
        :type percentum: int
        """
        self._percentum = percentum

    @property
    def start_time(self):
        r"""Gets the start_time of this ReportBean.

        开始时间

        :return: The start_time of this ReportBean.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ReportBean.

        开始时间

        :param start_time: The start_time of this ReportBean.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def template_type(self):
        r"""Gets the template_type of this ReportBean.

        报表类型 - PDF - ZIP

        :return: The template_type of this ReportBean.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this ReportBean.

        报表类型 - PDF - ZIP

        :param template_type: The template_type of this ReportBean.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def type(self):
        r"""Gets the type of this ReportBean.

        周期 - AUDIT_REPORT_DAY: 按天 - AUDIT_REPORT_WEEK： 按周 - AUDIT_REPORT_MONTH： 按月 - AUDIT_REPORT_YEAR：按年 - AUDIT_REPORT_REAL_TIME：立即

        :return: The type of this ReportBean.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ReportBean.

        周期 - AUDIT_REPORT_DAY: 按天 - AUDIT_REPORT_WEEK： 按周 - AUDIT_REPORT_MONTH： 按月 - AUDIT_REPORT_YEAR：按年 - AUDIT_REPORT_REAL_TIME：立即

        :param type: The type of this ReportBean.
        :type type: str
        """
        self._type = type

    @property
    def url(self):
        r"""Gets the url of this ReportBean.

        地址URL

        :return: The url of this ReportBean.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ReportBean.

        地址URL

        :param url: The url of this ReportBean.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, ReportBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
