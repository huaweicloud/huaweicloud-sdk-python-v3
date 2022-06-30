# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Quota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_type': 'str',
        'quota': 'int',
        'used': 'int'
    }

    attribute_map = {
        'project_type': 'project_type',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, project_type=None, quota=None, used=None):
        """Quota

        The model defined in huaweicloud sdk

        :param project_type: UGO的项目类型。
        :type project_type: str
        :param quota: 总配额。
        :type quota: int
        :param used: 已经使用的配额。
        :type used: int
        """
        
        

        self._project_type = None
        self._quota = None
        self._used = None
        self.discriminator = None

        self.project_type = project_type
        self.quota = quota
        self.used = used

    @property
    def project_type(self):
        """Gets the project_type of this Quota.

        UGO的项目类型。

        :return: The project_type of this Quota.
        :rtype: str
        """
        return self._project_type

    @project_type.setter
    def project_type(self, project_type):
        """Sets the project_type of this Quota.

        UGO的项目类型。

        :param project_type: The project_type of this Quota.
        :type project_type: str
        """
        self._project_type = project_type

    @property
    def quota(self):
        """Gets the quota of this Quota.

        总配额。

        :return: The quota of this Quota.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this Quota.

        总配额。

        :param quota: The quota of this Quota.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        """Gets the used of this Quota.

        已经使用的配额。

        :return: The used of this Quota.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this Quota.

        已经使用的配额。

        :param used: The used of this Quota.
        :type used: int
        """
        self._used = used

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
        if not isinstance(other, Quota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
