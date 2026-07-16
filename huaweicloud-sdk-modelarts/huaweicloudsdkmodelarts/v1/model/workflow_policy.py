# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'use_scene': 'str',
        'scene_id': 'str',
        'scenes': 'list[Scene]'
    }

    attribute_map = {
        'use_scene': 'use_scene',
        'scene_id': 'scene_id',
        'scenes': 'scenes'
    }

    def __init__(self, use_scene=None, scene_id=None, scenes=None):
        r"""WorkflowPolicy

        The model defined in huaweicloud sdk

        :param use_scene: 使用场景。
        :type use_scene: str
        :param scene_id: 场景ID。
        :type scene_id: str
        :param scenes: 场景。
        :type scenes: list[:class:`huaweicloudsdkmodelarts.v1.Scene`]
        """
        
        

        self._use_scene = None
        self._scene_id = None
        self._scenes = None
        self.discriminator = None

        if use_scene is not None:
            self.use_scene = use_scene
        if scene_id is not None:
            self.scene_id = scene_id
        if scenes is not None:
            self.scenes = scenes

    @property
    def use_scene(self):
        r"""Gets the use_scene of this WorkflowPolicy.

        使用场景。

        :return: The use_scene of this WorkflowPolicy.
        :rtype: str
        """
        return self._use_scene

    @use_scene.setter
    def use_scene(self, use_scene):
        r"""Sets the use_scene of this WorkflowPolicy.

        使用场景。

        :param use_scene: The use_scene of this WorkflowPolicy.
        :type use_scene: str
        """
        self._use_scene = use_scene

    @property
    def scene_id(self):
        r"""Gets the scene_id of this WorkflowPolicy.

        场景ID。

        :return: The scene_id of this WorkflowPolicy.
        :rtype: str
        """
        return self._scene_id

    @scene_id.setter
    def scene_id(self, scene_id):
        r"""Sets the scene_id of this WorkflowPolicy.

        场景ID。

        :param scene_id: The scene_id of this WorkflowPolicy.
        :type scene_id: str
        """
        self._scene_id = scene_id

    @property
    def scenes(self):
        r"""Gets the scenes of this WorkflowPolicy.

        场景。

        :return: The scenes of this WorkflowPolicy.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Scene`]
        """
        return self._scenes

    @scenes.setter
    def scenes(self, scenes):
        r"""Sets the scenes of this WorkflowPolicy.

        场景。

        :param scenes: The scenes of this WorkflowPolicy.
        :type scenes: list[:class:`huaweicloudsdkmodelarts.v1.Scene`]
        """
        self._scenes = scenes

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkflowPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
