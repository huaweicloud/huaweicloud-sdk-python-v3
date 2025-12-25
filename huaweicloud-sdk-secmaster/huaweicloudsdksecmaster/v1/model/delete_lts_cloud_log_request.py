# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLtsCloudLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'csvc': 'str',
        'source_name': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'csvc': 'csvc',
        'source_name': 'source_name'
    }

    def __init__(self, project_id=None, csvc=None, source_name=None):
        r"""DeleteLtsCloudLogRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param csvc: 日志分类
        :type csvc: str
        :param source_name: 日志名称
        :type source_name: str
        """
        
        

        self._project_id = None
        self._csvc = None
        self._source_name = None
        self.discriminator = None

        self.project_id = project_id
        self.csvc = csvc
        self.source_name = source_name

    @property
    def project_id(self):
        r"""Gets the project_id of this DeleteLtsCloudLogRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this DeleteLtsCloudLogRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DeleteLtsCloudLogRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this DeleteLtsCloudLogRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def csvc(self):
        r"""Gets the csvc of this DeleteLtsCloudLogRequest.

        日志分类

        :return: The csvc of this DeleteLtsCloudLogRequest.
        :rtype: str
        """
        return self._csvc

    @csvc.setter
    def csvc(self, csvc):
        r"""Sets the csvc of this DeleteLtsCloudLogRequest.

        日志分类

        :param csvc: The csvc of this DeleteLtsCloudLogRequest.
        :type csvc: str
        """
        self._csvc = csvc

    @property
    def source_name(self):
        r"""Gets the source_name of this DeleteLtsCloudLogRequest.

        日志名称

        :return: The source_name of this DeleteLtsCloudLogRequest.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this DeleteLtsCloudLogRequest.

        日志名称

        :param source_name: The source_name of this DeleteLtsCloudLogRequest.
        :type source_name: str
        """
        self._source_name = source_name

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
        if not isinstance(other, DeleteLtsCloudLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
