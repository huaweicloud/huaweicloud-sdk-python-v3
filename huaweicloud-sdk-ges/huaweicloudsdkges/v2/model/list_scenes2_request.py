# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScenes2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scene_name': 'str',
        'application_name': 'str',
        'graph_id': 'str'
    }

    attribute_map = {
        'scene_name': 'scene_name',
        'application_name': 'application_name',
        'graph_id': 'graph_id'
    }

    def __init__(self, scene_name=None, application_name=None, graph_id=None):
        r"""ListScenes2Request

        The model defined in huaweicloud sdk

        :param scene_name: 场景名称。 当有且只有scene_name有值时，返回对应scene_name下的所有application详情。 当有且只有scene_name、application_name有值时，返回与application_name对应的application详情。 当scene_name、application_name、graph_id均无值时,返回所有SceneApplication
        :type scene_name: str
        :param application_name: 应用程序名字。 当有且只有scene_name、application_name有值时，返回与application_name对应的application详情。 当scene_name、application_name、graph_id均无值时,返回所有SceneApplication。
        :type application_name: str
        :param graph_id: 图ID。 当有且只有graph_id有值时，返回对应图id下所订阅的application详情。 当scene_name、application_name、graph_id均无值时,返回所有SceneApplication。
        :type graph_id: str
        """
        
        

        self._scene_name = None
        self._application_name = None
        self._graph_id = None
        self.discriminator = None

        if scene_name is not None:
            self.scene_name = scene_name
        if application_name is not None:
            self.application_name = application_name
        if graph_id is not None:
            self.graph_id = graph_id

    @property
    def scene_name(self):
        r"""Gets the scene_name of this ListScenes2Request.

        场景名称。 当有且只有scene_name有值时，返回对应scene_name下的所有application详情。 当有且只有scene_name、application_name有值时，返回与application_name对应的application详情。 当scene_name、application_name、graph_id均无值时,返回所有SceneApplication

        :return: The scene_name of this ListScenes2Request.
        :rtype: str
        """
        return self._scene_name

    @scene_name.setter
    def scene_name(self, scene_name):
        r"""Sets the scene_name of this ListScenes2Request.

        场景名称。 当有且只有scene_name有值时，返回对应scene_name下的所有application详情。 当有且只有scene_name、application_name有值时，返回与application_name对应的application详情。 当scene_name、application_name、graph_id均无值时,返回所有SceneApplication

        :param scene_name: The scene_name of this ListScenes2Request.
        :type scene_name: str
        """
        self._scene_name = scene_name

    @property
    def application_name(self):
        r"""Gets the application_name of this ListScenes2Request.

        应用程序名字。 当有且只有scene_name、application_name有值时，返回与application_name对应的application详情。 当scene_name、application_name、graph_id均无值时,返回所有SceneApplication。

        :return: The application_name of this ListScenes2Request.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this ListScenes2Request.

        应用程序名字。 当有且只有scene_name、application_name有值时，返回与application_name对应的application详情。 当scene_name、application_name、graph_id均无值时,返回所有SceneApplication。

        :param application_name: The application_name of this ListScenes2Request.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def graph_id(self):
        r"""Gets the graph_id of this ListScenes2Request.

        图ID。 当有且只有graph_id有值时，返回对应图id下所订阅的application详情。 当scene_name、application_name、graph_id均无值时,返回所有SceneApplication。

        :return: The graph_id of this ListScenes2Request.
        :rtype: str
        """
        return self._graph_id

    @graph_id.setter
    def graph_id(self, graph_id):
        r"""Sets the graph_id of this ListScenes2Request.

        图ID。 当有且只有graph_id有值时，返回对应图id下所订阅的application详情。 当scene_name、application_name、graph_id均无值时,返回所有SceneApplication。

        :param graph_id: The graph_id of this ListScenes2Request.
        :type graph_id: str
        """
        self._graph_id = graph_id

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
        if not isinstance(other, ListScenes2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
