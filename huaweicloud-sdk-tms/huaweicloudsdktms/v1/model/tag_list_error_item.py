# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagListErrorItem:

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
        'resource_type': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'resource_type': 'resource_type',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, project_id=None, resource_type=None, error_code=None, error_msg=None):
        r"""TagListErrorItem

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        

        self._project_id = None
        self._resource_type = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        self.project_id = project_id
        self.resource_type = resource_type
        self.error_code = error_code
        self.error_msg = error_msg

    @property
    def project_id(self):
        r"""Gets the project_id of this TagListErrorItem.

        项目ID

        :return: The project_id of this TagListErrorItem.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TagListErrorItem.

        项目ID

        :param project_id: The project_id of this TagListErrorItem.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this TagListErrorItem.

        资源类型

        :return: The resource_type of this TagListErrorItem.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this TagListErrorItem.

        资源类型

        :param resource_type: The resource_type of this TagListErrorItem.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def error_code(self):
        r"""Gets the error_code of this TagListErrorItem.

        错误码

        :return: The error_code of this TagListErrorItem.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this TagListErrorItem.

        错误码

        :param error_code: The error_code of this TagListErrorItem.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this TagListErrorItem.

        错误信息

        :return: The error_msg of this TagListErrorItem.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this TagListErrorItem.

        错误信息

        :param error_msg: The error_msg of this TagListErrorItem.
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
        if not isinstance(other, TagListErrorItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
