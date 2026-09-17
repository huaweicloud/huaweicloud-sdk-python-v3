# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'status': 'str',
        'charging_rule': 'str',
        'type': 'str',
        'resource_name': 'str',
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'associated_edge_cluster_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'status': 'status',
        'charging_rule': 'charging_rule',
        'type': 'type',
        'resource_name': 'resource_name',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'associated_edge_cluster_id': 'associated_edge_cluster_id'
    }

    def __init__(self, resource_id=None, status=None, charging_rule=None, type=None, resource_name=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, associated_edge_cluster_id=None):
        r"""ResourceDetail

        The model defined in huaweicloud sdk

        :param resource_id: 资源id，添加资源时由边缘侧生成
        :type resource_id: str
        :param status: 资源状态，冻结:freeze、解冻:unfreeze、退订:delete。
        :type status: str
        :param charging_rule: 计费规则
        :type charging_rule: str
        :param type: 内部类型
        :type type: str
        :param resource_name: 资源名称，由边缘侧生成。
        :type resource_name: str
        :param cloud_service_type: 公有云CBC上注册的服务类型英文名
        :type cloud_service_type: str
        :param resource_type: CBC上注册的资源类型编码。
        :type resource_type: str
        :param resource_spec_code: 资源规格编码
        :type resource_spec_code: str
        :param associated_edge_cluster_id: 关联的边缘集群ID
        :type associated_edge_cluster_id: str
        """
        
        

        self._resource_id = None
        self._status = None
        self._charging_rule = None
        self._type = None
        self._resource_name = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._associated_edge_cluster_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if status is not None:
            self.status = status
        if charging_rule is not None:
            self.charging_rule = charging_rule
        if type is not None:
            self.type = type
        if resource_name is not None:
            self.resource_name = resource_name
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if associated_edge_cluster_id is not None:
            self.associated_edge_cluster_id = associated_edge_cluster_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceDetail.

        资源id，添加资源时由边缘侧生成

        :return: The resource_id of this ResourceDetail.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceDetail.

        资源id，添加资源时由边缘侧生成

        :param resource_id: The resource_id of this ResourceDetail.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def status(self):
        r"""Gets the status of this ResourceDetail.

        资源状态，冻结:freeze、解冻:unfreeze、退订:delete。

        :return: The status of this ResourceDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResourceDetail.

        资源状态，冻结:freeze、解冻:unfreeze、退订:delete。

        :param status: The status of this ResourceDetail.
        :type status: str
        """
        self._status = status

    @property
    def charging_rule(self):
        r"""Gets the charging_rule of this ResourceDetail.

        计费规则

        :return: The charging_rule of this ResourceDetail.
        :rtype: str
        """
        return self._charging_rule

    @charging_rule.setter
    def charging_rule(self, charging_rule):
        r"""Sets the charging_rule of this ResourceDetail.

        计费规则

        :param charging_rule: The charging_rule of this ResourceDetail.
        :type charging_rule: str
        """
        self._charging_rule = charging_rule

    @property
    def type(self):
        r"""Gets the type of this ResourceDetail.

        内部类型

        :return: The type of this ResourceDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceDetail.

        内部类型

        :param type: The type of this ResourceDetail.
        :type type: str
        """
        self._type = type

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ResourceDetail.

        资源名称，由边缘侧生成。

        :return: The resource_name of this ResourceDetail.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ResourceDetail.

        资源名称，由边缘侧生成。

        :param resource_name: The resource_name of this ResourceDetail.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ResourceDetail.

        公有云CBC上注册的服务类型英文名

        :return: The cloud_service_type of this ResourceDetail.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ResourceDetail.

        公有云CBC上注册的服务类型英文名

        :param cloud_service_type: The cloud_service_type of this ResourceDetail.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceDetail.

        CBC上注册的资源类型编码。

        :return: The resource_type of this ResourceDetail.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceDetail.

        CBC上注册的资源类型编码。

        :param resource_type: The resource_type of this ResourceDetail.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ResourceDetail.

        资源规格编码

        :return: The resource_spec_code of this ResourceDetail.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ResourceDetail.

        资源规格编码

        :param resource_spec_code: The resource_spec_code of this ResourceDetail.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def associated_edge_cluster_id(self):
        r"""Gets the associated_edge_cluster_id of this ResourceDetail.

        关联的边缘集群ID

        :return: The associated_edge_cluster_id of this ResourceDetail.
        :rtype: str
        """
        return self._associated_edge_cluster_id

    @associated_edge_cluster_id.setter
    def associated_edge_cluster_id(self, associated_edge_cluster_id):
        r"""Sets the associated_edge_cluster_id of this ResourceDetail.

        关联的边缘集群ID

        :param associated_edge_cluster_id: The associated_edge_cluster_id of this ResourceDetail.
        :type associated_edge_cluster_id: str
        """
        self._associated_edge_cluster_id = associated_edge_cluster_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
