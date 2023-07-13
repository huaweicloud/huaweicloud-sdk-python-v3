# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'tags': 'list[InstanceTagResult]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'tags': 'tags'
    }

    def __init__(self, instance_id=None, instance_name=None, tags=None):
        """InstanceResult

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param tags: 标签列表。如果没有标签，默认为空数组。
        :type tags: list[:class:`huaweicloudsdkgaussdbfornosql.v3.InstanceTagResult`]
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._tags = None
        self.discriminator = None

        self.instance_id = instance_id
        self.instance_name = instance_name
        self.tags = tags

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceResult.

        实例ID。

        :return: The instance_id of this InstanceResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceResult.

        实例ID。

        :param instance_id: The instance_id of this InstanceResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this InstanceResult.

        实例名称。

        :return: The instance_name of this InstanceResult.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this InstanceResult.

        实例名称。

        :param instance_name: The instance_name of this InstanceResult.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def tags(self):
        """Gets the tags of this InstanceResult.

        标签列表。如果没有标签，默认为空数组。

        :return: The tags of this InstanceResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.InstanceTagResult`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InstanceResult.

        标签列表。如果没有标签，默认为空数组。

        :param tags: The tags of this InstanceResult.
        :type tags: list[:class:`huaweicloudsdkgaussdbfornosql.v3.InstanceTagResult`]
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
        if not isinstance(other, InstanceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
