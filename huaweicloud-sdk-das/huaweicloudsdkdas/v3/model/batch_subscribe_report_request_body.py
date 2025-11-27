# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSubscribeReportRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscribe': 'bool',
        'email_template_id_list': 'list[int]'
    }

    attribute_map = {
        'subscribe': 'subscribe',
        'email_template_id_list': 'email_template_id_list'
    }

    def __init__(self, subscribe=None, email_template_id_list=None):
        r"""BatchSubscribeReportRequestBody

        The model defined in huaweicloud sdk

        :param subscribe: 是否订阅（true-订阅，false-取消订阅）
        :type subscribe: bool
        :param email_template_id_list: 邮件模板ID列表
        :type email_template_id_list: list[int]
        """
        
        

        self._subscribe = None
        self._email_template_id_list = None
        self.discriminator = None

        self.subscribe = subscribe
        self.email_template_id_list = email_template_id_list

    @property
    def subscribe(self):
        r"""Gets the subscribe of this BatchSubscribeReportRequestBody.

        是否订阅（true-订阅，false-取消订阅）

        :return: The subscribe of this BatchSubscribeReportRequestBody.
        :rtype: bool
        """
        return self._subscribe

    @subscribe.setter
    def subscribe(self, subscribe):
        r"""Sets the subscribe of this BatchSubscribeReportRequestBody.

        是否订阅（true-订阅，false-取消订阅）

        :param subscribe: The subscribe of this BatchSubscribeReportRequestBody.
        :type subscribe: bool
        """
        self._subscribe = subscribe

    @property
    def email_template_id_list(self):
        r"""Gets the email_template_id_list of this BatchSubscribeReportRequestBody.

        邮件模板ID列表

        :return: The email_template_id_list of this BatchSubscribeReportRequestBody.
        :rtype: list[int]
        """
        return self._email_template_id_list

    @email_template_id_list.setter
    def email_template_id_list(self, email_template_id_list):
        r"""Sets the email_template_id_list of this BatchSubscribeReportRequestBody.

        邮件模板ID列表

        :param email_template_id_list: The email_template_id_list of this BatchSubscribeReportRequestBody.
        :type email_template_id_list: list[int]
        """
        self._email_template_id_list = email_template_id_list

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
        if not isinstance(other, BatchSubscribeReportRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
