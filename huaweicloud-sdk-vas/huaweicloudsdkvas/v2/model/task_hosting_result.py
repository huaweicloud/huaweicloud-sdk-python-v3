# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskHostingResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hosting_result': 'TaskHostingResultHostingResult'
    }

    attribute_map = {
        'hosting_result': 'hosting_result'
    }

    def __init__(self, hosting_result=None):
        """TaskHostingResult

        The model defined in huaweicloud sdk

        :param hosting_result: 
        :type hosting_result: :class:`huaweicloudsdkvas.v2.TaskHostingResultHostingResult`
        """
        
        

        self._hosting_result = None
        self.discriminator = None

        if hosting_result is not None:
            self.hosting_result = hosting_result

    @property
    def hosting_result(self):
        """Gets the hosting_result of this TaskHostingResult.

        :return: The hosting_result of this TaskHostingResult.
        :rtype: :class:`huaweicloudsdkvas.v2.TaskHostingResultHostingResult`
        """
        return self._hosting_result

    @hosting_result.setter
    def hosting_result(self, hosting_result):
        """Sets the hosting_result of this TaskHostingResult.

        :param hosting_result: The hosting_result of this TaskHostingResult.
        :type hosting_result: :class:`huaweicloudsdkvas.v2.TaskHostingResultHostingResult`
        """
        self._hosting_result = hosting_result

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
        if not isinstance(other, TaskHostingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
