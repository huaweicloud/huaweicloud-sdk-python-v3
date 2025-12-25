# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCodeSegmentRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code_segment_name': 'str',
        'description': 'str',
        'code': 'str'
    }

    attribute_map = {
        'code_segment_name': 'code_segment_name',
        'description': 'description',
        'code': 'code'
    }

    def __init__(self, code_segment_name=None, description=None, code=None):
        r"""UpdateCodeSegmentRequestBody

        The model defined in huaweicloud sdk

        :param code_segment_name: 代码段名称
        :type code_segment_name: str
        :param description: 代码段描述信息
        :type description: str
        :param code: 代码片段
        :type code: str
        """
        
        

        self._code_segment_name = None
        self._description = None
        self._code = None
        self.discriminator = None

        if code_segment_name is not None:
            self.code_segment_name = code_segment_name
        if description is not None:
            self.description = description
        if code is not None:
            self.code = code

    @property
    def code_segment_name(self):
        r"""Gets the code_segment_name of this UpdateCodeSegmentRequestBody.

        代码段名称

        :return: The code_segment_name of this UpdateCodeSegmentRequestBody.
        :rtype: str
        """
        return self._code_segment_name

    @code_segment_name.setter
    def code_segment_name(self, code_segment_name):
        r"""Sets the code_segment_name of this UpdateCodeSegmentRequestBody.

        代码段名称

        :param code_segment_name: The code_segment_name of this UpdateCodeSegmentRequestBody.
        :type code_segment_name: str
        """
        self._code_segment_name = code_segment_name

    @property
    def description(self):
        r"""Gets the description of this UpdateCodeSegmentRequestBody.

        代码段描述信息

        :return: The description of this UpdateCodeSegmentRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCodeSegmentRequestBody.

        代码段描述信息

        :param description: The description of this UpdateCodeSegmentRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def code(self):
        r"""Gets the code of this UpdateCodeSegmentRequestBody.

        代码片段

        :return: The code of this UpdateCodeSegmentRequestBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this UpdateCodeSegmentRequestBody.

        代码片段

        :param code: The code of this UpdateCodeSegmentRequestBody.
        :type code: str
        """
        self._code = code

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
        if not isinstance(other, UpdateCodeSegmentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
