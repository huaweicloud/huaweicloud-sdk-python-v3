# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationTemplateByNameRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'enterprise_project_id': 'Enterprise-Project-Id'
    }

    def __init__(self, name=None, enterprise_project_id=None):
        r"""ListNotificationTemplateByNameRequest

        The model defined in huaweicloud sdk

        :param name: 消息通知模板名称。
        :type name: str
        :param enterprise_project_id: 企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。 - 查询单个企业项目下通知消息模板列表，填写企业项目id。 - 查询所有企业项目下通知消息模板列表，填写“all_granted_eps”。 - 不填，查询默认企业项目下通知消息模板列表。
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this ListNotificationTemplateByNameRequest.

        消息通知模板名称。

        :return: The name of this ListNotificationTemplateByNameRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListNotificationTemplateByNameRequest.

        消息通知模板名称。

        :param name: The name of this ListNotificationTemplateByNameRequest.
        :type name: str
        """
        self._name = name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListNotificationTemplateByNameRequest.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。 - 查询单个企业项目下通知消息模板列表，填写企业项目id。 - 查询所有企业项目下通知消息模板列表，填写“all_granted_eps”。 - 不填，查询默认企业项目下通知消息模板列表。

        :return: The enterprise_project_id of this ListNotificationTemplateByNameRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListNotificationTemplateByNameRequest.

        企业项目id。获取方式请参见：[获取企业项目ID](aom_04_0024.xml)。 - 查询单个企业项目下通知消息模板列表，填写企业项目id。 - 查询所有企业项目下通知消息模板列表，填写“all_granted_eps”。 - 不填，查询默认企业项目下通知消息模板列表。

        :param enterprise_project_id: The enterprise_project_id of this ListNotificationTemplateByNameRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListNotificationTemplateByNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
