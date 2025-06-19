# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobResourcesGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'resources': 'list[JobResource]'
    }

    attribute_map = {
        'name': 'name',
        'resources': 'resources'
    }

    def __init__(self, name=None, resources=None):
        r"""JobResourcesGroup

        The model defined in huaweicloud sdk

        :param name: 参数解释:   用户组名称 示例: group.tesddws 约束限制:  无 取值范围: 无 默认取值: 无
        :type name: str
        :param resources: 用户组资源。
        :type resources: list[:class:`huaweicloudsdkdli.v1.JobResource`]
        """
        
        

        self._name = None
        self._resources = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if resources is not None:
            self.resources = resources

    @property
    def name(self):
        r"""Gets the name of this JobResourcesGroup.

        参数解释:   用户组名称 示例: group.tesddws 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The name of this JobResourcesGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobResourcesGroup.

        参数解释:   用户组名称 示例: group.tesddws 约束限制:  无 取值范围: 无 默认取值: 无

        :param name: The name of this JobResourcesGroup.
        :type name: str
        """
        self._name = name

    @property
    def resources(self):
        r"""Gets the resources of this JobResourcesGroup.

        用户组资源。

        :return: The resources of this JobResourcesGroup.
        :rtype: list[:class:`huaweicloudsdkdli.v1.JobResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this JobResourcesGroup.

        用户组资源。

        :param resources: The resources of this JobResourcesGroup.
        :type resources: list[:class:`huaweicloudsdkdli.v1.JobResource`]
        """
        self._resources = resources

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
        if not isinstance(other, JobResourcesGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
