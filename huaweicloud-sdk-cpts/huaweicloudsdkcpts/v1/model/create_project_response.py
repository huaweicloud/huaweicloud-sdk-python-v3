# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProjectResponse(SdkResponse):

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
        'project_id': 'int'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'project_id': 'project_id'
    }

    def __init__(self, code=None, message=None, project_id=None):
        """CreateProjectResponse

        The model defined in huaweicloud sdk

        :param code: 响应码
        :type code: str
        :param message: 响应消息
        :type message: str
        :param project_id: 项目ID
        :type project_id: int
        """
        
        super(CreateProjectResponse, self).__init__()

        self._code = None
        self._message = None
        self._project_id = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if project_id is not None:
            self.project_id = project_id

    @property
    def code(self):
        """Gets the code of this CreateProjectResponse.

        响应码

        :return: The code of this CreateProjectResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreateProjectResponse.

        响应码

        :param code: The code of this CreateProjectResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this CreateProjectResponse.

        响应消息

        :return: The message of this CreateProjectResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateProjectResponse.

        响应消息

        :param message: The message of this CreateProjectResponse.
        :type message: str
        """
        self._message = message

    @property
    def project_id(self):
        """Gets the project_id of this CreateProjectResponse.

        项目ID

        :return: The project_id of this CreateProjectResponse.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CreateProjectResponse.

        项目ID

        :param project_id: The project_id of this CreateProjectResponse.
        :type project_id: int
        """
        self._project_id = project_id

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
        if not isinstance(other, CreateProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
