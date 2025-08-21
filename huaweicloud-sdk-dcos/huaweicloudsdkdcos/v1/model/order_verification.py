# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderVerification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'details': 'OrderServiceDetails',
        'attachments': 'list[UploadFileInfo]',
        'meet_expectation': 'bool',
        'comments': 'str'
    }

    attribute_map = {
        'result': 'result',
        'details': 'details',
        'attachments': 'attachments',
        'meet_expectation': 'meet_expectation',
        'comments': 'comments'
    }

    def __init__(self, result=None, details=None, attachments=None, meet_expectation=None, comments=None):
        r"""OrderVerification

        The model defined in huaweicloud sdk

        :param result: 服务情况，正常或异常
        :type result: str
        :param details: 
        :type details: :class:`huaweicloudsdkdcos.v1.OrderServiceDetails`
        :param attachments: 附件
        :type attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        :param meet_expectation: 是否符合预期
        :type meet_expectation: bool
        :param comments: 客户验收意见说明
        :type comments: str
        """
        
        

        self._result = None
        self._details = None
        self._attachments = None
        self._meet_expectation = None
        self._comments = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if details is not None:
            self.details = details
        if attachments is not None:
            self.attachments = attachments
        if meet_expectation is not None:
            self.meet_expectation = meet_expectation
        if comments is not None:
            self.comments = comments

    @property
    def result(self):
        r"""Gets the result of this OrderVerification.

        服务情况，正常或异常

        :return: The result of this OrderVerification.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this OrderVerification.

        服务情况，正常或异常

        :param result: The result of this OrderVerification.
        :type result: str
        """
        self._result = result

    @property
    def details(self):
        r"""Gets the details of this OrderVerification.

        :return: The details of this OrderVerification.
        :rtype: :class:`huaweicloudsdkdcos.v1.OrderServiceDetails`
        """
        return self._details

    @details.setter
    def details(self, details):
        r"""Sets the details of this OrderVerification.

        :param details: The details of this OrderVerification.
        :type details: :class:`huaweicloudsdkdcos.v1.OrderServiceDetails`
        """
        self._details = details

    @property
    def attachments(self):
        r"""Gets the attachments of this OrderVerification.

        附件

        :return: The attachments of this OrderVerification.
        :rtype: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        r"""Sets the attachments of this OrderVerification.

        附件

        :param attachments: The attachments of this OrderVerification.
        :type attachments: list[:class:`huaweicloudsdkdcos.v1.UploadFileInfo`]
        """
        self._attachments = attachments

    @property
    def meet_expectation(self):
        r"""Gets the meet_expectation of this OrderVerification.

        是否符合预期

        :return: The meet_expectation of this OrderVerification.
        :rtype: bool
        """
        return self._meet_expectation

    @meet_expectation.setter
    def meet_expectation(self, meet_expectation):
        r"""Sets the meet_expectation of this OrderVerification.

        是否符合预期

        :param meet_expectation: The meet_expectation of this OrderVerification.
        :type meet_expectation: bool
        """
        self._meet_expectation = meet_expectation

    @property
    def comments(self):
        r"""Gets the comments of this OrderVerification.

        客户验收意见说明

        :return: The comments of this OrderVerification.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this OrderVerification.

        客户验收意见说明

        :param comments: The comments of this OrderVerification.
        :type comments: str
        """
        self._comments = comments

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
        if not isinstance(other, OrderVerification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
