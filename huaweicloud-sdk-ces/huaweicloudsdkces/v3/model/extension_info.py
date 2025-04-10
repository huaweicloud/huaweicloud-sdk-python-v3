# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'version': 'version'
    }

    def __init__(self, name=None, status=None, version=None):
        r"""ExtensionInfo

        The model defined in huaweicloud sdk

        :param name: 插件名称
        :type name: str
        :param status: 插件状态, none未安装，running运行中，stopped已停止，fault故障（进程异常），unknown故障（连接异常）
        :type status: str
        :param version: 插件版本
        :type version: str
        """
        
        

        self._name = None
        self._status = None
        self._version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version

    @property
    def name(self):
        r"""Gets the name of this ExtensionInfo.

        插件名称

        :return: The name of this ExtensionInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExtensionInfo.

        插件名称

        :param name: The name of this ExtensionInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ExtensionInfo.

        插件状态, none未安装，running运行中，stopped已停止，fault故障（进程异常），unknown故障（连接异常）

        :return: The status of this ExtensionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExtensionInfo.

        插件状态, none未安装，running运行中，stopped已停止，fault故障（进程异常），unknown故障（连接异常）

        :param status: The status of this ExtensionInfo.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        r"""Gets the version of this ExtensionInfo.

        插件版本

        :return: The version of this ExtensionInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ExtensionInfo.

        插件版本

        :param version: The version of this ExtensionInfo.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ExtensionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
