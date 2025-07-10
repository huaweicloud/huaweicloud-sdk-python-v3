# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteScriptOrCommandReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gray_count': 'int',
        'resource_type': 'str',
        'gray_resource_ids': 'list[str]',
        'gray_fail_threshold': 'int',
        'resource_ids': 'list[str]',
        'script_ids': 'list[str]',
        'execution_timeout': 'int'
    }

    attribute_map = {
        'gray_count': 'gray_count',
        'resource_type': 'resource_type',
        'gray_resource_ids': 'gray_resource_ids',
        'gray_fail_threshold': 'gray_fail_threshold',
        'resource_ids': 'resource_ids',
        'script_ids': 'script_ids',
        'execution_timeout': 'execution_timeout'
    }

    def __init__(self, gray_count=None, resource_type=None, gray_resource_ids=None, gray_fail_threshold=None, resource_ids=None, script_ids=None, execution_timeout=None):
        r"""ExecuteScriptOrCommandReq

        The model defined in huaweicloud sdk

        :param gray_count: 灰度资源数量。
        :type gray_count: int
        :param resource_type: 资源类型，如桌面(DESKTOP)。
        :type resource_type: str
        :param gray_resource_ids: 灰度执行脚本的资源列表。
        :type gray_resource_ids: list[str]
        :param gray_fail_threshold: 灰度失败阈值，达到阈值后停止进行下一批资源执行脚本，小于gray_count。
        :type gray_fail_threshold: int
        :param resource_ids: 执行脚本的资源列表。
        :type resource_ids: list[str]
        :param script_ids: 执行的脚本列表。
        :type script_ids: list[str]
        :param execution_timeout: 执行脚本的超时时间，单位分钟。
        :type execution_timeout: int
        """
        
        

        self._gray_count = None
        self._resource_type = None
        self._gray_resource_ids = None
        self._gray_fail_threshold = None
        self._resource_ids = None
        self._script_ids = None
        self._execution_timeout = None
        self.discriminator = None

        if gray_count is not None:
            self.gray_count = gray_count
        if resource_type is not None:
            self.resource_type = resource_type
        if gray_resource_ids is not None:
            self.gray_resource_ids = gray_resource_ids
        if gray_fail_threshold is not None:
            self.gray_fail_threshold = gray_fail_threshold
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if script_ids is not None:
            self.script_ids = script_ids
        if execution_timeout is not None:
            self.execution_timeout = execution_timeout

    @property
    def gray_count(self):
        r"""Gets the gray_count of this ExecuteScriptOrCommandReq.

        灰度资源数量。

        :return: The gray_count of this ExecuteScriptOrCommandReq.
        :rtype: int
        """
        return self._gray_count

    @gray_count.setter
    def gray_count(self, gray_count):
        r"""Sets the gray_count of this ExecuteScriptOrCommandReq.

        灰度资源数量。

        :param gray_count: The gray_count of this ExecuteScriptOrCommandReq.
        :type gray_count: int
        """
        self._gray_count = gray_count

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ExecuteScriptOrCommandReq.

        资源类型，如桌面(DESKTOP)。

        :return: The resource_type of this ExecuteScriptOrCommandReq.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ExecuteScriptOrCommandReq.

        资源类型，如桌面(DESKTOP)。

        :param resource_type: The resource_type of this ExecuteScriptOrCommandReq.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def gray_resource_ids(self):
        r"""Gets the gray_resource_ids of this ExecuteScriptOrCommandReq.

        灰度执行脚本的资源列表。

        :return: The gray_resource_ids of this ExecuteScriptOrCommandReq.
        :rtype: list[str]
        """
        return self._gray_resource_ids

    @gray_resource_ids.setter
    def gray_resource_ids(self, gray_resource_ids):
        r"""Sets the gray_resource_ids of this ExecuteScriptOrCommandReq.

        灰度执行脚本的资源列表。

        :param gray_resource_ids: The gray_resource_ids of this ExecuteScriptOrCommandReq.
        :type gray_resource_ids: list[str]
        """
        self._gray_resource_ids = gray_resource_ids

    @property
    def gray_fail_threshold(self):
        r"""Gets the gray_fail_threshold of this ExecuteScriptOrCommandReq.

        灰度失败阈值，达到阈值后停止进行下一批资源执行脚本，小于gray_count。

        :return: The gray_fail_threshold of this ExecuteScriptOrCommandReq.
        :rtype: int
        """
        return self._gray_fail_threshold

    @gray_fail_threshold.setter
    def gray_fail_threshold(self, gray_fail_threshold):
        r"""Sets the gray_fail_threshold of this ExecuteScriptOrCommandReq.

        灰度失败阈值，达到阈值后停止进行下一批资源执行脚本，小于gray_count。

        :param gray_fail_threshold: The gray_fail_threshold of this ExecuteScriptOrCommandReq.
        :type gray_fail_threshold: int
        """
        self._gray_fail_threshold = gray_fail_threshold

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this ExecuteScriptOrCommandReq.

        执行脚本的资源列表。

        :return: The resource_ids of this ExecuteScriptOrCommandReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this ExecuteScriptOrCommandReq.

        执行脚本的资源列表。

        :param resource_ids: The resource_ids of this ExecuteScriptOrCommandReq.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def script_ids(self):
        r"""Gets the script_ids of this ExecuteScriptOrCommandReq.

        执行的脚本列表。

        :return: The script_ids of this ExecuteScriptOrCommandReq.
        :rtype: list[str]
        """
        return self._script_ids

    @script_ids.setter
    def script_ids(self, script_ids):
        r"""Sets the script_ids of this ExecuteScriptOrCommandReq.

        执行的脚本列表。

        :param script_ids: The script_ids of this ExecuteScriptOrCommandReq.
        :type script_ids: list[str]
        """
        self._script_ids = script_ids

    @property
    def execution_timeout(self):
        r"""Gets the execution_timeout of this ExecuteScriptOrCommandReq.

        执行脚本的超时时间，单位分钟。

        :return: The execution_timeout of this ExecuteScriptOrCommandReq.
        :rtype: int
        """
        return self._execution_timeout

    @execution_timeout.setter
    def execution_timeout(self, execution_timeout):
        r"""Sets the execution_timeout of this ExecuteScriptOrCommandReq.

        执行脚本的超时时间，单位分钟。

        :param execution_timeout: The execution_timeout of this ExecuteScriptOrCommandReq.
        :type execution_timeout: int
        """
        self._execution_timeout = execution_timeout

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
        if not isinstance(other, ExecuteScriptOrCommandReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
