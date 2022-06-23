# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectPrivilege:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'object': 'str',
        'applicant_project_id': 'str',
        'privileges': 'list[str]'
    }

    attribute_map = {
        'object': 'object',
        'applicant_project_id': 'applicant_project_id',
        'privileges': 'privileges'
    }

    def __init__(self, object=None, applicant_project_id=None, privileges=None):
        """ProjectPrivilege

        The model defined in huaweicloud sdk

        :param object: 授权时object的信息。
        :type object: str
        :param applicant_project_id: 授权的项目ID。
        :type applicant_project_id: str
        :param privileges: 授权操作信息。
        :type privileges: list[str]
        """
        
        

        self._object = None
        self._applicant_project_id = None
        self._privileges = None
        self.discriminator = None

        if object is not None:
            self.object = object
        if applicant_project_id is not None:
            self.applicant_project_id = applicant_project_id
        if privileges is not None:
            self.privileges = privileges

    @property
    def object(self):
        """Gets the object of this ProjectPrivilege.

        授权时object的信息。

        :return: The object of this ProjectPrivilege.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ProjectPrivilege.

        授权时object的信息。

        :param object: The object of this ProjectPrivilege.
        :type object: str
        """
        self._object = object

    @property
    def applicant_project_id(self):
        """Gets the applicant_project_id of this ProjectPrivilege.

        授权的项目ID。

        :return: The applicant_project_id of this ProjectPrivilege.
        :rtype: str
        """
        return self._applicant_project_id

    @applicant_project_id.setter
    def applicant_project_id(self, applicant_project_id):
        """Sets the applicant_project_id of this ProjectPrivilege.

        授权的项目ID。

        :param applicant_project_id: The applicant_project_id of this ProjectPrivilege.
        :type applicant_project_id: str
        """
        self._applicant_project_id = applicant_project_id

    @property
    def privileges(self):
        """Gets the privileges of this ProjectPrivilege.

        授权操作信息。

        :return: The privileges of this ProjectPrivilege.
        :rtype: list[str]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this ProjectPrivilege.

        授权操作信息。

        :param privileges: The privileges of this ProjectPrivilege.
        :type privileges: list[str]
        """
        self._privileges = privileges

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
        if not isinstance(other, ProjectPrivilege):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
