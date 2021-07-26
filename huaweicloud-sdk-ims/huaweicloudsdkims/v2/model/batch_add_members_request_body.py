# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddMembersRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'images': 'list[str]',
        'projects': 'list[str]'
    }

    attribute_map = {
        'images': 'images',
        'projects': 'projects'
    }

    def __init__(self, images=None, projects=None):
        """BatchAddMembersRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._images = None
        self._projects = None
        self.discriminator = None

        self.images = images
        self.projects = projects

    @property
    def images(self):
        """Gets the images of this BatchAddMembersRequestBody.

        镜像ID列表

        :return: The images of this BatchAddMembersRequestBody.
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this BatchAddMembersRequestBody.

        镜像ID列表

        :param images: The images of this BatchAddMembersRequestBody.
        :type: list[str]
        """
        self._images = images

    @property
    def projects(self):
        """Gets the projects of this BatchAddMembersRequestBody.

        项目ID列表

        :return: The projects of this BatchAddMembersRequestBody.
        :rtype: list[str]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this BatchAddMembersRequestBody.

        项目ID列表

        :param projects: The projects of this BatchAddMembersRequestBody.
        :type: list[str]
        """
        self._projects = projects

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchAddMembersRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
