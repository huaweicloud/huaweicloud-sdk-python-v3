# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResSceneRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'datasource_id': 'str',
        'ds_config': 'DsConfig',
        'scene_name': 'str',
        'specs_config': 'SpecsConfig',
        'type': 'str',
        'service_type': 'str'
    }

    attribute_map = {
        'category': 'category',
        'datasource_id': 'datasource_id',
        'ds_config': 'ds_config',
        'scene_name': 'scene_name',
        'specs_config': 'specs_config',
        'type': 'type',
        'service_type': 'service_type'
    }

    def __init__(self, category=None, datasource_id=None, ds_config=None, scene_name=None, specs_config=None, type=None, service_type=None):
        """UpdateResSceneRequestBody

        The model defined in huaweicloud sdk

        :param category: 场景类型： - customize，自定义推荐 - popularity，热门推荐 - relation，关联推荐 - personalization，猜你喜欢
        :type category: str
        :param datasource_id: 数据源id，字母、数字、下划线、减号组合32位。
        :type datasource_id: str
        :param ds_config: 
        :type ds_config: :class:`huaweicloudsdkres.v1.DsConfig`
        :param scene_name: 场景名称，1-64位的字母、数字、下划线、中划线组合。
        :type scene_name: str
        :param specs_config: 
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        :param type: 场景类型： - UI，基于用户推荐物品 - UU，基于用户推荐用户 - II，基于物品推荐物品 - IU，基于物品推荐用户
        :type type: str
        :param service_type: 服务类型： - rank，排序服务 - rec，推荐服务
        :type service_type: str
        """
        
        

        self._category = None
        self._datasource_id = None
        self._ds_config = None
        self._scene_name = None
        self._specs_config = None
        self._type = None
        self._service_type = None
        self.discriminator = None

        self.category = category
        self.datasource_id = datasource_id
        self.ds_config = ds_config
        self.scene_name = scene_name
        self.specs_config = specs_config
        self.type = type
        self.service_type = service_type

    @property
    def category(self):
        """Gets the category of this UpdateResSceneRequestBody.

        场景类型： - customize，自定义推荐 - popularity，热门推荐 - relation，关联推荐 - personalization，猜你喜欢

        :return: The category of this UpdateResSceneRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this UpdateResSceneRequestBody.

        场景类型： - customize，自定义推荐 - popularity，热门推荐 - relation，关联推荐 - personalization，猜你喜欢

        :param category: The category of this UpdateResSceneRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def datasource_id(self):
        """Gets the datasource_id of this UpdateResSceneRequestBody.

        数据源id，字母、数字、下划线、减号组合32位。

        :return: The datasource_id of this UpdateResSceneRequestBody.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """Sets the datasource_id of this UpdateResSceneRequestBody.

        数据源id，字母、数字、下划线、减号组合32位。

        :param datasource_id: The datasource_id of this UpdateResSceneRequestBody.
        :type datasource_id: str
        """
        self._datasource_id = datasource_id

    @property
    def ds_config(self):
        """Gets the ds_config of this UpdateResSceneRequestBody.

        :return: The ds_config of this UpdateResSceneRequestBody.
        :rtype: :class:`huaweicloudsdkres.v1.DsConfig`
        """
        return self._ds_config

    @ds_config.setter
    def ds_config(self, ds_config):
        """Sets the ds_config of this UpdateResSceneRequestBody.

        :param ds_config: The ds_config of this UpdateResSceneRequestBody.
        :type ds_config: :class:`huaweicloudsdkres.v1.DsConfig`
        """
        self._ds_config = ds_config

    @property
    def scene_name(self):
        """Gets the scene_name of this UpdateResSceneRequestBody.

        场景名称，1-64位的字母、数字、下划线、中划线组合。

        :return: The scene_name of this UpdateResSceneRequestBody.
        :rtype: str
        """
        return self._scene_name

    @scene_name.setter
    def scene_name(self, scene_name):
        """Sets the scene_name of this UpdateResSceneRequestBody.

        场景名称，1-64位的字母、数字、下划线、中划线组合。

        :param scene_name: The scene_name of this UpdateResSceneRequestBody.
        :type scene_name: str
        """
        self._scene_name = scene_name

    @property
    def specs_config(self):
        """Gets the specs_config of this UpdateResSceneRequestBody.

        :return: The specs_config of this UpdateResSceneRequestBody.
        :rtype: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        return self._specs_config

    @specs_config.setter
    def specs_config(self, specs_config):
        """Sets the specs_config of this UpdateResSceneRequestBody.

        :param specs_config: The specs_config of this UpdateResSceneRequestBody.
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        self._specs_config = specs_config

    @property
    def type(self):
        """Gets the type of this UpdateResSceneRequestBody.

        场景类型： - UI，基于用户推荐物品 - UU，基于用户推荐用户 - II，基于物品推荐物品 - IU，基于物品推荐用户

        :return: The type of this UpdateResSceneRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateResSceneRequestBody.

        场景类型： - UI，基于用户推荐物品 - UU，基于用户推荐用户 - II，基于物品推荐物品 - IU，基于物品推荐用户

        :param type: The type of this UpdateResSceneRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def service_type(self):
        """Gets the service_type of this UpdateResSceneRequestBody.

        服务类型： - rank，排序服务 - rec，推荐服务

        :return: The service_type of this UpdateResSceneRequestBody.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this UpdateResSceneRequestBody.

        服务类型： - rank，排序服务 - rec，推荐服务

        :param service_type: The service_type of this UpdateResSceneRequestBody.
        :type service_type: str
        """
        self._service_type = service_type

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
        if not isinstance(other, UpdateResSceneRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
