# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTemplateVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'steps': 'list[CreateBuildJobSteps]',
        'actions': 'object',
        'auto_update_sub_module': 'bool',
        'image': 'str',
        'image_source': 'str'
    }

    attribute_map = {
        'steps': 'steps',
        'actions': 'actions',
        'auto_update_sub_module': 'auto_update_sub_module',
        'image': 'image',
        'image_source': 'image_source'
    }

    def __init__(self, steps=None, actions=None, auto_update_sub_module=None, image=None, image_source=None):
        r"""QueryTemplateVo

        The model defined in huaweicloud sdk

        :param steps: 构建执行的步骤。
        :type steps: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        :param actions: 构建步骤中的action。
        :type actions: object
        :param auto_update_sub_module: 是否自动更新子模块。
        :type auto_update_sub_module: bool
        :param image: 配置镜像地址。
        :type image: str
        :param image_source: 配置镜像源的地址。
        :type image_source: str
        """
        
        

        self._steps = None
        self._actions = None
        self._auto_update_sub_module = None
        self._image = None
        self._image_source = None
        self.discriminator = None

        if steps is not None:
            self.steps = steps
        if actions is not None:
            self.actions = actions
        if auto_update_sub_module is not None:
            self.auto_update_sub_module = auto_update_sub_module
        if image is not None:
            self.image = image
        if image_source is not None:
            self.image_source = image_source

    @property
    def steps(self):
        r"""Gets the steps of this QueryTemplateVo.

        构建执行的步骤。

        :return: The steps of this QueryTemplateVo.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this QueryTemplateVo.

        构建执行的步骤。

        :param steps: The steps of this QueryTemplateVo.
        :type steps: list[:class:`huaweicloudsdkcodeartsbuild.v3.CreateBuildJobSteps`]
        """
        self._steps = steps

    @property
    def actions(self):
        r"""Gets the actions of this QueryTemplateVo.

        构建步骤中的action。

        :return: The actions of this QueryTemplateVo.
        :rtype: object
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this QueryTemplateVo.

        构建步骤中的action。

        :param actions: The actions of this QueryTemplateVo.
        :type actions: object
        """
        self._actions = actions

    @property
    def auto_update_sub_module(self):
        r"""Gets the auto_update_sub_module of this QueryTemplateVo.

        是否自动更新子模块。

        :return: The auto_update_sub_module of this QueryTemplateVo.
        :rtype: bool
        """
        return self._auto_update_sub_module

    @auto_update_sub_module.setter
    def auto_update_sub_module(self, auto_update_sub_module):
        r"""Sets the auto_update_sub_module of this QueryTemplateVo.

        是否自动更新子模块。

        :param auto_update_sub_module: The auto_update_sub_module of this QueryTemplateVo.
        :type auto_update_sub_module: bool
        """
        self._auto_update_sub_module = auto_update_sub_module

    @property
    def image(self):
        r"""Gets the image of this QueryTemplateVo.

        配置镜像地址。

        :return: The image of this QueryTemplateVo.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this QueryTemplateVo.

        配置镜像地址。

        :param image: The image of this QueryTemplateVo.
        :type image: str
        """
        self._image = image

    @property
    def image_source(self):
        r"""Gets the image_source of this QueryTemplateVo.

        配置镜像源的地址。

        :return: The image_source of this QueryTemplateVo.
        :rtype: str
        """
        return self._image_source

    @image_source.setter
    def image_source(self, image_source):
        r"""Sets the image_source of this QueryTemplateVo.

        配置镜像源的地址。

        :param image_source: The image_source of this QueryTemplateVo.
        :type image_source: str
        """
        self._image_source = image_source

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
        if not isinstance(other, QueryTemplateVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
