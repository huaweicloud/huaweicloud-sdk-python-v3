# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLaunchTemplateVersionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'launch_template_id': 'str',
        'image_id': 'str',
        'flavor_id': 'str',
        'version': 'list[int]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'launch_template_id': 'launch_template_id',
        'image_id': 'image_id',
        'flavor_id': 'flavor_id',
        'version': 'version'
    }

    def __init__(self, limit=None, marker=None, launch_template_id=None, image_id=None, flavor_id=None, version=None):
        r"""ListLaunchTemplateVersionsRequest

        The model defined in huaweicloud sdk

        :param limit: max number of resources to return
        :type limit: int
        :param marker: next page resource index id
        :type marker: str
        :param launch_template_id: 模板id
        :type launch_template_id: str
        :param image_id: 镜像id
        :type image_id: str
        :param flavor_id: 规格id
        :type flavor_id: str
        :param version: 版本
        :type version: list[int]
        """
        
        

        self._limit = None
        self._marker = None
        self._launch_template_id = None
        self._image_id = None
        self._flavor_id = None
        self._version = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if launch_template_id is not None:
            self.launch_template_id = launch_template_id
        if image_id is not None:
            self.image_id = image_id
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if version is not None:
            self.version = version

    @property
    def limit(self):
        r"""Gets the limit of this ListLaunchTemplateVersionsRequest.

        max number of resources to return

        :return: The limit of this ListLaunchTemplateVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLaunchTemplateVersionsRequest.

        max number of resources to return

        :param limit: The limit of this ListLaunchTemplateVersionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListLaunchTemplateVersionsRequest.

        next page resource index id

        :return: The marker of this ListLaunchTemplateVersionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListLaunchTemplateVersionsRequest.

        next page resource index id

        :param marker: The marker of this ListLaunchTemplateVersionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def launch_template_id(self):
        r"""Gets the launch_template_id of this ListLaunchTemplateVersionsRequest.

        模板id

        :return: The launch_template_id of this ListLaunchTemplateVersionsRequest.
        :rtype: str
        """
        return self._launch_template_id

    @launch_template_id.setter
    def launch_template_id(self, launch_template_id):
        r"""Sets the launch_template_id of this ListLaunchTemplateVersionsRequest.

        模板id

        :param launch_template_id: The launch_template_id of this ListLaunchTemplateVersionsRequest.
        :type launch_template_id: str
        """
        self._launch_template_id = launch_template_id

    @property
    def image_id(self):
        r"""Gets the image_id of this ListLaunchTemplateVersionsRequest.

        镜像id

        :return: The image_id of this ListLaunchTemplateVersionsRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListLaunchTemplateVersionsRequest.

        镜像id

        :param image_id: The image_id of this ListLaunchTemplateVersionsRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ListLaunchTemplateVersionsRequest.

        规格id

        :return: The flavor_id of this ListLaunchTemplateVersionsRequest.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ListLaunchTemplateVersionsRequest.

        规格id

        :param flavor_id: The flavor_id of this ListLaunchTemplateVersionsRequest.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def version(self):
        r"""Gets the version of this ListLaunchTemplateVersionsRequest.

        版本

        :return: The version of this ListLaunchTemplateVersionsRequest.
        :rtype: list[int]
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListLaunchTemplateVersionsRequest.

        版本

        :param version: The version of this ListLaunchTemplateVersionsRequest.
        :type version: list[int]
        """
        self._version = version

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
        if not isinstance(other, ListLaunchTemplateVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
