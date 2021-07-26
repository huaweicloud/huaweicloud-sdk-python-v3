# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateParamsRequest:


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
        'x_language': 'str',
        'body': 'ModifyTargetParamsReq'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, job_id=None, x_language=None, body=None):
        """UpdateParamsRequest - a model defined in huaweicloud sdk"""
        
        

        self._job_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.job_id = job_id
        self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def job_id(self):
        """Gets the job_id of this UpdateParamsRequest.

        任务ID

        :return: The job_id of this UpdateParamsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateParamsRequest.

        任务ID

        :param job_id: The job_id of this UpdateParamsRequest.
        :type: str
        """
        self._job_id = job_id

    @property
    def x_language(self):
        """Gets the x_language of this UpdateParamsRequest.

        请求语言类型

        :return: The x_language of this UpdateParamsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this UpdateParamsRequest.

        请求语言类型

        :param x_language: The x_language of this UpdateParamsRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def body(self):
        """Gets the body of this UpdateParamsRequest.


        :return: The body of this UpdateParamsRequest.
        :rtype: ModifyTargetParamsReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateParamsRequest.


        :param body: The body of this UpdateParamsRequest.
        :type: ModifyTargetParamsReq
        """
        self._body = body

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateParamsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
