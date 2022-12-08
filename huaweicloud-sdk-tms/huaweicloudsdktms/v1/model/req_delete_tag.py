# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqDeleteTag:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'resources': 'list[ResourceTagBody]',
        'tags': 'list[DeleteTagRequest]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'resources': 'resources',
        'tags': 'tags'
    }

    def __init__(self, project_id=None, resources=None, tags=None):
        """ReqDeleteTag

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，resource_type为region级别服务时为必选项。
        :type project_id: str
        :param resources: 资源列表
        :type resources: list[:class:`huaweicloudsdktms.v1.ResourceTagBody`]
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdktms.v1.DeleteTagRequest`]
        """
        
        

        self._project_id = None
        self._resources = None
        self._tags = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        self.resources = resources
        self.tags = tags

    @property
    def project_id(self):
        """Gets the project_id of this ReqDeleteTag.

        项目ID，resource_type为region级别服务时为必选项。

        :return: The project_id of this ReqDeleteTag.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ReqDeleteTag.

        项目ID，resource_type为region级别服务时为必选项。

        :param project_id: The project_id of this ReqDeleteTag.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resources(self):
        """Gets the resources of this ReqDeleteTag.

        资源列表

        :return: The resources of this ReqDeleteTag.
        :rtype: list[:class:`huaweicloudsdktms.v1.ResourceTagBody`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ReqDeleteTag.

        资源列表

        :param resources: The resources of this ReqDeleteTag.
        :type resources: list[:class:`huaweicloudsdktms.v1.ResourceTagBody`]
        """
        self._resources = resources

    @property
    def tags(self):
        """Gets the tags of this ReqDeleteTag.

        标签列表

        :return: The tags of this ReqDeleteTag.
        :rtype: list[:class:`huaweicloudsdktms.v1.DeleteTagRequest`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ReqDeleteTag.

        标签列表

        :param tags: The tags of this ReqDeleteTag.
        :type tags: list[:class:`huaweicloudsdktms.v1.DeleteTagRequest`]
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
        if not isinstance(other, ReqDeleteTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
