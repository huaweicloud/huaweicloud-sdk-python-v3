# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatTransitIpOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virsubnet_id': 'str',
        'ip_address': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[PrivateTag]'
    }

    attribute_map = {
        'virsubnet_id': 'virsubnet_id',
        'ip_address': 'ip_address',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags'
    }

    def __init__(self, virsubnet_id=None, ip_address=None, enterprise_project_id=None, tags=None):
        r"""CreatTransitIpOption

        The model defined in huaweicloud sdk

        :param virsubnet_id: 当前项目子网的ID。
        :type virsubnet_id: str
        :param ip_address: 中转IP地址。
        :type ip_address: str
        :param enterprise_project_id: 企业项目ID。创建中转IP时，关联的企业项目ID。
        :type enterprise_project_id: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        """
        
        

        self._virsubnet_id = None
        self._ip_address = None
        self._enterprise_project_id = None
        self._tags = None
        self.discriminator = None

        self.virsubnet_id = virsubnet_id
        if ip_address is not None:
            self.ip_address = ip_address
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this CreatTransitIpOption.

        当前项目子网的ID。

        :return: The virsubnet_id of this CreatTransitIpOption.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this CreatTransitIpOption.

        当前项目子网的ID。

        :param virsubnet_id: The virsubnet_id of this CreatTransitIpOption.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this CreatTransitIpOption.

        中转IP地址。

        :return: The ip_address of this CreatTransitIpOption.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this CreatTransitIpOption.

        中转IP地址。

        :param ip_address: The ip_address of this CreatTransitIpOption.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreatTransitIpOption.

        企业项目ID。创建中转IP时，关联的企业项目ID。

        :return: The enterprise_project_id of this CreatTransitIpOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreatTransitIpOption.

        企业项目ID。创建中转IP时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CreatTransitIpOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreatTransitIpOption.

        标签

        :return: The tags of this CreatTransitIpOption.
        :rtype: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreatTransitIpOption.

        标签

        :param tags: The tags of this CreatTransitIpOption.
        :type tags: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreatTransitIpOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
