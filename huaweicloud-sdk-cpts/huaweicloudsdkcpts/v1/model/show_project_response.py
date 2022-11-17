# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'project': 'Project'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'project': 'project'
    }

    def __init__(self, code=None, message=None, project=None):
        """ShowProjectResponse

        The model defined in huaweicloud sdk

        :param code: code
        :type code: str
        :param message: message
        :type message: str
        :param project: 
        :type project: :class:`huaweicloudsdkcpts.v1.Project`
        """
        
        super(ShowProjectResponse, self).__init__()

        self._code = None
        self._message = None
        self._project = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if project is not None:
            self.project = project

    @property
    def code(self):
        """Gets the code of this ShowProjectResponse.

        code

        :return: The code of this ShowProjectResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowProjectResponse.

        code

        :param code: The code of this ShowProjectResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ShowProjectResponse.

        message

        :return: The message of this ShowProjectResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowProjectResponse.

        message

        :param message: The message of this ShowProjectResponse.
        :type message: str
        """
        self._message = message

    @property
    def project(self):
        """Gets the project of this ShowProjectResponse.

        :return: The project of this ShowProjectResponse.
        :rtype: :class:`huaweicloudsdkcpts.v1.Project`
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ShowProjectResponse.

        :param project: The project of this ShowProjectResponse.
        :type project: :class:`huaweicloudsdkcpts.v1.Project`
        """
        self._project = project

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
        if not isinstance(other, ShowProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
