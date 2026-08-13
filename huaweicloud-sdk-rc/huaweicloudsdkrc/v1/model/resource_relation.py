# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceRelation:

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
        'resource_type': 'str',
        'related_resource_type': 'str',
        'related_resource_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'related_resource_type': 'related_resource_type',
        'related_resource_id': 'related_resource_id'
    }

    def __init__(self, resource_id=None, resource_type=None, related_resource_type=None, related_resource_id=None):
        r"""ResourceRelation

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param related_resource_type: 关联资源类型
        :type related_resource_type: str
        :param related_resource_id: 关联资源ID
        :type related_resource_id: str
        """
        
        

        self._resource_id = None
        self._resource_type = None
        self._related_resource_type = None
        self._related_resource_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if related_resource_type is not None:
            self.related_resource_type = related_resource_type
        if related_resource_id is not None:
            self.related_resource_id = related_resource_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceRelation.

        资源ID

        :return: The resource_id of this ResourceRelation.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceRelation.

        资源ID

        :param resource_id: The resource_id of this ResourceRelation.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ResourceRelation.

        资源类型

        :return: The resource_type of this ResourceRelation.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ResourceRelation.

        资源类型

        :param resource_type: The resource_type of this ResourceRelation.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def related_resource_type(self):
        r"""Gets the related_resource_type of this ResourceRelation.

        关联资源类型

        :return: The related_resource_type of this ResourceRelation.
        :rtype: str
        """
        return self._related_resource_type

    @related_resource_type.setter
    def related_resource_type(self, related_resource_type):
        r"""Sets the related_resource_type of this ResourceRelation.

        关联资源类型

        :param related_resource_type: The related_resource_type of this ResourceRelation.
        :type related_resource_type: str
        """
        self._related_resource_type = related_resource_type

    @property
    def related_resource_id(self):
        r"""Gets the related_resource_id of this ResourceRelation.

        关联资源ID

        :return: The related_resource_id of this ResourceRelation.
        :rtype: str
        """
        return self._related_resource_id

    @related_resource_id.setter
    def related_resource_id(self, related_resource_id):
        r"""Sets the related_resource_id of this ResourceRelation.

        关联资源ID

        :param related_resource_id: The related_resource_id of this ResourceRelation.
        :type related_resource_id: str
        """
        self._related_resource_id = related_resource_id

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
        if not isinstance(other, ResourceRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
