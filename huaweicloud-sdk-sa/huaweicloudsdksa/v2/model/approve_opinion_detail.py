# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApproveOpinionDetail:

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
        'content': 'str'
    }

    attribute_map = {
        'result': 'result',
        'content': 'content'
    }

    def __init__(self, result=None, content=None):
        """ApproveOpinionDetail

        The model defined in huaweicloud sdk

        :param result: Approve Result.
        :type result: str
        :param content: Approve content.
        :type content: str
        """
        
        

        self._result = None
        self._content = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if content is not None:
            self.content = content

    @property
    def result(self):
        """Gets the result of this ApproveOpinionDetail.

        Approve Result.

        :return: The result of this ApproveOpinionDetail.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ApproveOpinionDetail.

        Approve Result.

        :param result: The result of this ApproveOpinionDetail.
        :type result: str
        """
        self._result = result

    @property
    def content(self):
        """Gets the content of this ApproveOpinionDetail.

        Approve content.

        :return: The content of this ApproveOpinionDetail.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ApproveOpinionDetail.

        Approve content.

        :param content: The content of this ApproveOpinionDetail.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, ApproveOpinionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
