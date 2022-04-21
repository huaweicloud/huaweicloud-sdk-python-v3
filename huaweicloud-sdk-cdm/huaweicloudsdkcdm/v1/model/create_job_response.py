# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'validation_result': 'list[JobValidationResult]'
    }

    attribute_map = {
        'name': 'name',
        'validation_result': 'validation-result'
    }

    def __init__(self, name=None, validation_result=None):
        """CreateJobResponse

        The model defined in huaweicloud sdk

        :param name: 作业名称。
        :type name: str
        :param validation_result: 校验结果： - 如果修改失败，返回失败原因。 - 如果修改成功，返回空列表。
        :type validation_result: list[:class:`huaweicloudsdkcdm.v1.JobValidationResult`]
        """
        
        super(CreateJobResponse, self).__init__()

        self._name = None
        self._validation_result = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if validation_result is not None:
            self.validation_result = validation_result

    @property
    def name(self):
        """Gets the name of this CreateJobResponse.

        作业名称。

        :return: The name of this CreateJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateJobResponse.

        作业名称。

        :param name: The name of this CreateJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def validation_result(self):
        """Gets the validation_result of this CreateJobResponse.

        校验结果： - 如果修改失败，返回失败原因。 - 如果修改成功，返回空列表。

        :return: The validation_result of this CreateJobResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.JobValidationResult`]
        """
        return self._validation_result

    @validation_result.setter
    def validation_result(self, validation_result):
        """Sets the validation_result of this CreateJobResponse.

        校验结果： - 如果修改失败，返回失败原因。 - 如果修改成功，返回空列表。

        :param validation_result: The validation_result of this CreateJobResponse.
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
        if not isinstance(other, CreateJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
