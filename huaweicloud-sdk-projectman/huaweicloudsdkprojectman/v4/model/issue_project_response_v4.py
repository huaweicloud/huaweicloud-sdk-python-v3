# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueProjectResponseV4:

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
        'project_name': 'str',
        'project_num_id': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'project_name': 'project_name',
        'project_num_id': 'project_num_id'
    }

    def __init__(self, project_id=None, project_name=None, project_num_id=None):
        """IssueProjectResponseV4

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param project_num_id: 项目数字id
        :type project_num_id: int
        """
        
        

        self._project_id = None
        self._project_name = None
        self._project_num_id = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if project_num_id is not None:
            self.project_num_id = project_num_id

    @property
    def project_id(self):
        """Gets the project_id of this IssueProjectResponseV4.

        项目id

        :return: The project_id of this IssueProjectResponseV4.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this IssueProjectResponseV4.

        项目id

        :param project_id: The project_id of this IssueProjectResponseV4.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this IssueProjectResponseV4.

        项目名称

        :return: The project_name of this IssueProjectResponseV4.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this IssueProjectResponseV4.

        项目名称

        :param project_name: The project_name of this IssueProjectResponseV4.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def project_num_id(self):
        """Gets the project_num_id of this IssueProjectResponseV4.

        项目数字id

        :return: The project_num_id of this IssueProjectResponseV4.
        :rtype: int
        """
        return self._project_num_id

    @project_num_id.setter
    def project_num_id(self, project_num_id):
        """Sets the project_num_id of this IssueProjectResponseV4.

        项目数字id

        :param project_num_id: The project_num_id of this IssueProjectResponseV4.
        :type project_num_id: int
        """
        self._project_num_id = project_num_id

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
        if not isinstance(other, IssueProjectResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
