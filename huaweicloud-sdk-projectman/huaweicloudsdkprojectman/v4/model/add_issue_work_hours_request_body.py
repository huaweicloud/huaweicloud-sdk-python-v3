# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddIssueWorkHoursRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_date': 'str',
        'due_date': 'str',
        'work_hours': 'float',
        'work_hours_type_id': 'int'
    }

    attribute_map = {
        'start_date': 'start_date',
        'due_date': 'due_date',
        'work_hours': 'work_hours',
        'work_hours_type_id': 'work_hours_type_id'
    }

    def __init__(self, start_date=None, due_date=None, work_hours=None, work_hours_type_id=None):
        r"""AddIssueWorkHoursRequestBody

        The model defined in huaweicloud sdk

        :param start_date: 工时开始日期，年-月-日
        :type start_date: str
        :param due_date: 工时结束日期，年-月-日
        :type due_date: str
        :param work_hours: 工时总数（若工时日期范围包含多天，单日工时将设为“工时总数/天数”）
        :type work_hours: float
        :param work_hours_type_id: 工时类型id（项目预设工时类型id及名称对照：21:研发设计，22:后端开发，23:前端开发(Web)，24:前端开发(小程序)，25:前端开发(App)， 26:测试验证，27:缺陷修复，28:UI设计，29:会议，30:公共事务，31:培训，32:研究，33:其它，34:调休请假）
        :type work_hours_type_id: int
        """
        
        

        self._start_date = None
        self._due_date = None
        self._work_hours = None
        self._work_hours_type_id = None
        self.discriminator = None

        self.start_date = start_date
        self.due_date = due_date
        self.work_hours = work_hours
        if work_hours_type_id is not None:
            self.work_hours_type_id = work_hours_type_id

    @property
    def start_date(self):
        r"""Gets the start_date of this AddIssueWorkHoursRequestBody.

        工时开始日期，年-月-日

        :return: The start_date of this AddIssueWorkHoursRequestBody.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this AddIssueWorkHoursRequestBody.

        工时开始日期，年-月-日

        :param start_date: The start_date of this AddIssueWorkHoursRequestBody.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def due_date(self):
        r"""Gets the due_date of this AddIssueWorkHoursRequestBody.

        工时结束日期，年-月-日

        :return: The due_date of this AddIssueWorkHoursRequestBody.
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        r"""Sets the due_date of this AddIssueWorkHoursRequestBody.

        工时结束日期，年-月-日

        :param due_date: The due_date of this AddIssueWorkHoursRequestBody.
        :type due_date: str
        """
        self._due_date = due_date

    @property
    def work_hours(self):
        r"""Gets the work_hours of this AddIssueWorkHoursRequestBody.

        工时总数（若工时日期范围包含多天，单日工时将设为“工时总数/天数”）

        :return: The work_hours of this AddIssueWorkHoursRequestBody.
        :rtype: float
        """
        return self._work_hours

    @work_hours.setter
    def work_hours(self, work_hours):
        r"""Sets the work_hours of this AddIssueWorkHoursRequestBody.

        工时总数（若工时日期范围包含多天，单日工时将设为“工时总数/天数”）

        :param work_hours: The work_hours of this AddIssueWorkHoursRequestBody.
        :type work_hours: float
        """
        self._work_hours = work_hours

    @property
    def work_hours_type_id(self):
        r"""Gets the work_hours_type_id of this AddIssueWorkHoursRequestBody.

        工时类型id（项目预设工时类型id及名称对照：21:研发设计，22:后端开发，23:前端开发(Web)，24:前端开发(小程序)，25:前端开发(App)， 26:测试验证，27:缺陷修复，28:UI设计，29:会议，30:公共事务，31:培训，32:研究，33:其它，34:调休请假）

        :return: The work_hours_type_id of this AddIssueWorkHoursRequestBody.
        :rtype: int
        """
        return self._work_hours_type_id

    @work_hours_type_id.setter
    def work_hours_type_id(self, work_hours_type_id):
        r"""Sets the work_hours_type_id of this AddIssueWorkHoursRequestBody.

        工时类型id（项目预设工时类型id及名称对照：21:研发设计，22:后端开发，23:前端开发(Web)，24:前端开发(小程序)，25:前端开发(App)， 26:测试验证，27:缺陷修复，28:UI设计，29:会议，30:公共事务，31:培训，32:研究，33:其它，34:调休请假）

        :param work_hours_type_id: The work_hours_type_id of this AddIssueWorkHoursRequestBody.
        :type work_hours_type_id: int
        """
        self._work_hours_type_id = work_hours_type_id

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
        if not isinstance(other, AddIssueWorkHoursRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
