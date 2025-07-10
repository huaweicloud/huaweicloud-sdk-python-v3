# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityReportSubscriptionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'report_name': 'str',
        'report_category': 'str',
        'report_status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'report_name': 'report_name',
        'report_category': 'report_category',
        'report_status': 'report_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, enterprise_project_id=None, report_name=None, report_category=None, report_status=None, offset=None, limit=None):
        r"""ListSecurityReportSubscriptionsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。仅支持查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - all_granted_eps：所有企业项目  **默认取值：** all_granted_eps
        :type enterprise_project_id: str
        :param report_name: **参数解释：** 报告模板名称 **约束限制：** 不涉及 **取值范围：** 只能由中文、字母、数字和括号内所列符号（_-.:：）组成，且不能超过256个字符长度。 **默认取值：** 不涉及
        :type report_name: str
        :param report_category: **参数解释：** 报告类型 **约束限制：** 不涉及 **取值范围：** - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告  **默认取值：** 不涉及
        :type report_category: str
        :param report_status: **参数解释：** 开启状态 **约束限制：** 不涉及 **取值范围：** - opened：已开启 - closed：已关闭  **默认取值：** 不涉及
        :type report_status: str
        :param offset: **参数解释：** 分页查询的起始位置，表示从第几条记录开始返回（从0开始计数）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 0
        :type offset: int
        :param limit: **参数解释：** 分页查询的单页返回数量，控制每次请求返回的记录条数。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 1000
        :type limit: int
        """
        
        

        self._enterprise_project_id = None
        self._report_name = None
        self._report_category = None
        self._report_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        if report_name is not None:
            self.report_name = report_name
        if report_category is not None:
            self.report_category = report_category
        if report_status is not None:
            self.report_status = report_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。仅支持查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - all_granted_eps：所有企业项目  **默认取值：** all_granted_eps

        :return: The enterprise_project_id of this ListSecurityReportSubscriptionsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。仅支持查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - all_granted_eps：所有企业项目  **默认取值：** all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListSecurityReportSubscriptionsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def report_name(self):
        r"""Gets the report_name of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 报告模板名称 **约束限制：** 不涉及 **取值范围：** 只能由中文、字母、数字和括号内所列符号（_-.:：）组成，且不能超过256个字符长度。 **默认取值：** 不涉及

        :return: The report_name of this ListSecurityReportSubscriptionsRequest.
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        r"""Sets the report_name of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 报告模板名称 **约束限制：** 不涉及 **取值范围：** 只能由中文、字母、数字和括号内所列符号（_-.:：）组成，且不能超过256个字符长度。 **默认取值：** 不涉及

        :param report_name: The report_name of this ListSecurityReportSubscriptionsRequest.
        :type report_name: str
        """
        self._report_name = report_name

    @property
    def report_category(self):
        r"""Gets the report_category of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 报告类型 **约束限制：** 不涉及 **取值范围：** - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告  **默认取值：** 不涉及

        :return: The report_category of this ListSecurityReportSubscriptionsRequest.
        :rtype: str
        """
        return self._report_category

    @report_category.setter
    def report_category(self, report_category):
        r"""Sets the report_category of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 报告类型 **约束限制：** 不涉及 **取值范围：** - daily_report：安全日报 - weekly_report：安全周报 - monthly_report：安全月报 - custom_report：自定义报告  **默认取值：** 不涉及

        :param report_category: The report_category of this ListSecurityReportSubscriptionsRequest.
        :type report_category: str
        """
        self._report_category = report_category

    @property
    def report_status(self):
        r"""Gets the report_status of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 开启状态 **约束限制：** 不涉及 **取值范围：** - opened：已开启 - closed：已关闭  **默认取值：** 不涉及

        :return: The report_status of this ListSecurityReportSubscriptionsRequest.
        :rtype: str
        """
        return self._report_status

    @report_status.setter
    def report_status(self, report_status):
        r"""Sets the report_status of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 开启状态 **约束限制：** 不涉及 **取值范围：** - opened：已开启 - closed：已关闭  **默认取值：** 不涉及

        :param report_status: The report_status of this ListSecurityReportSubscriptionsRequest.
        :type report_status: str
        """
        self._report_status = report_status

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 分页查询的起始位置，表示从第几条记录开始返回（从0开始计数）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 0

        :return: The offset of this ListSecurityReportSubscriptionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 分页查询的起始位置，表示从第几条记录开始返回（从0开始计数）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 0

        :param offset: The offset of this ListSecurityReportSubscriptionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 分页查询的单页返回数量，控制每次请求返回的记录条数。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 1000

        :return: The limit of this ListSecurityReportSubscriptionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityReportSubscriptionsRequest.

        **参数解释：** 分页查询的单页返回数量，控制每次请求返回的记录条数。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 1000

        :param limit: The limit of this ListSecurityReportSubscriptionsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSecurityReportSubscriptionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
