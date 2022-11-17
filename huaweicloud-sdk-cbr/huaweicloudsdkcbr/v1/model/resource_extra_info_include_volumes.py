# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceExtraInfoIncludeVolumes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'os_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'os_version': 'os_version'
    }

    def __init__(self, id=None, os_version=None):
        """ResourceExtraInfoIncludeVolumes

        The model defined in huaweicloud sdk

        :param id: 卷ID，仅支持uuid
        :type id: str
        :param os_version: 操作系统类型
        :type os_version: str
        """
        
        

        self._id = None
        self._os_version = None
        self.discriminator = None

        self.id = id
        if os_version is not None:
            self.os_version = os_version

    @property
    def id(self):
        """Gets the id of this ResourceExtraInfoIncludeVolumes.

        卷ID，仅支持uuid

        :return: The id of this ResourceExtraInfoIncludeVolumes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourceExtraInfoIncludeVolumes.

        卷ID，仅支持uuid

        :param id: The id of this ResourceExtraInfoIncludeVolumes.
        :type id: str
        """
        self._id = id

    @property
    def os_version(self):
        """Gets the os_version of this ResourceExtraInfoIncludeVolumes.

        操作系统类型

        :return: The os_version of this ResourceExtraInfoIncludeVolumes.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this ResourceExtraInfoIncludeVolumes.

        操作系统类型

        :param os_version: The os_version of this ResourceExtraInfoIncludeVolumes.
        :type os_version: str
        """
        self._os_version = os_version

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
        if not isinstance(other, ResourceExtraInfoIncludeVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
