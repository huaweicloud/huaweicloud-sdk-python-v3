# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpdFieldsV2Request:

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
        'category_id': 'str',
        'category_layer_id': 'str',
        'target_project_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'category_id': 'category_id',
        'category_layer_id': 'category_layer_id',
        'target_project_id': 'target_project_id'
    }

    def __init__(self, project_id=None, category_id=None, category_layer_id=None, target_project_id=None):
        r"""ShowIpdFieldsV2Request

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param category_id: 工作项类型ID，工作项类型的唯一标识。 不同项目模型下可选值不同： - IPD-系统设备类：10021（RR）、10065（SF）、10020（IR）、10022（SR）、10029（AR）、10027（Task）、10033（Bug） - IPD-独立软件类：10021（RR）、10065（SF）、10020（IR）、10023（US）、10027（Task）、10033（Bug） - IPD-自运营软件/云服务类：10001（Epic）、10028（FE）、10021（RR）、10023（US）、10027（Task）、10033（Bug）
        :type category_id: str
        :param category_layer_id: 层级字段ID。用于过滤层级类型的字段，当需要按层级结构筛选字段时传入。
        :type category_layer_id: str
        :param target_project_id: 目标项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。当需要查询其他项目的字段配置时传入。
        :type target_project_id: str
        """
        
        

        self._project_id = None
        self._category_id = None
        self._category_layer_id = None
        self._target_project_id = None
        self.discriminator = None

        self.project_id = project_id
        self.category_id = category_id
        if category_layer_id is not None:
            self.category_layer_id = category_layer_id
        if target_project_id is not None:
            self.target_project_id = target_project_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowIpdFieldsV2Request.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this ShowIpdFieldsV2Request.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowIpdFieldsV2Request.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this ShowIpdFieldsV2Request.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def category_id(self):
        r"""Gets the category_id of this ShowIpdFieldsV2Request.

        工作项类型ID，工作项类型的唯一标识。 不同项目模型下可选值不同： - IPD-系统设备类：10021（RR）、10065（SF）、10020（IR）、10022（SR）、10029（AR）、10027（Task）、10033（Bug） - IPD-独立软件类：10021（RR）、10065（SF）、10020（IR）、10023（US）、10027（Task）、10033（Bug） - IPD-自运营软件/云服务类：10001（Epic）、10028（FE）、10021（RR）、10023（US）、10027（Task）、10033（Bug）

        :return: The category_id of this ShowIpdFieldsV2Request.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this ShowIpdFieldsV2Request.

        工作项类型ID，工作项类型的唯一标识。 不同项目模型下可选值不同： - IPD-系统设备类：10021（RR）、10065（SF）、10020（IR）、10022（SR）、10029（AR）、10027（Task）、10033（Bug） - IPD-独立软件类：10021（RR）、10065（SF）、10020（IR）、10023（US）、10027（Task）、10033（Bug） - IPD-自运营软件/云服务类：10001（Epic）、10028（FE）、10021（RR）、10023（US）、10027（Task）、10033（Bug）

        :param category_id: The category_id of this ShowIpdFieldsV2Request.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def category_layer_id(self):
        r"""Gets the category_layer_id of this ShowIpdFieldsV2Request.

        层级字段ID。用于过滤层级类型的字段，当需要按层级结构筛选字段时传入。

        :return: The category_layer_id of this ShowIpdFieldsV2Request.
        :rtype: str
        """
        return self._category_layer_id

    @category_layer_id.setter
    def category_layer_id(self, category_layer_id):
        r"""Sets the category_layer_id of this ShowIpdFieldsV2Request.

        层级字段ID。用于过滤层级类型的字段，当需要按层级结构筛选字段时传入。

        :param category_layer_id: The category_layer_id of this ShowIpdFieldsV2Request.
        :type category_layer_id: str
        """
        self._category_layer_id = category_layer_id

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this ShowIpdFieldsV2Request.

        目标项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。当需要查询其他项目的字段配置时传入。

        :return: The target_project_id of this ShowIpdFieldsV2Request.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this ShowIpdFieldsV2Request.

        目标项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。当需要查询其他项目的字段配置时传入。

        :param target_project_id: The target_project_id of this ShowIpdFieldsV2Request.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

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
        if not isinstance(other, ShowIpdFieldsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
