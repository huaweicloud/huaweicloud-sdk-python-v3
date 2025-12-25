# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInfo:

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
        'tags': 'list[Match]',
        'sys_tags': 'list[Match]',
        'resource_name': 'str',
        'resource_detail': 'object'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'resource_name': 'resource_name',
        'resource_detail': 'resource_detail'
    }

    def __init__(self, resource_id=None, tags=None, sys_tags=None, resource_name=None, resource_detail=None):
        r"""ResourceInfo

        The model defined in huaweicloud sdk

        :param resource_id: 资产ID
        :type resource_id: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdksecmaster.v1.Match`]
        :param sys_tags: 系统标签
        :type sys_tags: list[:class:`huaweicloudsdksecmaster.v1.Match`]
        :param resource_name: 资产名称
        :type resource_name: str
        :param resource_detail: 资产细节
        :type resource_detail: object
        """
        
        

        self._resource_id = None
        self._tags = None
        self._sys_tags = None
        self._resource_name = None
        self._resource_detail = None
        self.discriminator = None

        self.resource_id = resource_id
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        self.resource_name = resource_name
        if resource_detail is not None:
            self.resource_detail = resource_detail

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceInfo.

        资产ID

        :return: The resource_id of this ResourceInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceInfo.

        资产ID

        :param resource_id: The resource_id of this ResourceInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def tags(self):
        r"""Gets the tags of this ResourceInfo.

        标签

        :return: The tags of this ResourceInfo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Match`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ResourceInfo.

        标签

        :param tags: The tags of this ResourceInfo.
        :type tags: list[:class:`huaweicloudsdksecmaster.v1.Match`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ResourceInfo.

        系统标签

        :return: The sys_tags of this ResourceInfo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Match`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ResourceInfo.

        系统标签

        :param sys_tags: The sys_tags of this ResourceInfo.
        :type sys_tags: list[:class:`huaweicloudsdksecmaster.v1.Match`]
        """
        self._sys_tags = sys_tags

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ResourceInfo.

        资产名称

        :return: The resource_name of this ResourceInfo.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ResourceInfo.

        资产名称

        :param resource_name: The resource_name of this ResourceInfo.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this ResourceInfo.

        资产细节

        :return: The resource_detail of this ResourceInfo.
        :rtype: object
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this ResourceInfo.

        资产细节

        :param resource_detail: The resource_detail of this ResourceInfo.
        :type resource_detail: object
        """
        self._resource_detail = resource_detail

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
        if not isinstance(other, ResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
