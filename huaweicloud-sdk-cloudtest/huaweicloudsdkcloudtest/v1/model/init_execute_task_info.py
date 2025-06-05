# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InitExecuteTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'release_dev': 'str',
        'version_uri': 'str',
        'is_query': 'bool'
    }

    attribute_map = {
        'release_dev': 'release_dev',
        'version_uri': 'version_uri',
        'is_query': 'is_query'
    }

    def __init__(self, release_dev=None, version_uri=None, is_query=None):
        r"""InitExecuteTaskInfo

        The model defined in huaweicloud sdk

        :param release_dev: 版本信息
        :type release_dev: str
        :param version_uri: 分支/迭代uri
        :type version_uri: str
        :param is_query: 是否只查询，不初始化（如果不存在）
        :type is_query: bool
        """
        
        

        self._release_dev = None
        self._version_uri = None
        self._is_query = None
        self.discriminator = None

        if release_dev is not None:
            self.release_dev = release_dev
        if version_uri is not None:
            self.version_uri = version_uri
        if is_query is not None:
            self.is_query = is_query

    @property
    def release_dev(self):
        r"""Gets the release_dev of this InitExecuteTaskInfo.

        版本信息

        :return: The release_dev of this InitExecuteTaskInfo.
        :rtype: str
        """
        return self._release_dev

    @release_dev.setter
    def release_dev(self, release_dev):
        r"""Sets the release_dev of this InitExecuteTaskInfo.

        版本信息

        :param release_dev: The release_dev of this InitExecuteTaskInfo.
        :type release_dev: str
        """
        self._release_dev = release_dev

    @property
    def version_uri(self):
        r"""Gets the version_uri of this InitExecuteTaskInfo.

        分支/迭代uri

        :return: The version_uri of this InitExecuteTaskInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this InitExecuteTaskInfo.

        分支/迭代uri

        :param version_uri: The version_uri of this InitExecuteTaskInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def is_query(self):
        r"""Gets the is_query of this InitExecuteTaskInfo.

        是否只查询，不初始化（如果不存在）

        :return: The is_query of this InitExecuteTaskInfo.
        :rtype: bool
        """
        return self._is_query

    @is_query.setter
    def is_query(self, is_query):
        r"""Sets the is_query of this InitExecuteTaskInfo.

        是否只查询，不初始化（如果不存在）

        :param is_query: The is_query of this InitExecuteTaskInfo.
        :type is_query: bool
        """
        self._is_query = is_query

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
        if not isinstance(other, InitExecuteTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
