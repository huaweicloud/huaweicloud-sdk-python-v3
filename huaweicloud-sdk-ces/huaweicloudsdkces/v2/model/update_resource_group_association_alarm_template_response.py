# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResourceGroupAssociationAlarmTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'template_ids': 'list[str]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'template_ids': 'template_ids'
    }

    def __init__(self, group_id=None, template_ids=None):
        r"""UpdateResourceGroupAssociationAlarmTemplateResponse

        The model defined in huaweicloud sdk

        :param group_id: 资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串
        :type group_id: str
        :param template_ids: 关联的告警模板的ID列表
        :type template_ids: list[str]
        """
        
        super(UpdateResourceGroupAssociationAlarmTemplateResponse, self).__init__()

        self._group_id = None
        self._template_ids = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if template_ids is not None:
            self.template_ids = template_ids

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateResourceGroupAssociationAlarmTemplateResponse.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :return: The group_id of this UpdateResourceGroupAssociationAlarmTemplateResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateResourceGroupAssociationAlarmTemplateResponse.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :param group_id: The group_id of this UpdateResourceGroupAssociationAlarmTemplateResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def template_ids(self):
        r"""Gets the template_ids of this UpdateResourceGroupAssociationAlarmTemplateResponse.

        关联的告警模板的ID列表

        :return: The template_ids of this UpdateResourceGroupAssociationAlarmTemplateResponse.
        :rtype: list[str]
        """
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        r"""Sets the template_ids of this UpdateResourceGroupAssociationAlarmTemplateResponse.

        关联的告警模板的ID列表

        :param template_ids: The template_ids of this UpdateResourceGroupAssociationAlarmTemplateResponse.
        :type template_ids: list[str]
        """
        self._template_ids = template_ids

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
        if not isinstance(other, UpdateResourceGroupAssociationAlarmTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
