# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportOutlineResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'err_message': 'object',
        'outline': 'ReportOutline'
    }

    attribute_map = {
        'err_message': 'err_message',
        'outline': 'outline'
    }

    def __init__(self, err_message=None, outline=None):
        r"""ReportOutlineResult

        The model defined in huaweicloud sdk

        :param err_message: 错误信息
        :type err_message: object
        :param outline: 
        :type outline: :class:`huaweicloudsdkcpts.v1.ReportOutline`
        """
        
        

        self._err_message = None
        self._outline = None
        self.discriminator = None

        if err_message is not None:
            self.err_message = err_message
        if outline is not None:
            self.outline = outline

    @property
    def err_message(self):
        r"""Gets the err_message of this ReportOutlineResult.

        错误信息

        :return: The err_message of this ReportOutlineResult.
        :rtype: object
        """
        return self._err_message

    @err_message.setter
    def err_message(self, err_message):
        r"""Sets the err_message of this ReportOutlineResult.

        错误信息

        :param err_message: The err_message of this ReportOutlineResult.
        :type err_message: object
        """
        self._err_message = err_message

    @property
    def outline(self):
        r"""Gets the outline of this ReportOutlineResult.

        :return: The outline of this ReportOutlineResult.
        :rtype: :class:`huaweicloudsdkcpts.v1.ReportOutline`
        """
        return self._outline

    @outline.setter
    def outline(self, outline):
        r"""Sets the outline of this ReportOutlineResult.

        :param outline: The outline of this ReportOutlineResult.
        :type outline: :class:`huaweicloudsdkcpts.v1.ReportOutline`
        """
        self._outline = outline

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
        if not isinstance(other, ReportOutlineResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
