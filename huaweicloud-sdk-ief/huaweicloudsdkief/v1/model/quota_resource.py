# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'used': 'int',
        'min': 'int',
        'max': 'int',
        'quota': 'int',
        'project_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'used': 'used',
        'min': 'min',
        'max': 'max',
        'quota': 'quota',
        'project_id': 'project_id',
        'type': 'type'
    }

    def __init__(self, used=None, min=None, max=None, quota=None, project_id=None, type=None):
        """QuotaResource

        The model defined in huaweicloud sdk

        :param used: 已创建的资源个数
        :type used: int
        :param min: 最少可创建的资源个数
        :type min: int
        :param max: 最多可创建的资源个数
        :type max: int
        :param quota: 资源配额限制
        :type quota: int
        :param project_id: 项目ID
        :type project_id: str
        :param type: 查询配额的资源类型，支持填写： - edge_node: 边缘节点 - node_cert: 边缘节点证书 - edge_group: 边缘节点组 - group_cert: 边缘节点组证书 - application: 应用模板 - deployment: 容器应用 - device_template: 终端设备模板 - device: 终端设备 - app_version: 应用模板的版本 - tag: 标签  - configmap: 配置项 - secret: 密钥 - ief_instance: 铂金版实例 - service: 服务网格 - gateway: 服务网关
        :type type: str
        """
        
        

        self._used = None
        self._min = None
        self._max = None
        self._quota = None
        self._project_id = None
        self._type = None
        self.discriminator = None

        if used is not None:
            self.used = used
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if quota is not None:
            self.quota = quota
        if project_id is not None:
            self.project_id = project_id
        if type is not None:
            self.type = type

    @property
    def used(self):
        """Gets the used of this QuotaResource.

        已创建的资源个数

        :return: The used of this QuotaResource.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this QuotaResource.

        已创建的资源个数

        :param used: The used of this QuotaResource.
        :type used: int
        """
        self._used = used

    @property
    def min(self):
        """Gets the min of this QuotaResource.

        最少可创建的资源个数

        :return: The min of this QuotaResource.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this QuotaResource.

        最少可创建的资源个数

        :param min: The min of this QuotaResource.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this QuotaResource.

        最多可创建的资源个数

        :return: The max of this QuotaResource.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this QuotaResource.

        最多可创建的资源个数

        :param max: The max of this QuotaResource.
        :type max: int
        """
        self._max = max

    @property
    def quota(self):
        """Gets the quota of this QuotaResource.

        资源配额限制

        :return: The quota of this QuotaResource.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this QuotaResource.

        资源配额限制

        :param quota: The quota of this QuotaResource.
        :type quota: int
        """
        self._quota = quota

    @property
    def project_id(self):
        """Gets the project_id of this QuotaResource.

        项目ID

        :return: The project_id of this QuotaResource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this QuotaResource.

        项目ID

        :param project_id: The project_id of this QuotaResource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        """Gets the type of this QuotaResource.

        查询配额的资源类型，支持填写： - edge_node: 边缘节点 - node_cert: 边缘节点证书 - edge_group: 边缘节点组 - group_cert: 边缘节点组证书 - application: 应用模板 - deployment: 容器应用 - device_template: 终端设备模板 - device: 终端设备 - app_version: 应用模板的版本 - tag: 标签  - configmap: 配置项 - secret: 密钥 - ief_instance: 铂金版实例 - service: 服务网格 - gateway: 服务网关

        :return: The type of this QuotaResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QuotaResource.

        查询配额的资源类型，支持填写： - edge_node: 边缘节点 - node_cert: 边缘节点证书 - edge_group: 边缘节点组 - group_cert: 边缘节点组证书 - application: 应用模板 - deployment: 容器应用 - device_template: 终端设备模板 - device: 终端设备 - app_version: 应用模板的版本 - tag: 标签  - configmap: 配置项 - secret: 密钥 - ief_instance: 铂金版实例 - service: 服务网格 - gateway: 服务网关

        :param type: The type of this QuotaResource.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, QuotaResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
