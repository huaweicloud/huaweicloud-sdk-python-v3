# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelativeResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relative_resource_id': 'str',
        'relative_resource_name': 'str',
        'relative_type': 'int',
        'relative_cloud_service_type': 'str',
        'relative_resource_type': 'str',
        'extend_params': 'str'
    }

    attribute_map = {
        'relative_resource_id': 'relative_resource_id',
        'relative_resource_name': 'relative_resource_name',
        'relative_type': 'relative_type',
        'relative_cloud_service_type': 'relative_cloud_service_type',
        'relative_resource_type': 'relative_resource_type',
        'extend_params': 'extend_params'
    }

    def __init__(self, relative_resource_id=None, relative_resource_name=None, relative_type=None, relative_cloud_service_type=None, relative_resource_type=None, extend_params=None):
        """RelativeResource

        The model defined in huaweicloud sdk

        :param relative_resource_id: 关联的资源ID
        :type relative_resource_id: str
        :param relative_resource_name: 有资源名称的云资源，都需要返回resourceName，如果为空值，则返回“”。
        :type relative_resource_name: str
        :param relative_type: * 关联关系类型，描述relativeResourceId和resourceId间的关联关系：    * 0：挂载(弱关联)，表示relativeResourceId和resourceId两者有关联关系，     * 但是两者可以独立使用、分别进行交易，且分别使用和交易都不影响整套云服务的使用；比如云主机和数据盘。 *     1：绑定(强关联)，表示relativeResourceId和resourceId是强绑定关系，      两者必须一起使用、一起进行交易，缺少其中一个会造成整套云服务不能使用；比如云主机和系统盘。           缺省值为0(挂载)。           subResources中的RelativeResource，此字段是必填；mainResources中的RelativeResource，
        :type relative_type: int
        :param relative_cloud_service_type: 比如ECS云服务类型为‘hws.service.type.ec2’
        :type relative_cloud_service_type: str
        :param relative_resource_type: 比如VM的资源类型为‘hws.resource.type.vm’
        :type relative_resource_type: str
        :param extend_params: 扩展信息，Key:Value格式
        :type extend_params: str
        """
        
        

        self._relative_resource_id = None
        self._relative_resource_name = None
        self._relative_type = None
        self._relative_cloud_service_type = None
        self._relative_resource_type = None
        self._extend_params = None
        self.discriminator = None

        if relative_resource_id is not None:
            self.relative_resource_id = relative_resource_id
        if relative_resource_name is not None:
            self.relative_resource_name = relative_resource_name
        if relative_type is not None:
            self.relative_type = relative_type
        if relative_cloud_service_type is not None:
            self.relative_cloud_service_type = relative_cloud_service_type
        if relative_resource_type is not None:
            self.relative_resource_type = relative_resource_type
        if extend_params is not None:
            self.extend_params = extend_params

    @property
    def relative_resource_id(self):
        """Gets the relative_resource_id of this RelativeResource.

        关联的资源ID

        :return: The relative_resource_id of this RelativeResource.
        :rtype: str
        """
        return self._relative_resource_id

    @relative_resource_id.setter
    def relative_resource_id(self, relative_resource_id):
        """Sets the relative_resource_id of this RelativeResource.

        关联的资源ID

        :param relative_resource_id: The relative_resource_id of this RelativeResource.
        :type relative_resource_id: str
        """
        self._relative_resource_id = relative_resource_id

    @property
    def relative_resource_name(self):
        """Gets the relative_resource_name of this RelativeResource.

        有资源名称的云资源，都需要返回resourceName，如果为空值，则返回“”。

        :return: The relative_resource_name of this RelativeResource.
        :rtype: str
        """
        return self._relative_resource_name

    @relative_resource_name.setter
    def relative_resource_name(self, relative_resource_name):
        """Sets the relative_resource_name of this RelativeResource.

        有资源名称的云资源，都需要返回resourceName，如果为空值，则返回“”。

        :param relative_resource_name: The relative_resource_name of this RelativeResource.
        :type relative_resource_name: str
        """
        self._relative_resource_name = relative_resource_name

    @property
    def relative_type(self):
        """Gets the relative_type of this RelativeResource.

        * 关联关系类型，描述relativeResourceId和resourceId间的关联关系：    * 0：挂载(弱关联)，表示relativeResourceId和resourceId两者有关联关系，     * 但是两者可以独立使用、分别进行交易，且分别使用和交易都不影响整套云服务的使用；比如云主机和数据盘。 *     1：绑定(强关联)，表示relativeResourceId和resourceId是强绑定关系，      两者必须一起使用、一起进行交易，缺少其中一个会造成整套云服务不能使用；比如云主机和系统盘。           缺省值为0(挂载)。           subResources中的RelativeResource，此字段是必填；mainResources中的RelativeResource，

        :return: The relative_type of this RelativeResource.
        :rtype: int
        """
        return self._relative_type

    @relative_type.setter
    def relative_type(self, relative_type):
        """Sets the relative_type of this RelativeResource.

        * 关联关系类型，描述relativeResourceId和resourceId间的关联关系：    * 0：挂载(弱关联)，表示relativeResourceId和resourceId两者有关联关系，     * 但是两者可以独立使用、分别进行交易，且分别使用和交易都不影响整套云服务的使用；比如云主机和数据盘。 *     1：绑定(强关联)，表示relativeResourceId和resourceId是强绑定关系，      两者必须一起使用、一起进行交易，缺少其中一个会造成整套云服务不能使用；比如云主机和系统盘。           缺省值为0(挂载)。           subResources中的RelativeResource，此字段是必填；mainResources中的RelativeResource，

        :param relative_type: The relative_type of this RelativeResource.
        :type relative_type: int
        """
        self._relative_type = relative_type

    @property
    def relative_cloud_service_type(self):
        """Gets the relative_cloud_service_type of this RelativeResource.

        比如ECS云服务类型为‘hws.service.type.ec2’

        :return: The relative_cloud_service_type of this RelativeResource.
        :rtype: str
        """
        return self._relative_cloud_service_type

    @relative_cloud_service_type.setter
    def relative_cloud_service_type(self, relative_cloud_service_type):
        """Sets the relative_cloud_service_type of this RelativeResource.

        比如ECS云服务类型为‘hws.service.type.ec2’

        :param relative_cloud_service_type: The relative_cloud_service_type of this RelativeResource.
        :type relative_cloud_service_type: str
        """
        self._relative_cloud_service_type = relative_cloud_service_type

    @property
    def relative_resource_type(self):
        """Gets the relative_resource_type of this RelativeResource.

        比如VM的资源类型为‘hws.resource.type.vm’

        :return: The relative_resource_type of this RelativeResource.
        :rtype: str
        """
        return self._relative_resource_type

    @relative_resource_type.setter
    def relative_resource_type(self, relative_resource_type):
        """Sets the relative_resource_type of this RelativeResource.

        比如VM的资源类型为‘hws.resource.type.vm’

        :param relative_resource_type: The relative_resource_type of this RelativeResource.
        :type relative_resource_type: str
        """
        self._relative_resource_type = relative_resource_type

    @property
    def extend_params(self):
        """Gets the extend_params of this RelativeResource.

        扩展信息，Key:Value格式

        :return: The extend_params of this RelativeResource.
        :rtype: str
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        """Sets the extend_params of this RelativeResource.

        扩展信息，Key:Value格式

        :param extend_params: The extend_params of this RelativeResource.
        :type extend_params: str
        """
        self._extend_params = extend_params

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
        if not isinstance(other, RelativeResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
