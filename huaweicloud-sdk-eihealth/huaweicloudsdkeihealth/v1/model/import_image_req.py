# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportImageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_project_id': 'str',
        'image_id': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'source_project_id': 'source_project_id',
        'image_id': 'image_id',
        'tag': 'tag'
    }

    def __init__(self, source_project_id=None, image_id=None, tag=None):
        """ImportImageReq

        The model defined in huaweicloud sdk

        :param source_project_id: 源项目ID
        :type source_project_id: str
        :param image_id: 镜像ID
        :type image_id: str
        :param tag: 镜像tag
        :type tag: str
        """
        
        

        self._source_project_id = None
        self._image_id = None
        self._tag = None
        self.discriminator = None

        self.source_project_id = source_project_id
        self.image_id = image_id
        self.tag = tag

    @property
    def source_project_id(self):
        """Gets the source_project_id of this ImportImageReq.

        源项目ID

        :return: The source_project_id of this ImportImageReq.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        """Sets the source_project_id of this ImportImageReq.

        源项目ID

        :param source_project_id: The source_project_id of this ImportImageReq.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def image_id(self):
        """Gets the image_id of this ImportImageReq.

        镜像ID

        :return: The image_id of this ImportImageReq.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImportImageReq.

        镜像ID

        :param image_id: The image_id of this ImportImageReq.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def tag(self):
        """Gets the tag of this ImportImageReq.

        镜像tag

        :return: The tag of this ImportImageReq.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ImportImageReq.

        镜像tag

        :param tag: The tag of this ImportImageReq.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ImportImageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
