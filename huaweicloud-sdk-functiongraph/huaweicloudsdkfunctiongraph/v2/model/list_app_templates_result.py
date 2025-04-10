# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppTemplatesResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'runtime': 'str',
        'category': 'str',
        'description': 'str',
        'image': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'runtime': 'runtime',
        'category': 'category',
        'description': 'description',
        'image': 'image'
    }

    def __init__(self, id=None, name=None, runtime=None, category=None, description=None, image=None):
        r"""ListAppTemplatesResult

        The model defined in huaweicloud sdk

        :param id: 模板id
        :type id: str
        :param name: 模板名称
        :type name: str
        :param runtime: 模板执行运行时
        :type runtime: str
        :param category: 模板使用场景
        :type category: str
        :param description: 模板描述
        :type description: str
        :param image: 模板镜像文件（base64编码）
        :type image: str
        """
        
        

        self._id = None
        self._name = None
        self._runtime = None
        self._category = None
        self._description = None
        self._image = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if runtime is not None:
            self.runtime = runtime
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if image is not None:
            self.image = image

    @property
    def id(self):
        r"""Gets the id of this ListAppTemplatesResult.

        模板id

        :return: The id of this ListAppTemplatesResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAppTemplatesResult.

        模板id

        :param id: The id of this ListAppTemplatesResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListAppTemplatesResult.

        模板名称

        :return: The name of this ListAppTemplatesResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAppTemplatesResult.

        模板名称

        :param name: The name of this ListAppTemplatesResult.
        :type name: str
        """
        self._name = name

    @property
    def runtime(self):
        r"""Gets the runtime of this ListAppTemplatesResult.

        模板执行运行时

        :return: The runtime of this ListAppTemplatesResult.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ListAppTemplatesResult.

        模板执行运行时

        :param runtime: The runtime of this ListAppTemplatesResult.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def category(self):
        r"""Gets the category of this ListAppTemplatesResult.

        模板使用场景

        :return: The category of this ListAppTemplatesResult.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListAppTemplatesResult.

        模板使用场景

        :param category: The category of this ListAppTemplatesResult.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this ListAppTemplatesResult.

        模板描述

        :return: The description of this ListAppTemplatesResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListAppTemplatesResult.

        模板描述

        :param description: The description of this ListAppTemplatesResult.
        :type description: str
        """
        self._description = description

    @property
    def image(self):
        r"""Gets the image of this ListAppTemplatesResult.

        模板镜像文件（base64编码）

        :return: The image of this ListAppTemplatesResult.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this ListAppTemplatesResult.

        模板镜像文件（base64编码）

        :param image: The image of this ListAppTemplatesResult.
        :type image: str
        """
        self._image = image

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
        if not isinstance(other, ListAppTemplatesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
