# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageTemplateListResponseBodyResultImageTemplates:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'organization': 'str',
        'image_name': 'str',
        'image_label': 'str',
        'base_image': 'str',
        'title': 'str',
        'description': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'organization': 'organization',
        'image_name': 'image_name',
        'image_label': 'image_label',
        'base_image': 'base_image',
        'title': 'title',
        'description': 'description',
        'create_time': 'create_time'
    }

    def __init__(self, image_id=None, organization=None, image_name=None, image_label=None, base_image=None, title=None, description=None, create_time=None):
        r"""ShowImageTemplateListResponseBodyResultImageTemplates

        The model defined in huaweicloud sdk

        :param image_id: 镜像模版ID
        :type image_id: str
        :param organization: swr镜像组织
        :type organization: str
        :param image_name: 镜像名
        :type image_name: str
        :param image_label: 镜像label
        :type image_label: str
        :param base_image: 操作系统
        :type base_image: str
        :param title: 镜像标题
        :type title: str
        :param description: 镜像描述
        :type description: str
        :param create_time: 镜像创建日期
        :type create_time: str
        """
        
        

        self._image_id = None
        self._organization = None
        self._image_name = None
        self._image_label = None
        self._base_image = None
        self._title = None
        self._description = None
        self._create_time = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if organization is not None:
            self.organization = organization
        if image_name is not None:
            self.image_name = image_name
        if image_label is not None:
            self.image_label = image_label
        if base_image is not None:
            self.base_image = base_image
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time

    @property
    def image_id(self):
        r"""Gets the image_id of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像模版ID

        :return: The image_id of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像模版ID

        :param image_id: The image_id of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def organization(self):
        r"""Gets the organization of this ShowImageTemplateListResponseBodyResultImageTemplates.

        swr镜像组织

        :return: The organization of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        r"""Sets the organization of this ShowImageTemplateListResponseBodyResultImageTemplates.

        swr镜像组织

        :param organization: The organization of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :type organization: str
        """
        self._organization = organization

    @property
    def image_name(self):
        r"""Gets the image_name of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像名

        :return: The image_name of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像名

        :param image_name: The image_name of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_label(self):
        r"""Gets the image_label of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像label

        :return: The image_label of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :rtype: str
        """
        return self._image_label

    @image_label.setter
    def image_label(self, image_label):
        r"""Sets the image_label of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像label

        :param image_label: The image_label of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :type image_label: str
        """
        self._image_label = image_label

    @property
    def base_image(self):
        r"""Gets the base_image of this ShowImageTemplateListResponseBodyResultImageTemplates.

        操作系统

        :return: The base_image of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :rtype: str
        """
        return self._base_image

    @base_image.setter
    def base_image(self, base_image):
        r"""Sets the base_image of this ShowImageTemplateListResponseBodyResultImageTemplates.

        操作系统

        :param base_image: The base_image of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :type base_image: str
        """
        self._base_image = base_image

    @property
    def title(self):
        r"""Gets the title of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像标题

        :return: The title of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像标题

        :param title: The title of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像描述

        :return: The description of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像描述

        :param description: The description of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像创建日期

        :return: The create_time of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowImageTemplateListResponseBodyResultImageTemplates.

        镜像创建日期

        :param create_time: The create_time of this ShowImageTemplateListResponseBodyResultImageTemplates.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, ShowImageTemplateListResponseBodyResultImageTemplates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
