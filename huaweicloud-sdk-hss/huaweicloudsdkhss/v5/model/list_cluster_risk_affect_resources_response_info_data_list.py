# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterRiskAffectResourcesResponseInfoDataList:

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
        'resource_id': 'str',
        'resource_type': 'str',
        'namespace': 'str',
        'hit_rule': 'str',
        'hit_path_list': 'list[str]',
        'first_scan_time': 'int',
        'last_scan_time': 'int'
    }

    attribute_map = {
        'resource_name': 'resource_name',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'namespace': 'namespace',
        'hit_rule': 'hit_rule',
        'hit_path_list': 'hit_path_list',
        'first_scan_time': 'first_scan_time',
        'last_scan_time': 'last_scan_time'
    }

    def __init__(self, resource_name=None, resource_id=None, resource_type=None, namespace=None, hit_rule=None, hit_path_list=None, first_scan_time=None, last_scan_time=None):
        r"""ListClusterRiskAffectResourcesResponseInfoDataList

        The model defined in huaweicloud sdk

        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_id: 资源id
        :type resource_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param namespace: 资源所属的命名空间
        :type namespace: str
        :param hit_rule: 资源被检测出风险的命中规则
        :type hit_rule: str
        :param hit_path_list: 资源存在风险的路径列表
        :type hit_path_list: list[str]
        :param first_scan_time: 首次扫描时间
        :type first_scan_time: int
        :param last_scan_time: 最近扫描时间
        :type last_scan_time: int
        """
        
        

        self._resource_name = None
        self._resource_id = None
        self._resource_type = None
        self._namespace = None
        self._hit_rule = None
        self._hit_path_list = None
        self._first_scan_time = None
        self._last_scan_time = None
        self.discriminator = None

        if resource_name is not None:
            self.resource_name = resource_name
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if namespace is not None:
            self.namespace = namespace
        if hit_rule is not None:
            self.hit_rule = hit_rule
        if hit_path_list is not None:
            self.hit_path_list = hit_path_list
        if first_scan_time is not None:
            self.first_scan_time = first_scan_time
        if last_scan_time is not None:
            self.last_scan_time = last_scan_time

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源名称

        :return: The resource_name of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源名称

        :param resource_name: The resource_name of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源id

        :return: The resource_id of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源id

        :param resource_id: The resource_id of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源类型

        :return: The resource_type of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源类型

        :param resource_type: The resource_type of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def namespace(self):
        r"""Gets the namespace of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源所属的命名空间

        :return: The namespace of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源所属的命名空间

        :param namespace: The namespace of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def hit_rule(self):
        r"""Gets the hit_rule of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源被检测出风险的命中规则

        :return: The hit_rule of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :rtype: str
        """
        return self._hit_rule

    @hit_rule.setter
    def hit_rule(self, hit_rule):
        r"""Sets the hit_rule of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源被检测出风险的命中规则

        :param hit_rule: The hit_rule of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :type hit_rule: str
        """
        self._hit_rule = hit_rule

    @property
    def hit_path_list(self):
        r"""Gets the hit_path_list of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源存在风险的路径列表

        :return: The hit_path_list of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :rtype: list[str]
        """
        return self._hit_path_list

    @hit_path_list.setter
    def hit_path_list(self, hit_path_list):
        r"""Sets the hit_path_list of this ListClusterRiskAffectResourcesResponseInfoDataList.

        资源存在风险的路径列表

        :param hit_path_list: The hit_path_list of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :type hit_path_list: list[str]
        """
        self._hit_path_list = hit_path_list

    @property
    def first_scan_time(self):
        r"""Gets the first_scan_time of this ListClusterRiskAffectResourcesResponseInfoDataList.

        首次扫描时间

        :return: The first_scan_time of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :rtype: int
        """
        return self._first_scan_time

    @first_scan_time.setter
    def first_scan_time(self, first_scan_time):
        r"""Sets the first_scan_time of this ListClusterRiskAffectResourcesResponseInfoDataList.

        首次扫描时间

        :param first_scan_time: The first_scan_time of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :type first_scan_time: int
        """
        self._first_scan_time = first_scan_time

    @property
    def last_scan_time(self):
        r"""Gets the last_scan_time of this ListClusterRiskAffectResourcesResponseInfoDataList.

        最近扫描时间

        :return: The last_scan_time of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :rtype: int
        """
        return self._last_scan_time

    @last_scan_time.setter
    def last_scan_time(self, last_scan_time):
        r"""Sets the last_scan_time of this ListClusterRiskAffectResourcesResponseInfoDataList.

        最近扫描时间

        :param last_scan_time: The last_scan_time of this ListClusterRiskAffectResourcesResponseInfoDataList.
        :type last_scan_time: int
        """
        self._last_scan_time = last_scan_time

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
        if not isinstance(other, ListClusterRiskAffectResourcesResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
