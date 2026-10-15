# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetHealthReportConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'template_id': 'str'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'template_id': 'template_id'
    }

    def __init__(self, instance_ids=None, template_id=None):
        r"""BatchSetHealthReportConfigReq

        The model defined in huaweicloud sdk

        :param instance_ids: 实例ID列表，最大100条。
        :type instance_ids: list[str]
        :param template_id: 健康报告模板ID。
        :type template_id: str
        """
        
        

        self._instance_ids = None
        self._template_id = None
        self.discriminator = None

        self.instance_ids = instance_ids
        self.template_id = template_id

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this BatchSetHealthReportConfigReq.

        实例ID列表，最大100条。

        :return: The instance_ids of this BatchSetHealthReportConfigReq.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this BatchSetHealthReportConfigReq.

        实例ID列表，最大100条。

        :param instance_ids: The instance_ids of this BatchSetHealthReportConfigReq.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def template_id(self):
        r"""Gets the template_id of this BatchSetHealthReportConfigReq.

        健康报告模板ID。

        :return: The template_id of this BatchSetHealthReportConfigReq.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this BatchSetHealthReportConfigReq.

        健康报告模板ID。

        :param template_id: The template_id of this BatchSetHealthReportConfigReq.
        :type template_id: str
        """
        self._template_id = template_id

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
        if not isinstance(other, BatchSetHealthReportConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
