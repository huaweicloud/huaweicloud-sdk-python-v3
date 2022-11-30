# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateByJobIdRequest:

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
        'body': 'ListTemplateByJobIdRequestBody'
    }

    attribute_map = {
        'job_id': 'job_id',
        'body': 'body'
    }

    def __init__(self, job_id=None, body=None):
        """ListTemplateByJobIdRequest

        The model defined in huaweicloud sdk

        :param job_id: 作业id。
        :type job_id: str
        :param body: Body of the ListTemplateByJobIdRequest
        :type body: :class:`huaweicloudsdkaom.v1.ListTemplateByJobIdRequestBody`
        """
        
        

        self._job_id = None
        self._body = None
        self.discriminator = None

        self.job_id = job_id
        if body is not None:
            self.body = body

    @property
    def job_id(self):
        """Gets the job_id of this ListTemplateByJobIdRequest.

        作业id。

        :return: The job_id of this ListTemplateByJobIdRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListTemplateByJobIdRequest.

        作业id。

        :param job_id: The job_id of this ListTemplateByJobIdRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def body(self):
        """Gets the body of this ListTemplateByJobIdRequest.

        :return: The body of this ListTemplateByJobIdRequest.
        :rtype: :class:`huaweicloudsdkaom.v1.ListTemplateByJobIdRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListTemplateByJobIdRequest.

        :param body: The body of this ListTemplateByJobIdRequest.
        :type body: :class:`huaweicloudsdkaom.v1.ListTemplateByJobIdRequestBody`
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
        if not isinstance(other, ListTemplateByJobIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
