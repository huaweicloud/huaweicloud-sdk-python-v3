# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteAlarmTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_ids': 'list[str]'
    }

    attribute_map = {
        'template_ids': 'template_ids'
    }

    def __init__(self, template_ids=None):
        """BatchDeleteAlarmTemplatesResponse

        The model defined in huaweicloud sdk

        :param template_ids: 成功删除的告警模板ID列表
        :type template_ids: list[str]
        """
        
        super(BatchDeleteAlarmTemplatesResponse, self).__init__()

        self._template_ids = None
        self.discriminator = None

        if template_ids is not None:
            self.template_ids = template_ids

    @property
    def template_ids(self):
        """Gets the template_ids of this BatchDeleteAlarmTemplatesResponse.

        成功删除的告警模板ID列表

        :return: The template_ids of this BatchDeleteAlarmTemplatesResponse.
        :rtype: list[str]
        """
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        """Sets the template_ids of this BatchDeleteAlarmTemplatesResponse.

        成功删除的告警模板ID列表

        :param template_ids: The template_ids of this BatchDeleteAlarmTemplatesResponse.
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
        if not isinstance(other, BatchDeleteAlarmTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
