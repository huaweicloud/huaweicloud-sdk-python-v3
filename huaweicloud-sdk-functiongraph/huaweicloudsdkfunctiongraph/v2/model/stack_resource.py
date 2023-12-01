# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'physical_resource_id': 'str',
        'physical_resource_name': 'str',
        'logical_resource_name': 'str',
        'logical_resource_type': 'str',
        'resource_status': 'str',
        'status_message': 'str',
        'href': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'physical_resource_id': 'physical_resource_id',
        'physical_resource_name': 'physical_resource_name',
        'logical_resource_name': 'logical_resource_name',
        'logical_resource_type': 'logical_resource_type',
        'resource_status': 'resource_status',
        'status_message': 'status_message',
        'href': 'href',
        'display_name': 'display_name'
    }

    def __init__(self, physical_resource_id=None, physical_resource_name=None, logical_resource_name=None, logical_resource_type=None, resource_status=None, status_message=None, href=None, display_name=None):
        """StackResource

        The model defined in huaweicloud sdk

        :param physical_resource_id: 物理资源id
        :type physical_resource_id: str
        :param physical_resource_name: 物理资源名称
        :type physical_resource_name: str
        :param logical_resource_name: 逻辑资源名称
        :type logical_resource_name: str
        :param logical_resource_type: 逻辑资源类型
        :type logical_resource_type: str
        :param resource_status: 资源状态
        :type resource_status: str
        :param status_message: 状态信息
        :type status_message: str
        :param href: 超链接地址
        :type href: str
        :param display_name: 云服务名称
        :type display_name: str
        """
        
        

        self._physical_resource_id = None
        self._physical_resource_name = None
        self._logical_resource_name = None
        self._logical_resource_type = None
        self._resource_status = None
        self._status_message = None
        self._href = None
        self._display_name = None
        self.discriminator = None

        if physical_resource_id is not None:
            self.physical_resource_id = physical_resource_id
        if physical_resource_name is not None:
            self.physical_resource_name = physical_resource_name
        if logical_resource_name is not None:
            self.logical_resource_name = logical_resource_name
        if logical_resource_type is not None:
            self.logical_resource_type = logical_resource_type
        if resource_status is not None:
            self.resource_status = resource_status
        if status_message is not None:
            self.status_message = status_message
        if href is not None:
            self.href = href
        if display_name is not None:
            self.display_name = display_name

    @property
    def physical_resource_id(self):
        """Gets the physical_resource_id of this StackResource.

        物理资源id

        :return: The physical_resource_id of this StackResource.
        :rtype: str
        """
        return self._physical_resource_id

    @physical_resource_id.setter
    def physical_resource_id(self, physical_resource_id):
        """Sets the physical_resource_id of this StackResource.

        物理资源id

        :param physical_resource_id: The physical_resource_id of this StackResource.
        :type physical_resource_id: str
        """
        self._physical_resource_id = physical_resource_id

    @property
    def physical_resource_name(self):
        """Gets the physical_resource_name of this StackResource.

        物理资源名称

        :return: The physical_resource_name of this StackResource.
        :rtype: str
        """
        return self._physical_resource_name

    @physical_resource_name.setter
    def physical_resource_name(self, physical_resource_name):
        """Sets the physical_resource_name of this StackResource.

        物理资源名称

        :param physical_resource_name: The physical_resource_name of this StackResource.
        :type physical_resource_name: str
        """
        self._physical_resource_name = physical_resource_name

    @property
    def logical_resource_name(self):
        """Gets the logical_resource_name of this StackResource.

        逻辑资源名称

        :return: The logical_resource_name of this StackResource.
        :rtype: str
        """
        return self._logical_resource_name

    @logical_resource_name.setter
    def logical_resource_name(self, logical_resource_name):
        """Sets the logical_resource_name of this StackResource.

        逻辑资源名称

        :param logical_resource_name: The logical_resource_name of this StackResource.
        :type logical_resource_name: str
        """
        self._logical_resource_name = logical_resource_name

    @property
    def logical_resource_type(self):
        """Gets the logical_resource_type of this StackResource.

        逻辑资源类型

        :return: The logical_resource_type of this StackResource.
        :rtype: str
        """
        return self._logical_resource_type

    @logical_resource_type.setter
    def logical_resource_type(self, logical_resource_type):
        """Sets the logical_resource_type of this StackResource.

        逻辑资源类型

        :param logical_resource_type: The logical_resource_type of this StackResource.
        :type logical_resource_type: str
        """
        self._logical_resource_type = logical_resource_type

    @property
    def resource_status(self):
        """Gets the resource_status of this StackResource.

        资源状态

        :return: The resource_status of this StackResource.
        :rtype: str
        """
        return self._resource_status

    @resource_status.setter
    def resource_status(self, resource_status):
        """Sets the resource_status of this StackResource.

        资源状态

        :param resource_status: The resource_status of this StackResource.
        :type resource_status: str
        """
        self._resource_status = resource_status

    @property
    def status_message(self):
        """Gets the status_message of this StackResource.

        状态信息

        :return: The status_message of this StackResource.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this StackResource.

        状态信息

        :param status_message: The status_message of this StackResource.
        :type status_message: str
        """
        self._status_message = status_message

    @property
    def href(self):
        """Gets the href of this StackResource.

        超链接地址

        :return: The href of this StackResource.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this StackResource.

        超链接地址

        :param href: The href of this StackResource.
        :type href: str
        """
        self._href = href

    @property
    def display_name(self):
        """Gets the display_name of this StackResource.

        云服务名称

        :return: The display_name of this StackResource.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this StackResource.

        云服务名称

        :param display_name: The display_name of this StackResource.
        :type display_name: str
        """
        self._display_name = display_name

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
        if not isinstance(other, StackResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
