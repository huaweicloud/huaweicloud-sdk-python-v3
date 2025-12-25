# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteReportActionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_content': 'str',
        'email_title': 'str',
        'email_to': 'str',
        'email_cc': 'str',
        'email_content': 'str',
        'report_file_type': 'str',
        'action': 'str',
        'report_page': 'str',
        'page_config': 'PageConfigPx'
    }

    attribute_map = {
        'report_content': 'report_content',
        'email_title': 'email_title',
        'email_to': 'email_to',
        'email_cc': 'email_cc',
        'email_content': 'email_content',
        'report_file_type': 'report_file_type',
        'action': 'action',
        'report_page': 'report_page',
        'page_config': 'page_config'
    }

    def __init__(self, report_content=None, email_title=None, email_to=None, email_cc=None, email_content=None, report_file_type=None, action=None, report_page=None, page_config=None):
        r"""ExecuteReportActionInfo

        The model defined in huaweicloud sdk

        :param report_content: 报告的base64编码
        :type report_content: str
        :param email_title: 邮件标题
        :type email_title: str
        :param email_to: 收件人邮箱
        :type email_to: str
        :param email_cc: 抄送人邮箱
        :type email_cc: str
        :param email_content: 邮件内容
        :type email_content: str
        :param report_file_type: 附件类型
        :type report_file_type: str
        :param action: API的动作支持send和download
        :type action: str
        :param report_page: 安全报告Base64编码的内容
        :type report_page: str
        :param page_config: 
        :type page_config: :class:`huaweicloudsdksecmaster.v1.PageConfigPx`
        """
        
        

        self._report_content = None
        self._email_title = None
        self._email_to = None
        self._email_cc = None
        self._email_content = None
        self._report_file_type = None
        self._action = None
        self._report_page = None
        self._page_config = None
        self.discriminator = None

        if report_content is not None:
            self.report_content = report_content
        if email_title is not None:
            self.email_title = email_title
        if email_to is not None:
            self.email_to = email_to
        if email_cc is not None:
            self.email_cc = email_cc
        if email_content is not None:
            self.email_content = email_content
        if report_file_type is not None:
            self.report_file_type = report_file_type
        self.action = action
        if report_page is not None:
            self.report_page = report_page
        if page_config is not None:
            self.page_config = page_config

    @property
    def report_content(self):
        r"""Gets the report_content of this ExecuteReportActionInfo.

        报告的base64编码

        :return: The report_content of this ExecuteReportActionInfo.
        :rtype: str
        """
        return self._report_content

    @report_content.setter
    def report_content(self, report_content):
        r"""Sets the report_content of this ExecuteReportActionInfo.

        报告的base64编码

        :param report_content: The report_content of this ExecuteReportActionInfo.
        :type report_content: str
        """
        self._report_content = report_content

    @property
    def email_title(self):
        r"""Gets the email_title of this ExecuteReportActionInfo.

        邮件标题

        :return: The email_title of this ExecuteReportActionInfo.
        :rtype: str
        """
        return self._email_title

    @email_title.setter
    def email_title(self, email_title):
        r"""Sets the email_title of this ExecuteReportActionInfo.

        邮件标题

        :param email_title: The email_title of this ExecuteReportActionInfo.
        :type email_title: str
        """
        self._email_title = email_title

    @property
    def email_to(self):
        r"""Gets the email_to of this ExecuteReportActionInfo.

        收件人邮箱

        :return: The email_to of this ExecuteReportActionInfo.
        :rtype: str
        """
        return self._email_to

    @email_to.setter
    def email_to(self, email_to):
        r"""Sets the email_to of this ExecuteReportActionInfo.

        收件人邮箱

        :param email_to: The email_to of this ExecuteReportActionInfo.
        :type email_to: str
        """
        self._email_to = email_to

    @property
    def email_cc(self):
        r"""Gets the email_cc of this ExecuteReportActionInfo.

        抄送人邮箱

        :return: The email_cc of this ExecuteReportActionInfo.
        :rtype: str
        """
        return self._email_cc

    @email_cc.setter
    def email_cc(self, email_cc):
        r"""Sets the email_cc of this ExecuteReportActionInfo.

        抄送人邮箱

        :param email_cc: The email_cc of this ExecuteReportActionInfo.
        :type email_cc: str
        """
        self._email_cc = email_cc

    @property
    def email_content(self):
        r"""Gets the email_content of this ExecuteReportActionInfo.

        邮件内容

        :return: The email_content of this ExecuteReportActionInfo.
        :rtype: str
        """
        return self._email_content

    @email_content.setter
    def email_content(self, email_content):
        r"""Sets the email_content of this ExecuteReportActionInfo.

        邮件内容

        :param email_content: The email_content of this ExecuteReportActionInfo.
        :type email_content: str
        """
        self._email_content = email_content

    @property
    def report_file_type(self):
        r"""Gets the report_file_type of this ExecuteReportActionInfo.

        附件类型

        :return: The report_file_type of this ExecuteReportActionInfo.
        :rtype: str
        """
        return self._report_file_type

    @report_file_type.setter
    def report_file_type(self, report_file_type):
        r"""Sets the report_file_type of this ExecuteReportActionInfo.

        附件类型

        :param report_file_type: The report_file_type of this ExecuteReportActionInfo.
        :type report_file_type: str
        """
        self._report_file_type = report_file_type

    @property
    def action(self):
        r"""Gets the action of this ExecuteReportActionInfo.

        API的动作支持send和download

        :return: The action of this ExecuteReportActionInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExecuteReportActionInfo.

        API的动作支持send和download

        :param action: The action of this ExecuteReportActionInfo.
        :type action: str
        """
        self._action = action

    @property
    def report_page(self):
        r"""Gets the report_page of this ExecuteReportActionInfo.

        安全报告Base64编码的内容

        :return: The report_page of this ExecuteReportActionInfo.
        :rtype: str
        """
        return self._report_page

    @report_page.setter
    def report_page(self, report_page):
        r"""Sets the report_page of this ExecuteReportActionInfo.

        安全报告Base64编码的内容

        :param report_page: The report_page of this ExecuteReportActionInfo.
        :type report_page: str
        """
        self._report_page = report_page

    @property
    def page_config(self):
        r"""Gets the page_config of this ExecuteReportActionInfo.

        :return: The page_config of this ExecuteReportActionInfo.
        :rtype: :class:`huaweicloudsdksecmaster.v1.PageConfigPx`
        """
        return self._page_config

    @page_config.setter
    def page_config(self, page_config):
        r"""Sets the page_config of this ExecuteReportActionInfo.

        :param page_config: The page_config of this ExecuteReportActionInfo.
        :type page_config: :class:`huaweicloudsdksecmaster.v1.PageConfigPx`
        """
        self._page_config = page_config

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
        if not isinstance(other, ExecuteReportActionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
