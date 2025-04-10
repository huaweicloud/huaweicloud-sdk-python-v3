# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelationInfo:

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
        'relative_type': 'str'
    }

    attribute_map = {
        'relative_resource_id': 'relative_resource_id',
        'relative_type': 'relative_type'
    }

    def __init__(self, relative_resource_id=None, relative_type=None):
        r"""RelationInfo

        The model defined in huaweicloud sdk

        :param relative_resource_id: |参数名称：关联资源ID。| |参数约束及描述：关联资源ID。|
        :type relative_resource_id: str
        :param relative_type: |参数名称：关联资源类型。| |参数约束及描述：关联资源类型，父资源：PARENT；根资源：ROOT|
        :type relative_type: str
        """
        
        

        self._relative_resource_id = None
        self._relative_type = None
        self.discriminator = None

        if relative_resource_id is not None:
            self.relative_resource_id = relative_resource_id
        if relative_type is not None:
            self.relative_type = relative_type

    @property
    def relative_resource_id(self):
        r"""Gets the relative_resource_id of this RelationInfo.

        |参数名称：关联资源ID。| |参数约束及描述：关联资源ID。|

        :return: The relative_resource_id of this RelationInfo.
        :rtype: str
        """
        return self._relative_resource_id

    @relative_resource_id.setter
    def relative_resource_id(self, relative_resource_id):
        r"""Sets the relative_resource_id of this RelationInfo.

        |参数名称：关联资源ID。| |参数约束及描述：关联资源ID。|

        :param relative_resource_id: The relative_resource_id of this RelationInfo.
        :type relative_resource_id: str
        """
        self._relative_resource_id = relative_resource_id

    @property
    def relative_type(self):
        r"""Gets the relative_type of this RelationInfo.

        |参数名称：关联资源类型。| |参数约束及描述：关联资源类型，父资源：PARENT；根资源：ROOT|

        :return: The relative_type of this RelationInfo.
        :rtype: str
        """
        return self._relative_type

    @relative_type.setter
    def relative_type(self, relative_type):
        r"""Sets the relative_type of this RelationInfo.

        |参数名称：关联资源类型。| |参数约束及描述：关联资源类型，父资源：PARENT；根资源：ROOT|

        :param relative_type: The relative_type of this RelationInfo.
        :type relative_type: str
        """
        self._relative_type = relative_type

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
        if not isinstance(other, RelationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
