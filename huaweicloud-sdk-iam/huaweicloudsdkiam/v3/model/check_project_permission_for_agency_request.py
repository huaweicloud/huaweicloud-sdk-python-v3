# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckProjectPermissionForAgencyRequest:

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
        'agency_id': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'agency_id': 'agency_id',
        'role_id': 'role_id'
    }

    def __init__(self, project_id=None, agency_id=None, role_id=None):
        """CheckProjectPermissionForAgencyRequest

        The model defined in huaweicloud sdk

        :param project_id: 委托方的项目ID，获取方式请参见：[获取项目名称、项目ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。
        :type project_id: str
        :param agency_id: 委托ID，获取方式请参见：[获取委托名、委托ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。
        :type agency_id: str
        :param role_id: 权限ID，获取方式请参见：[获取权限名、权限ID](https://support.huaweicloud.com/api-iam/iam_10_0001.html)。
        :type role_id: str
        """
        
        

        self._project_id = None
        self._agency_id = None
        self._role_id = None
        self.discriminator = None

        self.project_id = project_id
        self.agency_id = agency_id
        self.role_id = role_id

    @property
    def project_id(self):
        """Gets the project_id of this CheckProjectPermissionForAgencyRequest.

        委托方的项目ID，获取方式请参见：[获取项目名称、项目ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The project_id of this CheckProjectPermissionForAgencyRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CheckProjectPermissionForAgencyRequest.

        委托方的项目ID，获取方式请参见：[获取项目名称、项目ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param project_id: The project_id of this CheckProjectPermissionForAgencyRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def agency_id(self):
        """Gets the agency_id of this CheckProjectPermissionForAgencyRequest.

        委托ID，获取方式请参见：[获取委托名、委托ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The agency_id of this CheckProjectPermissionForAgencyRequest.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        """Sets the agency_id of this CheckProjectPermissionForAgencyRequest.

        委托ID，获取方式请参见：[获取委托名、委托ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param agency_id: The agency_id of this CheckProjectPermissionForAgencyRequest.
        :type agency_id: str
        """
        self._agency_id = agency_id

    @property
    def role_id(self):
        """Gets the role_id of this CheckProjectPermissionForAgencyRequest.

        权限ID，获取方式请参见：[获取权限名、权限ID](https://support.huaweicloud.com/api-iam/iam_10_0001.html)。

        :return: The role_id of this CheckProjectPermissionForAgencyRequest.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this CheckProjectPermissionForAgencyRequest.

        权限ID，获取方式请参见：[获取权限名、权限ID](https://support.huaweicloud.com/api-iam/iam_10_0001.html)。

        :param role_id: The role_id of this CheckProjectPermissionForAgencyRequest.
        :type role_id: str
        """
        self._role_id = role_id

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
        if not isinstance(other, CheckProjectPermissionForAgencyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
