# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResIntelligentSceneRequestNBody:

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
        'scene_name': 'str',
        'specs_config': 'SpecsConfig',
        'schedule': 'str',
        'job_configs': 'JobConfig'
    }

    attribute_map = {
        'category': 'category',
        'datasource_id': 'datasource_id',
        'scene_name': 'scene_name',
        'specs_config': 'specs_config',
        'schedule': 'schedule',
        'job_configs': 'job_configs'
    }

    def __init__(self, category=None, datasource_id=None, scene_name=None, specs_config=None, schedule=None, job_configs=None):
        """CreateResIntelligentSceneRequestNBody

        The model defined in huaweicloud sdk

        :param category: 场景类型： - popularity，热门推荐 - relation，关联推荐 - personalization，猜你喜欢
        :type category: str
        :param datasource_id: 数据源id。
        :type datasource_id: str
        :param scene_name: 场景名称:字母、数字、下划线、中划线组合。
        :type scene_name: str
        :param specs_config: 
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        :param schedule: 调度信息。
        :type schedule: str
        :param job_configs: 
        :type job_configs: :class:`huaweicloudsdkres.v1.JobConfig`
        """
        
        

        self._category = None
        self._datasource_id = None
        self._scene_name = None
        self._specs_config = None
        self._schedule = None
        self._job_configs = None
        self.discriminator = None

        self.category = category
        self.datasource_id = datasource_id
        self.scene_name = scene_name
        self.specs_config = specs_config
        if schedule is not None:
            self.schedule = schedule
        self.job_configs = job_configs

    @property
    def category(self):
        """Gets the category of this CreateResIntelligentSceneRequestNBody.

        场景类型： - popularity，热门推荐 - relation，关联推荐 - personalization，猜你喜欢

        :return: The category of this CreateResIntelligentSceneRequestNBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CreateResIntelligentSceneRequestNBody.

        场景类型： - popularity，热门推荐 - relation，关联推荐 - personalization，猜你喜欢

        :param category: The category of this CreateResIntelligentSceneRequestNBody.
        :type category: str
        """
        self._category = category

    @property
    def datasource_id(self):
        """Gets the datasource_id of this CreateResIntelligentSceneRequestNBody.

        数据源id。

        :return: The datasource_id of this CreateResIntelligentSceneRequestNBody.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """Sets the datasource_id of this CreateResIntelligentSceneRequestNBody.

        数据源id。

        :param datasource_id: The datasource_id of this CreateResIntelligentSceneRequestNBody.
        :type datasource_id: str
        """
        self._datasource_id = datasource_id

    @property
    def scene_name(self):
        """Gets the scene_name of this CreateResIntelligentSceneRequestNBody.

        场景名称:字母、数字、下划线、中划线组合。

        :return: The scene_name of this CreateResIntelligentSceneRequestNBody.
        :rtype: str
        """
        return self._scene_name

    @scene_name.setter
    def scene_name(self, scene_name):
        """Sets the scene_name of this CreateResIntelligentSceneRequestNBody.

        场景名称:字母、数字、下划线、中划线组合。

        :param scene_name: The scene_name of this CreateResIntelligentSceneRequestNBody.
        :type scene_name: str
        """
        self._scene_name = scene_name

    @property
    def specs_config(self):
        """Gets the specs_config of this CreateResIntelligentSceneRequestNBody.


        :return: The specs_config of this CreateResIntelligentSceneRequestNBody.
        :rtype: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        return self._specs_config

    @specs_config.setter
    def specs_config(self, specs_config):
        """Sets the specs_config of this CreateResIntelligentSceneRequestNBody.


        :param specs_config: The specs_config of this CreateResIntelligentSceneRequestNBody.
        :type specs_config: :class:`huaweicloudsdkres.v1.SpecsConfig`
        """
        self._specs_config = specs_config

    @property
    def schedule(self):
        """Gets the schedule of this CreateResIntelligentSceneRequestNBody.

        调度信息。

        :return: The schedule of this CreateResIntelligentSceneRequestNBody.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this CreateResIntelligentSceneRequestNBody.

        调度信息。

        :param schedule: The schedule of this CreateResIntelligentSceneRequestNBody.
        :type schedule: str
        """
        self._schedule = schedule

    @property
    def job_configs(self):
        """Gets the job_configs of this CreateResIntelligentSceneRequestNBody.


        :return: The job_configs of this CreateResIntelligentSceneRequestNBody.
        :rtype: :class:`huaweicloudsdkres.v1.JobConfig`
        """
        return self._job_configs

    @job_configs.setter
    def job_configs(self, job_configs):
        """Sets the job_configs of this CreateResIntelligentSceneRequestNBody.


        :param job_configs: The job_configs of this CreateResIntelligentSceneRequestNBody.
        :type job_configs: :class:`huaweicloudsdkres.v1.JobConfig`
        """
        self._job_configs = job_configs

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
        if not isinstance(other, CreateResIntelligentSceneRequestNBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
