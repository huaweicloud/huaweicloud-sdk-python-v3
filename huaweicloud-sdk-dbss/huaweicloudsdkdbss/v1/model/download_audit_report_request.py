# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadAuditReportRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'id': 'str',
        'local': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'id': 'id',
        'local': 'local'
    }

    def __init__(self, instance_id=None, id=None, local=None):
        r"""DownloadAuditReportRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。可通过查询实例列表接口ID字段获取 **约束限制**： 不涉及 **取值范围**： 以查询实例列表接口值为准，字符长度32-64。 **默认取值**： 不涉及 
        :type instance_id: str
        :param id: **参数解释**： 报表ID。可通过查询报表接口ID值获取。 **约束限制**： 不涉及 **取值范围**： 以查询报表接口值为准，字符长度16-64。 **默认取值**： 不涉及 
        :type id: str
        :param local: **参数解释**： 语言区域。 **约束限制**： 仅支持取值范围约定的值 **取值范围**： - en-us : 英语 - zh-cn : 中文 **默认取值**： en-us 
        :type local: str
        """
        
        

        self._instance_id = None
        self._id = None
        self._local = None
        self.discriminator = None

        self.instance_id = instance_id
        self.id = id
        if local is not None:
            self.local = local

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DownloadAuditReportRequest.

        **参数解释**： 实例ID。可通过查询实例列表接口ID字段获取 **约束限制**： 不涉及 **取值范围**： 以查询实例列表接口值为准，字符长度32-64。 **默认取值**： 不涉及 

        :return: The instance_id of this DownloadAuditReportRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DownloadAuditReportRequest.

        **参数解释**： 实例ID。可通过查询实例列表接口ID字段获取 **约束限制**： 不涉及 **取值范围**： 以查询实例列表接口值为准，字符长度32-64。 **默认取值**： 不涉及 

        :param instance_id: The instance_id of this DownloadAuditReportRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def id(self):
        r"""Gets the id of this DownloadAuditReportRequest.

        **参数解释**： 报表ID。可通过查询报表接口ID值获取。 **约束限制**： 不涉及 **取值范围**： 以查询报表接口值为准，字符长度16-64。 **默认取值**： 不涉及 

        :return: The id of this DownloadAuditReportRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DownloadAuditReportRequest.

        **参数解释**： 报表ID。可通过查询报表接口ID值获取。 **约束限制**： 不涉及 **取值范围**： 以查询报表接口值为准，字符长度16-64。 **默认取值**： 不涉及 

        :param id: The id of this DownloadAuditReportRequest.
        :type id: str
        """
        self._id = id

    @property
    def local(self):
        r"""Gets the local of this DownloadAuditReportRequest.

        **参数解释**： 语言区域。 **约束限制**： 仅支持取值范围约定的值 **取值范围**： - en-us : 英语 - zh-cn : 中文 **默认取值**： en-us 

        :return: The local of this DownloadAuditReportRequest.
        :rtype: str
        """
        return self._local

    @local.setter
    def local(self, local):
        r"""Sets the local of this DownloadAuditReportRequest.

        **参数解释**： 语言区域。 **约束限制**： 仅支持取值范围约定的值 **取值范围**： - en-us : 英语 - zh-cn : 中文 **默认取值**： en-us 

        :param local: The local of this DownloadAuditReportRequest.
        :type local: str
        """
        self._local = local

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
        if not isinstance(other, DownloadAuditReportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
