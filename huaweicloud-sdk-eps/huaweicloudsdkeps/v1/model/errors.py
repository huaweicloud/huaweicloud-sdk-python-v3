# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Errors:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'project_id': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'project_id': 'project_id',
        'resource_type': 'resource_type'
    }

    def __init__(self, error_code=None, error_msg=None, project_id=None, resource_type=None):
        """Errors

        The model defined in huaweicloud sdk

        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误描述
        :type error_msg: str
        :param project_id: ProjectID
        :type project_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._project_id = None
        self._resource_type = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if project_id is not None:
            self.project_id = project_id
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def error_code(self):
        """Gets the error_code of this Errors.

        错误码

        :return: The error_code of this Errors.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this Errors.

        错误码

        :param error_code: The error_code of this Errors.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this Errors.

        错误描述

        :return: The error_msg of this Errors.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this Errors.

        错误描述

        :param error_msg: The error_msg of this Errors.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def project_id(self):
        """Gets the project_id of this Errors.

        ProjectID

        :return: The project_id of this Errors.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Errors.

        ProjectID

        :param project_id: The project_id of this Errors.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_type(self):
        """Gets the resource_type of this Errors.

        资源类型

        :return: The resource_type of this Errors.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Errors.

        资源类型

        :param resource_type: The resource_type of this Errors.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, Errors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
