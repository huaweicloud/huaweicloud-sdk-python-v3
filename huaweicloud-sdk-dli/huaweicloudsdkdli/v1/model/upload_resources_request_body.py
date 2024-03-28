# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadResourcesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'paths': 'list[str]',
        'group': 'str'
    }

    attribute_map = {
        'paths': 'paths',
        'group': 'group'
    }

    def __init__(self, paths=None, group=None):
        """UploadResourcesRequestBody

        The model defined in huaweicloud sdk

        :param paths: 用户OBS对象路径列表，OBS对象路径为OBS对象URL。
        :type paths: list[str]
        :param group: 所属资源分组名。
        :type group: str
        """
        
        

        self._paths = None
        self._group = None
        self.discriminator = None

        self.paths = paths
        self.group = group

    @property
    def paths(self):
        """Gets the paths of this UploadResourcesRequestBody.

        用户OBS对象路径列表，OBS对象路径为OBS对象URL。

        :return: The paths of this UploadResourcesRequestBody.
        :rtype: list[str]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """Sets the paths of this UploadResourcesRequestBody.

        用户OBS对象路径列表，OBS对象路径为OBS对象URL。

        :param paths: The paths of this UploadResourcesRequestBody.
        :type paths: list[str]
        """
        self._paths = paths

    @property
    def group(self):
        """Gets the group of this UploadResourcesRequestBody.

        所属资源分组名。

        :return: The group of this UploadResourcesRequestBody.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this UploadResourcesRequestBody.

        所属资源分组名。

        :param group: The group of this UploadResourcesRequestBody.
        :type group: str
        """
        self._group = group

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
        if not isinstance(other, UploadResourcesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
