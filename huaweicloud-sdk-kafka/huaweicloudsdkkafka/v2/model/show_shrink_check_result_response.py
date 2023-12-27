# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShrinkCheckResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'check_detail': 'list[ShowShrinkCheckResponseBodyCheckDetail]'
    }

    attribute_map = {
        'success': 'success',
        'check_detail': 'check_detail'
    }

    def __init__(self, success=None, check_detail=None):
        """ShowShrinkCheckResultResponse

        The model defined in huaweicloud sdk

        :param success: 缩容检查是否通过
        :type success: bool
        :param check_detail: broker检查结果
        :type check_detail: list[:class:`huaweicloudsdkkafka.v2.ShowShrinkCheckResponseBodyCheckDetail`]
        """
        
        super(ShowShrinkCheckResultResponse, self).__init__()

        self._success = None
        self._check_detail = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if check_detail is not None:
            self.check_detail = check_detail

    @property
    def success(self):
        """Gets the success of this ShowShrinkCheckResultResponse.

        缩容检查是否通过

        :return: The success of this ShowShrinkCheckResultResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ShowShrinkCheckResultResponse.

        缩容检查是否通过

        :param success: The success of this ShowShrinkCheckResultResponse.
        :type success: bool
        """
        self._success = success

    @property
    def check_detail(self):
        """Gets the check_detail of this ShowShrinkCheckResultResponse.

        broker检查结果

        :return: The check_detail of this ShowShrinkCheckResultResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowShrinkCheckResponseBodyCheckDetail`]
        """
        return self._check_detail

    @check_detail.setter
    def check_detail(self, check_detail):
        """Sets the check_detail of this ShowShrinkCheckResultResponse.

        broker检查结果

        :param check_detail: The check_detail of this ShowShrinkCheckResultResponse.
        :type check_detail: list[:class:`huaweicloudsdkkafka.v2.ShowShrinkCheckResponseBodyCheckDetail`]
        """
        self._check_detail = check_detail

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
        if not isinstance(other, ShowShrinkCheckResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
