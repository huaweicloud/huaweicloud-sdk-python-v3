# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'validation_result': 'list[JobValidationResult]'
    }

    attribute_map = {
        'validation_result': 'validation-result'
    }

    def __init__(self, validation_result=None):
        """StopJobResponse

        The model defined in huaweicloud sdk

        :param validation_result: 校验结构：如果停止作业接失败，返回失败原因，请参见validation-result参数说明。如果停止成功，返回空列表。
        :type validation_result: list[:class:`huaweicloudsdkcdm.v1.JobValidationResult`]
        """
        
        super(StopJobResponse, self).__init__()

        self._validation_result = None
        self.discriminator = None

        if validation_result is not None:
            self.validation_result = validation_result

    @property
    def validation_result(self):
        """Gets the validation_result of this StopJobResponse.

        校验结构：如果停止作业接失败，返回失败原因，请参见validation-result参数说明。如果停止成功，返回空列表。

        :return: The validation_result of this StopJobResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.JobValidationResult`]
        """
        return self._validation_result

    @validation_result.setter
    def validation_result(self, validation_result):
        """Sets the validation_result of this StopJobResponse.

        校验结构：如果停止作业接失败，返回失败原因，请参见validation-result参数说明。如果停止成功，返回空列表。

        :param validation_result: The validation_result of this StopJobResponse.
        :type validation_result: list[:class:`huaweicloudsdkcdm.v1.JobValidationResult`]
        """
        self._validation_result = validation_result

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
        if not isinstance(other, StopJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
