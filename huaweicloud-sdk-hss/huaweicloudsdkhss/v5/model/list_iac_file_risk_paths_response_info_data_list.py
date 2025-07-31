# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIacFileRiskPathsResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_name': 'str',
        'resource_type': 'str',
        'namespace': 'str',
        'hit_rule': 'str',
        'hit_path': 'str'
    }

    attribute_map = {
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'namespace': 'namespace',
        'hit_rule': 'hit_rule',
        'hit_path': 'hit_path'
    }

    def __init__(self, resource_name=None, resource_type=None, namespace=None, hit_rule=None, hit_path=None):
        r"""ListIacFileRiskPathsResponseInfoDataList

        The model defined in huaweicloud sdk

        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param namespace: 资源所属的命名空间
        :type namespace: str
        :param hit_rule: 风险命中的规则
        :type hit_rule: str
        :param hit_path: 存在风险的路径
        :type hit_path: str
        """
        
        

        self._resource_name = None
        self._resource_type = None
        self._namespace = None
        self._hit_rule = None
        self._hit_path = None
        self.discriminator = None

        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if namespace is not None:
            self.namespace = namespace
        if hit_rule is not None:
            self.hit_rule = hit_rule
        if hit_path is not None:
            self.hit_path = hit_path

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListIacFileRiskPathsResponseInfoDataList.

        资源名称

        :return: The resource_name of this ListIacFileRiskPathsResponseInfoDataList.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListIacFileRiskPathsResponseInfoDataList.

        资源名称

        :param resource_name: The resource_name of this ListIacFileRiskPathsResponseInfoDataList.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListIacFileRiskPathsResponseInfoDataList.

        资源类型

        :return: The resource_type of this ListIacFileRiskPathsResponseInfoDataList.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListIacFileRiskPathsResponseInfoDataList.

        资源类型

        :param resource_type: The resource_type of this ListIacFileRiskPathsResponseInfoDataList.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def namespace(self):
        r"""Gets the namespace of this ListIacFileRiskPathsResponseInfoDataList.

        资源所属的命名空间

        :return: The namespace of this ListIacFileRiskPathsResponseInfoDataList.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListIacFileRiskPathsResponseInfoDataList.

        资源所属的命名空间

        :param namespace: The namespace of this ListIacFileRiskPathsResponseInfoDataList.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def hit_rule(self):
        r"""Gets the hit_rule of this ListIacFileRiskPathsResponseInfoDataList.

        风险命中的规则

        :return: The hit_rule of this ListIacFileRiskPathsResponseInfoDataList.
        :rtype: str
        """
        return self._hit_rule

    @hit_rule.setter
    def hit_rule(self, hit_rule):
        r"""Sets the hit_rule of this ListIacFileRiskPathsResponseInfoDataList.

        风险命中的规则

        :param hit_rule: The hit_rule of this ListIacFileRiskPathsResponseInfoDataList.
        :type hit_rule: str
        """
        self._hit_rule = hit_rule

    @property
    def hit_path(self):
        r"""Gets the hit_path of this ListIacFileRiskPathsResponseInfoDataList.

        存在风险的路径

        :return: The hit_path of this ListIacFileRiskPathsResponseInfoDataList.
        :rtype: str
        """
        return self._hit_path

    @hit_path.setter
    def hit_path(self, hit_path):
        r"""Sets the hit_path of this ListIacFileRiskPathsResponseInfoDataList.

        存在风险的路径

        :param hit_path: The hit_path of this ListIacFileRiskPathsResponseInfoDataList.
        :type hit_path: str
        """
        self._hit_path = hit_path

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
        if not isinstance(other, ListIacFileRiskPathsResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
