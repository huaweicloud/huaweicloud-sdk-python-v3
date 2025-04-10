# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaseReportDetailResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'detail': 'CaseReportDetails',
        'err_message': 'str'
    }

    attribute_map = {
        'detail': 'detail',
        'err_message': 'err_message'
    }

    def __init__(self, detail=None, err_message=None):
        r"""CaseReportDetailResult

        The model defined in huaweicloud sdk

        :param detail: 
        :type detail: :class:`huaweicloudsdkcpts.v1.CaseReportDetails`
        :param err_message: 错误信息
        :type err_message: str
        """
        
        

        self._detail = None
        self._err_message = None
        self.discriminator = None

        if detail is not None:
            self.detail = detail
        if err_message is not None:
            self.err_message = err_message

    @property
    def detail(self):
        r"""Gets the detail of this CaseReportDetailResult.

        :return: The detail of this CaseReportDetailResult.
        :rtype: :class:`huaweicloudsdkcpts.v1.CaseReportDetails`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this CaseReportDetailResult.

        :param detail: The detail of this CaseReportDetailResult.
        :type detail: :class:`huaweicloudsdkcpts.v1.CaseReportDetails`
        """
        self._detail = detail

    @property
    def err_message(self):
        r"""Gets the err_message of this CaseReportDetailResult.

        错误信息

        :return: The err_message of this CaseReportDetailResult.
        :rtype: str
        """
        return self._err_message

    @err_message.setter
    def err_message(self, err_message):
        r"""Sets the err_message of this CaseReportDetailResult.

        错误信息

        :param err_message: The err_message of this CaseReportDetailResult.
        :type err_message: str
        """
        self._err_message = err_message

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
        if not isinstance(other, CaseReportDetailResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
