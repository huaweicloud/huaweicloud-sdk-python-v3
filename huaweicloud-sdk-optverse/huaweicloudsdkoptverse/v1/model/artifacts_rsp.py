# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArtifactsRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'filenames': 'list[str]',
        'stage_name': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'filenames': 'filenames',
        'stage_name': 'stage_name'
    }

    def __init__(self, create_time=None, filenames=None, stage_name=None):
        r"""ArtifactsRsp

        The model defined in huaweicloud sdk

        :param create_time: **参数解释**： 创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type create_time: str
        :param filenames: **参数解释**： 标签列表。 **约束限制**： 产物列表不能超过10条。 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type filenames: list[str]
        :param stage_name: **参数解释**： 绑定状态。 **约束限制**： 不涉及 **取值范围**： * requirement_analyzer：构建需求文档。 * modeling：构建数学模型。 * data：校验模型数据。 * solver：求解数学模型。 * report：业务辅助分析。 * business_planner：构建需求文档 * data_agent：原始数据处理 * vrp：路径规划求解 **默认取值**： 不涉及 
        :type stage_name: str
        """
        
        

        self._create_time = None
        self._filenames = None
        self._stage_name = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if filenames is not None:
            self.filenames = filenames
        if stage_name is not None:
            self.stage_name = stage_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ArtifactsRsp.

        **参数解释**： 创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The create_time of this ArtifactsRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ArtifactsRsp.

        **参数解释**： 创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param create_time: The create_time of this ArtifactsRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def filenames(self):
        r"""Gets the filenames of this ArtifactsRsp.

        **参数解释**： 标签列表。 **约束限制**： 产物列表不能超过10条。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The filenames of this ArtifactsRsp.
        :rtype: list[str]
        """
        return self._filenames

    @filenames.setter
    def filenames(self, filenames):
        r"""Sets the filenames of this ArtifactsRsp.

        **参数解释**： 标签列表。 **约束限制**： 产物列表不能超过10条。 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param filenames: The filenames of this ArtifactsRsp.
        :type filenames: list[str]
        """
        self._filenames = filenames

    @property
    def stage_name(self):
        r"""Gets the stage_name of this ArtifactsRsp.

        **参数解释**： 绑定状态。 **约束限制**： 不涉及 **取值范围**： * requirement_analyzer：构建需求文档。 * modeling：构建数学模型。 * data：校验模型数据。 * solver：求解数学模型。 * report：业务辅助分析。 * business_planner：构建需求文档 * data_agent：原始数据处理 * vrp：路径规划求解 **默认取值**： 不涉及 

        :return: The stage_name of this ArtifactsRsp.
        :rtype: str
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        r"""Sets the stage_name of this ArtifactsRsp.

        **参数解释**： 绑定状态。 **约束限制**： 不涉及 **取值范围**： * requirement_analyzer：构建需求文档。 * modeling：构建数学模型。 * data：校验模型数据。 * solver：求解数学模型。 * report：业务辅助分析。 * business_planner：构建需求文档 * data_agent：原始数据处理 * vrp：路径规划求解 **默认取值**： 不涉及 

        :param stage_name: The stage_name of this ArtifactsRsp.
        :type stage_name: str
        """
        self._stage_name = stage_name

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
        if not isinstance(other, ArtifactsRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
