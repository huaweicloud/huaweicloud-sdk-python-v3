# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCaseRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'contents': 'list[CaseInfo]',
        'for_loop_params': 'list[object]'
    }

    attribute_map = {
        'contents': 'contents',
        'for_loop_params': 'for_loop_params'
    }

    def __init__(self, contents=None, for_loop_params=None):
        """UpdateCaseRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._contents = None
        self._for_loop_params = None
        self.discriminator = None

        if contents is not None:
            self.contents = contents
        if for_loop_params is not None:
            self.for_loop_params = for_loop_params

    @property
    def contents(self):
        """Gets the contents of this UpdateCaseRequestBody.

        contents

        :return: The contents of this UpdateCaseRequestBody.
        :rtype: list[CaseInfo]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this UpdateCaseRequestBody.

        contents

        :param contents: The contents of this UpdateCaseRequestBody.
        :type: list[CaseInfo]
        """
        self._contents = contents

    @property
    def for_loop_params(self):
        """Gets the for_loop_params of this UpdateCaseRequestBody.

        for_loop_params

        :return: The for_loop_params of this UpdateCaseRequestBody.
        :rtype: list[object]
        """
        return self._for_loop_params

    @for_loop_params.setter
    def for_loop_params(self, for_loop_params):
        """Sets the for_loop_params of this UpdateCaseRequestBody.

        for_loop_params

        :param for_loop_params: The for_loop_params of this UpdateCaseRequestBody.
        :type: list[object]
        """
        self._for_loop_params = for_loop_params

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
        if not isinstance(other, UpdateCaseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
