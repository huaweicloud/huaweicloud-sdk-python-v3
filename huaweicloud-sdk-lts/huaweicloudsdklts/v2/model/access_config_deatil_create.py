# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigDeatilCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'paths': 'list[str]',
        'black_paths': 'list[str]',
        'format': 'AccessConfigFormatCreate',
        'windows_log_info': 'AccessConfigWindowsLogInfoCreate'
    }

    attribute_map = {
        'paths': 'paths',
        'black_paths': 'black_paths',
        'format': 'format',
        'windows_log_info': 'windows_log_info'
    }

    def __init__(self, paths=None, black_paths=None, format=None, windows_log_info=None):
        """AccessConfigDeatilCreate

        The model defined in huaweicloud sdk

        :param paths: 采集路径。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符&lt;&gt; &#39; | \&quot; 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次
        :type paths: list[str]
        :param black_paths: 采集路径黑名单。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符&lt;&gt; &#39; | \&quot; 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次
        :type black_paths: list[str]
        :param format: 
        :type format: :class:`huaweicloudsdklts.v2.AccessConfigFormatCreate`
        :param windows_log_info: 
        :type windows_log_info: :class:`huaweicloudsdklts.v2.AccessConfigWindowsLogInfoCreate`
        """
        
        

        self._paths = None
        self._black_paths = None
        self._format = None
        self._windows_log_info = None
        self.discriminator = None

        self.paths = paths
        if black_paths is not None:
            self.black_paths = black_paths
        self.format = format
        if windows_log_info is not None:
            self.windows_log_info = windows_log_info

    @property
    def paths(self):
        """Gets the paths of this AccessConfigDeatilCreate.

        采集路径。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符<> ' | \" 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次

        :return: The paths of this AccessConfigDeatilCreate.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this AccessConfigDeatilCreate.

        采集路径。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符<> ' | \" 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次

        :param paths: The paths of this AccessConfigDeatilCreate.
        :type paths: list[str]
        """
        self._paths = paths

    @property
    def black_paths(self):
        """Gets the black_paths of this AccessConfigDeatilCreate.

        采集路径黑名单。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符<> ' | \" 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次

        :return: The black_paths of this AccessConfigDeatilCreate.
        :rtype: list[str]
        """
        return self._black_paths

    @black_paths.setter
    def black_paths(self, black_paths):
        """Sets the black_paths of this AccessConfigDeatilCreate.

        采集路径黑名单。 1. 路径必须以/或者字母:\\\\开头 2. 不能包含特殊字符<> ' | \" 且不能只输入/ 3. 第一级目录不支持通配符*：不能以/**   /*开头 4.**只能出现一次

        :param black_paths: The black_paths of this AccessConfigDeatilCreate.
        :type black_paths: list[str]
        """
        self._black_paths = black_paths

    @property
    def format(self):
        """Gets the format of this AccessConfigDeatilCreate.

        :return: The format of this AccessConfigDeatilCreate.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigFormatCreate`
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AccessConfigDeatilCreate.

        :param format: The format of this AccessConfigDeatilCreate.
        :type format: :class:`huaweicloudsdklts.v2.AccessConfigFormatCreate`
        """
        self._format = format

    @property
    def windows_log_info(self):
        """Gets the windows_log_info of this AccessConfigDeatilCreate.

        :return: The windows_log_info of this AccessConfigDeatilCreate.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigWindowsLogInfoCreate`
        """
        return self._windows_log_info

    @windows_log_info.setter
    def windows_log_info(self, windows_log_info):
        """Sets the windows_log_info of this AccessConfigDeatilCreate.

        :param windows_log_info: The windows_log_info of this AccessConfigDeatilCreate.
        :type windows_log_info: :class:`huaweicloudsdklts.v2.AccessConfigWindowsLogInfoCreate`
        """
        self._windows_log_info = windows_log_info

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
        if not isinstance(other, AccessConfigDeatilCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
