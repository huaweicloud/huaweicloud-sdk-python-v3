# coding: utf-8

import pprint
import re

import six





class RecognizeDriverLicenseRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'body': 'RecognizeDriverLicenseRequestBody'
    }

    attribute_map = {
        'project_id': 'project_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, body=None):
        """RecognizeDriverLicenseRequest - a model defined in huaweicloud sdk"""
        
        

        self._project_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        """Gets the project_id of this RecognizeDriverLicenseRequest.


        :return: The project_id of this RecognizeDriverLicenseRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RecognizeDriverLicenseRequest.


        :param project_id: The project_id of this RecognizeDriverLicenseRequest.
        :type: str
        """
        self._project_id = project_id

    @property
    def body(self):
        """Gets the body of this RecognizeDriverLicenseRequest.


        :return: The body of this RecognizeDriverLicenseRequest.
        :rtype: RecognizeDriverLicenseRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this RecognizeDriverLicenseRequest.


        :param body: The body of this RecognizeDriverLicenseRequest.
        :type: RecognizeDriverLicenseRequestBody
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecognizeDriverLicenseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
