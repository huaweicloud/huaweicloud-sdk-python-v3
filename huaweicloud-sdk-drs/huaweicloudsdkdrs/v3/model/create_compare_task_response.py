# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCompareTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'object_level_compare_create_result': 'CreateCompareTaskResult',
        'data_level_compare_create_result': 'CreateCompareTaskResult',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'object_level_compare_create_result': 'object_level_compare_create_result',
        'data_level_compare_create_result': 'data_level_compare_create_result',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, job_id=None, object_level_compare_create_result=None, data_level_compare_create_result=None, error_code=None, error_msg=None):
        """CreateCompareTaskResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务id。
        :type job_id: str
        :param object_level_compare_create_result: 
        :type object_level_compare_create_result: :class:`huaweicloudsdkdrs.v3.CreateCompareTaskResult`
        :param data_level_compare_create_result: 
        :type data_level_compare_create_result: :class:`huaweicloudsdkdrs.v3.CreateCompareTaskResult`
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误信息。
        :type error_msg: str
        """
        
        super(CreateCompareTaskResponse, self).__init__()

        self._job_id = None
        self._object_level_compare_create_result = None
        self._data_level_compare_create_result = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if object_level_compare_create_result is not None:
            self.object_level_compare_create_result = object_level_compare_create_result
        if data_level_compare_create_result is not None:
            self.data_level_compare_create_result = data_level_compare_create_result
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def job_id(self):
        """Gets the job_id of this CreateCompareTaskResponse.

        任务id。

        :return: The job_id of this CreateCompareTaskResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateCompareTaskResponse.

        任务id。

        :param job_id: The job_id of this CreateCompareTaskResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def object_level_compare_create_result(self):
        """Gets the object_level_compare_create_result of this CreateCompareTaskResponse.


        :return: The object_level_compare_create_result of this CreateCompareTaskResponse.
        :rtype: :class:`huaweicloudsdkdrs.v3.CreateCompareTaskResult`
        """
        return self._object_level_compare_create_result

    @object_level_compare_create_result.setter
    def object_level_compare_create_result(self, object_level_compare_create_result):
        """Sets the object_level_compare_create_result of this CreateCompareTaskResponse.


        :param object_level_compare_create_result: The object_level_compare_create_result of this CreateCompareTaskResponse.
        :type object_level_compare_create_result: :class:`huaweicloudsdkdrs.v3.CreateCompareTaskResult`
        """
        self._object_level_compare_create_result = object_level_compare_create_result

    @property
    def data_level_compare_create_result(self):
        """Gets the data_level_compare_create_result of this CreateCompareTaskResponse.


        :return: The data_level_compare_create_result of this CreateCompareTaskResponse.
        :rtype: :class:`huaweicloudsdkdrs.v3.CreateCompareTaskResult`
        """
        return self._data_level_compare_create_result

    @data_level_compare_create_result.setter
    def data_level_compare_create_result(self, data_level_compare_create_result):
        """Sets the data_level_compare_create_result of this CreateCompareTaskResponse.


        :param data_level_compare_create_result: The data_level_compare_create_result of this CreateCompareTaskResponse.
        :type data_level_compare_create_result: :class:`huaweicloudsdkdrs.v3.CreateCompareTaskResult`
        """
        self._data_level_compare_create_result = data_level_compare_create_result

    @property
    def error_code(self):
        """Gets the error_code of this CreateCompareTaskResponse.

        错误码。

        :return: The error_code of this CreateCompareTaskResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CreateCompareTaskResponse.

        错误码。

        :param error_code: The error_code of this CreateCompareTaskResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this CreateCompareTaskResponse.

        错误信息。

        :return: The error_msg of this CreateCompareTaskResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CreateCompareTaskResponse.

        错误信息。

        :param error_msg: The error_msg of this CreateCompareTaskResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, CreateCompareTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
