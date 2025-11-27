# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSubscribeReportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_email_template_ids': 'list[int]',
        'failed_email_template_ids': 'list[int]'
    }

    attribute_map = {
        'success_email_template_ids': 'success_email_template_ids',
        'failed_email_template_ids': 'failed_email_template_ids'
    }

    def __init__(self, success_email_template_ids=None, failed_email_template_ids=None):
        r"""BatchSubscribeReportResponse

        The model defined in huaweicloud sdk

        :param success_email_template_ids: 成功的邮件模板列表
        :type success_email_template_ids: list[int]
        :param failed_email_template_ids: 失败的邮件模板列表
        :type failed_email_template_ids: list[int]
        """
        
        super().__init__()

        self._success_email_template_ids = None
        self._failed_email_template_ids = None
        self.discriminator = None

        if success_email_template_ids is not None:
            self.success_email_template_ids = success_email_template_ids
        if failed_email_template_ids is not None:
            self.failed_email_template_ids = failed_email_template_ids

    @property
    def success_email_template_ids(self):
        r"""Gets the success_email_template_ids of this BatchSubscribeReportResponse.

        成功的邮件模板列表

        :return: The success_email_template_ids of this BatchSubscribeReportResponse.
        :rtype: list[int]
        """
        return self._success_email_template_ids

    @success_email_template_ids.setter
    def success_email_template_ids(self, success_email_template_ids):
        r"""Sets the success_email_template_ids of this BatchSubscribeReportResponse.

        成功的邮件模板列表

        :param success_email_template_ids: The success_email_template_ids of this BatchSubscribeReportResponse.
        :type success_email_template_ids: list[int]
        """
        self._success_email_template_ids = success_email_template_ids

    @property
    def failed_email_template_ids(self):
        r"""Gets the failed_email_template_ids of this BatchSubscribeReportResponse.

        失败的邮件模板列表

        :return: The failed_email_template_ids of this BatchSubscribeReportResponse.
        :rtype: list[int]
        """
        return self._failed_email_template_ids

    @failed_email_template_ids.setter
    def failed_email_template_ids(self, failed_email_template_ids):
        r"""Sets the failed_email_template_ids of this BatchSubscribeReportResponse.

        失败的邮件模板列表

        :param failed_email_template_ids: The failed_email_template_ids of this BatchSubscribeReportResponse.
        :type failed_email_template_ids: list[int]
        """
        self._failed_email_template_ids = failed_email_template_ids

    def to_dict(self):
        import warnings
        warnings.warn("BatchSubscribeReportResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, BatchSubscribeReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
