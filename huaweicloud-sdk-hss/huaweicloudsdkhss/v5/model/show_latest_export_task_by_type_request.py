# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLatestExportTaskByTypeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'export_task_type': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'export_task_type': 'export_task_type',
        'task_id': 'task_id'
    }

    def __init__(self, enterprise_project_id=None, export_task_type=None, task_id=None):
        r"""ShowLatestExportTaskByTypeRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param export_task_type: 导出任务类型
        :type export_task_type: str
        :param task_id: 导出任务ID
        :type task_id: str
        """
        
        

        self._enterprise_project_id = None
        self._export_task_type = None
        self._task_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if export_task_type is not None:
            self.export_task_type = export_task_type
        self.task_id = task_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowLatestExportTaskByTypeRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowLatestExportTaskByTypeRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowLatestExportTaskByTypeRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowLatestExportTaskByTypeRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def export_task_type(self):
        r"""Gets the export_task_type of this ShowLatestExportTaskByTypeRequest.

        导出任务类型

        :return: The export_task_type of this ShowLatestExportTaskByTypeRequest.
        :rtype: str
        """
        return self._export_task_type

    @export_task_type.setter
    def export_task_type(self, export_task_type):
        r"""Sets the export_task_type of this ShowLatestExportTaskByTypeRequest.

        导出任务类型

        :param export_task_type: The export_task_type of this ShowLatestExportTaskByTypeRequest.
        :type export_task_type: str
        """
        self._export_task_type = export_task_type

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowLatestExportTaskByTypeRequest.

        导出任务ID

        :return: The task_id of this ShowLatestExportTaskByTypeRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowLatestExportTaskByTypeRequest.

        导出任务ID

        :param task_id: The task_id of this ShowLatestExportTaskByTypeRequest.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, ShowLatestExportTaskByTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
