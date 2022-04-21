# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProjectRequestV4:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'project_name': 'project_name'
    }

    def __init__(self, description=None, project_name=None):
        """UpdateProjectRequestV4

        The model defined in huaweicloud sdk

        :param description: 项目描述
        :type description: str
        :param project_name: 项目名
        :type project_name: str
        """
        
        

        self._description = None
        self._project_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.project_name = project_name

    @property
    def description(self):
        """Gets the description of this UpdateProjectRequestV4.

        项目描述

        :return: The description of this UpdateProjectRequestV4.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateProjectRequestV4.

        项目描述

        :param description: The description of this UpdateProjectRequestV4.
        :type description: str
        """
        self._description = description

    @property
    def project_name(self):
        """Gets the project_name of this UpdateProjectRequestV4.

        项目名

        :return: The project_name of this UpdateProjectRequestV4.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this UpdateProjectRequestV4.

        项目名

        :param project_name: The project_name of this UpdateProjectRequestV4.
        :type project_name: str
        """
        self._project_name = project_name

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
        if not isinstance(other, UpdateProjectRequestV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
