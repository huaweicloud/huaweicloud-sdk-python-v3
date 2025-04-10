# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateReleaseReqBodyValues:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_pull_policy': 'str',
        'image_tag': 'str'
    }

    attribute_map = {
        'image_pull_policy': 'imagePullPolicy',
        'image_tag': 'imageTag'
    }

    def __init__(self, image_pull_policy=None, image_tag=None):
        r"""CreateReleaseReqBodyValues

        The model defined in huaweicloud sdk

        :param image_pull_policy: 镜像拉取策略
        :type image_pull_policy: str
        :param image_tag: 镜像标签
        :type image_tag: str
        """
        
        

        self._image_pull_policy = None
        self._image_tag = None
        self.discriminator = None

        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if image_tag is not None:
            self.image_tag = image_tag

    @property
    def image_pull_policy(self):
        r"""Gets the image_pull_policy of this CreateReleaseReqBodyValues.

        镜像拉取策略

        :return: The image_pull_policy of this CreateReleaseReqBodyValues.
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        r"""Sets the image_pull_policy of this CreateReleaseReqBodyValues.

        镜像拉取策略

        :param image_pull_policy: The image_pull_policy of this CreateReleaseReqBodyValues.
        :type image_pull_policy: str
        """
        self._image_pull_policy = image_pull_policy

    @property
    def image_tag(self):
        r"""Gets the image_tag of this CreateReleaseReqBodyValues.

        镜像标签

        :return: The image_tag of this CreateReleaseReqBodyValues.
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        r"""Sets the image_tag of this CreateReleaseReqBodyValues.

        镜像标签

        :param image_tag: The image_tag of this CreateReleaseReqBodyValues.
        :type image_tag: str
        """
        self._image_tag = image_tag

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
        if not isinstance(other, CreateReleaseReqBodyValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
