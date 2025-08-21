# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportProfileVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'profile_id': 'str',
        'name': 'str',
        'category': 'str',
        'status': 'int',
        'report_id': 'str',
        'last_time': 'int'
    }

    attribute_map = {
        'profile_id': 'profile_id',
        'name': 'name',
        'category': 'category',
        'status': 'status',
        'report_id': 'report_id',
        'last_time': 'last_time'
    }

    def __init__(self, profile_id=None, name=None, category=None, status=None, report_id=None, last_time=None):
        r"""ReportProfileVO

        The model defined in huaweicloud sdk

        :param profile_id: **参数解释**： 模板ID **取值范围**： 不涉及
        :type profile_id: str
        :param name: **参数解释**： 模板名称 **取值范围**： 不涉及
        :type name: str
        :param category: **参数解释**： 模板类型 **取值范围**： daily 日报 weekly 周报 custom 自定义报告
        :type category: str
        :param status: **参数解释**： 启用状态 **取值范围**： 不涉及
        :type status: int
        :param report_id: **参数解释**： 最新的报告的ID **取值范围**： 不涉及
        :type report_id: str
        :param last_time: **参数解释**： 最新的报告的生成时间 **取值范围**： 不涉及
        :type last_time: int
        """
        
        

        self._profile_id = None
        self._name = None
        self._category = None
        self._status = None
        self._report_id = None
        self._last_time = None
        self.discriminator = None

        if profile_id is not None:
            self.profile_id = profile_id
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        if status is not None:
            self.status = status
        if report_id is not None:
            self.report_id = report_id
        if last_time is not None:
            self.last_time = last_time

    @property
    def profile_id(self):
        r"""Gets the profile_id of this ReportProfileVO.

        **参数解释**： 模板ID **取值范围**： 不涉及

        :return: The profile_id of this ReportProfileVO.
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        r"""Sets the profile_id of this ReportProfileVO.

        **参数解释**： 模板ID **取值范围**： 不涉及

        :param profile_id: The profile_id of this ReportProfileVO.
        :type profile_id: str
        """
        self._profile_id = profile_id

    @property
    def name(self):
        r"""Gets the name of this ReportProfileVO.

        **参数解释**： 模板名称 **取值范围**： 不涉及

        :return: The name of this ReportProfileVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ReportProfileVO.

        **参数解释**： 模板名称 **取值范围**： 不涉及

        :param name: The name of this ReportProfileVO.
        :type name: str
        """
        self._name = name

    @property
    def category(self):
        r"""Gets the category of this ReportProfileVO.

        **参数解释**： 模板类型 **取值范围**： daily 日报 weekly 周报 custom 自定义报告

        :return: The category of this ReportProfileVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ReportProfileVO.

        **参数解释**： 模板类型 **取值范围**： daily 日报 weekly 周报 custom 自定义报告

        :param category: The category of this ReportProfileVO.
        :type category: str
        """
        self._category = category

    @property
    def status(self):
        r"""Gets the status of this ReportProfileVO.

        **参数解释**： 启用状态 **取值范围**： 不涉及

        :return: The status of this ReportProfileVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ReportProfileVO.

        **参数解释**： 启用状态 **取值范围**： 不涉及

        :param status: The status of this ReportProfileVO.
        :type status: int
        """
        self._status = status

    @property
    def report_id(self):
        r"""Gets the report_id of this ReportProfileVO.

        **参数解释**： 最新的报告的ID **取值范围**： 不涉及

        :return: The report_id of this ReportProfileVO.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this ReportProfileVO.

        **参数解释**： 最新的报告的ID **取值范围**： 不涉及

        :param report_id: The report_id of this ReportProfileVO.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def last_time(self):
        r"""Gets the last_time of this ReportProfileVO.

        **参数解释**： 最新的报告的生成时间 **取值范围**： 不涉及

        :return: The last_time of this ReportProfileVO.
        :rtype: int
        """
        return self._last_time

    @last_time.setter
    def last_time(self, last_time):
        r"""Sets the last_time of this ReportProfileVO.

        **参数解释**： 最新的报告的生成时间 **取值范围**： 不涉及

        :param last_time: The last_time of this ReportProfileVO.
        :type last_time: int
        """
        self._last_time = last_time

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
        if not isinstance(other, ReportProfileVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
