# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBackendTargetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_system_path': 'str',
        'obs': 'ObsDataRepository'
    }

    attribute_map = {
        'file_system_path': 'file_system_path',
        'obs': 'obs'
    }

    def __init__(self, file_system_path=None, obs=None):
        r"""CreateBackendTargetRequestBody

        The model defined in huaweicloud sdk

        :param file_system_path: 联动目录名称，SFS Turbo会在文件系统根目录下以该名称创建一个子目录，该目录用于绑定后端存储。必须是文件系统根目录下不存在的目录名。限制如下： - 长度不能超过63个字符，子目录名称不能是“.”或“..” - 不支持多层目录，不能包含字符&#39;/&#39; 
        :type file_system_path: str
        :param obs: 
        :type obs: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepository`
        """
        
        

        self._file_system_path = None
        self._obs = None
        self.discriminator = None

        self.file_system_path = file_system_path
        self.obs = obs

    @property
    def file_system_path(self):
        r"""Gets the file_system_path of this CreateBackendTargetRequestBody.

        联动目录名称，SFS Turbo会在文件系统根目录下以该名称创建一个子目录，该目录用于绑定后端存储。必须是文件系统根目录下不存在的目录名。限制如下： - 长度不能超过63个字符，子目录名称不能是“.”或“..” - 不支持多层目录，不能包含字符'/' 

        :return: The file_system_path of this CreateBackendTargetRequestBody.
        :rtype: str
        """
        return self._file_system_path

    @file_system_path.setter
    def file_system_path(self, file_system_path):
        r"""Sets the file_system_path of this CreateBackendTargetRequestBody.

        联动目录名称，SFS Turbo会在文件系统根目录下以该名称创建一个子目录，该目录用于绑定后端存储。必须是文件系统根目录下不存在的目录名。限制如下： - 长度不能超过63个字符，子目录名称不能是“.”或“..” - 不支持多层目录，不能包含字符'/' 

        :param file_system_path: The file_system_path of this CreateBackendTargetRequestBody.
        :type file_system_path: str
        """
        self._file_system_path = file_system_path

    @property
    def obs(self):
        r"""Gets the obs of this CreateBackendTargetRequestBody.

        :return: The obs of this CreateBackendTargetRequestBody.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepository`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this CreateBackendTargetRequestBody.

        :param obs: The obs of this CreateBackendTargetRequestBody.
        :type obs: :class:`huaweicloudsdksfsturbo.v1.ObsDataRepository`
        """
        self._obs = obs

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
        if not isinstance(other, CreateBackendTargetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
